# bedrock-docs

[![Built with Material for MkDocs](https://img.shields.io/badge/Material_for_MkDocs-526CFE?style=for-the-badge&logo=MaterialForMkDocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)

## 贡献

克隆本仓库至本地。复制`tools`文件夹，粘贴至`docs`文件夹的根目录上。

在控制台中运行如下命令以安装依赖：

```shell
pip install mkdocs-material[recommended,git,imaging]
pip install mkdocs-rss-plugin
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-git-committers-plugin-2
pip install mkdocs-minify-plugin
pip install mkdocs-glightbox
``` 

然后在控制台中使用`python -m mkdocs serve --dirtyreload`命令即可在[http://127.0.0.1:8000/bedrock-docs/](http://127.0.0.1:8000/bedrock-docs/)实时看到做出的更改。

提交并推送更改后，可以在[https://miemiemethod.github.io/bedrock-docs/](https://miemiemethod.github.io/bedrock-docs/)查看更改后的效果。

