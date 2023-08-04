
进行 GitLab 的免密登录方式一般有两种:
- http 下在首次输入用户名及密码后将登录信息 store 到本地
- 在本地通过 ssh-keygen 生成一对密码，将公钥信息拷贝黏贴到 GitLab 用户配置中

在运维过程中常常要拉取仓库，免密操作是必要的。第一种方式不可取。第二种方式最好应该是创建一个专门的运维账户进行操作。

以第二种方式为例，假设 GitLab 的运维帐户为 ops 。

现在在要拉取仓库的目标机器上创建一对密码:
```sh
    ssh-keygen -t rsa -C "for ops"
```
这之后，会在执行上述命令的 Linux 用户的家目录下(具体为 `~/.ssh/`)产生一双文件 id_rsa 和 id_rsa.pub，分别代表生成的私钥和公钥。将公钥内容进行拷贝，进行后续粘贴。

以 ops 用户登录 GitLab，点击右上角用户图标，在展开的下拉列表中选择 `Setting` 点击进入，在左边的 `User Settings` 栏中，找到 `SSH Keys` 点击进入，将之前拷贝的公钥粘贴到缺省内容为 `Typically starts with "ssh-rsa"` 的富文本栏中，之后点击 `Add Key` 进行保存。

这个时候，就可以在目标机器上以 ssh 方式对仓库进行操作了。这里以克隆为例:
```sh
    git clone git@192.168.x.x:this-dev/study.git
```
