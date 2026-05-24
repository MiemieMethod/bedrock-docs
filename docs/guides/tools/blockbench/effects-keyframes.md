# 粒子与音效关键帧

Blockbench可以在动画时间轴中预览粒子、音效和指令关键帧，并把它们导出到基岩版动画文件。该功能只负责制作和导出动画数据；粒子文件、音效定义和客户端实体引用仍然需要在资源包中正确配置。

## 启用效果动画器

在动画模式中，点击时间轴上方的**Animate Effects**按钮即可显示效果动画器。效果动画器通常包含三类关键帧：

| 类型 | 用途 |
|------|------|
| 粒子关键帧 | 在指定时间触发粒子特效。 |
| 音效关键帧 | 在指定时间播放音效。 |
| 指令关键帧 | 在指定时间执行Molang表达式，常用于修改变量。 |

粒子关键帧可以指定定位器，使粒子跟随模型中的某个点。定位器适合放在手部、口部、喷口、脚底等需要精确发射位置的骨骼下。

## 在Blockbench中预览

选中效果关键帧后，可以在关键帧面板中选择预览文件。音效预览需要`.ogg`文件；粒子预览需要粒子JSON文件。桌面版在文件更新后通常能重新加载粒子效果；网页版或音效文件可能需要重新选择文件。

预览只说明Blockbench能找到并显示该文件，不代表游戏中已经完成资源注册。导入游戏前仍应检查资源包路径、标识符、短名称和内容日志。

## 在资源包中注册效果

基岩版客户端实体文件需要在`description`中把效果登记为短名称。粒子特效写入`particle_effects`，音效写入`sound_effects`。短名称只在当前客户端实体文件内使用。

```json title="entity/example.entity.json" hl_lines="7-12"
{
  "format_version": "1.10.0",
  "minecraft:client_entity": {
    "description": {
      "identifier": "demo:example",
      "...": "...",
      "particle_effects": {
        "spark": "demo:spark"
      },
      "sound_effects": {
        "step_custom": "demo.step"
      }
    }
  }
}
```

粒子特效的完整标识符来自`particles`目录中的粒子文件。音效的完整标识符来自`sounds\sound_definitions.json`。例如：

```json title="sounds/sound_definitions.json"
{
  "format_version": "1.14.0",
  "sound_definitions": {
    "demo.step": {
      "category": "neutral",
      "sounds": [
        "sounds/demo/step"
      ]
    }
  }
}
```

## 在关键帧中填写短名称

资源包注册完成后，在Blockbench的效果关键帧中填写短名称，例如`spark`或`step_custom`。导出的动画文件会在对应时间点引用这些短名称，游戏再通过客户端实体文件把短名称解析为完整粒子或音效标识符。

/// tip | 调试顺序
如果效果在游戏中没有出现，先确认动画本身是否播放，再检查客户端实体是否登记了短名称，最后检查粒子文件或`sound_definitions.json`是否存在标识符错误。
///