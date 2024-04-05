# <!-- md:samp CameraPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CameraPacket -->数据包，数字ID是`73`。

## 结构

```viz
digraph CameraPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
		4	[comment="name: \"ActorUniqueID\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=ActorUniqueID];
	}
	0	[comment="name: \"CameraPacket\", typeName: \"\", id: 0, branchId: 73, recurseId: -1, attributes: 0, notes: \"\"",
		label=CameraPacket];
	1	[comment="name: \"Camera ID\", typeName: \"ActorUniqueID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Camera ID"];
	0 -> 1;
	3	[comment="name: \"Target Player ID\", typeName: \"ActorUniqueID\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Target Player ID"];
	0 -> 3;
	1 -> 2;
	3 -> 4;
}

```

## 字段

/// define
CameraPacket

Camera ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。

Target Player ID：[<!-- md:samp ActorUniqueID -->](refs/protocols/types/actoruniqueid.md)

- 类型：ActorUniqueID。


///
