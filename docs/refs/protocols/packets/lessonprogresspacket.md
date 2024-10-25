# <!-- md:samp LessonProgressPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp LessonProgressPacket -->数据包，数字ID是`183`。该数据包用于protocol.packet.lessonprogresspacket.description

## 结构

```viz
digraph "LessonProgressPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="LessonProgressPacket",comment="name: \"LessonProgressPacket\", typeName: \"\", id: 0, branchId: 183, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Lesson Action",comment="name: \"Lesson Action\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Score",comment="name: \"Score\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="varint",comment="name: \"varint\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Activity Id",comment="name: \"Activity Id\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="string",comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='LessonProgressPacket'
[lesson_action][score][activity_id]
```

/// html | div.result
//// define
Lesson Action：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.lessonprogresspacket.lesson_action.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Start`|`0`|protocol.enum.start|
  |`Complete`|`1`|protocol.enum.complete|
  |`Restart`|`2`|protocol.enum.restart|



////
//// define
Score：<!-- md:samp varint -->

- 基本类型。protocol.packet.lessonprogresspacket.score.description


////
//// define
Activity Id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.packet.lessonprogresspacket.activity_id.description


////

///

