# <!-- md:samp PlayerAuthInputPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PlayerAuthInputPacket -->数据包，数字ID是`144`。

## 结构

```viz
digraph PlayerAuthInputPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec2\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"Vec2\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		8	[comment="name: \"float\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		10	[comment="name: \"unsigned varint64\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
		12	[comment="name: \"unsigned varint\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		14	[comment="name: \"unsigned varint\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		16	[comment="name: \"varint\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		19	[comment="name: \"[No Data]\", typeName: \"\", id: 19, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		22	[comment="name: \"Vec3\", typeName: \"\", id: 22, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		24	[comment="name: \"unsigned varint64\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
		26	[comment="name: \"Vec3\", typeName: \"\", id: 26, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		29	[comment="name: \"[No Data]\", typeName: \"\", id: 29, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		76	[comment="name: \"PackedItemUseLegacyInventoryTransaction\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PackedItemUseLegacyInventoryTransaction];
		79	[comment="name: \"[No Data]\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		85	[comment="name: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, \
notes: \"\"",
			label="TypedClientNetId<struct ItemStackRequestIdTag,int,0>"];
		88	[comment="name: \"unsigned varint\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		91	[comment="name: \"byte\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		93	[comment="name: \"byte\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		102	[comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackRequestSlotInfo];
		104	[comment="name: \"ItemStackRequestSlotInfo\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ItemStackRequestSlotInfo];
		107	[comment="name: \"unsigned varint\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		110	[comment="name: \"string\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		112	[comment="name: \"int\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		115	[comment="name: \"[No Data]\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		159	[comment="name: \"PlayerBlockActions\", typeName: \"\", id: 159, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=PlayerBlockActions];
		162	[comment="name: \"[No Data]\", typeName: \"\", id: 162, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		165	[comment="name: \"Vec2\", typeName: \"\", id: 165, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
		167	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 167, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		169	[comment="name: \"Vec2\", typeName: \"\", id: 169, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec2];
	}
	0	[comment="name: \"PlayerAuthInputPacket\", typeName: \"\", id: 0, branchId: 144, recurseId: -1, attributes: 0, notes: \"\"",
		label=PlayerAuthInputPacket];
	1	[comment="name: \"Player Rotation\", typeName: \"Vec2\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Rotation"];
	0 -> 1;
	3	[comment="name: \"Player Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Position"];
	0 -> 3;
	5	[comment="name: \"Move Vector\", typeName: \"Vec2\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Move Vector"];
	0 -> 5;
	7	[comment="name: \"Player's Head Rotation\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Player's Head Rotation"];
	0 -> 7;
	9	[comment="name: \"Input Data\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Input Data"];
	0 -> 9;
	11	[comment="name: \"Input Mode\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: InputMode\"",
		label="Input Mode"];
	0 -> 11;
	13	[comment="name: \"Play Mode\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ClientPlayMode\"",
		label="Play Mode"];
	0 -> 13;
	15	[comment="name: \"New Interaction Model\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: NewInteractionModel\"",
		label="New Interaction Model"];
	0 -> 15;
	17	[comment="name: \"Dependency on 'Play Mode == ClientPlayMode::Reality'\", typeName: \"\", id: 17, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'Play Mode == ClientPlayMode::Reality'",
		shape=note];
	0 -> 17;
	23	[comment="name: \"Client tick\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"Which simulation frame client is on. \
Used to match corrections\"",
		label="Client tick"];
	0 -> 23;
	25	[comment="name: \"Pos Delta\", typeName: \"Vec3\", id: 25, branchId: 0, recurseId: -1, attributes: 256, notes: \"Velocity\"",
		label="Pos Delta"];
	0 -> 25;
	27	[comment="name: \"Dependency on 'ItemUseTransaction and PerformItemInteraction bit set'\", typeName: \"\", id: 27, branchId: 0, recurseId: -1, \
attributes: 2, notes: \"\"",
		label="Dependency on 'ItemUseTransaction and PerformItemInteraction bit set'",
		shape=note];
	0 -> 27;
	77	[comment="name: \"Dependency on 'ItemStackRequest and PerformItemStackRequest bit set'\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, \
attributes: 2, notes: \"\"",
		label="Dependency on 'ItemStackRequest and PerformItemStackRequest bit set'",
		shape=note];
	0 -> 77;
	113	[comment="name: \"Dependency on 'PerformBlockActions bit set'\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'PerformBlockActions bit set'",
		shape=note];
	0 -> 113;
	160	[comment="name: \"Dependency on 'IsInClientPredictedVehicle bit set'\", typeName: \"\", id: 160, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'IsInClientPredictedVehicle bit set'",
		shape=note];
	0 -> 160;
	168	[comment="name: \"Analog MoveVector\", typeName: \"Vec2\", id: 168, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Analog MoveVector"];
	0 -> 168;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	13 -> 14;
	15 -> 16;
	18	[comment="name: \"if (0)\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	17 -> 18;
	20	[comment="name: \"if (1)\", typeName: \"\", id: 20, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	17 -> 20;
	18 -> 19;
	21	[comment="name: \"VR Gaze Direction\", typeName: \"Vec3\", id: 21, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="VR Gaze Direction"];
	20 -> 21;
	21 -> 22;
	23 -> 24;
	25 -> 26;
	28	[comment="name: \"if (0)\", typeName: \"\", id: 28, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	27 -> 28;
	30	[comment="name: \"if (1)\", typeName: \"\", id: 30, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	27 -> 30;
	28 -> 29;
	31	[comment="name: \"Item Use Transaction\", typeName: \"PackedItemUseLegacyInventoryTransaction\", id: 31, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label="Item Use Transaction"];
	30 -> 31;
	31 -> 76;
	78	[comment="name: \"if (0)\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	77 -> 78;
	80	[comment="name: \"if (1)\", typeName: \"\", id: 80, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	77 -> 80;
	78 -> 79;
	81	[comment="name: \"Client Request Id\", typeName: \"TypedClientNetId<struct ItemStackRequestIdTag,int,0>\", id: 81, branchId: 0, recurseId: -1, \
attributes: 256, notes: \"\"",
		label="Client Request Id"];
	80 -> 81;
	86	[comment="name: \"Actions\", typeName: \"\", id: 86, branchId: 0, recurseId: -1, attributes: 8, notes: \"There are a variety of possible actions \
each with their own schema; this (Take) is just one example. Refer to the Item Stack Net Manager documentation.\"",
		label=Actions];
	80 -> 86;
	105	[comment="name: \"Strings To Filter\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 8, notes: \"Array of strings to submit \
to profanity filtering service\"",
		label="Strings To Filter"];
	80 -> 105;
	111	[comment="name: \"StringsToFilterOrigin\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: TextProcessingEventOrigin\"",
		label=StringsToFilterOrigin];
	80 -> 111;
	81 -> 85;
	87	[comment="name: \"Array Size\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	86 -> 87;
	89	[comment="name: \"example element\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	86 -> 89;
	87 -> 88;
	90	[comment="name: \"Action type\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemStackRequestActionType\"",
		label="Action type"];
	89 -> 90;
	92	[comment="name: \"Amount\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Amount];
	89 -> 92;
	94	[comment="name: \"Source\", typeName: \"ItemStackRequestSlotInfo\", id: 94, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Source];
	89 -> 94;
	103	[comment="name: \"Destination\", typeName: \"ItemStackRequestSlotInfo\", id: 103, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Destination];
	89 -> 103;
	90 -> 91;
	92 -> 93;
	94 -> 102;
	103 -> 104;
	106	[comment="name: \"Array Size\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	105 -> 106;
	108	[comment="name: \"example element\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	105 -> 108;
	106 -> 107;
	109	[comment="name: \"String To Filter\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 0, notes: \"Indivdiual string that needs \
checking\"",
		label="String To Filter"];
	108 -> 109;
	109 -> 110;
	111 -> 112;
	114	[comment="name: \"if (0)\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	113 -> 114;
	116	[comment="name: \"if (1)\", typeName: \"\", id: 116, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	113 -> 116;
	114 -> 115;
	117	[comment="name: \"Player Block Actions\", typeName: \"PlayerBlockActions\", id: 117, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Block Actions"];
	116 -> 117;
	117 -> 159;
	161	[comment="name: \"if (0)\", typeName: \"\", id: 161, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	160 -> 161;
	163	[comment="name: \"if (1)\", typeName: \"\", id: 163, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	160 -> 163;
	161 -> 162;
	164	[comment="name: \"Vehicle Rotation\", typeName: \"Vec2\", id: 164, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Vehicle Rotation"];
	163 -> 164;
	166	[comment="name: \"Client Predicted Vehicle\", typeName: \"ActorUniqueID\", id: 166, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Client Predicted Vehicle"];
	163 -> 166;
	164 -> 165;
	166 -> 167;
	168 -> 169;
}

```

