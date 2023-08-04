

### 测试环境

* ubuntu server 16.04.7 amd64


### 版本说明

* Anaconda3-2021.05-Linux-x86_64.sh
 
  下载地址: https://www.anaconda.com/products/individual-d

* celery 5.1.2

  测试时，这个是最新的版本。

* redis 6.2.4

  对 redis 版本没有特殊要求。

* PostgreSQL 13.1

  外部数据库。可以部署在同一机器上，也可以部署在其他机器上，但要确保 celery 可以访问得到。

### 参考

* [使用Celery](https://zhuanlan.zhihu.com/p/22304455)
* 
[异步任务神器 Celery 快速入门教程](https://blog.csdn.net/chenqiuge1984/article/details/80127446?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control)
* [celery配置参考](https://www.cnblogs.com/cwp-bg/p/8759638.html#celery配置)
* [celery异常](https://docs.celeryproject.org/en/4.0/reference/celery.exceptions.html#celery.exceptions)


### 内容

* [环境部署](01_环境部署.md)
* [组件测试](02_组件测试.md)
* [多任务测试](03_多任务测试.md)
* [使用配置](04_使用配置.md)
* [调用任务](05_调用任务.md)
* [定期任务](06_定期任务.md)
* [获取存储结果](07_获取存储结果.md)
