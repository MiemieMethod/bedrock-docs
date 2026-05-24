# 第一个物品

/// details-info | 署名信息
- 该页面内容翻译自[nernar.github.io](https://nernar.github.io/docs/items/first-item)
- 原文档采用[GNU通用公共许可证第3版](https://www.gnu.org/licenses/gpl-3.0.html)（GPL-3.0）授权
///

原文档将物品创建过程分为四步：贴图准备、ID注册、物品创建和交互绑定。

## 贴图与目录

- 贴图格式通常为`png`或`tga`。
- 物品贴图放入资源目录的`items-opaque`子目录。
- 贴图名通常使用`纹理名_数据值`形式，例如`oxidized_stick_0.png`。

## 注册流程示例

```javascript
IDRegistry.genItemID("oxidized_stick");
Item.createItem("oxidized_stick", "item.oxidized_stick.name", {
  name: "oxidized_stick",
  data: 0
}, {
  stack: 64
});
```

## 事件绑定示例

```javascript
Item.registerUseFunction("oxidized_stick", function(coords, item, block, playerUid) {
  Entity.addVelocity(playerUid, 0, 0.5 * Math.random(), 0);
});
```

## 注意事项

- 建议优先使用针对物品的专用注册函数，减少通用回调中的重复判断。
- 不应在高频事件中执行过重逻辑，以免旧设备出现明显卡顿。
