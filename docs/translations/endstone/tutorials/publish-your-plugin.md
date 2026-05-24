# 发布您的插件

假设您已完成新版本的所有工作，编写了发布说明，增加了版本号，标记了发布，并准备发布。

## 安装`twine`

如果您还没有这样做，您将需要安装[Twine]。[Twine]是一个用于将Python包发布到PyPI和其他存储库的实用程序。

```shell
pip install twine
```

## 构建您的包

构建您的包就像一行命令一样简单。

```shell
pipx run build
```

这将在隔离的环境中构建包，在`dist/`目录中生成源分布和wheel。

## 上传到[TestPyPI]

与是所有python包的实际索引的[PyPI]不同，[TestPyPI]是Python Package Index的单独实例。这是在不影响真实索引的情况下尝试分发工具和流程的好地方。

由于[TestPyPI]与实时[PyPI]有单独的数据库，您需要专门为TestPyPI创建的单独用户帐户。前往https://test.pypi.org/account/register/来注册您的帐户。

完成后，您可以通过指定`--repository`/`-r`标志使用twine将分发上传到[TestPyPI]：

```shell
twine upload -r testpypi dist/*
```

Twine将提示输入您的**API令牌**或用户名和密码。

!!! tip
    出于安全原因，强烈建议在将包上传到PyPI时**创建API令牌**而不是使用用户名和密码。如果您还没有这样做，请在[PyPI](https://pypi.org/manage/account/token/)和[TestPyPI](https://test.pypi.org/manage/account/token/)上创建一个API令牌。您还将被要求选择此令牌的范围，目前您可以将令牌保留为不受限制。

## 上传到[PyPI]

现在，如果一切看起来都对，您可以上传到实际的Python Package Index - [PyPI]：

```shell
twine upload -r pypi dist/*
```

## 使用GitHub Actions CI/CD工作流发布

GitHub Actions CI/CD允许您在GitHub平台上发生事件时运行一系列命令。如果您想在每次创建发布时自动将您的插件发布到PyPI，这将是一个很好的选择。

有关更多信息，请按照[说明](https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/)进行操作。

## 就是这样！

**:partying_face: 恭喜！** 如果一切顺利，您应该很快就能在`https://pypi.org/project/<package name>`上看到您的插件。


[Twine]: https://twine.readthedocs.io/

[PyPI]: https://pypi.org/

[TestPyPI]: https://test.pypi.org/
