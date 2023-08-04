
### elasticsearch 与机器环境 JDK 版本不一致

执行如下命令查看版本
```sh
    /usr/local/elasticsearch-7.11.2/bin --version
```
如果出现如下打印:
```sh
    Future versions of Elasticsearch will require Java 11; your Java version from [/usr/local/jdk1.8.0_281/jre] does not meet this requirement. Consider switching to a distribution of Elasticsearch with a bundled JDK. If you are already using a distribution with a bundled JDK, ensure the JAVA_HOME environment variable is not set.
```
说明当前机器环境本身的 jdk 与 es 要求的 jdk 版本不一致。

es 本身自带 jdk, 如果机器环境也安装了 jdk, 则 es 会优先选择使用机器环境上的 jdk 。

不过还是想让 es 使用自己的 jdk, 一种方法是"抹除"机器环境上的 jdk。不过这种方法可能会对其他依赖机器环境 jdk 的程序造成影响，针对于此，可以按照上述打印提示在机器环境中不设置 ${JAVA_HOME} 变量。

具体修改一般在 `/etc/profile` 中进行。修改后结果大致如下:
```sh
    # export JAVA_HOME=/usr/local/jdk1.8.0_281
    export JRE_HOME=/usr/local/jdk1.8.0_281/jre
    export CLASSPATH=.:/usr/local/jdk1.8.0_281/lib:${JRE_HOME}/lib
    export PATH=/usr/local/jdk1.8.0_281/bin:$PATH
```
