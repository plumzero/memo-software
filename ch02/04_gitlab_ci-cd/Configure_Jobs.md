
`.gitlab-ci.yml` 的用法说明，这个文件用作 GitLab Runner 对工程中作业的管理。

参考: help/ci/yaml/README.md

### 作业

在 `.gitlab-ci.yml` 中可以定义一组作业，同时约束它们怎样以及在什么时候运行。作业的组成格式呈阶梯状，如下:
```yml
job1:
  script: "execute-script-for-job1"

job2:
  script: "execute-script-for-job2"
```
- 上面定义了两个独立的作业，名称分别为 "job1" 和 "job2"，作业至少应包含 `script` 关键字。
- 每个作业执行不同的命令。命令可以是串联的，如`./configure; make; make install`，也可以是一个脚本。
- 作业由 Runners 运行，每项作业的运行是独立的。
- 对于作业名称的命名是任意的，但应避免使用以下关键字：
  ```shell
    image
    services
    stages
    types
    before_script
    after_script
    variables
    cache
  ```

可以通过以下不同的参数来定义各个作业的行为(常用):

| 参数关键字 | 是否必须 | 描述 |
|:----------|:--------|:-----|
| script    | 是      | 定义由 Runner 执行的脚本命令 |
| stage     | 否      | 定义作业的阶段，默认为 test |
| only      | 否      | 定义该作业适用的 git 分支或标签 |
| except    | 否      | 定义该作业不适用的 git 分支或标签 |
| tags      | 否      | 定义用于选择 Runner 的标签列表 |
| when      | 否      | 定义什么时候运行作业，可选项有 `on_success`、`on_failure`、`always` 或者 `manual` |
| cache     | 否      | 定义要保存的用于随后运行的文件 |
| before_script | 否  | 定义一组命令，在运行每个作业之前都要执行这组命令 |
| after_script | 否   | 定义一组命令，在运行每个作业之后都要执行这组命令 |

`before_script` 和 `after_script` 的最低环境要求为 GitLab 8.7 和 Gitlab Runner v1.2。这两个参数也可以作为全局参数，此时作业内的对应参数(如果定义的话)会对其进行重写。如下:
```yml
before_script:
  - global before script

job:
  before_script:
    - execute this instead of global before script
  script:
    - my command
  after_script:
    - execute this after my script
```

----
`stages` 位于全局中，通常用来定义可以为作业所使用的阶段。`stages` 中元素的顺序定义了其在作业中执行的顺序:
- 1. 所有作业中相同的阶段(stage)并行运行
- 2. 作业中下一个阶段在上一个阶段成功完成之后运行
下面举例说明，这里定义了 3 个阶段:
```yml
stages:
  - build
  - test
  - deploy
```
- 1. 所有的作业会并行执行 build 阶段
- 2. 当所有的作业都成功完成 build 后，会并行执行 test 阶段
- 3. 同样按上述方式执行 deploy 阶段
- 4. 所有作业的 deploy 阶段执行成功之后，当前提交被标记为 `passed`
- 5. 如果其中有任何一步出错，该提交会被标记为 `failed` 且不会执行后续阶段
  
关于阶段的使用，有两点需要注意:
- 1. 如果 `.gitlab-ci.yml` 未定义 `stages`，默认可以在作业中使用 `build`、`test`和`deploy`。
- 2. 如果作业中没有指定任何一个阶段，会将 `test` 作为阶段。

----
`stage` 定义于作业中，依赖于全局的 `stages`，它将不同的作业划分为不同的阶段，位于相同阶段中的作业并行运行。示例:
```yml
stages:
  - build
  - test
  - deploy

job 1:
  stage: build
  script: make build dependencies

job 2:
  stage: build
  script: make build artifacts

job 3:
  stage: test
  script: make test

job 4:
  stage: deploy
  script: make deploy
```

----
`script` 是作业中唯一一个必备的关键字，shell 格式定义，由 Runner 执行。例如:
```yml
job:
  script: "bundle exec rspec"
```
也可以通过数组的形式定义多个命令:
```yml
job:
  script:
    - uname -a
    - bundle exec rspec
```
需要注意的是，如果脚本命令中含有特殊字符(`:`, `{`, `}`, `[`, `]`, `,`, `&`, `*`, `#`, `?`, `|`, `-`, `<`, `>`, `=`, `!`, `%`, `@`, ```)，则需要使用单引号或双引号对命令进行包裹。

----
`only` 和 `except` 用于设置作业的策略(policy)限制，支持正则表达式。

----
`tag` 用于从 Runners 列表中选择特定的 Runners 用于运行这个工程。

`tag` 可以在注册一个 Runner 时指定，比如可以是 "ruby"、"postgres"、"development"等。
```yml
job:
  tags:
    - ruby
    - postgres
```

----
`when` 的可选项如下及含义如下:

| 可选项 | 含义 |
|:------|:-----|
| on_success | 缺省项，当前面所有的 stage 都执行成功之后才会运行这个作业 |
| on_failure | 当前面的 stage 至少有一个错误时，运行该作业 |
| always     | 无论前面执行的怎么，都运行 |
| manual     | 手动运行 |

例如对于下面的文件:
```yml
stages:
  - build
  - cleanup_build
  - test
  - deploy
  - cleanup

build_job:
  stage: build
  script:
    - make build

cleanup_build_job:
  stage: cleanup_build
  script:
    - cleanup build when failed
  when: on_failure

test_job:
  stage: test
  script:
    - make test

deploy_job:
  stage: deploy
  script:
    - make deploy
  when: manual

cleanup_job:
  stage: cleanup
  script:
    - cleanup after jobs
  when: always
```
- 1. 当作业 build_job 出错时，会执行作业 cleanup_build_job
- 2. 无论 pipeline 中的最后一步成功或失败，均执行作业 cleanup_job
- 3. 作业 deploy_job 需要手动执行

----
`cache` 既可以置于全局，也可以置于单个作业中。cache 用来指定在各个作业之间需要缓存的文件或目录。

`cache:paths` 用来指定要缓存的文件或目录路径，支持通配符。如下:
```yml
rspec:
  script: test
  cache:
    paths:
      - binaries/*.apk
      - .config
```
表示缓存 binaries 下的所有 .apk 结尾的文件，以及 .config 文件。

局部 `cache` 会重写全局 `cache`，比如下面的 rspec 作业只会缓存 binary/ 目录:
```yml
cache:
  paths:
    - my/files

rspec:
  script: test
  cache:
    key: rspec
    paths:
      - binaries/
```
需要注意的是，既然 `cache` 用于在作业之间共享，那么在不同的作业中使用不同的路径时，也需要设置一个不同的 `cache:key`，否则缓存内容会被重写。

