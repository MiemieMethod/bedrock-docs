# <!-- md:samp ServerboundDiagnosticsPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ServerboundDiagnosticsPacket -->数据包，数字ID是`315`。该数据包用于protocol.packet.serverbounddiagnosticspacket.description

## 结构

```viz
digraph "ServerboundDiagnosticsPacket" {
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
0 -> 11
11 -> 12
0 -> 13
13 -> 14
0 -> 15
15 -> 16
0 -> 17
17 -> 18

0 [label="ServerboundDiagnosticsPacket",comment="name: \"ServerboundDiagnosticsPacket\", typeName: \"\", id: 0, branchId: 315, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="AvgFps",comment="name: \"AvgFps\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="float",comment="name: \"float\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="AvgServerSimTickTimeMS",comment="name: \"AvgServerSimTickTimeMS\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
4 [label="float",comment="name: \"float\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="AvgClientSimTickTimeMS",comment="name: \"AvgClientSimTickTimeMS\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="float",comment="name: \"float\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="AvgBeginFrameTimeMS",comment="name: \"AvgBeginFrameTimeMS\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
8 [label="float",comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="AvgInputTimeMS",comment="name: \"AvgInputTimeMS\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="float",comment="name: \"float\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="AvgRenderTimeMS",comment="name: \"AvgRenderTimeMS\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="float",comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
13 [label="AvgEndFrameTimeMS",comment="name: \"AvgEndFrameTimeMS\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
14 [label="float",comment="name: \"float\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
15 [label="AvgRemainderTimePercent",comment="name: \"AvgRemainderTimePercent\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
16 [label="float",comment="name: \"float\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
17 [label="AvgUnaccountedTimePercent",comment="name: \"AvgUnaccountedTimePercent\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
18 [label="float",comment="name: \"float\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12;14;16;18}

}

```

## 字段

```title='ServerboundDiagnosticsPacket'
[avgfps][avgserversimticktimems][avgclientsimticktimems][avgbeginframetimems][avginputtimems][avgrendertimems][avgendframetimems][avgremaindertimepercent][avgunaccountedtimepercent]
```

/// html | div.result
//// define
AvgFps：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgfps.description


////
//// define
AvgServerSimTickTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgserversimticktimems.description


////
//// define
AvgClientSimTickTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgclientsimticktimems.description


////
//// define
AvgBeginFrameTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgbeginframetimems.description


////
//// define
AvgInputTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avginputtimems.description


////
//// define
AvgRenderTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgrendertimems.description


////
//// define
AvgEndFrameTimeMS：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgendframetimems.description


////
//// define
AvgRemainderTimePercent：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgremaindertimepercent.description


////
//// define
AvgUnaccountedTimePercent：<!-- md:samp float -->

- 基本类型。protocol.packet.serverbounddiagnosticspacket.avgunaccountedtimepercent.description


////

///

