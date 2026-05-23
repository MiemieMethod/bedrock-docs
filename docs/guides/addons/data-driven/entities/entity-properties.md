# 实体属性<!-- md:flag vanilla -->

在以往的实体开发中，如果需要为实体存储一个状态量，我们往往会借助所谓的"哑组件"——这些组件在语义上原本代表某种游戏行为，但在自定义实体上却几乎没有实际效果，因此被当作存储变量来使用。例如，`minecraft:variant`和`minecraft:mark_variant`各能存储一个整数，可以用`query.variant`和`query.mark_variant`Molang查询读取；`minecraft:is_baby`、`minecraft:is_sheared`等可以充当布尔量，分别通过`query.is_baby`、`query.is_sheared`读取。

然而哑组件存在两个明显缺陷：其一，它们在语义上与用途不符，时间一长很难回忆起"这个`minecraft:is_baby`到底在我的实体里控制什么功能"；其二，可供借用的哑组件数目有限，当需要存储更多状态时便会捉襟见肘。**实体属性**（**Entity Property**）正是为了解决这两个问题而出现的。

/// warning | 版本要求
实体属性需要将实体服务端定义文件的`format_version`设为`1.16.0`或更高版本，且需开启实验性玩法中的**Beta API**（在部分版本中可能标注为**假日创作者功能**）。<!-- md:flag vanilla -->
///

## 定义属性

在实体服务端定义文件（行为包`entities/`目录下的JSON文件）的`minecraft:entity.description`对象中，添加`properties`字段来声明该实体拥有的属性：

```json title="BP/entities/bee.json（节选）"
{
  "format_version": "1.18.20",
  "minecraft:entity": {
    "description": {
      "identifier": "minecraft:bee",
      "is_spawnable": true,
      "is_summonable": true,
      "is_experimental": false,
      "properties": {
        "minecraft:has_nectar": {
          "type": "bool",
          "client_sync": true,
          "default": "query.had_component_group('has_nectar')"
        }
      }
    }
  }
}
```

`properties`是一个对象，其中每个键值对定义一个属性，键名即属性名。属性名建议带命名空间（如`minecraft:has_nectar`），以避免与其他属性冲突。属性对象支持以下字段：

/// define
`type` <!-- md:flag required -->

- 属性的类型。支持`"bool"`（布尔值）、`"int"`（整数）、`"float"`（浮点数）、`"enum"`（字符串枚举）四种。

`range` <!-- md:flag required -->

- 属性的取值范围。`int`和`float`类型填写`[最小值, 最大值]`的两元素数组；`enum`类型填写所有合法枚举字符串的数组，最多16个元素。`bool`类型不需要此字段。

`client_sync`

- 是否将该属性同步到客户端，默认为`false`。开启后，客户端的动画、动画控制器、渲染控制器和粒子均可读取该属性值。

`default`

- 实体**首次初始化**时该属性的默认值。之后从存档加载时，读取上次保存时的实际值，不再使用默认值。可以直接填写与`type`对应的字面量值，也可以填写一个Molang表达式字符串；表达式仅支持`query.had_component_group`查询，且无法访问实体自定义变量。

///

实体首次生成时，引擎按`default`值初始化各属性，并将它们存入内存和NBT存档，供后续读写。

## 读取属性

### 通过Molang读取

游戏提供了两个专用查询函数用于读取实体属性：

- `query.has_property('<属性名>')` — 检查该属性是否存在，返回`1.0`（存在）或`0.0`（不存在）。
- `query.property('<属性名>')` — 返回该属性的当前值。数字类型返回浮点数，枚举类型返回其字符串的哈希值，布尔类型返回`1.0`或`0.0`。

这两个函数可以在动画、动画控制器、渲染控制器、粒子等支持Molang的所有地方使用（前提是该属性开启了`client_sync`，或者在服务端上下文中）。

### 通过过滤器读取

在实体的组件组条件、AI意向过滤器等需要过滤器的位置，可以使用以下过滤器按类型读取属性：

