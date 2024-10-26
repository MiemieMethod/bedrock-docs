---
标题：什么是脚本 API？
类别：常规
导航顺序：2
提及：
    - ConsoleTerm
    - Herobrine643928
    - JaylyDev
    - SmokeyStack
    - ThomasOrs
    - gdm3
描述：脚本到底是什么！？
---

::: 警告
脚本 API 目前正在积极开发中，破坏性更改频繁。此页面假设使用 Minecraft 1.21.20 的格式。
:::

## API

API 代表应用程序编程接口（Application Programming Interface），它是一种在两个应用程序之间建立联系的方式。应用程序这个术语包含的内容远超你想象的。一个应用程序可以是一个简单的脚本、一个游戏，或者整个操作系统。

你经常遇到的一个 API 就在你面前，它是应用程序与操作系统之间的接口。屏幕上的光标就是这个 API。为什么这与 API 有关？因为应用程序可以通过操作系统提供的 API 知道光标在屏幕上的位置，而无需实现自己的光标。这使得像 Minecraft 这样的程序能够使用 API 系统，从而让我们看到应用程序。

总结：API 是两个或多个应用程序之间的一种相互或单向交互！

## 脚本 API

也许你已经在某个地方听说过“脚本 API”这个术语。了解这个名称背后隐藏的内容是很重要的。

当听到这个术语时，很多人会想象出不同的东西，比如程序、脚本，甚至编程语言（《Minecraft 中的神秘实验？:]》），但实际上，它只是一个 API。API 是一组函数，允许我们与 Minecraft 进行交互。我们可以接收事件、读取方块、修改实体、创建粒子等等！这个 API 在[官方网站](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/minecraft-server)上也有详细文档。

## API 模块？

API 根据功能划分为其他子模块。有些 API 函数可能对普通用户不太安全，因此仅在服务器上允许使用，或者在某些设备上无法工作。为此，我们有不同的 API 函数包，称为模块。

模块应根据其包含的功能命名。

[原始作者](https://github.com/JaylyDev/ScriptAPI/tree/main/docs/MinecraftApi#readme) - 作者 [ConMaster2112](https://github.com/ConsoleTerm)