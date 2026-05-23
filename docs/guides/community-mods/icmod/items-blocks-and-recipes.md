# 物品、方块与配方

InnerCore的物品、方块与配方系统使用JavaScript或TypeScript脚本注册内容，并由资源目录提供纹理。这里的能力属于旧第三方客户端模组生态，不是国际版附加包原生格式。

/// warning | 不要混淆开发体系
本文出现的`IDRegistry`、`Item`、`Block`、`Recipes`等接口来自InnerCore/CoreEngine资料。它们不能直接用于官方附加包、国际版脚本API或服务端插件。
///

## 物品资源

物品纹理通常放在资源目录的`items-opaque`子目录中，文件名采用`纹理名_数据值.png`或`纹理名_数据值.tga`形式。资料以`oxidized_stick_0.png`为例；脚本中只引用不带扩展名和目录的纹理名，并用数据值选择变种。

```text
assets/resources/items-opaque/oxidized_stick_0.png
```

`build.config`中必须有资源目录描述，否则资源不会按模组资源加载：

```json title="build.config"
{
  "resources": [
    {
      "path": "assets/resources/",
      "resourceType": "resource"
    }
  ]
}
```

## 注册物品

资料中的第一个物品先注册翻译，再生成数值ID，最后创建物品。

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

`IDRegistry.genItemID`会为字符串标识符生成旧引擎内部使用的数值标识符。`ItemID.oxidized_stick`则提供该数值ID。资料说明，生成后的物品可能在游戏界面中表现为类似`minecraft:item_oxidized_stick`的形式。

默认物品会进入创造模式物品栏。若物品仅用于技术逻辑，可在附加参数中设置`isTech: true`。

## 物品行为

物品使用逻辑可通过专用函数绑定，也可直接监听回调。资料更推荐在能满足需求时使用专用函数，因为它已经处理了部分方块界面与方块实体交互判断。

```javascript
Item.registerUseFunction("oxidized_stick", function(coords, item, block, playerUid) {
  Entity.addVelocity(playerUid, 0, 0.5 * Math.random(), 0);
});
```

等价的直接回调需要自行判断物品ID：

```javascript
Callback.addCallback("ItemUse", function(coords, item, block, isExternal, playerUid) {
  if (item.id == ItemID.oxidized_stick) {
    Entity.addVelocity(playerUid, 0, 0.5 * Math.random(), 0);
  }
});
```

资料还介绍了投掷物、食物和盔甲：投掷物使用`Item.createThrowableItem`和`Item.registerThrowableFunction`，食物使用`Item.createFoodItem`和`FoodEaten`回调，盔甲使用`Item.createArmorItem`并提供部位、护甲值、耐久、击退抗性和穿戴纹理路径。

## 物品额外数据

InnerCore资料把物品上的额外数据称为`ItemExtraData`。它可保存字符串、整数、浮点数、布尔值、对象和长整数等数据，并通过`ItemInstance`的`extra`字段随物品传递。

```javascript
const extraData = new ItemExtraData();
extraData.putString("rune", "fire");

Entity.setCarriedItem(player, item.id, item.count, item.data, extraData);
```

读取时可提供默认值：

```javascript
const rune = item.extra ? item.extra.getString("rune", "unknown") : "unknown";
```

这种机制适合旧InnerCore物品的附加状态，例如随机符文、特殊耐久或自定义数据。新附加包项目不应照搬该接口。

## 配方

资料把配方分为无序配方、有序配方和烧炼配方。无序配方只要求输入物品集合；有序配方使用图案和掩码；烧炼配方使用熔炉输入、输出和可选燃料。

```javascript
Recipes.addShapeless({
  id: VanillaItemID.diamond,
  count: 1,
  data: 0
}, [
  { id: VanillaItemID.iron_ingot, data: 0 },
  { id: VanillaItemID.gold_ingot, data: -1 },
  { id: VanillaItemID.flint }
]);
```

```javascript
Recipes.addShaped2(VanillaItemID.sapling, 1, 0, [" l ", "lll", " o "], [
  "o", VanillaBlockID.log, 0,
  "l", VanillaBlockID.leaves, 0
]);
```

```javascript
Recipes.addFurnace(VanillaItemID.rotten_flesh, 0, VanillaItemID.leather, 0);
Recipes.addFurnaceFuel(VanillaBlockID.magma, 0, 400);
```

配方回调可修改结果、消耗输入或取消合成。资料特别提醒，配方和工作台事件会影响所有相关配方，处理时应先做简单判断。

## 方块资源

方块纹理通常放在`terrain-atlas`子目录。文件名仍使用`纹理名_数据值.png`形式；脚本中引用`["纹理名",数据值]`。

```text
assets/resources/terrain-atlas/log_oxidized_top_0.png
assets/resources/terrain-atlas/log_oxidized_side_0.png
```

方块的6个面按底面、顶面、背面、正面、左面、右面描述。资料指出，列表不足6项时，最后一项会重复用于剩余面。

```javascript
[
  ["crafting_table_bottom", 0],
  ["crafting_table_top", 0],
  ["crafting_table_front", 0],
  ["crafting_table_front", 0],
  ["crafting_table_side", 0]
]
```

## 注册方块

注册方块时同样先生成ID，再调用`Block.createBlock`。一个方块ID可包含多个变种，以节省旧版数值ID空间。

```javascript
IDRegistry.genBlockID("oxidized_log");
Block.createBlock("oxidized_log", [{
  name: "Oxidized Log",
  texture: [
    ["oxidized_log_top", 0],
    ["oxidized_log_top", 0],
    ["oxidized_log_side", 0]
  ],
  inCreative: true
}], "opaque");
```

第三个参数可为特殊类型名，也可为属性对象。资料列出的属性包括`base`、`material`、`sound`、`solid`、`renderlayer`、`lightlevel`、`lightopacity`、`explosionres`、`friction`、`destroytime`等。多个方块共用的属性可通过`Block.createSpecialType`注册。

## 液体与模型

液体由静止方块、流动方块和桶物品组合而成。资料使用`Block.createLiquidBlock`注册完整液体，并指出液体会设置自己的渲染层和渲染类型。

```javascript
Block.createLiquidBlock("ink", {
  name: "Ink",
  tickDelay: 30,
  still: {
    texture: ["ink", 0]
  },
  flowing: {
    texture: ["ink", 0]
  },
  bucket: {
    texture: { name: "bucket_ink", meta: 0 }
  },
  uiTextures: ["liquid_ink"]
});
```

复杂方块形状使用`BlockRenderer`和`ICRender`。模型由盒体组成，可设置静态渲染、碰撞箱、击中轮廓，也可在坐标上进行客户端映射。资料特别提醒：映射是客户端侧的，不应把它当作稳定的方块状态系统；简单旋转和状态变化优先使用方块变种。
