
在对 gitlab 仓库进行访问时，除了 https 的密码访问和 git 的密钥访问外，还可以通过 oauth2 进行访问。

不过这种方式好像只适用于对单个仓库的访问。不过即使这样，也会有一些特定的应用场景，比如 docker 。

### 配置

通过网页进入某个仓库，找到 `Settings`，鼠标移入后在弹出列表中找到 `Access Tokens`:

![](img/oauth2_settings_access_token.png)

点击进入如下页面:

![](img/oauth2_settings_access_token_add.png)

填选我们需要的:

![](img/oauth2_settings_access_token_create.png)

点击创建后，如下:

![](img/oauth2_settings_access_token_created.png)

拷贝生成的 token 字符串就可以使用了。

### 使用

示例:
```s
  git remote add tag_origin https://oauth2:${gitlab_access_token}@git.gitlab.net/gitlab-dev/platform/packsoft.git
  git tag -a tag_origin -m "Production Version $tag_name"
  git push -f tag_origin "my-tag"
```
