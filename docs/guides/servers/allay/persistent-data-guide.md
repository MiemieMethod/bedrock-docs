---
comments: true
---

# 数据持久化

如果你想把插件自定义数据挂到世界、实体、方块实体或物品栈上，Allay推荐使用PDC，而不是直接碰内部NBT或把数据塞进描述文本。本指南只讲已经明确支持的做法。

## PDC适合解决什么问题

过去很多插件会把自定义数据塞进NBT、物品名称或描述里，但这些方法要么依赖内部实现，要么容易和别的插件冲突。PDC的优势是：

- 不需要直接访问服务端内部NBT实现。
- 生命周期更清晰，数据会跟随持有者保存。
- 可以存各种基础类型，也能嵌套更复杂的数据结构。

Allay资料列出的PDC持有者包括：

- `World`
- `Entity`
- `BlockEntity`
- `ItemStack`

## 写入一条最简单的数据

先准备一个键，再把值写进持有者的`PersistentDataContainer`。

```java linenums="1"
import org.allaymc.api.item.type.ItemTypes;
import org.allaymc.api.pdc.PersistentDataType;
import org.allaymc.api.utils.identifier.Identifier;

var key = new Identifier("allaymc", "example-key");
var itemStack = ItemTypes.DIAMOND.createItemStack();

itemStack.getPersistentDataContainer().set(
        key,
        PersistentDataType.STRING,
        "I love AllayMC"
);
```

/// tip | 键最好复用
资料建议尽量复用`Identifier`对象，而不是每次读写时都重新构造一遍。用插件命名空间做前缀也更不容易和别的插件冲突。
///

## 读取数据

读取时要同时知道键和数据类型：

```java linenums="1"
import org.allaymc.api.pdc.PersistentDataType;
import org.allaymc.api.utils.identifier.Identifier;

var key = new Identifier("allaymc", "example-key");
var pdc = itemStack.getPersistentDataContainer();

if (pdc.has(key, PersistentDataType.STRING)) {
    String value = pdc.get(key, PersistentDataType.STRING);
    player.sendMessage(value);
}
```

## 支持哪些类型

Allay明确列出的原生类型包括：

- `Byte`、`Byte Array`
- `Short`
- `Integer`、`Integer Array`
- `Long`、`Long Array`
- `Float`
- `Double`
- `String`
- `Boolean`
- `PersistentDataContainer`
- `List`

其中`PersistentDataContainer`和`List`很实用，因为它们让你可以把结构化数据也放进去。

## 嵌套容器

```java linenums="1"
PersistentDataContainer container = itemStack.getPersistentDataContainer();
PersistentDataContainer nested = container.getAdapterContext().newPersistentDataContainer();

nested.set(key, PersistentDataType.STRING, "nested-value");
// 然后再把nested作为一个嵌套容器写回你的业务结构中
```

## 存列表

```java linenums="1"
container.set(
    key,
    PersistentDataType.LIST.strings(),
    List.of("a", "list", "of", "strings")
);

List<String> strings = container.get(key, PersistentDataType.LIST.strings());
```

## 自定义类型

如果原生类型不够用，你可以自己实现`PersistentDataType`，把复杂对象拆成原生类型再存。给出的示例是把`UUID`拆成`byte[]`：

```java linenums="1"
import org.allaymc.api.pdc.PersistentDataAdapterContext;
import org.allaymc.api.pdc.PersistentDataType;

import java.nio.ByteBuffer;
import java.util.UUID;

public class UUIDDataType implements PersistentDataType<byte[], UUID> {
    @Override
    public Class<byte[]> getPrimitiveType() {
        return byte[].class;
    }

    @Override
    public Class<UUID> getComplexType() {
        return UUID.class;
    }

    @Override
    public byte[] toPrimitive(UUID complex, PersistentDataAdapterContext context) {
        var buffer = ByteBuffer.wrap(new byte[16]);
        buffer.putLong(complex.getMostSignificantBits());
        buffer.putLong(complex.getLeastSignificantBits());
        return buffer.array();
    }

    @Override
    public UUID fromPrimitive(byte[] primitive, PersistentDataAdapterContext context) {
        var buffer = ByteBuffer.wrap(primitive);
        return new UUID(buffer.getLong(), buffer.getLong());
    }
}
```

使用时别忘了把自定义类型实例传进`get()`、`set()`和`has()`：

```java linenums="1"
container.set(key, new UUIDDataType(), uuid);
```

## 一个特别重要的坑

/// warning | 数据不会自动搬家
PDC不会替你在不同持有者之间自动复制数据。例如，一个带有PDC的`ItemStack`被放置成带方块实体的方块后，它的数据不会自动出现在对应的`BlockEntity`上。需要迁移时，你得自己复制。
///

## 什么时候适合继续读别的页面

- 想把PDC绑在自定义物品或菜单物品上，继续看[物品API](item-guide.md)和[容器API](container-guide.md)。
- 想把PDC和界面交互绑在一起，继续看[表单开发](form-guide.md)。