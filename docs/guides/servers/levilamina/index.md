# LeviLamina开发者指南

这里收录LeviLamina官方开发者指南在本站中的实践性落位。建议先阅读[LeviLamina入门](../levilamina.md)，再按官方目录顺序查阅下面的条目。

## 使用前提

本页默认读者已经能够启动至少一个受支持的LeviLamina环境。如果尚未完成这一点，应先补齐以下前置步骤：

1. 在[支持的版本](../../../translations/levilamina/versions.md)中确认BDS、客户端和LeviLamina版本匹配。
2. 按目标环境完成[在服务器上安装](../../../translations/levilamina/install-server.md)或[在客户端上安装](../../../translations/levilamina/install-client.md)。
3. 需要理解官方首页与仓库首页分工时，再对照[官方文档首页](../../../translations/levilamina/official-docs-home.md)和[仓库README](../../../translations/levilamina/repository-readme.md)。
4. 环境可启动后，再回到本页选择构建、命令、事件或发布等专题。

## 快速导航

### 教程
- [创建你的第一个模组](create-your-first-mod.md) - 从模板项目开始构建第一个模组。
- [发布你的第一个模组](publish-your-first-mod.md) - 准备`tooth.json`并发布模组。
- [发布你的第一个整合包](publish-your-first-pack.md) - 准备`tooth.json`并发布整合包。

### 如何做到……
- [事件系统](event-guide.md) - 订阅和发布事件。
- [接口导出指南](interface-export-guide.md) - 导出模组中的函数和方法。
- [找函数指南](find-function-guide.md) - 在BDS二进制中定位目标函数。
- [表单开发](form-guide.md) - 创建交互式表单界面。
- [钩子系统](hook-guide.md) - 底层内存钩子和函数拦截。
- [国际化](i18n-guide.md) - 多语言支持。
- [物品相关指南](item-guide.md) - 理解ItemStack、Item和同步注意事项。
- [命令注册](command-guide.md) - 编写自定义命令。
- [协程使用](coro-guide.md) - 异步编程和协程。
- [项目构建指南](build-guide.md) - 使用xmake构建LeviLamina模组。

### 相关资源
- [LeviLamina](../../../docs/server/levilamina.md) - 概念和架构说明。
- [LeviLamina API模块](../../../refs/server/levilamina-api.md) - 模块级API概览。
- [官方文档首页](../../../translations/levilamina/official-docs-home.md) - 查看官方文档站首页承担的入口职责。
- [常见问题](../../../translations/levilamina/faq.md) - 查看项目起源与更名缘由。
- [支持的版本](../../../translations/levilamina/versions.md) - 兼容的LeviLamina和BDS版本。
- [仓库README](../../../translations/levilamina/repository-readme.md) - 查看仓库落地页承担的安装、贡献与许可证入口职责。
- [法律与发布说明](../../../translations/levilamina/legal-release-notes.md) - 区分许可证、EULA与更新风险。
- [LeviLamina文档归档](../../../translations/levilamina/index.md) - 原始资料脉络索引。

## 获取帮助

如果你遇到问题，请：

1. 先查阅[问题排除](../../../translations/levilamina/troubleshooting.md)。
2. 再对照[常见问题](../../../translations/levilamina/faq.md)与[支持的版本](../../../translations/levilamina/versions.md)。
3. 检查[常见错误码](../levilamina.md#常见错误码)。
4. 前往[LeviLamina官方文档](https://levilamina.liteldev.com)或[GitHub讨论区](https://github.com/LiteLDev/LeviLamina/discussions)寻求帮助。
