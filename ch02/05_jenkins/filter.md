
分支过滤，如下:

![](img/branch_filter_1.png)

表示只有当源分支名称以 "emergency" 开头且目标分支名称为 "master" 时，才会触发构建(当然，前提是已经支持了 `Push Events`)。


![](img/branch_filter_2.png)

表示只有当源分支名称以 "emergency" 或 "branch" 开头时，才会触发构建(当然，前提是已经支持了 `Push Events`)。
