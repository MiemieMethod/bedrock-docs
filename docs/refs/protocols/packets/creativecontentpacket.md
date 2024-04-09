# <!-- md:samp CreativeContentPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp CreativeContentPacket -->数据包，数字ID是`145`。该数据包用于protocol.packet.creativecontentpacket.description

## 结构

```viz
digraph "CreativeContentPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 9
4 -> 10
10 -> 11

0 [label="CreativeContentPacket",comment="name: \"CreativeContentPacket\", typeName: \"\", id: 0, branchId: 145, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Write Entries",comment="name: \"Write Entries\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Creative Net Id",comment="name: \"Creative Net Id\", typeName: \"TypedServerNetId<struct CreativeItemNetIdTag,unsigned int,0>\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
9 [label="TypedServerNetId<struct CreativeItemNetIdTag,unsigned int,0>",comment="name: \"TypedServerNetId<struct CreativeItemNetIdTag,unsigned int,0>\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
10 [label="Item Instance",comment="name: \"Item Instance\", typeName: \"NetworkItemInstanceDescriptor\", id: 10, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
11 [label="NetworkItemInstanceDescriptor",comment="name: \"NetworkItemInstanceDescriptor\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;9;11}

}

```

## 字段

```title='CreativeContentPacket'
[write_entries]
```

/// html | div.result
```title='Write Entries'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.creativecontentpacket.数组大小.description


/////
```title='示例元素'
[creative_net_id][item_instance]
```

///// html | div.result
////// define
Creative Net Id：[<!-- md:samp TypedServerNetId&lt;struct CreativeItemNetIdTag,unsigned int,0&gt; -->](../types/typedservernetid_struct_creativeitemnetidtag,unsigned_int,0_.md)

- 特殊类型。protocol.packet.creativecontentpacket.creative_net_id.description


//////
////// define
Item Instance：[<!-- md:samp NetworkItemInstanceDescriptor -->](../types/networkiteminstancedescriptor.md)

- 特殊类型。protocol.packet.creativecontentpacket.item_instance.description


//////

/////

////

///

