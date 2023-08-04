
傻瓜式地，在已经安装好了 gitlab-runner 的前提下，为一个项目配置 CI/CD 只要三步。
1. 在项目的顶层目录创建一个 `.gitlab-ci.yml` 文件，并提交到 gitlab 中。点开 `CI/CD -> Pipelines` 界面确认一些东西。
2. 展开 `Setting -> CI/CD -> Runners`，将 url 和 token 注册到 gitlab-runner 中。
3. 展开 `Setting -> CI/CD -> Runners`，确认一些东西。

关于 .gitlab-ci.yml 文件，它位于工程根目录下，用于配置工程 CI 活动。每次向仓库执行提交时，GitLab 都会寻找 `.gitlab-ci.yml` 文件并在 `Runners` 上运行相应的作业。

这里说明一下整个 `.gitlab-ci.yml` 文件的动作过程。


### 创建

```yml
before_script:
  - apt-get update -qq && apt-get install -y -qq sqlite3 libsqlite3-dev nodejs
  - ruby -v
  - which ruby
  - gem install bundler --no-ri --no-rdoc
  - bundle install --jobs $(nproc)  "${FLAGS[@]}"

rspec:
  script:
    - bundle exec rspec

rubocop:
  script:
    - bundle exec rubocop
```
该配置定义了两个作业，分别是 rspec 和 rubocop, 作业名称是任意的。在进行每个作业之前，将会执行 `before_script` 脚本任务，before_script 是个特殊字。

如果想要检查工程下的 `.gitlab-ci.yml` 是否有效，可以点击 `CI/CD` 进入相关页面，找到 `CI Lint` 按钮，点击进入检查页面。


### 提交

`.gitlab-ci.yml` 创建完毕之后，将其添加到 Git 仓库追踪并推到 GitLab 上。
```shell
    git add .gitlab-ci.yml
    git commit -m "Add .gitlab-ci.yml"
    git push origin master
```
提交之后进入 `CI/CD` 的 `Pipelines` 页面，会看到关于 pipeline 的一些东西。


### 配置 Runner

Runner 会运行在 `gitlab-ci.yml` 中定义的作业，Runner 所在机器与 GitLab 服务器之间必须可以进行网络互通。

Runner 可以仅服务于 GitLab 上的某个工程，也可以服务于多个工程，此时称为共享 Runner。

通过 `Settings -> CI/CD` 可以查看当前工程是否设置了 Runner，一般设置 Runner 遵循以下两个步骤:
- [安装](Install_GitLab_Runner.md)
- [配置](Configuring_GitLab_Runners.md)
设置了 Runner 之后，通过 `Setting -> CI/CD` 可以看到 Runners 页面。

通过 `Setting -> CI/CD -> Runners`，点击 `Enable shared runners` 开启共享 Runners 。


之后就可以使用了。

[在.gitlab-ci.yml中配置作业](Configure_Jobs.md)


### 配置免密登录

[SSH keys](https://wiki.archlinux.org/title/SSH_keys_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

以下命令在`GitLab Runners`服务运行的机器上(这里假设是 `192.168.37.20`)以 `gitlab-runner` 用户身份执行。假设 `192.168.37.26` 为部署目标机器，`lb` 为部署目标机器用户身份。
```sh
    ssh-keygen                          // 生成密钥对
    ssh-copy-id lb@192.168.37.26        // 将公钥拷贝到目标机器
    ssh lb@192.168.37.26                // 测试是否登录成功
```

### 示例

按照以上步骤操作完成后，可以编写出如下的示例 `.gitlab-ci.yml` 文件:
```yml
stages:
  - build
  - deploy

variables:
  DEPLOY_MACHINE_HOST: "lb@192.168.37.26"

build_job:
  stage: build
  tags:
    - mytag
  cache:
    paths:
      - bin/
    policy: push
  only:
    - test
    - master
  script:
    - export GOPROXY=https://goproxy.cn,direct
    - make clean
    - make deps
    - make build
    - make install

deploy_job:
  stage: deploy
  tags:
    - mytag
  cache:
    paths:
      - build/
    policy: pull
  only:
    - test
  script:
    - pid=`ssh $DEPLOY_MACHINE_HOST " ps -ef | grep myprogram |grep -v grep " |awk '{print $2}'` ||true
    - echo $pid | xargs ssh $DEPLOY_MACHINE_HOST "kill -9" ||true
    - cd bin/
    - scp myprogram myprogram.sh $DEPLOY_MACHINE_HOST:/path/to/services/
    - ssh $DEPLOY_MACHINE_HOST "cd /path/to/services/; nohup bash myprogram.sh >/dev/null 2>&1 &"
```