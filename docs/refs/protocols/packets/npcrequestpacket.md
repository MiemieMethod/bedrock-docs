# <!-- md:samp NpcRequestPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp NpcRequestPacket -->数据包，数字ID是`98`。该数据包用于protocol.packet.npcrequestpacket.description

## 结构

```viz
digraph "NpcRequestPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10

0 [label="NpcRequestPacket",comment="name: \"NpcRequestPacket\", typeName: \"\", id: 0, branchId: 98, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="NPC Runtime ID",comment="name: \"NPC Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Request Type",comment="name: \"Request Type\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Actions",comment="name: \"Actions\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Action Index",comment="name: \"Action Index\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Scene Name",comment="name: \"Scene Name\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10}

}

```

## 字段

```title='NpcRequestPacket'
[npc_runtime_id][request_type][actions][action_index][scene_name]
```

/// html | div.result
//// define
NPC Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 特殊类型。protocol.packet.npcrequestpacket.npc_runtime_id.description


////
//// define
Request Type：<!-- md:samp byte -->

- 基本类型枚举。protocol.packet.npcrequestpacket.request_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`SetActions`|`0`|protocol.enum.setactions|
  |`ExecuteAction`|`1`|protocol.enum.executeaction|
  |`ExecuteClosingCommands`|`2`|protocol.enum.executeclosingcommands|
  |`SetName`|`3`|protocol.enum.setname|
  |`SetSkin`|`4`|protocol.enum.setskin|
  |`SetInteractText`|`5`|protocol.enum.setinteracttext|
  |`ExecuteOpeningCommands`|`6`|protocol.enum.executeopeningcommands|



////
//// define
Actions：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcrequestpacket.actions.description


////
//// define
Action Index：<!-- md:samp byte -->

- 基本类型。protocol.packet.npcrequestpacket.action_index.description


////
//// define
Scene Name：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.npcrequestpacket.scene_name.description


////

///

