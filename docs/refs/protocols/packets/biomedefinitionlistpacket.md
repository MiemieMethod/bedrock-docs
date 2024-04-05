# <!-- md:samp BiomeDefinitionListPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp BiomeDefinitionListPacket -->数据包，数字ID是`122`。

## 结构

```viz
digraph BiomeDefinitionListPacket {
	graph [rankdir=LR];
	{
		graph [rank=max];
		2	[comment="name: \"CompoundTag\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=CompoundTag];
	}
	0	[comment="name: \"BiomeDefinitionListPacket\", typeName: \"\", id: 0, branchId: 122, recurseId: -1, attributes: 0, notes: \"\"",
		label=BiomeDefinitionListPacket];
	1	[comment="name: \"Biome Definition Data\", typeName: \"CompoundTag\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"CompoundTag \
containing one object per biome definition:BiomeName: {temperature (float),downfall(float),red_spores (float),blue_spores (float),\
ash (float),white_ash (float),depth (float),height (float),waterColorR (float),waterColorG (float),waterColorB (float),waterColorA (\
float),waterTransparency (float),rain (bool),tags (ListTag)name_hash, (std::string)}\"",
		label="Biome Definition Data"];
	0 -> 1;
	1 -> 2;
}

```

## 字段

/// define
BiomeDefinitionListPacket

Biome Definition Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 类型：CompoundTag。CompoundTag containing one object per biome definition:BiomeName: {temperature (float),downfall(float),red_spores (float),blue_spores (float),ash (float),white_ash (float),depth (float),height (float),waterColorR (float),waterColorG (float),waterColorB (float),waterColorA (float),waterTransparency (float),rain (bool),tags (ListTag)'name'_hash, (std::string)}


///
