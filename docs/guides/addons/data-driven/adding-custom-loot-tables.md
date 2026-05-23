# 自定义战利品表

战利品表用于决定实体死亡、方块破坏、容器填充等场景会产出什么物品。它属于行为包，通常放在`loot_tables`目录下。

## 最小战利品表

```json title="demo_BP/loot_tables/entities/robot.json"
{
  "pools": [
    {
      "rolls": 1,
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond"
        }
      ]
    }
  ]
}
```

这张表每次被调用都会产出1个钻石。

## 挂到实体上

在实体行为文件中添加：

```json
"minecraft:loot": {
  "table": "loot_tables/entities/robot.json"
}
```

路径从行为包根目录开始写。

## 权重和次数

```json
{
  "pools": [
    {
      "rolls": {
        "min": 1,
        "max": 3
      },
      "entries": [
        {
          "type": "item",
          "name": "minecraft:diamond",
          "weight": 1
        },
        {
          "type": "item",
          "name": "minecraft:coal",
          "weight": 4
        }
      ]
    }
  ]
}
```

`rolls`可以是固定数，也可以是范围。`weight`控制同一个池中条目的相对概率；示例中煤炭相对钻石更容易被选中。

## 函数和条件

战利品函数可以改变数量、附魔、名称、耐久等。下面让掉落数量在0到2之间：

```json
"functions": [
  {
    "function": "set_count",
    "count": {
      "min": 0,
      "max": 2
    }
  }
]
```

条件可以限制掉落场景，例如只在被玩家击杀时掉落。官方示例中洞穴蜘蛛的蜘蛛眼池就使用了`killed_by_player`条件。

## 测试建议

战利品表有随机性。测试时请多击杀几次实体，或者临时把`rolls`和`weight`改成确定值。确认能掉落后，再恢复概率设计。

## 为结构容器添加战利品表

放置在世界中的结构（通过`/structure load`或结构方块放置）内的容器（箱子、桶等）可以绑定战利品表，在玩家第一次打开时随机填充内容。这需要在结构文件的NBT数据中为容器方块实体设置`LootTable`字符串标签。

### 准备工作

首先在行为包的`loot_tables/`目录下（推荐使用`loot_tables/chests/`子目录）创建战利品表文件。然后将结构导出到行为包的`structures/`目录。

### 使用NBT Studio（桌面端）

[NBT Studio](https://github.com/tryashtar/nbt-studio/releases)是一款可编辑结构文件NBT数据的桌面应用程序。

1. 打开NBT Studio，用 ++ctrl+o++ 打开结构文件。
2. 用 ++ctrl+f++ 搜索容器方块（如`chest`）定位到目标容器。
3. 定位至 `block_position_data` > `block_entity_data`，在此节点下新建一个字符串（String）标签。
4. 将标签名设为`LootTable`，值设为战利品表路径（从行为包根目录起，如`loot_tables/chests/my_structure_loot.json`）。
5. 用 ++ctrl+s++ 保存文件。

<!-- 截图：NBT Studio主界面打开结构文件后的树状展示，展示block_position_data > block_entity_data下新增LootTable字符串标签的样子。 -->

### 使用Loot Tabler（浏览器端）

[Loot Tabler](https://mcbe-essentials.github.io/structure-editor/loot-tabler) 是一款无需安装即可使用的在线工具，适合在移动设备上操作。

1. 访问网站，点击"Upload"上传结构文件。
2. 在容器列表中找到目标容器（通过位置坐标等信息定位）。
3. 在"Loot Table"输入框填入战利品表路径。"Loot Table Seed"留空或填`0`可实现每次随机生成，填入特定数值则固定生成结果。
4. 下载修改后的结构文件，放回行为包的`structures/`目录。

/// tip | 移动设备导出结构
Minecraft基岩版移动端原生不支持导出结构到可访问的文件系统位置，可使用[Export Structure Button](https://mcpedl.com/export-structure-button-android-addon/)资源包解决此问题。
///

### 测试验证

加载结构（`/structure load`），然后打开对应容器，确认内容物与战利品表定义一致。
