
### 说明

vscode 插件，搜索 `Emmet`, 找到 `Mithril Emmet` 安装即可。


### 用途

快速编写 `.html` 或 `.css` 文件。


### 用法

在后缀为 `.html` 或 `.css` 的文件输入指定缩写后按 `Tab` 键即会生成相应代码。


### 语法规则

| 表达式       | 含义 |
|:------------|:-----|
| E           | 标签 |
| E#id        | id 属性 |
| E.class     | class 属性 |
| E[attr=foo] | 某一特定属性 |
| E{foo}      | 标签内容为 foo |
| E>N         | N 是 E 的子元素 |
| E+N         | N 是 E 的同级元素 |
| E^N         | N 是 E 的上级元素 |


### 基本用法示例

元素(Elements)表达式与展开对应内容

| 表达式          | 内容 |
|:---------------|:-----|
| div            | `<div></div>` |
| html:5         | [click me!](t/v5.html) |
| a:mail         | `<a href="mailto:"></a>` |
| a:link         | `<a href="http://"></a>` |
| base           | `<base href="">` |
| br             | `<br>` |
| link           | `<link rel="stylesheet" href="">` |
| script:src     | `<script src=""></script>` |
| form:get       | `<form action="" method="get"></form>` |
| label          | `<label for=""></label>` |
| input          | `<input type="text">` |
| inp            | `<input type="text" name="" id="">` |
| input:h        | `<input type="hidden" name="">` |
| input:email    | `<input type="email" name="" id="">` |
| input:password | `<input type="password" name="" id="">` |
| input:checkbox | `<input type="checkbox" name="" id="">` |
| input:radio    | `<input type="radio" name="" id="">` |
| select         | `<select name="" id=""></select>` |
| option         | `<option value=""></option>` |
| bq             | `<blockquote></blockquote>` |
| btn            | `<button></button>` |
| btn:s          | `<button type="submit"></button>` |
| btn:r          | `<button type="reset"></button>` |

生成元素的同时添加文本(Text)

| 表达式示例    | 内容 |
|:-------------|:-----|
| div{hello}   | `<div>hello</div>` |
| a{click-me!} | `<a href="">click-me!</a>` |

生成元素的同时添加元素属性

| 表达式示例    | 内容 | 说明 |
|:-------------|:-----|:----|
| div.test     | `<div class="test"></div>` | |
| div#pageId   | `<div id="pageId"></div>` | |
| .class       | `<div class="class"></div>` | 隐式标签自动联想 |
| em>.class    | `<em><span class="class"></span></em>` | 隐式标签自动联想 |
| table>.row>.col | [click me!](t/table_row_col.html) | 隐式标签自动联想 |
| div.test1.test2.test3 | `<div class="test1 test2 test3"></div>` | 绑定多个类名 |
| a[href='#' data-title='customer' target='_blank'] | `<a href="#" data-title="customer" target="_blank"></a>` | |
| form[method='POST' action='/upload' enctype='multipart/form-data']{Choose an image to upload: }>input[type='image' value='file']+input[type="submit" value="Upload"] | [click me!](t/form_input_input.html) |

嵌套操作符

| 表达式示例    | 内容 |
|:-------------|:-----|
| div#pageId>ul>li | [click me!](t/div_ul_li.html) |
| div#pageId+div.child | [click me!](t/div_div_child.html) |
| div>p.parent>span.child^ul.brother>li | [click me!](t/div_p_span_ul_li.html) |

分组操作符

| 表达式示例    | 内容 |
|:-------------|:-----|
| div>(ul>li+span)>a | [click me!](t/div_li_span_a.html) |
| ul>li*3      | [click me!](t/ul_li_3.html) |
| tr*5>(td{&nbsp})*5 | [click me!](t/tr_5_td_space_5.html)