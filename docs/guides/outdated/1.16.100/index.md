# 1.16.100

1.16.100附近的旧教程在今天仍有两个常见用途：读懂早期新版物品格式，以及读懂PBR纹理集示例。它不应该作为新项目的整体目标版本，但某些文件格式示例仍会出现`"format_version": "1.16.100"`。

## 先分清“旧版本”和“仍被使用的格式版本”

基岩版很多文件都有自己的`format_version`。它不总是等同于当前游戏版本。Microsoft Learn的当前平台版本指南说明，某些文件类型的现代格式版本会停留在较早版本，不能只凭数字判断它已经废弃。

因此，看到`1.16.100`时先问两个问题：

1. 这个文件类型的当前官方示例是否仍使用它？
2. 这个文件是否依赖旧实验性接口或已迁移的行为？

如果答案是前者，它可能只是历史格式号；如果答案是后者，就应迁移。

## 纹理集中的1.16.100

PBR纹理集文档仍会给出这样的示例：

```json
{
  "format_version": "1.16.100",
  "minecraft:texture_set": {
    "color": "grass_carried",
    "metalness_emissive_roughness": "grass_carried_mer",
    "heightmap": "grass_carried_heightmap"
  }
}
```

这类文件放在纹理旁边，用来把颜色、MER、法线或高度图组合为一个纹理集。维护旧RTX包时，经常会看到它。

迁移到Vibrant Visuals时要注意：

- 可以继续理解MER：红色是金属度，绿色是自发光，蓝色是粗糙度。
- 如果要使用次表面散射，应改用支持MERS的更新纹理集格式。
- 不要同时定义`normal`和`heightmap`。
- 不要同时定义`metalness_emissive_roughness`和`metalness_emissive_roughness_subsurface`。

## 旧物品格式语境

旧版Bedrock Wiki记录过1.16.100.56测试版引入的新物品格式。该格式示例把物品写在行为包`items`目录，并在`description`中使用`identifier`和`category`，组件中可写食物、使用时长、使用动画等内容。

旧资料还记录了一个重要变化：物品行为文件需要`category`才会显示在`/give`命令和创造物品栏中；资源包侧的旧物品文件不再按旧方式使用，图标等资源侧内容也不应再按旧资源包物品定义照搬，应回到当前物品组件和资源引用规则中重新确认。

这类知识适合用来读旧项目，不适合直接作为最新版物品教程。新物品应回到最新版附加包教程和当前参考资料中确认字段。

## 维护建议

1. 对纹理集文件，先检查内容日志是否有`CONTENT_ERROR`。
2. 对物品文件，先确认当前游戏是否仍接受组件和事件写法。
3. 若旧教程要求开启已经改名或移除的实验性开关，不要照抄，改查当前版本说明。
4. 如果只是为了PBR纹理集示例，可以优先阅读[使用并自定义延迟渲染](../../shaders/getting-started-with-deferred-lighting.md)。

## 相关页面

- [物品与方块格式迁移](item-block-format-migration.md)
