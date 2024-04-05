# <!-- md:samp PackedItemUseLegacyInventoryTransaction -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp PackedItemUseLegacyInventoryTransaction -->类型。

## 结构

```viz
digraph PackedItemUseLegacyInventoryTransaction {
	graph [rankdir=LR];
	{
		graph [rank=max];
		37	[comment="name: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: \
512, notes: \"\"",
			label="TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>"];
		40	[comment="name: \"[No Data]\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="[No Data]"];
		44	[comment="name: \"unsigned varint\", typeName: \"\", id: 44, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		47	[comment="name: \"byte\", typeName: \"\", id: 47, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		50	[comment="name: \"unsigned varint\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		53	[comment="name: \"byte\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=byte];
		56	[comment="name: \"unsigned varint\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		59	[comment="name: \"InventoryAction\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=InventoryAction];
		61	[comment="name: \"unsigned varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
		63	[comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkBlockPosition];
		65	[comment="name: \"varint\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		67	[comment="name: \"varint\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=varint];
		69	[comment="name: \"NetworkItemStackDescriptor\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=NetworkItemStackDescriptor];
		71	[comment="name: \"Vec3\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		73	[comment="name: \"Vec3\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label=Vec3];
		75	[comment="name: \"unsigned varint\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\"",
			label="unsigned varint"];
	}
	32	[comment="name: \"PackedItemUseLegacyInventoryTransaction\", typeName: \"\", id: 32, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=PackedItemUseLegacyInventoryTransaction];
	33	[comment="name: \"ID\", typeName: \"TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>\", id: 33, branchId: 0, recurseId: -1, attributes: \
256, notes: \"\"",
		label=ID];
	32 -> 33;
	38	[comment="name: \"Dependency on 'valid ID'\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 2, notes: \"\"",
		label="Dependency on 'valid ID'",
		shape=note];
	32 -> 38;
	54	[comment="name: \"Actions\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Actions];
	32 -> 54;
	60	[comment="name: \"Action Type\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ItemUseInventoryTransaction::\
ActionType\"",
		label="Action Type"];
	32 -> 60;
	62	[comment="name: \"Position\", typeName: \"NetworkBlockPosition\", id: 62, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Position];
	32 -> 62;
	64	[comment="name: \"Face\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Face];
	32 -> 64;
	66	[comment="name: \"Slot\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	32 -> 66;
	68	[comment="name: \"Item\", typeName: \"NetworkItemStackDescriptor\", id: 68, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Item];
	32 -> 68;
	70	[comment="name: \"From Position\", typeName: \"Vec3\", id: 70, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="From Position"];
	32 -> 70;
	72	[comment="name: \"Click Position\", typeName: \"Vec3\", id: 72, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label="Click Position"];
	32 -> 72;
	74	[comment="name: \"Target Block Id\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Target Block Id"];
	32 -> 74;
	33 -> 37;
	39	[comment="name: \"if (0)\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (0)",
		shape=diamond];
	38 -> 39;
	41	[comment="name: \"if (1)\", typeName: \"\", id: 41, branchId: 1, recurseId: -1, attributes: 4, notes: \"\"",
		label="if (1)",
		shape=diamond];
	38 -> 41;
	39 -> 40;
	42	[comment="name: \"Container Slots\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label="Container Slots"];
	41 -> 42;
	43	[comment="name: \"Array Size\", typeName: \"\", id: 43, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	42 -> 43;
	45	[comment="name: \"example element\", typeName: \"\", id: 45, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	42 -> 45;
	43 -> 44;
	46	[comment="name: \"Container Enum Name\", typeName: \"\", id: 46, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ContainerEnumName\"",
		label="Container Enum Name"];
	45 -> 46;
	48	[comment="name: \"Slots\", typeName: \"\", id: 48, branchId: 0, recurseId: -1, attributes: 8, notes: \"\"",
		label=Slots];
	45 -> 48;
	46 -> 47;
	49	[comment="name: \"Array Size\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	48 -> 49;
	51	[comment="name: \"example element\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	48 -> 51;
	49 -> 50;
	52	[comment="name: \"Slot\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label=Slot];
	51 -> 52;
	52 -> 53;
	55	[comment="name: \"Array Size\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 0, notes: \"\"",
		label="Array Size"];
	54 -> 55;
	57	[comment="name: \"example element\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 16, notes: \"\"",
		label="example element",
		style=dotted];
	54 -> 57;
	55 -> 56;
	58	[comment="name: \"Action\", typeName: \"InventoryAction\", id: 58, branchId: 0, recurseId: -1, attributes: 256, notes: \"\"",
		label=Action];
	57 -> 58;
	58 -> 59;
	60 -> 61;
	62 -> 63;
	64 -> 65;
	66 -> 67;
	68 -> 69;
	70 -> 71;
	72 -> 73;
	74 -> 75;
}

```

## 字段

/// define
PackedItemUseLegacyInventoryTransaction

ID：[<!-- md:samp TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0> -->](../types/typedclientnetid<struct_itemstacklegacyrequestidtag,int,0>.md)

- 类型：TypedClientNetId<struct ItemStackLegacyRequestIdTag,int,0>。

Dependency on 'valid ID'

//// tab | if (0)
///// define
if (0)：<!-- md:samp [No Data] -->

- 类型：[No Data]。


/////

////

//// tab | if (1)
///// define
if (1)

Container Slots

////// define
Container Slots数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


//////


////// define
Container Slots的示例元素

Container Enum Name：<!-- md:samp byte -->

- 类型：byte。enumeration: ContainerEnumName

Slots

/////// define
Slots数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///////


/////// define
Slots的示例元素

Slot：<!-- md:samp byte -->

- 类型：byte。


///////



//////



/////

////


Actions

//// define
Actions数组的大小：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


////


//// define
Actions的示例元素

Action：[<!-- md:samp InventoryAction -->](../types/inventoryaction.md)

- 类型：InventoryAction。


////


Action Type：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。enumeration: ItemUseInventoryTransaction::ActionType

Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 类型：NetworkBlockPosition。

Face：<!-- md:samp varint -->

- 类型：varint。

Slot：<!-- md:samp varint -->

- 类型：varint。

Item：[<!-- md:samp NetworkItemStackDescriptor -->](../types/networkitemstackdescriptor.md)

- 类型：NetworkItemStackDescriptor。

From Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

Click Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 类型：Vec3。

Target Block Id：<!-- md:samp unsigned varint -->

- 类型：unsigned varint。


///
