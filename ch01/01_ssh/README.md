
以通过 ssh 连接 Debian 虚拟机为例。


### 配置

1. sshd 服务。

确保要连接的目标机器安装了 sshd 服务，可以通过`which sshd`查看。


如果没有安装，可以通过 `apt-get` 进行安装:
```shell
    apt-get install openssh-server
```

2. 配置。

进入 `/etc/ssh/` 目录下查看有没有 sshd 相关的配置，如 `sshd_config`。
  
打开 `/etc/ssh/sshd_config`，修改下列配置选项:
```shell
    PasswordAuthentication   将 no 改为 yes
    PermitRootLogin          将 without-password 改为 yes
```

3. 重启 sshd 服务生效(可以使用如下方式):
* service sshd restart
* systemctl restart sshd
* /etc/init.d/ssh restart


### 测试与使用

查看 22 端口是否正在监听:
```shell
  netstat -ant | grep 22  
```

查看 sshd 服务状态:
```shell
  service sshd status        # 查看服务状态。显示结果会因服务种类不同而有多有少
```


### 注意事项

1. ping 不通内网和外网。
   ```shell
     connect: Network is unreachable
   ```
   解决办法: 设置虚拟机为桥接模式

2. 确保 apt 源可用，以下载相关软件，如 openssh-server 。

3. ssh 带命令行参数时，无法在其中实现切换用户(即 su)的操作，因为 su 是通过 tty 来进行的。
 