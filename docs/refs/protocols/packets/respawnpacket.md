# <!-- md:samp RespawnPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp RespawnPacket -->数据包，数字ID是`45`。

## 结构

```viz
digraph RespawnPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"Vec3\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		4	[comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		6	[comment="name: \"ActorRuntimeID\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorRuntimeID];
	}
	0	[comment="name: \"RespawnPacket\", typeName: \"\", id: 0, branchId: 45, recurseId: -1, attributes: 0, notes: \"\"",
		label=RespawnPacket];
	1	[comment="name: \"Position\", typeName: \"Vec3\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	0 -> 1;
	3	[comment="name: \"State\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerRespawnState\"",
		label=State];
	0 -> 3;
	5	[comment="name: \"Player Runtime Id\", typeName: \"ActorRuntimeID\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Player Runtime Id"];
	0 -> 5;
	1 -> 2;
	3 -> 4;
	5 -> 6;
}

```

## 字段

/// define
RespawnPacket

Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

State：<!-- md:samp byte -->

- 类型：byte。enumeration: PlayerRespawnState

Player Runtime Id：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- 类型：ActorRuntimeID。


///
