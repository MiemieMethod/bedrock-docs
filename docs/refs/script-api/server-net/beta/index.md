# `@minecraft/server-net`

> 文档版本：1.21.60.21

`@minecraft/server-net`模块的`1.0.0-beta`版本，UUID为`777b1798-13a6-401c-9cba-0cf17e31a81b`。该模块是script_api.@minecraft/server-net.description

/// info | 依赖
该模块依赖于以下模块：

- `@minecraft/common`|`1.0.0`|`77ec12b4-1b2b-4c98-8d34-d1cd63f849d5`
- `@minecraft/server`|`1.0.0`|`b26a4d4c-afdf-4690-88f8-931846312678`
- `@minecraft/server-admin`|`1.0.0-beta`|`53d7f2bf-bf9c-49c4-ad1f-7c803d947920`
///

## 对象

/// define
`beforeEvents`


///

```js
static read-only beforeEvents: NetworkBeforeEvents;
```

/// html | div.result
//// define
`beforeEvents`：[`NetworkBeforeEvents`](./networkbeforeevents.md)

- script_api.@minecraft/server-net.beforeevents.description


////

///


/// define
`http`


///

```js
static read-only http: HttpClient;
```

/// html | div.result
//// define
`http`：[`HttpClient`](./httpclient.md)

- script_api.@minecraft/server-net.http.description


////

///


## 类

|类|描述|
|---|---|
|[`HttpClient`](./httpclient.md)||
|[`HttpHeader`](./httpheader.md)||
|[`HttpRequest`](./httprequest.md)||
|[`HttpResponse`](./httpresponse.md)||
|[`NetworkBeforeEvents`](./networkbeforeevents.md)||
|[`PacketReceiveBeforeEventSignal`](./packetreceivebeforeeventsignal.md)||
|[`PacketReceivedBeforeEvent`](./packetreceivedbeforeevent.md)||
|[`PacketSendBeforeEvent`](./packetsendbeforeevent.md)||
|[`PacketSendBeforeEventSignal`](./packetsendbeforeeventsignal.md)||

## 接口

|接口|描述|
|---|---|
|[`PacketEventOptions`](./packeteventoptions.md)||

## 枚举

|枚举|描述|
|---|---|
|[`HttpRequestMethod`](./httprequestmethod.md)||
|[`PacketId`](./packetid.md)||
