# <!-- md:samp MotionPredictionHintsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp MotionPredictionHintsPacket -->数据包，数字ID是`157`。

## 结构

```viz
digraph MotionPredictionHintsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"bool\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	0	[comment="name: \"MotionPredictionHintsPacket\", typeName: \"\", id: 0, branchId: 157, recurseId: -1, attributes: 0, notes: \"\"",
		label=MotionPredictionHintsPacket];
	1	[comment="name: \"mRuntimeId\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"Id of moving actor\"",
		label=mRuntimeId];
	0 -> 1;
	3	[comment="name: \"mMotion\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Position delta\"",
		label=mMotion];
	0 -> 3;
	5	[comment="name: \"mOnGround\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"Not falling / jumping\"",
		label=mOnGround];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
MotionPredictionHintsPacket

mRuntimeId：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。Id of moving actor

mMotion：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。Position delta

mOnGround：<!-- md:samp bool -->

- 类型：bool。Not falling / jumping


///
