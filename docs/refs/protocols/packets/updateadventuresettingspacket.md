# <!-- md:samp UpdateAdventureSettingsPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp UpdateAdventureSettingsPacket -->数据包，数字ID是`188`。

## 结构

```viz
digraph UpdateAdventureSettingsPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		13	[comment="name: \"AdventureSettings\", typeName: \"\", id: 13, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=AdventureSettings];
	}
	0	[comment="name: \"UpdateAdventureSettingsPacket\", typeName: \"\", id: 0, branchId: 188, recurseId: -1, attributes: 0, notes: \"\"",
		label=UpdateAdventureSettingsPacket];
	1	[comment="name: \"Adventure Settings\", typeName: \"AdventureSettings\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Adventure Settings"];
	0 -> 1;
	1 -> 13;
}

```

## 字段

/// define
UpdateAdventureSettingsPacket

Adventure Settings：[<!-- md:samp AdventureSettings -->](../types/adventuresettings.md)

- 类型：AdventureSettings。


///
