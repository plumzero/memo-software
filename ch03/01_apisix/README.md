
### 部署环境

Ubuntu 16.04.5 为主。

RHEL 7.5 有余力时部署。


### 版本说明

|  Bar       |  Ver  |
|:----------|:-------|
| Lua       | 5.1.5  |
| LuaRocks  | 3.5.0  |
| OpenResty | 19.3.1 |
| etcd      | 3.4.13 |
| APISIX    | 2.3    |

Lua 要使用 5.1 版本。


### 参考

[官方README](https://github.com/apache/apisix/blob/v2.3/README_CN.md)

[Apache APISIX 文档索引](https://github.com/apache/apisix/blob/v2.3/doc/zh-cn/README.md)


### 备忘

意义不明但应该很重要的文件  apisix-dashboard 的 `schema.json` 。


### 内容

[编译与部署](01_编译与部署.md)

[启动与运行](02_启动与运行.md)

[可视化控制](03_部署面板.md)

可以通过面板来实现服务的配置与访问。不过，为了更好的学习 `apisix`，针对开发者，这里插入一项[快速入门指南](02+_快速入门指南.md)。


### 测试

[http测试](04_http测试.md)

[基本认证测试](05_基本认证测试.md)

[协议转换测试](06_协议转换测试.md)


### 配置

[可视化配置](07_通过dashboard可视化配置.md)

[apisix配置文件](08_apisix配置文件.md)

[dashboard配置文件](09_dashboard配置文件.md)


### 更多功能测试




### 针对开发者

[插件](https://github.com/apache/apisix/blob/v2.3/doc/zh-cn/README.md#%E6%8F%92%E4%BB%B6)

[插件开发指南](https://github.com/apache/apisix/blob/v2.3/doc/zh-cn/plugin-develop.md)

[插件开发示例](https://github.com/apache/apisix/blob/v2.3/doc/zh-cn/plugins/echo.md)

[管理员控制集群接口](https://github.com/apache/apisix/blob/v2.3/doc/zh-cn/admin-api.md)

