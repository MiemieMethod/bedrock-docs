# <!-- md:samp AnimateEntityPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp AnimateEntityPacket -->数据包，数字ID是`158`。

## 结构

```viz
digraph AnimateEntityPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"string\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		4	[comment="name: \"string\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		6	[comment="name: \"string\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		8	[comment="name: \"int\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=int];
		10	[comment="name: \"string\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=string];
		12	[comment="name: \"float\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=float];
		15	[comment="name: \"unsigned varint\", typeName: \"\", id: 15, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		18	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 18, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
	}
	0	[comment="name: \"AnimateEntityPacket\", typeName: \"\", id: 0, branchId: 158, recurseId: -1, attributes: 0, notes: \"\"",
		label=AnimateEntityPacket];
	1	[comment="name: \"mAnimation\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of the animation that the specified \
entities are to play.\"",
		label=mAnimation];
	0 -> 1;
	3	[comment="name: \"mNextState\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"The next state to transition to once \
the specified animation is finished playing.\"",
		label=mNextState];
	0 -> 3;
	5	[comment="name: \"mStopExpression\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"The stop expression, the the condition \
that determines when to transition to the next state.\"",
		label=mStopExpression];
	0 -> 5;
	7	[comment="name: \"Stop expression molang version\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: MolangVersion\"",
		label="Stop expression molang version"];
	0 -> 7;
	9	[comment="name: \"mController\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"The name of an animation controller\"",
		label=mController];
	0 -> 9;
	11	[comment="name: \"mBlendOutTime\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"The amount of time to blend out \
of this animation\"",
		label=mBlendOutTime];
	0 -> 11;
	13	[comment="name: \"mRuntimeIds\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 8, notes: \"ActorRuntimeIDs of the entities that \
will play the specified animation\"",
		label=mRuntimeIds];
	0 -> 13;
	1 -> 2;
	3 -> 4;
	5 -> 6;
	7 -> 8;
	9 -> 10;
	11 -> 12;
	14	[comment="name: \"Array Size\", typeName: \"\", id: 14, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	13 -> 14;
	16	[comment="name: \"example element\", typeName: \"\", id: 16, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	13 -> 16;
	14 -> 15;
	17	[comment="name: \"runtimeId\", typeName: \"ActorRuntimeID\", id: 17, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=runtimeId];
	16 -> 17;
	17 -> 18;
}

```

## 字段

/// define
AnimateEntityPacket

mAnimation：<!-- md:samp string -->

- 类型：string。The 'name' of the animation that the specified entities are to play.

mNextState：<!-- md:samp string -->

- 类型：string。The next state to transition to once the specified animation is finished playing.

mStopExpression：<!-- md:samp string -->

- 类型：string。The stop expression, the the condition that determines when to transition to the next state.

Stop expression molang version：<!-- md:samp int -->

- 类型：int。enumeration: MolangVersion

mController：<!-- md:samp string -->

- 类型：string。The 'name' of an animation controller

mBlendOutTime：<!-- md:samp float -->

- 类型：float。The amount of time to blend out of this animation

mRuntimeIds

//// define
mRuntimeIds数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
mRuntimeIds的示例元素

runtimeId：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


////



///
