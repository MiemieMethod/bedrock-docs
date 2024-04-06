# <!-- md:samp ActorPickRequestPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorPickRequestPacket -->数据包，数字ID是`35`。

## 结构

```viz
digraph "ActorPickRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ActorPickRequestPacket",comment="name: \"ActorPickRequestPacket\", typeName: \"\", id: 0, branchId: 35, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Actor ID",comment="name: \"Actor ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Target Actor ID\""];
2 [label="int64",comment="name: \"int64\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Max Slots",comment="name: \"Max Slots\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"number of empty hotbar slots (to decide whether to overwrite a slot or add it to an empty one)\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="With Data",comment="name: \"With Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"whether we want to store the NBT data along with the item\""];
6 [label="bool",comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ActorPickRequestPacket'
[actor_id][max_slots][with_data]
```

/// html | div.result
//// define
Actor ID：<!-- md:samp int64 -->

- 基本类型。Target Actor ID


////
//// define
Max Slots：<!-- md:samp byte -->

- 基本类型。number of empty hotbar slots (to dec'id'e whether to overwrite a slot or add it to an empty one)


////
//// define
With Data：<!-- md:samp bool -->

- 基本类型。whether we want to store the NBT data along with the item


////

///

