# EndstonePython插件工作流

这篇教程把文档中的“创建插件→安装插件→发布插件”三段流程串成一条可执行路线。你可以把它当成日常开发清单，按顺序做完就能从空项目走到可发布插件。

## 步骤1：先准备一个可复用环境

先创建虚拟环境并安装Endstone。后续写插件、调试插件、构建插件都在这个环境里完成：

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install endstone
```

Linux下激活命令改为`. venv/bin/activate`。

## 步骤2：创建项目并声明入口点

项目名建议使用`endstone-`前缀，包名用下划线风格。最小`pyproject.toml`如下：

```toml title="pyproject.toml"
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "endstone-my-plugin"
version = "0.1.0"
description = "My first Python plugin for Endstone servers!"

[project.entry-points."endstone"]
my-plugin = "endstone_my_plugin:MyPlugin"
```

然后实现插件主类并设置`api_version`。如果你的Endstone版本发生变化，记得同步调整这个值。

## 步骤3：优先使用可编辑安装

开发阶段最推荐的方式是：

```powershell
pip install --editable .
```

这样改完源码后，回到服务器执行`/reload`就能快速验证。只有当你要发版或交付给他人时，再构建轮子包。

## 步骤4：构建并安装到服务器

```powershell
pip install pipx
pipx run build --wheel
```

构建成功后，把`dist`目录中的`.whl`复制到服务器的{{file|plugins}}目录，重启服务器确认加载日志。

## 步骤5：发布前检查

准备发布时，至少检查这三件事：

1. `version`是否递增。
2. `api_version`是否与目标Endstone大版本兼容。
3. 入口点名是否等于项目名去掉`endstone-`前缀后的部分。

确认后再用`twine`上传到TestPyPI或PyPI。

## 延伸阅读

- [创建您的第一个插件（翻译）](../../../translations/endstone/tutorials/create-your-first-plugin.md)
- [安装您的插件（翻译）](../../../translations/endstone/tutorials/install-your-plugin.md)
- [发布您的插件（翻译）](../../../translations/endstone/tutorials/publish-your-plugin.md)