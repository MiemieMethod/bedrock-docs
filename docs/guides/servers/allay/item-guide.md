---
comments: true
---

# 物品API

本指南会带你把Allay的物品API真正用起来。读完后，你应该能创建物品栈、修改名称和描述、处理耐久，并理解`ItemType`、`ItemStack`、`ItemData`和`ItemTag`之间的分工。

## 先分清几个核心对象

| 类型 | 作用 |
|------|------|
| `ItemType` | 物品种类，例如钻石、钻石剑、苹果。 |
| `ItemStack` | 具体的物品实例，包含数量、损坏值、自定义名称、描述和魔咒等数据。 |
| `ItemData` | 某个物品种类的元数据，例如最大堆叠数、耐久、攻击伤害。 |
| `ItemTag` | 物品分类标签，例如是否为剑、是否为食物、是否属于某种品质。 |

如果你只是想“拿一个物品出来用”，通常从`ItemTypes`开始就够了。

```java linenums="1"
import org.allaymc.api.item.type.ItemType;
import org.allaymc.api.item.type.ItemTypes;

ItemType<?> diamond = ItemTypes.DIAMOND;
ItemType<?> sword = ItemTypes.DIAMOND_SWORD;
ItemType<?> apple = ItemTypes.APPLE;
```

## 创建物品栈

最常见的入口是`ItemType#createItemStack()`。

```java linenums="1"
import org.allaymc.api.item.ItemStack;
import org.allaymc.api.item.type.ItemTypes;

ItemStack oneApple = ItemTypes.APPLE.createItemStack();
ItemStack diamonds = ItemTypes.DIAMOND.createItemStack(64);
ItemStack sword = ItemTypes.DIAMOND_SWORD.createItemStack();
```

如果你还要同时指定数量或附加值，也可以改用初始化信息：

```java linenums="1"
import org.allaymc.api.item.ItemStack;
import org.allaymc.api.item.ItemStackInitInfo;
import org.allaymc.api.item.type.ItemTypes;

ItemStack customStack = ItemTypes.DIAMOND_SWORD.createItemStack(
        ItemStackInitInfo.builder()
                .count(1)
                .meta(0)
                .build()
);
```

## 读取和修改数量

`ItemStack`是可变对象，所以你拿到它以后可以直接改数量。

```java linenums="1"
import org.allaymc.api.item.ItemStack;
import org.allaymc.api.item.type.ItemTypes;

ItemStack stack = ItemTypes.DIAMOND.createItemStack(32);

int count = stack.getCount();
stack.setCount(64);
stack.reduceCount(10);
stack.increaseCount(5);

boolean isFull = stack.isFull();
boolean isEmpty = stack.isEmptyOrAir();
```

/// warning | 可变对象提醒
Allay的`ItemStack`不是不可变值对象。一个物品栈如果正被多个地方复用，直接修改它可能会把其他逻辑一起改掉。需要“基于原物品做一份新副本”时，先复制再改。
///

```java linenums="1"
ItemStack original = ItemTypes.DIAMOND_SWORD.createItemStack();
original.setCustomName("原件");

ItemStack copy = original.copy();
copy.setCustomName("副本");
```

## 设置名称和描述

给物品加自定义名称和描述是最常见的玩法接口之一：

```java linenums="1"
import org.allaymc.api.item.ItemStack;
import org.allaymc.api.item.type.ItemTypes;

import java.util.List;

ItemStack sword = ItemTypes.DIAMOND_SWORD.createItemStack();
sword.setCustomName("§6王者之刃");
sword.setLore(List.of(
        "§7一把测试用武器",
        "§c+10攻击伤害"
));
```

如果你希望名称可翻译，优先把文本交给[国际化](i18n-guide.md)系统处理，而不是把固定中文硬写进代码。

## 处理耐久和损坏值

工具和武器通常要关心耐久：

```java linenums="1"
import org.allaymc.api.item.ItemStack;
import org.allaymc.api.item.type.ItemTypes;

ItemStack pickaxe = ItemTypes.DIAMOND_PICKAXE.createItemStack();

int maxDurability = pickaxe.getMaxDamage();
int currentDamage = pickaxe.getDamage();

pickaxe.setDamage(100);

boolean broken = pickaxe.isBroken();
boolean applied = pickaxe.tryIncreaseDamage(1);
```

`tryIncreaseDamage(1)`比直接`setDamage()`更适合真实玩法流程，因为它会按Allay的物品逻辑处理耐久增长。

## 从注册表查找物品

当你的标识符来自配置文件、命令参数或网络数据时，不适合写死在`ItemTypes`里。这时可以走注册表：

```java linenums="1"
import org.allaymc.api.item.type.ItemType;
import org.allaymc.api.registry.Registries;
import org.allaymc.api.utils.identifier.Identifier;

ItemType<?> diamond = Registries.ITEM_TYPE.get(new Identifier("minecraft:diamond"));
ItemType<?> sword = Registries.ITEM_TYPE.get(new Identifier("minecraft:diamond_sword"));
```

记得处理返回值为空的情况，因为标识符可能拼错，也可能引用了当前环境里尚未注册的内容。

## 读取物品元数据与标签

`ItemData`适合回答“这个物品本身是什么性质”，`ItemTag`适合回答“这个物品属于哪一类”。

```java linenums="1"
import org.allaymc.api.item.data.ItemData;
import org.allaymc.api.item.tag.ItemTags;
import org.allaymc.api.item.type.ItemTypes;

ItemData swordData = ItemTypes.DIAMOND_SWORD.getItemData();
int maxStack = swordData.maxStackSize();
int maxDamage = swordData.maxDamage();
int attackDamage = swordData.attackDamage();

boolean isSword = ItemTypes.DIAMOND_SWORD.hasItemTag(ItemTags.IS_SWORD);
boolean isFood = ItemTypes.APPLE.hasItemTag(ItemTags.IS_FOOD);
boolean isDiamondTier = ItemTypes.DIAMOND_PICKAXE.hasItemTag(ItemTags.DIAMOND_TIER);
```

这类判断很适合做命令过滤、配方限制、菜单分类和自定义逻辑分支。

## 实战建议

- 只需要生成原版物品时，优先使用`ItemTypes`。
- 需要跨系统传递物品时，先确认你传的是`ItemType`还是`ItemStack`。
- 修改共享物品前先复制，尤其是做菜单、奖励模板或缓存物品时。
- 需要自定义客户端渲染时，继续阅读[自定义物品](custom-item-guide.md)。
