# <!-- md:samp CameraShakePacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraShakePacket -->数据包，数字ID是`159`。

## 结构

```viz
digraph "CameraShakePacket" {
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

0 [label="CameraShakePacket",comment="name: \"CameraShakePacket\", typeName: \"\", id: 0, branchId: 159, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Intensity",comment="name: \"Intensity\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Camera shake intensity\""];
2 [label="float",comment="name: \"float\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Seconds",comment="name: \"Seconds\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"Duration\""];
4 [label="float",comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Shake Type",comment="name: \"Shake Type\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CameraShakeType\""];
6 [label="byte",comment="name: \"byte\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Shake action",comment="name: \"Shake action\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: CameraShakeAction\""];
8 [label="byte",comment="name: \"byte\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8}

}

```

## 字段

```title='CameraShakePacket'
[intensity][seconds][shake_type][shake_action]
```

/// html | div.result
//// define
Intensity：<!-- md:samp float -->

- <!-- md:samp float -->类型。Camera shake intensity


////
//// define
Seconds：<!-- md:samp float -->

- <!-- md:samp float -->类型。Duration


////
//// define
Shake Type：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Positional`|`0`||
  |`Rotational`|`1`||



////
//// define
Shake action：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Add`|`0`||
  |`Stop`|`1`||



////

///

