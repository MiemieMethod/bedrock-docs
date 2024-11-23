# <!-- md:samp ContainerRegistryCleanupPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp ContainerRegistryCleanupPacket -->数据包，数字ID是`317`。该数据包用于protocol.packet.containerregistrycleanuppacket.description

## 结构

```viz
digraph "ContainerRegistryCleanupPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
2 -> 3
1 -> 4
4 -> 5
5 -> 6

0 [label="ContainerRegistryCleanupPacket",comment="name: \"ContainerRegistryCleanupPacket\", typeName: \"\", id: 0, branchId: 317, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Removed Containers",comment="name: \"Removed Containers\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 8, notes: \"\""];
2 [label="Array Size",comment="name: \"Array Size\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
3 [label="unsigned varint",comment="name: \"unsigned varint\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
4 [label="example element",style=dotted,comment="name: \"example element\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 16, notes: \"\""];
5 [label="Full Container Name",comment="name: \"Full Container Name\", typeName: \"FullContainerName\", id: 5, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
6 [label="FullContainerName",comment="name: \"FullContainerName\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;3;6}

}

```

## 字段

```title='ContainerRegistryCleanupPacket'
[removed_containers]
```

/// html | div.result
```title='Removed Containers'
[array_size][[example_element]..]
```

//// html | div.result
///// define
数组大小：<!-- md:samp unsigned varint -->

- 基本类型。protocol.packet.containerregistrycleanuppacket.removed_containers.array_size.description


/////
```title='示例元素'
[full_container_name]
```

///// html | div.result
////// define
Full Container Name：[<!-- md:samp FullContainerName -->](../types/fullcontainername.md)

- 特殊类型。protocol.packet.containerregistrycleanuppacket.removed_containers.example_element.full_container_name.description


//////

/////

////

///

