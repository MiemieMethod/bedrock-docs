# 罗盘方位显示

这是一个很轻量的动作栏罗盘模板，通过`ry`和`rym`把朝向映射成8个方位文本。

![罗盘演示](../../../assets/images/guides/misc/compass-display/demo.gif)
<!-- 图片获取方式：从知识库源文件compass-display.md中的demo.gif提取。 -->

## 命令模板

```mcfunction title="BP/functions/wiki/displays/compass.mcfunction"
title @a[rym=157.5,ry=-157.5] actionbar 北(N)
title @a[rym=-22.5,ry=22.5] actionbar 南(S)
title @a[rym=-112.5,ry=-67.5] actionbar 东(E)
title @a[rym=67.5,ry=112.5] actionbar 西(W)
title @a[rym=-157.5,ry=-112.5] actionbar 东北(NE)
title @a[rym=112.5,ry=157.5] actionbar 西北(NW)
title @a[rym=-67.5,ry=-22.5] actionbar 东南(SE)
title @a[rym=22.5,ry=67.5] actionbar 西南(SW)
```

/// tip | 条件触发
可以把这组命令与[移动状态检测](./detect-movements.md)或`hasitem`条件联动，只在特定状态显示罗盘。
///

## 继续阅读

- [目标选择器](../../docs/general/target-selector.md)
- [移动状态检测](./detect-movements.md)
