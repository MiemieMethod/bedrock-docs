---
title: 原版物品标识符
category: 文档
tags:
    - 废弃
mentions:
    - TheDoctor15
    - Medicaljewel105
    - Luthorius
    - epxzzy
    - SmokeyStack
description: 原版物品标识符效果。
---

:::danger
此方法在1.18.30之后不再有效。
:::

`identifier`是一个必需的参数，位于物品行为文件的描述中。它接受原版Minecraft名称，如`<namespace>:<vanilla item>`，这将根据所使用的标识符应用某些硬编码的物品行为。

```json title="BP/items/custom_item.json#minecraft:item"
"description": {
    "identifier": "wiki:totem_of_undying",
    "category": "items"
}
```

:::warning
并非所有原版标识符及其行为都有文档记录。以下列表可能缺少关于已知标识符的重要信息，这些标识符会影响物品。

请考虑进行实验。
:::

## 已知标识符效果

命名空间是可以更改的，了解更多关于命名空间的信息请[点击这里](../concepts/namespaces.md)。

### namespace:banner

-   物品图标和模型将更改为原版横幅的样式。

---

### namespace:bow

-   使用时会增加小幅度的缩放，缩放功能需要物品可用。

---

### namespace:crossbow

-   物品将在你的手臂上水平旋转。

---

### namespace:diamond

-   被接受为有效物品，可以改变信标发出的效果。

---

### namespace:emerald

-   被接受为有效物品，可以改变信标发出的效果。

---

### namespace:filled_map

-   将添加持有地图的动画。
-   可以放入制图台中。

---

### namespace:gold_ingot

-   被接受为有效物品，可以改变信标发出的效果。

---

### namespace:iron_ingot

-   被接受为有效物品，可以改变信标发出的效果。

---

### namespace:lapis_lazuli

-   使物品可以与附魔台一起使用，以替代青金石进行物品附魔。

---

### namespace:lead

-   将表现得像一个引导绳。

---

### namespace:map

-   将使用持有地图的动画。

---

### namespace:netherite_ingot

-   在自定义锻造配方中被接受为次要物品。
-   被接受为有效物品，可以改变信标发出的效果。

---

### namespace:shield

-   物品图标将永久更改为原版盾牌的样式。
-   添加盾牌动画和行为。

---

### namespace:spyglass

-   使其像望远镜一样可缩放，缩放功能需要物品可用。

---

### namespace:skull

-   物品图标将更改为原版骷髅的样式。
-   该物品可以放置在盔甲架和玩家身上，只有在此时骷髅的模型和纹理才会应用。

---

### namespace:totem_of_undying

-   将表现得像不死图腾。

---