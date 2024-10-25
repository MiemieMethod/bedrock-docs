# <!-- md:samp ItemComponentPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ItemComponentPacket -->数据包，数字ID是`162`。该数据包用于protocol.packet.itemcomponentpacket.description

## 结构

```viz
digraph "ItemComponentPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6
4 -> 7
7 -> 8

0 [label="ItemComponentPacket",comment="name: \"ItemComponentPacket\", typeName: \"\", id: 0, branchId: 162, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Items",comment="name: \"Items\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of component based items\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="ComponentItem name",comment="name: \"ComponentItem name\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Component data",comment="name: \"Component data\", typeName: \"CompoundTag\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"Compound tag members - itemname: string, itemid: short, itemcomponents: {[componentkey:string]: { ...component definition here... } } }\""];
8 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6;8}

}

```

## 字段

```title='ItemComponentPacket'
[items]
```

/// html | div.result
```title='Items'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.itemcomponentpacket.items.array_size.description


/////
```title='示例元素'
[componentitem_name][component_data]
```

///// html | div.result
////// define
ComponentItem name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.itemcomponentpacket.items.example_element.componentitem_name.description


//////
////// define
Component data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。protocol.packet.itemcomponentpacket.items.example_element.component_data.descriptionCompound tag members - item'name': string, item'id': short, itemcomponents: {[componentkey:string]: { ...component definition here... } } }


//////

/////

////

///

