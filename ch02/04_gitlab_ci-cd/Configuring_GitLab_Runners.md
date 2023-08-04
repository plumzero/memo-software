
[Registering runners](https://docs.gitlab.com/runner/register/index.html)

在 Linux 下注册一个 runner 。

```shell
    sudo gitlab-runner register
```

接下来按照提示输入。

```shell
Enter the GitLab instance URL (for example, https://gitlab.com/):
```
GitLab instance URL 可以在 GitLab 页面通过 `Settings -> CI/CD`，展开 `Runners` 选项，找到 `Setup a specific Runner manually`。拷贝 url 即可。

```shell
Enter the registration token:
```
token 同样通过上面的方法找到。

```shell
Enter a description for the runner:
```
一个简单的描述。

```shell
Enter tags for the runner (comma-separated):
```
与 `.gitlab-ci.yml` 中作业中的 `tags` 项有关。

```shell
Enter an executor: ssh, docker+machine, kubernetes, docker, docker-ssh, parallels, docker-ssh+machine, custom, shell, virtualbox:
```
选定一个执行器，一般大家都使用 docker，这里选用 shell 。

注意，注册之后，还要去 `Settings -> CI/CD`页面，展开 `Runners` 选项查看是否可用(为绿色)。如果不可用，可能会有 `New runner. Has not connected yet` 的提示，这个时候可以尝试重新启动 gitlab-runner，之后再查看该页面。