```json
{
  "test": "int_property",
  "subject": "self",
  "operator": "==",
  "domain": "demo:my_int_prop",
  "value": 3
}
```

`domain`字段填写要查询的属性名，`value`填写要比较的值：

/// define
`int_property`

- 适用于`int`类型属性，按整数比较。

`float_property`

- 适用于`float`类型属性，按浮点数比较。

`bool_property`

- 适用于`bool`类型属性，按布尔值比较。

`enum_property`

- 适用于`enum`类型属性，按枚举字符串比较。

`has_property`

- 检查属性是否存在，属性名填入`value`字段而非`domain`字段。

///

## 修改属性

目前可以通过实体事件响应`set_property`修改属性值：

```json title="BP/entities/bee.json（节选）"
{
  "events": {
    "collected_nectar": {
      "set_property": {
        "minecraft:has_nectar": true
      }
    },
    "minecraft:exited_hive": {
      "set_property": {
        "minecraft:has_nectar": false
      }
    }
  }
}
```

`set_property`是一个对象，每个键值对表示一次赋值，键为属性名，值为要赋予的目标值或一个Molang表达式字符串。

/// warning | 赋值是异步的
`set_property`中的Molang表达式**计算是同步的**，但**赋值到属性是异步的**——真正的更新要等到下一刻才会反映。因此，在同一个事件中如果同时对同一属性的两条`set_property`表达式调用了`query.property`，它们看到的仍然是旧值，而不是上一条赋值的结果。

此外，`set_property`的Molang表达式内只能使用`query.property`和`query.has_property`，无法访问实体自定义变量。
///

## 完整示例

以下是一个简化的蜜蜂实体，演示了实体属性的完整定义-读取-修改流程：

```json title="BP/entities/bee.json"
{
  "format_version": "1.18.20",
  "minecraft:entity": {
    "description": {
      "identifier": "minecraft:bee",
      "is_spawnable": true,
      "is_summonable": true,
      "is_experimental": false,
      "properties": {
        "minecraft:has_nectar": {
          "type": "bool",
          "client_sync": true,
          "default": "query.had_component_group('has_nectar')"
        }
      }
    },
    "component_groups": {
      "has_nectar": {
        "minecraft:grows_crop": {
          "charges": 10,
          "chance": 0.03
        }
      }
    },
    "components": {},
    "events": {
      "minecraft:exited_hive": {
        "set_property": {
          "minecraft:has_nectar": false
        }
      },
      "collected_nectar": {
        "set_property": {
          "minecraft:has_nectar": true
        }
      },
      "find_hive_timeout": {
        "sequence": [
          {
            "filters": {
              "test": "bool_property",
              "operator": "!=",
              "domain": "minecraft:has_nectar"
            },
            "remove": {
              "component_groups": ["find_hive"]
            },
            "add": {
              "component_groups": ["look_for_food"]
            }
          }
        ]
      }
    }
  }
}
```

这个示例中，`minecraft:has_nectar`属性：
- 在`description.properties`中被定义为布尔类型，并通过`query.had_component_group`从旧组件组状态迁移初始值；
- 在`events.collected_nectar`中通过`set_property`设为`true`；
- 在`events.find_hive_timeout`中通过`bool_property`过滤器读取，用于条件分支。

## 从哑组件迁移

如果你的旧实体用`minecraft:is_baby`之类的哑组件存储状态，迁移到实体属性的思路是：

1. 在`description.properties`中新增对应的属性，类型根据原哑组件对应。
2. 用`query.property`替换原有的`query.is_baby`等Molang查询。
3. 在事件中用`set_property`替换原有的`add`/`remove`组件组操作。
4. 如果需要用过滤器判断，改用对应类型的属性过滤器。

迁移时可以利用`default`字段的`query.had_component_group`在不破坏存档兼容性的前提下完成初始值对齐，如同上方蜜蜂示例所示。
