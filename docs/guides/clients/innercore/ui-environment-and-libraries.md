# 界面、环境与库

Nernar维护的InnerCore文档还包含旧界面系统、区块源、粒子、维度、库和变更记录资料。本页只整理知识库中正文较完整的部分，并明确说明资料不足之处。

## 世界访问对象

InnerCore资料使用`BlockSource`表示对世界区域的访问。它按维度或上下文取得，适合读取和修改方块、实体与环境。

```javascript
const region = BlockSource.getDefaultForDimension(EDimension.NORMAL);
```

若已知活动对象，可根据活动对象取得对应维度的区块源：

```javascript
Callback.addCallback("EntityAdded", function(entity) {
  const region = BlockSource.getDefaultForActor(entity);
});
```

世界生成事件中应使用专门的生成上下文；客户端侧只能使用客户端上下文读取或显示相关信息。资料强调，客户端侧修改不会成为服务端世界状态。

常见操作包括放置方块、读取方块ID、读取方块状态、设置额外方块、生成实体和查询区域。资料中的例子使用`setBlock`、`getBlockId`、`getBlock`和`setExtraBlock`演示了这些能力。

```javascript
region.setBlock(x, y, z, VanillaTileID.dirt);
const id = region.getBlockId(x, y, z);
const state = region.getBlock(x, y, z);
```

额外方块与物品额外数据没有关系。资料把它描述为世界中另一层方块，典型用途是液体含水，也可用于旧结构组合，但有自己的破坏和交互限制。

## 粒子

粒子是客户端显示内容。资料建议优先使用全局粒子发射方式，只有复杂需求才考虑更复杂的发射器系统。

```javascript
Particles.addParticle(type, x, y, z, velX, velY, velZ, data);
Particles.addFarParticle(type, x, y, z, velX, velY, velZ, data);
```

粒子图案通常通过循环生成，例如圆、线、螺旋或爆炸。由于粒子是客户端内容，多人环境中应由服务端判断结果，再通过客户端包通知需要看到效果的玩家。

## 旧界面系统

InnerCore资料中的UI系统以窗口、背景绘制和元素为核心。元素写在窗口描述对象的`elements`字段中，每个元素有类型、坐标和交互处理函数。

```javascript
new UI.Window({
  elements: {
    label: {
      type: "text",
      x: 20,
      y: 40,
      text: "Hello"
    }
  }
});
```

坐标和尺寸使用旧UI单位，资料说明可理解为窗口宽度的千分比。元素可通过`z`设置叠放深度，并可处理`onClick`、`onLongClick`和`onTouchEvent`。常见元素包括图片、文本、按钮、槽位和其他交互控件。

/// warning | 旧界面资料仅用于维护
这些UI对象属于InnerCore旧客户端界面系统。它们不等同于官方JSON UI，也不等同于现代Ore UI或附加包界面格式。
///

## 维度与世界生成

Nernar文档包含自定义维度、生物群系、生成器和矿石生成主题，但英文正文中有多篇仍是“未本地化”占位。可核验的资料只支持以下结论：

- InnerCore变更记录说明，Horizon时代的InnerCore曾改进自定义维度，使维度成为独立世界，而不只是普通世界中的特殊区域。
- 后续版本继续添加维度属性、天气、天空、迷雾颜色、生成器和维度传送相关修复。
- 手动矿石生成资料强调：生成通常需要选择表面、检查条件、放置方块，并注意伪随机、种子相关随机和噪声图之间的差异。
- 生成逻辑必须控制性能开销，避免在生成事件中进行过量计算。

由于知识库中缺少完整英文维度教程，本页不提供自定义维度API步骤。需要维护旧项目时，应回到原项目代码和对应InnerCore版本的API参考核对。

## 库

资料源中有大量库页面，包括BackpackAPI、BetterFoliage、RecipeViewer、KernelExtension、Component、DungeonUtility、Fireflies、Timer、Translate、TreeCapitator和VeinMiner等。其中相当一部分英文页面只有“未本地化”占位，俄文页面较完整但与英文正文存在覆盖差异。

这些库更适合作为旧项目依赖清单和迁移线索，而不是本站当前手动维护的API参考。创建新页面前至少需要确认：

1. 库是否仍可下载。
2. 目标InnerCore版本是否兼容。
3. 库许可证是否允许翻译或整理。
4. 旧项目是否确实依赖该库。

### KernelExtension

KernelExtension资料较完整。它是InnerCore的模组库，用于向Java和JavaScript模组暴露InnerCore本体没有直接导出的能力。资料给出两种接入方式：在主脚本中监听`ModAPI.addAPICallback`，或在`launcher.js`中监听并在可用时再`Launch`，从而让模组强依赖该库。

```javascript
ModAPI.addAPICallback("KernelExtension", function(api) {
  // api是KernelExtension暴露的命名空间。
});
```

```javascript title="launcher.js"
ConfigureMultiplayer({
  name: "KEX-Dependent mod",
  version: "1.0",
  isClientOnly: false
});

ModAPI.addAPICallback("KernelExtension", function(api) {
  if (typeof api.getKEXVersionCode === "function" && api.getKEXVersionCode() >= 300) {
    Launch({ KEX: api });
  }
});
```

TypeScript项目还可使用相应声明文件获得补全和文档提示。由于该库强依赖旧InnerCore生态，本页仅记录接入模式，不把它整理为本站通用参考。

## 变更记录的含义

变更记录显示，InnerCore曾经历从旧独立应用到Horizon包的转变，并在后期加入或修复多人、64位架构、自定义维度、代码生成API、方块与物品命名空间、Java接口暴露、声音控制和模组浏览器等能力。这些信息有助于判断旧模组为什么依赖某个版本，但不能直接证明这些能力在现代官方基岩版中存在。
