# ICMod

ICMod这里指以InnerCore、CoreEngine和Horizon为中心的Android客户端模组开发方式。Nernar维护的InnerCore文档说明，InnerCore扩展Android版Minecraft的基础功能，用于创建会改变玩法的模组；它的思路与BlockLauncher相近，但模组不再只是单个脚本，而是一个带构建配置、脚本、资源、图标和设置的完整文件夹。

/// warning | 历史生态
InnerCore不是Mojang当前提供的国际版原生能力，也不等同于附加包、脚本API或服务器插件。这里的内容主要用于维护旧Android客户端模组、理解早期社区模组生态，以及将旧项目迁移到更现代的开发方式。
///

/// html | div.grid.cards
- :material-package-variant: __[准备环境与项目结构](environment-and-structure.md)__
  说明Horizon、InnerCore、CoreEngine、项目目录、构建配置和脚本生命周期。
- :material-cube-outline: __[物品、方块与配方](items-blocks-and-recipes.md)__
  整理物品、方块、纹理、液体、渲染模型、配方和物品额外数据。
- :material-sync-circle: __[事件、存储与多人](events-storage-and-multiplayer.md)__
  说明回调、可更新对象、配置、保存、客户端/服务端包和多人安全边界。
- :material-shape-outline: __[界面、环境与库](ui-environment-and-libraries.md)__
  说明旧界面系统、世界访问对象、粒子、维度资料状态，以及第三方库的定位。
///

## 模组结构

一个典型模组文件夹包含这些内容：

/// html | div.treeview
- 模组文件夹
    - `.dex`
    - `dev`
        - `.includes`
        - `header.js`
    - `assets`
        - `resources`
            - `terrain-atlas`
            - `items-opaque`
        - `gui`
    - `launcher.js`
    - `build.config`
    - `mod.info`
    - `mod_icon.png`
    - `config.json`
    - `config.info.json`
///

其中`build.config`描述加载、编译和构建流程；`dev`通常放主要脚本；`assets`放资源；`mod.info`提供模组名、作者、版本和简介；`config.json`保存设置，默认可包含`enabled`来控制模组是否启用。

## 第一个物品

InnerCore物品教程从贴图、资源路径和注册脚本开始。物品贴图通常放在资源目录的`items-opaque`子文件夹中，文件名采用`纹理名_数据值.png`形式。注册物品时，先为字符串标识符生成数值ID，再创建物品。

```javascript title="dev/oxidized_stick.js"
Translation.addTranslation("item.oxidized_stick.name", {
  en: "Oxidized Stick"
});

IDRegistry.genItemID("oxidized_stick");

Item.createItem("oxidized_stick", "item.oxidized_stick.name", {
  name: "oxidized_stick",
  data: 0
}, {
  stack: 64
});
```

教程资料说明，生成后的物品在游戏中会表现为类似`minecraft:item_oxidized_stick`的形式；`ItemID`对象则提供由`IDRegistry.genItemID`生成的数值标识符。

## 绑定交互逻辑

给物品添加功能时，可以使用`Item.registerUseFunction`：

```javascript
Item.registerUseFunction("oxidized_stick", function(coords, item, block, playerUid) {
  Entity.addVelocity(playerUid, 0, 0.5 * Math.random(), 0);
});
```

也可以直接使用回调系统：

```javascript
Callback.addCallback("ItemUse", function(coords, item, block, isExternal, playerUid) {
  if (item.id == ItemID.oxidized_stick) {
    Entity.addVelocity(playerUid, 0, 0.5 * Math.random(), 0);
  }
});
```

InnerCore文档建议不要在事件回调内部反复注册新的回调，否则每次事件发生都会叠加新的处理器。它还提醒开发者在事件中先做简单判断，再执行昂贵逻辑，因为多个模组同时运行时性能压力会叠加。

## 和BlockLauncher的差异

InnerCore文档把BlockLauncher视为相近平台，并指出InnerCore相较旧BlockLauncher生态的关键差异：模组是完整文件夹，脚本可以有多个执行上下文并共享全局空间；资源由配置文件决定加载方式；可以在模组中使用Java和原生代码；多数情况下不需要提前手动编译，加载器或工具链会处理构建。

## 继续学习路线

1. 先读准备环境、模组结构和构建配置。
2. 再做第一个物品、第一个方块和基础配方。
3. 学回调、可更新对象、保存和网络包。
4. 最后再研究旧界面、世界访问对象、粒子、维度和第三方库。

/// warning | 兼容性优先
ICMod生态依赖特定客户端和加载器环境。开始维护旧项目之前，先确认目标Minecraft版本、InnerCore版本和所需库版本。
///

## 资料状态

Nernar维护的InnerCore文档同时包含英文教程、俄文翻译、库文档、变更记录和站点工程文件。英文教程中有一部分页面仅含“未本地化”占位，维度、生物群系、方块实体、发布和部分库资料并不完整。因此，本组页面只整理已有且可核验的内容；缺失处会明确标注为资料不足，不补写未经资料支持的API细节。