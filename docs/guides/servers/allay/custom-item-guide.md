---
comments: true
---

# 自定义物品

自定义物品允许你为物品生成客户端定义，控制贴图、名称、手持偏移、冷却和一些特殊标记。本页只讲Allay资料里已经明确给出的那部分能力。

## 先处理构建配置

和自定义方块一样，自定义物品依赖Allay服务端模块，所以需要：

```kotlin title="build.gradle.kts"
allay {
    apiOnly = false
}
```

/// warning | 版本风险
这组接口不是纯API层接口。Allay升级时，它们的类名、位置或行为都可能调整。
///

## 最小可用示例

先从只指定贴图开始：

```java linenums="1"
import org.allaymc.server.item.type.AllayItemType;
import org.allaymc.server.item.type.CustomItemDefinitionGenerator;

AllayItemType.builder(MyItemStackImpl.class)
    .identifier("myplugin:ruby")
    .itemDefinitionGenerator(
        CustomItemDefinitionGenerator.builder()
            .texture("ruby")
            .build())
    .build();
```

`texture(...)`是必需项，它需要对应到资源包里的物品贴图定义。

## 加显示名称和特殊效果

```java linenums="1"
AllayItemType.builder(MyItemStackImpl.class)
    .identifier("myplugin:enchanted_crystal")
    .itemDefinitionGenerator(
        CustomItemDefinitionGenerator.builder()
            .texture("enchanted_crystal")
            .displayName("附魔水晶")
            .foil(true)
            .build())
    .build();
```

这里的`foil(true)`会让物品始终带附魔光泽。

## 常用生成器字段

| 字段 | 说明 |
|------|------|
| `texture` | 资源包中的物品纹理名，必需。 |
| `displayName` | 物品显示名称。 |
| `renderOffsets` | 手持时的位置、旋转和缩放。 |
| `foil` | 是否总是显示附魔光泽。 |
| `canDestroyInCreative` | 创造模式下是否允许直接破坏方块。 |
| `allowOffHand` | 是否允许放入副手。 |
| `cooldown` | 使用冷却秒数。 |
| `customProperties` | 自定义属性。 |
| `customComponents` | 自定义基岩版组件。 |

## 调整手持偏移

如果贴图尺寸大于16×16，或者你想让武器看起来更大，优先用`RenderOffsets.textureSize(...)`或`RenderOffsets.scale(...)`：

```java linenums="1"
import org.allaymc.server.item.type.CustomItemDefinitionGenerator;
import org.allaymc.server.item.type.CustomItemDefinitionGenerator.RenderOffsets;

CustomItemDefinitionGenerator.builder()
    .texture("greatsword")
    .renderOffsets(RenderOffsets.textureSize(32))
    .build();
```

要完全手动控制，也可以自己构造偏移：

```java linenums="1"
import org.allaymc.server.item.type.CustomItemDefinitionGenerator.RenderOffsets;
import org.allaymc.server.item.type.CustomItemDefinitionGenerator.RenderOffsets.Hand;
import org.allaymc.server.item.type.CustomItemDefinitionGenerator.RenderOffsets.Offset;
import org.joml.Vector3f;

RenderOffsets offsets = RenderOffsets.builder()
    .mainHand(Hand.builder()
        .firstPerson(Offset.builder()
            .rotation(new Vector3f(0, 45, 0))
            .scale(new Vector3f(1.5f, 1.5f, 1.5f))
            .build())
        .build())
    .build();
```

## 常见特殊标记

```java linenums="1"
CustomItemDefinitionGenerator.builder()
    .texture("magic_orb")
    .displayName("魔法球")
    .allowOffHand(true)
    .cooldown(1)
    .canDestroyInCreative(false)
    .build();
```

这些选项常见用途如下：

- `allowOffHand(true)`：副手道具、护符、盾牌类物品。
- `cooldown(1)`：技能道具、投掷物或传送物品。
- `canDestroyInCreative(false)`：避免某些工具在创造模式下表现得像普通方块破坏器。

## 自动识别机制

Allay资料说明，生成器会根据物品组件自动补出一些客户端属性：

- 带`ItemArmorBaseComponent`时，会自动识别盔甲槽位和护甲值。
- 带`ItemToolComponent`时，会自动设置手持表现和攻击伤害。
- 带`ItemEdibleComponent`时，会自动写入食用动画和使用时长。
- 如果物品本身可损坏，还会自动带上耐久相关属性。

这意味着很多情况下你不需要手动把每个客户端细节都重新写一遍。

## 一个更完整的示例

```java linenums="1"
AllayItemType.builder(GreatSwordImpl.class)
    .identifier("myplugin:greatsword")
    .itemData(ItemData.builder()
        .maxStackSize(1)
        .maxDamage(2000)
        .attackDamage(12)
        .build())
    .addComponent(ItemToolComponentImpl.class)
    .itemDefinitionGenerator(
        CustomItemDefinitionGenerator.builder()
            .texture("greatsword")
            .displayName("巨剑")
            .renderOffsets(RenderOffsets.textureSize(32))
            .canDestroyInCreative(false)
            .build())
    .build();
```

## 使用提醒

- 自定义物品一定还需要资源包配合，否则客户端只会看到缺失贴图。
- 贴图名必须和资源包里的定义一致。
- 尺寸大于16×16的贴图，优先使用`textureSize(...)`辅助方法。
- 如果你只是要改数量、名称和描述，而不是做客户端定义，请回到[物品API](item-guide.md)。
