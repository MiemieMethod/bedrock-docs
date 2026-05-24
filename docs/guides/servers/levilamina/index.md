# LeviLamina开发者指南

这里收录LeviLamina开发过程中最常见的实践型指南。建议先阅读[LeviLamina入门](../levilamina.md)，再按需要查阅下面的条目。

## 快速导航

### 开发基础
- [项目构建](build-guide.md) - 使用xmake构建LeviLamina模组。
- [命令注册](command-guide.md) - 编写自定义命令。
- [事件系统](event-guide.md) - 订阅和发布事件。

### 进阶技巧
- [找函数指南](find-function-guide.md) - 在BDS二进制中定位目标函数。
- [接口导出指南](interface-export-guide.md) - 导出模组中的函数和方法。
- [物品相关指南](item-guide.md) - 理解ItemStack、Item和同步注意事项。
- [表单开发](form-guide.md) - 创建交互式表单界面。
- [钩子系统](hook-guide.md) - 底层内存钩子和函数拦截。
- [协程使用](coro-guide.md) - 异步编程和协程。
- [国际化](i18n-guide.md) - 多语言支持。

### 教程
- [创建你的第一个模组](create-your-first-mod.md) - 从模板项目开始构建第一个模组。
- [发布你的第一个模组](publish-your-first-mod.md) - 准备`tooth.json`并发布模组。
- [发布你的第一个整合包](publish-your-first-pack.md) - 准备`tooth.json`并发布整合包。

### 相关资源
- [LeviLamina文档](../../docs/server/levilamina.md) - 概念和架构说明。
- [LeviLamina API参考](../../refs/server/levilamina-api.md) - 模块级API概览。
- [版本支持](../../translations/levilamina/versions.md) - 兼容的LeviLamina和BDS版本。
- [官方文档归档](../../translations/levilamina/index.md) - 原始资料脉络索引。

## 获取帮助

如果你遇到问题，请：

1. 查阅[LeviLamina FAQ](../../translations/levilamina/faq.md)。
2. 检查[常见错误码](../levilamina.md#常见错误码)。
3. 前往[LeviLamina官方文档](https://levilamina.liteldev.com)或[GitHub讨论区](https://github.com/LiteLDev/LeviLamina/discussions)寻求帮助。
