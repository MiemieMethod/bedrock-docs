---
标题：实体属性
类别：通用
标签：
    - 实验性
提及：
    - SirLich
    - sermah
    - MedicalJewel105
    - Luthorius
    - stirante
    - TheItsNameless
    - SmokeyStack
描述：实体属性的实现旨在高效地保存数据或存储实体上的值，而无需在实体的服务器端使用组件或属性，类似于区块属性。

---

关于在1.16.230.52 Minecraft基岩版测试版中引入的新实体属性（也称为演员属性）的文档。实体属性的实现旨在高效地保存数据或存储实体上的值，而无需在实体的服务器端（行为包）使用组件或属性（例如，“minecraft:variant”），类似于区块属性。

## 实体属性定义

### 在实体上定义属性

实体属性定义：

<CodeHeader></CodeHeader>

```json
{
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:properties_example",
            "properties": {
                "property:number_range_example": {
                    "values": {
                        "min": 0,
                        "max": 100
                    }
                },
                "property:number_enum_example": {
                    "values": [1, 2]
                },
                "property:string_enum_example": {
                    "values": ["first", "second", "third"]
                },
                "property:boolean_enum_example": {
                    "values": [true, false]
                }
            }
        }
    }
}
```

### 实体属性对象字段

#### `values`

:::warning
`values`属性是必需的，省略此字段可能导致错误和无法注册属性。
:::

`values`字段可以被评估为枚举值的数组，或最小值和最大值的范围（注意：整数、浮点数和布尔枚举值目前仅支持两个值）：

<CodeHeader></CodeHeader>

```json
"property:range_example": {
    "values": {
      "min": 0,
      "max": 5
    }
}
```

**或者**

<CodeHeader></CodeHeader>

```json
"property:enum_example":{
    "values":[
        1,
        2
    ]
}
```

#### `default`

您可以通过在定义的属性对象内的`default`字段设置实体属性的默认值（默认情况下为枚举数组索引的第一个值）：

<CodeHeader></CodeHeader>

```json
"property:default_value_example":{
    "values":[
        true,
        false
    ],
    "default":false
}
```

如您所见，默认属性在实体生成到世界时被设置为`false`而不是`true`。

#### `client_sync`

要通过资源包（客户端）进行同步，可以使用`client_sync`字段允许客户端实体访问实体属性。默认情况下，该值设置为`false`。

<CodeHeader></CodeHeader>

```json
"property:client_sync_example": {
    "values": {
      "min": 0,
      "max": 20
    },
    "client_sync": true
}
```

### 操作和访问实体属性

您可以通过Molang实体查询访问实体属性： - `q.property` - `q.has_property`

:::warning
这些Molang实体查询是实验性功能的一部分。
:::

通过实体事件，您可以使用`set_property`事件响应将实体属性设置为某个值：

<CodeHeader></CodeHeader>

```json
"events":{
    "event:set_entity_property":{
        "set_property":{
            "property:number_enum_example":2,
            "property:string_enum_example":"'second'",
            "property:boolean_enum_example":"!q.property('property:boolean_enum_example')"
        }
    }
}
```

## 实体别名

:::warning
此功能已被弃用，需指定版本号为1.21.10或更高。
:::

您可以为实体定义别名，以通过`summon`命令召唤具有设置的实体属性值的实体。实体可以具有多个别名，使用自定义实体标识符：

<CodeHeader></CodeHeader>

```json
{
    "format_version": "1.16.0",
    "minecraft:entity": {
        "description": {
            "identifier": "wiki:properties_example",
            "is_spawnable": true,
            "is_summonable": true,
            "is_experimental": false,
            "properties": {
                "property:property_index": {
                    "client_sync": true,
                    "values": {
                        "min": 0,
                        "max": 2
                    },
                    "default": 0
                }
            },
            "aliases": {
                "wiki:default_alias": {},
                "wiki:first_alias": {
                    "property:property_index": 1
                },
                "wiki:second_alias": {
                    "property:property_index": 2
                }
            }
        }
    }
}
```

现在，实体有多个别名，您可以通过`summon`命令使用定义的别名标识符来生成具有设置属性的实体：`/summon ewiki:first_alias`将生成属性`property:property_index`设置为1的实体。