## 字段

/// define
PlayerAuthInputPacket

Player Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 类型：Vec2。

Player Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

Move Vector：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 类型：Vec2。

Player's Head Rotation：<!-- md:samp float -->

- 类型：float。

Input Data：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。

Input Mode：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: InputMode

Play Mode：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ClientPlayMode

New Interaction Model：<!-- md:samp varint -->

- 类型：varint。enumeration: NewInteractionModel

Dependency on 'Play Mode == ClientPlayMode::Reality'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

VR Gaze Direction：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。


/////

////


Client tick：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。Which simulation frame client is on. Used to match corrections

Pos Delta：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Velocity

Dependency on 'ItemUseTransaction and PerformItemInteraction bit set'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Item Use Transaction：[<!-- md:samp PackedItemUseLegacyInventoryTransaction -->](../types/packeditemuselegacyinventorytransaction.md)

- 类型：PackedItemUseLegacyInventoryTransaction。


/////

////


Dependency on 'ItemStackRequest and PerformItemStackRequest bit set'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Client Request Id：[<!-- md:samp TypedClientNetId<struct ItemStackRequestIdTag,int,0> -->](../types/typedclientnetid<struct_itemstackrequestidtag,int,0>.md)

- 类型：TypedClientNetId<struct ItemStackRequestIdTag,int,0>。

