# <!-- md:samp OnScreenTextureAnimationPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp OnScreenTextureAnimationPacket -->数据包，数字ID是`130`。

## 结构

```dot
digraph OnScreenTextureAnimationPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"unsigned int\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned int"];
	}
	0	[comment="name: \"OnScreenTextureAnimationPacket\", typeName: \"\", id: 0, branchId: 130, recurseId: -1, attributes: 0, notes: \"\"",
		label=OnScreenTextureAnimationPacket];
	1	[comment="name: \"Effect Id\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"Id of the effect whose icon should be \
shown on-screen.\"",
		label="Effect Id"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
OnScreenTextureAnimationPacket

Effect Id：<!-- md:samp unsigned int -->

- 类型：unsigned int。Id of the effect whose icon should be shown on-screen.


///
