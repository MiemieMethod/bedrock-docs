# 脚本API<!-- md:flag vanilla -->

这一组教程只讲国际版附加包中的脚本API。它使用`@minecraft/server`等`@minecraft/*`模块，以JavaScript或TypeScript编写行为包脚本；它不讲中国版模组SDK，也不使用`mod.server.extraServerApi`或`mod.client.extraClientApi`。

如果你已经会制作普通行为包，这里就是从“写JSON配置”迈向“写程序逻辑”的入口。本组目前先让世界自动发出消息，再把项目升级为TypeScript工程；事件、多人游戏、安全调试和服务端部署适合在脚本入口跑通后继续补充。

/// html | div.grid.cards
- :material-language-javascript: __[构建第一个脚本](building-your-first-scripts.md)__
  从`manifest.json`中的脚本模块开始，创建`scripts/main.js`，用`system.runInterval`让世界每隔一段时间执行一次代码。
- :material-language-typescript: __[使用TypeScript构建包](building-packs-with-typescript.md)__
  使用Node.js、NPM和官方TypeScript启动项目，把`main.ts`编译并部署为Minecraft可加载的JavaScript。
///

## 开始前要知道什么

脚本API脚本属于行为包的一部分。行为包通过`manifest.json`声明一个`type`为`script`的模块，并通过`dependencies`声明它需要的`@minecraft/server`等脚本模块；脚本模块的`entry`字段指向入口文件，例如`scripts/main.js`。游戏加载世界和行为包后，会执行这个入口文件。

官方入门资料使用JavaScript解释脚本基础，并建议在更复杂的项目中使用TypeScript。TypeScript本身不会被Minecraft直接执行，它必须先编译为JavaScript；这样做的好处是可以获得类型检查、自动补全、内联参考文档和更早暴露的编译错误。

## 推荐学习顺序

1. 先完成[构建第一个脚本](building-your-first-scripts.md)，确认脚本模块能被世界加载。
2. 学会使用`/reload`重新加载脚本，并打开内容日志查看错误。
3. 再进入[使用TypeScript构建包](building-packs-with-typescript.md)，把项目迁移到可编译、可部署、可调试的工程结构。
4. 继续查阅脚本API参考时，优先确认模块名、模块版本和稳定性标记。预览版、测试版或实验性API可能在后续版本改变。

/// warning | 不要混用两个生态
国际版脚本API和中国版模组SDK都能写逻辑，但它们的运行环境、语言、包结构和接口名称完全不同。本系列中的`world.afterEvents`、`system.runInterval`、`@minecraft/server`只适用于国际版脚本API；中国版Python脚本请阅读[模组SDK](../modsdk/index.md)系列。
///