Actions

////// define
Actions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


//////


////// define
Actions的示例元素

Action type：<!-- md:samp byte -->

- 类型：byte。enumeration: ItemStackRequestActionType

Amount：<!-- md:samp byte -->

- 类型：byte。

Source：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 类型：ItemStackRequestSlotInfo。

Destination：[<!-- md:samp ItemStackRequestSlotInfo -->](../types/itemstackrequestslotinfo.md)

- 类型：ItemStackRequestSlotInfo。


//////


Strings To Filter

////// define
Strings To Filter数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


//////


////// define
Strings To Filter的示例元素

String To Filter：<!-- md:samp string -->

- 类型：string。Indivdiual string that needs checking


//////


StringsToFilterOrigin：<!-- md:samp int -->

- 类型：int。enumeration: TextProcessingEventOrigin


/////

////


Dependency on 'PerformBlockActions bit set'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Player Block Actions：[<!-- md:samp PlayerBlockActions -->](../types/playerblockactions.md)

- 类型：PlayerBlockActions。


/////

////


Dependency on 'IsInClientPredictedVehicle bit set'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Vehicle Rotation：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 类型：Vec2。

Client Predicted Vehicle：[<!-- md:samp ActorUniqueID -->](../types/actoruniqueid.md)

- 类型：ActorUniqueID。


/////

////


Analog MoveVector：[<!-- md:samp Vec2 -->](../types/vec2.md)

- 类型：Vec2。


///
