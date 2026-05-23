# 制作纹理包

这一页会做一个最简单的资源包：把原版泥土方块的纹理替换成你自己的图片。它不会添加新方块，只是利用资源栈覆盖同名资源，因此非常适合用来确认资源包结构和清单文件是否正确。

## 创建资源包

在`development_resource_packs`中创建文件夹`demo_texture_RP`，然后放入资源包清单文件：

```json title="demo_texture_RP/manifest.json"
{
  "format_version": 2,
  "header": {
    "name": "Demo Texture Pack",
    "description": "Replace the dirt texture.",
    "uuid": "填入第一个UUID",
    "version": [1, 0, 0],
    "min_engine_version": [1, 21, 80]
  },
  "modules": [
    {
      "type": "resources",
      "uuid": "填入第二个UUID",
      "version": [1, 0, 0]
    }
  ]
}
```

再创建纹理目录：

/// html | div.treeview
- `demo_texture_RP`
    - `manifest.json`
    - `textures`
        - `blocks`
            - `dirt.png`
///

`dirt.png`建议先使用16×16像素PNG图片。你可以画一个明显的纯色图案，这样进游戏后很容易判断是否覆盖成功。

## 为什么文件名必须相同

资源包覆盖原版资源时，游戏根据路径和文件名查找资源。这里把图片命名为`textures/blocks/dirt.png`，就是在覆盖原版同路径的泥土纹理。如果其他资源包加载在你的包之后，并且也提供了同名文件，后加载的包会覆盖你这个文件。

## 进游戏测试

1. 创建或打开一个测试世界。
2. 在资源包列表中激活`Demo Texture Pack`。
3. 进入世界并放置泥土方块。
4. 如果泥土仍然是原版纹理，退出世界再重新进入一次。

纹理和模型通常不适合依赖`/reload`热重载。你改完图片后，如果没有变化，先重进世界，再检查文件路径。

## 常见问题

- 包没有出现在列表里：检查`manifest.json`是不是合法JSON，两个UUID是否不同。
- 包出现了但纹理没变化：检查路径是否正好是`textures/blocks/dirt.png`。
- 只改了草方块侧面却没有生效：草方块不是单纯的`dirt.png`，它有自己的纹理和渲染规则。
- 图片边缘出现奇怪颜色：确认透明通道和像素尺寸，先用无透明的16×16图片排除问题。

完成这一页后，你已经理解了资源包最核心的覆盖机制。接下来可以继续学习本地化，让包名和游戏内内容显示更友好。
