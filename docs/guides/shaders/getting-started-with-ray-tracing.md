# 启用光线追踪并制作PBR包<!-- md:flag vanilla -->

RTX光线追踪是国际版较早公开的PBR路线。它仍受支持，但文档已经提示它很大程度上被Vibrant Visuals取代。现在学习这条路线，主要是为了维护旧RTX资源包，或理解PBR纹理集在光线追踪模式中的表现。

## 硬件和版本要求

官方光线追踪入门文档列出的最低环境包括：

- Windows64位系统。
- 支持DirectX硬件光线追踪的GPU，例如NVIDIA GeForce RTX20系列及更高，或AMD Radeon RX6000系列及更高。
- 至少8GB内存。
- Minecraft1.16.200或更高版本。

VR和MR头显不受支持。即使资源包格式正确，设备不满足要求时也无法启用光线追踪图形模式。

## 先体验官方市场内容

如果你的设备满足要求，最稳妥的第一步不是自己写包，而是在市场中下载带RTX标识的免费世界。进入世界后确认：

1. 视频设置中能启用光线追踪。
2. 金属、玻璃、发光方块和阴影表现正常。
3. 设备帧率和温度可接受。

这样做可以先排除硬件和游戏设置问题，再调试自己的资源包。

## 制作最小PBR纹理集

RTX资源包和Vibrant Visuals都使用纹理集。以铁块镜面效果为例：

/// html | div.treeview
- RP
    - textures
        - blocks
            - {/{file|iron_block.png}}
            - {/{file|iron_block_mer.png}}
            - {/{file|iron_block.texture_set.json}}
///

`iron_block.texture_set.json`：

```json
{
  "format_version": "1.16.100",
  "minecraft:texture_set": {
    "color": "iron_block",
    "metalness_emissive_roughness": "iron_block_mer"
  }
}
```

要得到镜面感，思路是：

- 粗糙度接近`0.0`，也就是MER蓝色通道接近黑色。
- 金属度接近`1.0`，也就是MER红色通道接近白色。
- 自发光保持`0.0`，也就是MER绿色通道保持黑色。

/// note | RTX只使用MER
纹理集参考文档说明，`metalness_emissive_roughness_subsurface`中的次表面散射只受Vibrant Visuals支持，RTX不会使用该字段。
///

## 在清单中声明能力

为了让游戏按PBR资源处理你的包，在`manifest.json`中加入能力声明。旧RTX包通常使用`"raytraced"`；如果同一个包也要面向Vibrant Visuals，可以同时考虑`"pbr"`，但要在目标版本中实际测试。

```json
"capabilities": [
  "raytraced"
]
```

如果你是从新项目开始，并且目标不是RTX专用设备，优先回到[使用并自定义延迟渲染](getting-started-with-deferred-lighting.md)使用`"pbr"`路线。

## 测试顺序

1. 把资源包放入`development_resource_packs`。
2. 进入一个支持RTX的世界。
3. 启用你的资源包。
4. 开启光线追踪。
5. 放置被修改的方块。
6. 调整MER纹理后重新进入世界查看效果。

如果没有效果，先看内容日志是否报告纹理集错误。纹理集无效时，游戏会记录`CONTENT_ERROR`并忽略它。常见原因包括缺少`color`层、同时定义法线和高度图、同时定义MER和MERS、引用的纹理不存在，或图像通道数量不符合要求。

## 何时迁移到Vibrant Visuals

如果你希望资源包覆盖方块以外的实体、物品和粒子PBR，或希望控制水、大气、色彩分级和本地光照，应迁移到Vibrant Visuals路线。RTX路线的优势在于兼容既有光线追踪资源和特定玩家设备，而不是作为新项目的默认选择。