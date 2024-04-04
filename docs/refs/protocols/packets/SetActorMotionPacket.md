# <!-- md:samp SetActorMotionPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetActorMotionPacket -->数据包，数字ID是`40`。

## 结构

```viz
digraph SetActorMotionPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
		4	[comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		6	[comment="name: \"unsigned varint64\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint64"];
	}
	0	[comment="name: \"SetActorMotionPacket\", typeName: \"\", id: 0, branchId: 40, recurseId: -1, attributes: 0, notes: \"\"",
		label=SetActorMotionPacket];
	1	[comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Runtime ID"];
	0 -> 1;
	3	[comment="name: \"Motion\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Motion];
	0 -> 3;
	5	[comment="name: \"Server Tick\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Server Tick"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
SetActorMotionPacket

Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](refs/protocols/types/ActorRuntimeID.md)

- 类型：ActorRuntimeID。

Motion：[<!-- md:samp Vec3 -->](refs/protocols/types/Vec3.md)

- 类型：Vec3。

Server Tick：<!-- md:samp unsigned varint64 -->

- 类型：unsigned varint64。


///
