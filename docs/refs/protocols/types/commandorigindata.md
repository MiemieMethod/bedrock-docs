# <!-- md:samp CommandOriginData -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CommandOriginData -->类型。该类型用于protocol.type.commandorigindata.description

## 结构

```viz
digraph "CommandOriginData" {
rankdir = LR
4
4 -> 5
5 -> 6
4 -> 7
7 -> 8
4 -> 9
9 -> 10
4 -> 11
11 -> 12
12 -> 13
11 -> 14
14 -> 15
11 -> 16
16 -> 17
17 -> 18
11 -> 19
19 -> 20
20 -> 21

4 [label="CommandOriginData",comment="name: \"CommandOriginData\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
5 [label="Command Type",comment="name: \"Command Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CommandOriginType\""];
6 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Command UUID",comment="name: \"Command UUID\", typeName: \"mce::UUID\", id: 7, branchId: 0, recurseId: -1, attributes: 256, notes: \"Unique UUID that represents an instantiation of a command. Each time a command is run it should be given a UUID to represent that instance.\""];
8 [label="mce::UUID",comment="name: \"mce::UUID\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Request ID",comment="name: \"Request ID\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="string",comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Dependency on 'Command Type'",shape=note,comment="name: \"Dependency on 'Command Type'\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 2, notes: \"\""];
12 [label="if (0)",shape=diamond,comment="name: \"if (0)\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 4, notes: \"\""];
13 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
14 [label="if (5)",shape=diamond,comment="name: \"if (5)\", typeName: \"\", id: 14, branchId: 5, recurseId: -1, attributes: 4, notes: \"\""];
15 [label="[No Data]",comment="name: \"[No Data]\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
16 [label="if (4)",shape=diamond,comment="name: \"if (4)\", typeName: \"\", id: 16, branchId: 4, recurseId: -1, attributes: 4, notes: \"\""];
17 [label="Player ID",comment="name: \"Player ID\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
19 [label="if (3)",shape=diamond,comment="name: \"if (3)\", typeName: \"\", id: 19, branchId: 3, recurseId: -1, attributes: 4, notes: \"\""];
20 [label="Player ID",comment="name: \"Player ID\", typeName: \"\", id: 20, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
21 [label="varint64",comment="name: \"varint64\", typeName: \"\", id: 21, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;6;8;10;13;15;18;21}

}

```

## 字段

```title='CommandOriginData'
[command_type][command_uuid][request_id][dependency_on_command_type]
```

/// html | div.result
//// define
Command Type：<!-- md:samp unsigned varint -->

- 基本类型枚举。protocol.type.commandorigindata.command_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Player`|`0`|protocol.enum.player|
  |`CommandBlock`|`1`|protocol.enum.commandblock|
  |`MinecartCommandBlock`|`2`|protocol.enum.minecartcommandblock|
  |`DevConsole`|`3`|protocol.enum.devconsole|
  |`Test`|`4`|protocol.enum.test|
  |`AutomationPlayer`|`5`|protocol.enum.automationplayer|
  |`ClientAutomation`|`6`|protocol.enum.clientautomation|
  |`DedicatedServer`|`7`|protocol.enum.dedicatedserver|
  |`Entity`|`8`|protocol.enum.entity|
  |`Virtual`|`9`|protocol.enum.virtual|
  |`GameArgument`|`10`|protocol.enum.gameargument|
  |`EntityServer`|`11`|protocol.enum.entityserver|
  |`Precompiled`|`12`|protocol.enum.precompiled|
  |`GameDirectorEntityServer`|`13`|protocol.enum.gamedirectorentityserver|
  |`Scripting`|`14`|protocol.enum.scripting|
  |`ExecuteContext`|`15`|protocol.enum.executecontext|



////
//// define
Command UUID：[<!-- md:samp mce::UUID -->](../types/mce__uuid.md)

- 特殊类型。protocol.type.commandorigindata.command_uuid.descriptionUnique UUID that represents an instantiation of a command. Each time a command is run it should be given a UUID to represent that instance.


////
//// define
Request ID：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.commandorigindata.request_id.description


////
> 依赖于`Command Type`

///// tab | `Command Type`如果为`0`
////// define
if (0)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Command Type`如果为`5`
////// define
if (5)：<!-- md:samp [No Data] -->

- 无数据


//////

/////

///// tab | `Command Type`如果为`4`
```title='if (4)'
[player_id]
```

////// html | div.result
/////// define
Player ID：<!-- md:samp varint64 -->

- 基本类型。protocol.type.commandorigindata.player_id.description


///////

//////

/////

///// tab | `Command Type`如果为`3`
```title='if (3)'
[player_id]
```

////// html | div.result
/////// define
Player ID：<!-- md:samp varint64 -->

- 基本类型。protocol.type.commandorigindata.player_id.description


///////

//////

/////

///

