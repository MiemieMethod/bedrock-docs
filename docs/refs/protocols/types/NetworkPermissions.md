# <!-- md:samp NetworkPermissions -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp NetworkPermissions -->类型。

## 结构

```dot
digraph NetworkPermissions {
	graph [rankdir=LR];
	{
		graph [rank=max];
		199	[comment="name: \"bool\", typeName: \"\", id: 199, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=bool];
	}
	197	[comment="name: \"NetworkPermissions\", typeName: \"\", id: 197, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=NetworkPermissions];
	198	[comment="name: \"serverAuthSoundEnabled\", typeName: \"\", id: 198, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=serverAuthSoundEnabled];
	197 -> 198;
	198 -> 199;
}

```

## 字段

/// define
NetworkPermissions

serverAuthSoundEnabled：<!-- md:samp bool -->

- 类型：bool。


///
