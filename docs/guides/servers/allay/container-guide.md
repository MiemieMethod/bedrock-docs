---
comments: true
---

# 容器API

容器API负责管理玩家物品栏、箱子、熔炉，以及Allay里非常实用的伪容器界面。本指南重点讲“怎么拿到容器”“怎么改槽位”“怎么做自定义GUI”。

## 容器是什么

Allay里最基础的接口是`Container`。它负责保存物品，也负责管理查看者和监听器。

常见容器类型如下：

| 类型 | 大小 | 说明 |
|------|------|------|
| `INVENTORY` | `36` | 玩家主物品栏。 |
| `ARMOR` | `4` | 盔甲槽。 |
| `OFFHAND` | `1` | 副手槽。 |
| `CHEST` | `27` | 单箱子。 |
| `DOUBLE_CHEST` | `54` | 大箱子。 |
| `BARREL` | `27` | 木桶。 |
| `ENDER_CHEST` | `27` | 末影箱。 |
| `BREWING_STAND` | `5` | 酿造台。 |
| `CRAFTING_TABLE` | `9` | 工作台。 |
| `FAKE_CHEST` | `27` | 伪箱子容器。 |
| `FAKE_DOUBLE_CHEST` | `54` | 伪大箱子容器。 |

## 先拿到玩家容器

玩家本身实现了`ContainerHolder`，所以可以直接取出不同类型的容器：

```java linenums="1"
import org.allaymc.api.container.ContainerTypes;
import org.allaymc.api.entity.interfaces.EntityPlayer;

public void inspectPlayer(EntityPlayer player) {
    var inventory = player.getContainer(ContainerTypes.INVENTORY);
    var armor = player.getContainer(ContainerTypes.ARMOR);
    var offhand = player.getContainer(ContainerTypes.OFFHAND);
}
```

如果你只想处理手上物品，也可以直接用玩家接口：

```java linenums="1"
var itemInHand = player.getItemInHand();
int handSlot = player.getHandSlot();
player.clearItemInHand();
```

## 读写槽位

日常物品栏操作基本都围绕`getItemStack()`、`setItemStack()`、`clearSlot()`和`tryAddItem()`。

```java linenums="1"
import org.allaymc.api.container.ContainerTypes;
import org.allaymc.api.item.type.ItemTypes;

var inventory = player.getContainer(ContainerTypes.INVENTORY);

inventory.setItemStack(0, ItemTypes.DIAMOND.createItemStack(64));
var firstItem = inventory.getItemStack(0);
inventory.clearSlot(0);

player.tryAddItem(ItemTypes.EMERALD.createItemStack(16));
```

`tryAddItem()`会优先合并已有堆叠，再尝试找空槽，所以通常比你手动遍历槽位更省事。

## 处理方块容器

玩家打开某个容器方块以后，可以从控制器里读到当前界面对应的容器：

```java linenums="1"
import org.allaymc.api.container.ContainerTypes;
import org.allaymc.api.item.type.ItemTypes;

var controller = player.getController();
if (controller != null) {
    var openedChest = controller.getOpenedContainer(ContainerTypes.CHEST);
    if (openedChest != null) {
        openedChest.tryAddItem(ItemTypes.GOLD_INGOT.createItemStack(16));
    }
}
```

这类写法适合做“打开箱子时自动塞入奖励”“检查玩家当前正在编辑哪个容器”之类的逻辑。

## 监听容器变化

Allay容器支持打开、关闭和槽位变化监听：

```java linenums="1"
import org.allaymc.api.container.Container;
import org.allaymc.api.container.ContainerViewer;

public void bindListeners(Container container) {
    container.addOpenListener((ContainerViewer viewer) -> {
        System.out.println("有人打开了容器");
    });

    container.addCloseListener((ContainerViewer viewer) -> {
        System.out.println("有人关闭了容器");
    });

    container.addSlotChangeListener(0, itemStack -> {
        System.out.println("0号槽被改成了：" + itemStack.getItemType().getIdentifier());
    });
}
```

如果你要做商店、拍卖行或任务面板，这组监听器会非常常用。

## 用伪容器做自定义GUI

Allay提供了伪容器系统，它不依赖真实方块，非常适合做菜单。

```java linenums="1"
import org.allaymc.api.container.FakeContainerFactory;
import org.allaymc.api.item.type.ItemTypes;

var menu = FakeContainerFactory.getFactory().createFakeChestContainer();
menu.setCustomName("主菜单");
menu.setItemStack(0, ItemTypes.DIAMOND.createItemStack());
menu.setItemStack(4, ItemTypes.EMERALD.createItemStack());
```

你还可以给某个槽位直接绑定点击逻辑：

```java linenums="1"
menu.setItemStackWithListener(0, ItemTypes.DIAMOND_SWORD.createItemStack(), () -> {
    player.sendMessage("你点击了钻石剑。");
});

menu.addClickListener(4, () -> {
    player.sendMessage("你点击了绿宝石。");
});
```

最后把它展示给玩家：

```java linenums="1"
menu.addPlayer(player);
```

/// warning | `addPlayer()`与`addViewer()`不要混用
伪容器要优先使用`addPlayer()`而不是普通的`addViewer()`。Allay资料明确说明，`addPlayer()`会在打开界面前处理客户端所需的伪方块流程；只加查看者可能导致界面状态不完整。
///

## 什么时候该继续读别的页面

- 想往容器里放更复杂的物品数据，继续看[物品API](item-guide.md)。
- 想做“容器打开后执行命令”一类交互，继续看[注册命令](command-guide.md)和[事件系统](event-guide.md)。
- 想保存菜单状态或绑定自定义标记，继续看[数据持久化](persistent-data-guide.md)。