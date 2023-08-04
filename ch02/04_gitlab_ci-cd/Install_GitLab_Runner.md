
[Install GitLab Runner manually on GNU/Linux](https://docs.gitlab.com/runner/install/linux-manually.html)

这里采用二进制方式安装，安装环境为 Linux x86-64 。


下载二进制包到指定目录
```shell
    sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64"
```

赋予权限
```shell
    sudo chmod +x /usr/local/bin/gitlab-runner
```

创建 gitlab-runner 用户
```shell
    sudo useradd --comment 'GitLab Runner' --create-home gitlab-runner --shell /bin/bash
```

安装并运行服务
```shell
    sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
    sudo gitlab-runner start
```

### 更新操作

关闭服务
```shell
    sudo gitlab-runner stop
```

下载更新包替换
```shell
    sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64"
```

重新赋予权限后启动
```shell
    sudo chmod +x /usr/local/bin/gitlab-runner
    sudo gitlab-runner start
```

