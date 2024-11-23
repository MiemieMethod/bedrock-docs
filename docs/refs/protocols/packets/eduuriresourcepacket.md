# <!-- md:samp EduUriResourcePacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp EduUriResourcePacket -->数据包，数字ID是`170`。该数据包用于protocol.packet.eduuriresourcepacket.description

## 结构

```viz
digraph "EduUriResourcePacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="EduUriResourcePacket",comment="name: \"EduUriResourcePacket\", typeName: \"\", id: 0, branchId: 170, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Edu Shared URI Resource",comment="name: \"Edu Shared URI Resource\", typeName: \"EduSharedUriResource\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="EduSharedUriResource",comment="name: \"EduSharedUriResource\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='EduUriResourcePacket'
[edu_shared_uri_resource]
```

/// html | div.result
//// define
Edu Shared URI Resource：[<!-- md:samp EduSharedUriResource -->](../types/edushareduriresource.md)

- 特殊类型。protocol.packet.eduuriresourcepacket.edu_shared_uri_resource.description


////

///

