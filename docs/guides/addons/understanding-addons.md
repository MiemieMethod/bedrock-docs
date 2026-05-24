# 认识附加包

这一节先不急着写复杂内容。我们先把附加包的骨架搭起来：一个资源包、一个行为包、两个清单文件，以及它们之间的依赖关系。只要这一步稳定，后面的实体、方块、物品、配方都只是往正确的位置继续添加文件。

## 资源包和行为包

资源包负责“看得见、听得到”的内容，例如纹理、模型、动画、粒子、声音、迷雾和语言文件。行为包负责“会发生什么”的内容，例如实体行为、方块定义、物品定义、配方、战利品表、函数、地物、生物群系和结构。

最小资源包如下：

```json title="demo_RP/manifest.json"
{
  "format_version": 2,
  "header": {
    "name": "Demo Resource Pack",
    "description": "Demo Resource Pack",
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

最小行为包如下：

```json title="demo_BP/manifest.json"
{
  "format_version": 2,
  "header": {
    "name": "Demo Behavior Pack",
    "description": "Demo Behavior Pack",
    "uuid": "填入第三个UUID",
    "version": [1, 0, 0],
    "min_engine_version": [1, 21, 80]
  },
  "modules": [
    {
      "type": "data",
      "uuid": "填入第四个UUID",
      "version": [1, 0, 0]
    }
  ],
  "dependencies": [
    {
      "uuid": "填入资源包header.uuid",
      "version": [1, 0, 0]
    }
  ]
}
```

如果行为包依赖资源包，激活行为包时游戏会尝试同时启用对应资源包。这里最容易写错的是UUID：依赖项填写资源包`header.uuid`，而不是资源包模块UUID。

## 放进开发目录

把`demo_RP`放进`development_resource_packs`，把`demo_BP`放进`development_behavior_packs`。然后创建一个测试世界，在“附加包”里分别激活资源包和行为包。

/// tip | 建议单独建测试世界
教程中的世界最好开启作弊、使用创造模式，并且不要放入你长期游玩的存档。这样你可以随时删除世界、清空包缓存或重新导入。
///

## 给项目定命名空间

命名空间是你自己的内容和原版内容之间的边界。示例中使用`demo`，所以物品可以叫`demo:coin`，实体可以叫`demo:robot`。不要把自定义内容放在`minecraft`命名空间下，除非你正在明确覆盖原版内容。

## 第一次验证

现在你还没有添加任何实际内容，所以验证目标很简单：

1. 世界设置中能看到两个包。
2. 激活时没有“清单无效”或“依赖缺失”提示。
3. 内容日志没有JSON语法错误。

如果这三项都通过，就可以进入下一页，先做一个能看见变化的纹理包。