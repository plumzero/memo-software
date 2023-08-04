
使用 vscode ssh 连接虚拟机时，总是报 "XHR failed" 错误，原来是虚拟机上的时间不同步所致。这个时候就很有必要通过 NTP 服务进行时间同步。


### 环境与版本
```
    Debian 8.0
    ntp-4.2.8p15
```


### 编译安装

解压 配置
```
    tar -zxvf ntp-4.2.8p15.tar.gz
    cd ntp-4.2.8p15
    ./configure --prefix=/usr/local/ntp
```

编译 测试(可选) 安装
```
    make
    make check
    make install
```


编译完成后没找到所谓的 `ntp.conf` 文件，还是 `apt-get` 安装吧...
```sh
    apt-get install ntp
``` 
安装后会在搜索路径下有 `ntpq` 命令。

通过 `chkconfig --list ntp` 查看:
```
    ntp                       0:off  1:off  2:on   3:on   4:on   5:on   6:off
```
已经安装并启动了。
