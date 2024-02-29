# 如何贡献

欢迎贡献基岩文档。我们非常感谢您的帮助，无论是提交错误报告、修复错误、改进文档或提供新的内容。在作出贡献之前，请阅读以下指南。

## 构建与编辑文档

本网站文档使用[Material for MkDocs](https://squidfunk.github.io/)软件提供支持。要在本地构建和编辑文档，您需要安装以下软件：

- [Python](https://www.python.org/downloads/)
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

在安装完成Python后，您可以在控制台中运行如下命令以安装依赖：

```shell
pip install mkdocs-material[recommended,git,imaging]
pip install mkdocs-rss-plugin
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-git-committers-plugin-2
pip install mkdocs-minify-plugin
pip install mkdocs-glightbox
```

这将安装MkDocs和Material for MkDocs以及其他必要的插件。然后，您可以在本项目的根目录于控制台中使用`python -m mkdocs serve --dirtyreload`命令，此后即可在`localhost:8000`实时看到做出的更改。

注意，如果发生错误，请将`tools`文件夹复制(1)到`docs`文件夹内再重新执行命令。
{ .annotate }

1.  注意：不是移动。

在完成编辑后，您可以提交并推送更改。GitHub Actions会自动构建并将文档推送至GitHub Pages。然后，您可以在[https://miemiemethod.github.io/bedrock-docs/](https://miemiemethod.github.io/bedrock-docs/)查看更改后的效果。

## 文档语法

本文档使用Markdown语法编写。如果您不熟悉Markdown语法，可以参考[这篇文章](https://www.markdownguide.org/basic-syntax/)，或这篇[中文文章](https://markdown-zh.readthedocs.io/en/latest/)。此外，您还可以参考[Material for MkDocs的文档](https://squidfunk.github.io/mkdocs-material/reference/)以了解更多关于Material for MkDocs的独有语法，以及参考[PyMdown Extensions的文档](https://facelessuser.github.io/pymdown-extensions/)以了解更多关于PyMdown Extensions提供的额外语法。本站加载有所有PyMdown Extensions提供的扩展，请编者放心使用。

此外，此处也以中文语言重新记录了一些上述的额外语法：

### 一般内联语法

| 描述   | 语法                                              | 效果                  |
|------|-------------------------------------------------|---------------------|
| 删除   | `~~删除~~`                                        | ~~删除~~              |
| 下划线  | `^^插入^^`                                        | ^^插入^^              |
| 下标   | `~下标~`                                          | ~下标~                |
| 上标   | `^上标^`                                          | ^上标^                |
| 插入   | <code>{\++插入++}</code>                          | {++插入++}            |
| 移除   | <code>{\--移除-\-}</code>                         | {--移除--}            |
| 替换   | <code>{\~\~A\~>B~~}</code>                      | {~~A~>B~~}          |
| 高亮   | <code>{\==高亮==}</code><br/><code>\==高亮==</code> | {==高亮==}            |
| 注释   | <code>{\>>注释<<}</code>                          | {>>注释<<}            |
| 代码高亮 | <code>\`#!js foo = 1 / 2;\`</code>              | `#!js foo = 1 / 2;` |
| 快捷键  | `++ctrl+alt+delete++`                           | ++ctrl+alt+delete++ |
| 进度条  | `[=85% "85%"]`                                  | [=85% "85%"]        |

值得注意的是，如果上下标中含有空格，空格需要转义，即使用<code>\\ </code>代替单纯的<code> </code>。快捷键语法中的各键位标识符详见[Keys扩展文档](https://facelessuser.github.io/pymdown-extensions/extensions/keys/#extendingmodifying-key-map-index)。进度条允许[注入](#注入特性)一些类使其变成糖衣色、动态糖衣色或窄进度条，具体详见[Progress扩展文档](https://facelessuser.github.io/pymdown-extensions/extensions/progressbar/#overview)。

### 注入特性

依赖于[Attribute Lists扩展](https://python-markdown.github.io/extensions/attr_list/)，本文档支持向HTML标签注入特性。在一个可能会被解析为HTML标签的语法结构之后使用语法`{:.class #id key=value key="spaced value"}`来注入特性，其中`.class`代表类，`#id`代表锚点ID，`key=value`代表键值对，`key="spaced value"`代表键值对中的值含有空格，每一种皆是可选的，其中类和键值对可以有任意多个。此外，`{: }`中的冒号可以省略，即`{.class #id key=value key="spaced value"}`也是合法的。例如给一个段落的`#!html <p>`标签注入：

```markdown
这是一个段落。
{:.data-class #custom-id key1=value key2="spaced value"}
```

/// html | div.result
//// tab | HTML
```html
<p class="data-class" id="custom-id" key1="value" key2="spaced value">这是一个段落。</p>
```
////
//// tab | 效果
这是一个段落。
{:.data-class #custom-id key1=value key2="spaced value"}
////
///

### 围栏

围栏语法即代码块语法。

### 内容块

#### 警告

#### HTML

#### 定义

#### 标签

### 注解

注解通过注入`annotate`类，紧跟着给出一个有序列表来实现。例如，在段落中使用注解：

```markdown
这是一个段落(1)。
{.annotate}

1.  这是一个注解。
```

/// html | div.result
这是一个段落(1)。
{.annotate}

1.  这是一个注解。
///

注解可以在任何支持注入的地方使用。例如，在围栏中使用注解：

/// tab | 常规
````markdown
```{.python .annotate}
print("Hello, World!") # 这是一个注释。(1)
```

1.  这是一个注解。
````

//// html | div.result
```{.python .annotate}
print("Hello, World!") # 这是一个注释。(1)
```

1.  这是一个注解。
////
///
/// tab | 隐藏注释
````markdown
```{.python .annotate}
print("Hello, World!") # 这是一个注释。(1)!
```

1.  这是一个注解。
````

//// html | div.result
```{.python .annotate}
print("Hello, World!") # 这是一个注释。(1)!
```

1.  这是一个注解。
////
///

有些地方虽然不支持注入语法，但是支持自定义类，因此也可以使用注解。例如，在内容块中使用注解：

/// tab | 警告
```markdown
/// note | 注
    attrs: { class: annotate }
这是一个内容块(1)。
///

1.  这是一个注解。
```

//// html | div.result
///// note | 注
      attrs: { class: annotate }
这是一个内容块(1)。
/////

1.  这是一个注解。
////
///
/// tab | HTML
```markdown
/// html | div.annotate
这是一个内容块(1)。
///

1.  这是一个注解。
```

//// html | div.result
///// html | div.annotate
这是一个内容块(1)。
/////

1.  这是一个注解。
////
///
/// tab | 标签
```markdown
/// tab | 标签1
这是一个内容块(1)。
///
/// tab | 标签2
    attrs: { class: annotate }
这是一个内容块(2)。
///

1.  这是一个注解。
2.  这是第二个注解。
```

//// html | div.result
///// tab | 标签1
这是一个内容块(1)。
/////
///// tab | 标签2
     attrs: { class: annotate }
这是一个内容块(2)。
/////

1.  这是一个注解。
2.  这是第二个注解。
////
///

你可以在注解中使用[内联语法](#一般内联语法)，以及使用另一个注解。例如：

```markdown
这是一个段落(1)。
{.annotate}

1.  这是一个注解。在注解底部缩进对齐使用`{ .annotate }`以在注解中添加注解。(1)
    { .annotate }

    1.  这里是第二个注解。
```

/// html | div.result
这是一个段落(1)。
{.annotate}

1.  这是一个注解。在注解底部缩进对齐使用`{ .annotate }`以在注解中添加注解。(1)
    { .annotate }

    1.  这里是第二个注解。
///


### 公式

### 图片

图片可以通过[注入](#注入特性)实现左右对齐、设置宽度和懒加载等，具体详见[Material for MkDocs图片参考文档](https://squidfunk.github.io/mkdocs-material/reference/images/#usage)。

### 按钮

### 图表

### 脚注

### 网格

### 工具提示