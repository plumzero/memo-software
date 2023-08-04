
[下载](https://github.com/etcd-io/etcd/releases/download/v3.4.13/etcd-v3.4.13-linux-amd64.tar.gz)

版本: v3.4.13

`etcd` 使用 golang 编写，为了避免编译不规范，这里直接使用编译好的二进制包。

解压后链接:
```sh
    ln -s /usr/local/etcd/etcd /usr/bin/etcd
    ln -s /usr/local/etcd/etcdctl /usr/bin/etcdctl
```


### 运行

```sh
    nohup etcd &
```

