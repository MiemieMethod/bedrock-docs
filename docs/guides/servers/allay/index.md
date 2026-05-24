# Allay开发者指南

欢迎来到Allay插件开发指南！这里提供了详细的教程和示例，帮助你快速上手Allay服务端开发。

## 快速开始

在开始之前，请先阅读[Allay框架说明](../../docs/server/allay.md)了解基本概念和架构。

### 第一步：安装和配置

- [安装Allay](installation.md) - 获取Java环境、下载Allay服务端、运行第一个服务器

### 第二步：创建第一个插件

- [创建第一个插件](first-plugin.md) - 使用JavaPluginTemplate创建基础插件项目

### 第三步：学习核心功能

## 核心功能教程

### 命令与事件
- [注册命令](command-guide.md) - 实现自定义命令、参数、权限和错误处理
- [事件系统](event-guide.md) - 监听游戏事件并在插件中处理

### 异步编程
- [任务调度](schedule-guide.md) - 使用调度器运行异步任务，了解多线程作用域

### UI交互
- [表单开发](form-guide.md) - 创建交互式表单和菜单界面
- [Boss栏](bossbars-guide.md) - 显示Boss血条和自定义进度条

### 游戏数据

- [方块API](block-guide.md) - 与方块状态、属性和容器交互
- [物品API](item-guide.md) - 管理物品栏、物品堆叠和物品数据
- [容器API](container-guide.md) - 创建自定义容器和操作物品

### 玩家与配置

- [权限系统](permission-guide.md) - 设计和管理权限树
- [配置文件](config-guide.md) - 使用YAML配置管理插件参数
- [国际化](i18n-guide.md) - 实现多语言支持
- [记分板](scoreboard-guide.md) - 使用记分板显示数据和排行

### 高级主题

- [数据持久化](persistent-data-guide.md) - 使用数据容器保存自定义数据
- [自定义方块](custom-block-guide.md) - 创建带有自定义渲染的方块
- [自定义物品](custom-item-guide.md) - 创建带有自定义渲染的物品
- [绘图形状](primitive-shapes-guide.md) - 使用调试形状进行客户端渲染

## 服务器配置

- [使用Terra世界生成器](terra-guide.md) - 集成Terra插件实现自定义地形生成

## 常见问题与故障排除

遇到问题？请查阅：
- [Allay框架说明中的FAQ](../../docs/server/allay.md#常见问题与限制)
- [Allay官方文档](https://docs.allaymc.org/)
- [GitHub Discussions](https://github.com/AllayMC/Allay/discussions)

## 相关资源

- [Allay框架概述](../../docs/server/allay.md) - 架构、线程模型、插件系统详解
- [Allay API参考](../../refs/server/allay-api.md) - API模块概览
- [Allay源码仓库](https://github.com/AllayMC/Allay)
- [官方插件中心](https://hub.allaymc.org/)
