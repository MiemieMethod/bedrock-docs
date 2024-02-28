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

本文档使用Markdown语法编写。如果您不熟悉Markdown语法，可以参考[这篇文章](https://www.markdownguide.org/basic-syntax/)，或这篇[中文文章](https://markdown-zh.readthedocs.io/en/latest/)。此外，您还可以参考[Material for MkDocs的文档](https://squidfunk.github.io/mkdocs-material/reference/)以了解更多关于Material for MkDocs的独有语法，以及参考[PyMdown Extensions的文档](https://facelessuser.github.io/pymdown-extensions/)以了解更多关于PyMdown Extensions提供的额外语法。本站加载有所有PyMdown Extensions提供的提供的扩展，请编者放心使用。

