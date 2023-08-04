
apisix 的配置文件路径相对顶层目录为 `conf/config.yaml` 。

https://www.jianshu.com/p/19607e0c7005?utm_campaign=haruki


more: apisix_cli_test

### 限定ip访问

通过 `allow_admin` 限定为某个子网或某些ip访问:
```sh
apisix:
    allow_admin:
        - 127.0.0.9
```