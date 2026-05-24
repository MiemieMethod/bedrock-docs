# 杂项教程

杂项教程用于收纳不适合放入某一条主线、但仍然有实践价值的内容。这里的页面不应该变成“什么都能放”的垃圾桶；如果某个主题已经能归入附加包、工具、着色器、服务端或过时教程，就应优先放到对应系列中。

## 什么内容适合放在这里

- 横跨多个主线，但篇幅不足以单独成为系列的实践流程。
- 与开发习惯、项目组织、排查顺序有关的教程。
- 不依赖某个具体API版本的通用建议。
- 暂时没有合适目录，但未来可能会拆分到正式系列的内容。

## 什么内容不应放在这里

- 已经过时但仍有兼容性价值的教程。它们应放到[过时教程](../outdated/index.md)。
- 某个工具的教程。它们应放到[软件工具](../tools/index.md)。
- 某个渲染管线的教程。它们应放到[着色器](../shaders/index.md)。
- API参考。它们应放到参考品类，而不是教程品类。

## 建议的阅读方式

当你在主线教程中遇到“这不是本系列重点，但确实需要做”的步骤时，再回到这里寻找补充说明。杂项教程不会假设你按顺序阅读，因此每篇都应在开头说明前置知识和适用范围。

## 命令技巧专题

### execute与逻辑控制

- [新版execute命令](./execute-command.md)
- [乘法执行分叉](./execution-forking.md)
- [execute逻辑门](./logic-gates.md)
- [在方块位置执行命令](./execute-at-block.md)

### 记分板系统

- [记分板运算](./scoreboard-operations.md)
- [记分板计时器](./scoreboard-timers.md)
- [实体计数器](./entity-counter.md)
- [分数比较](./comparing-scores.md)

### 检测与交互

- [移动状态检测](./detect-movements.md)
- [注视检测](./detect-looking.md)
- [降雨检测](./detect-rain.md)
- [掉落来源检测](./detect-item-drop.md)

### 显示与表现

- [轨道摄像机](./orbital-camera.md)
- [MBE方块实体](./block-entities.md)
- [FMBE显示实体](./display-entities.md)
- [playanimation命令](./playanimation.md)
- [罗盘方位显示](./compass-display.md)
- [动态文本显示](./dynamic-displays.md)

### 结构与玩法技巧

- [二进制逻辑](./binary-logic.md)
- [单命令球体生成](./sphere-command.md)
- [发放NBT物品](./giving-nbt-items.md)
- [自定义合成器](./custom-crafting.md)
- [多人位置错排](./rearrange-positions.md)