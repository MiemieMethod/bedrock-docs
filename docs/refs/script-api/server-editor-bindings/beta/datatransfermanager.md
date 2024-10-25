# `DataTransferManager`

> 文档版本：1.21.50.25

`DataTransferManager`类。script_api.@minecraft/server-editor-bindings.datatransfermanager.description

## 方法

/// define
`getRegisteredAccessors`


///

script_api.@minecraft/server-editor-bindings.datatransfermanager.getregisteredaccessors.description

```js
getRegisteredAccessors(): DataTransferCollectionNameData[]
```

/// html | div.result
//// define
返回值：<code><a href="../datatransfercollectionnamedata/">DataTransferCollectionNameData</a>[]</code>

- script_api.@minecraft/server-editor-bindings.datatransfermanager.getregisteredaccessors.return


////

///


/// define
`requestData`


///

script_api.@minecraft/server-editor-bindings.datatransfermanager.requestdata.description

```js
requestData(collectionUniqueId: string): Promise<DataTransferRequestResponse>
```

/// html | div.result
//// define
`collectionUniqueId`：`string`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.requestdata.collectionuniqueid.description


////

//// define
返回值：<code>Promise&lt;<a href="../datatransferrequestresponse/">DataTransferRequestResponse</a>&gt;</code>

- script_api.@minecraft/server-editor-bindings.datatransfermanager.requestdata.return


////

///


/// define
`sendData`


///

script_api.@minecraft/server-editor-bindings.datatransfermanager.senddata.description

```js
sendData(collectionUniqueId: string, jsonData: string): void
```

/// html | div.result
//// define
`collectionUniqueId`：`string`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.senddata.collectionuniqueid.description


////

//// define
`jsonData`：`string`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.senddata.jsondata.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.senddata.return


////

///


/// define
`sendDataToClipboard`


///

script_api.@minecraft/server-editor-bindings.datatransfermanager.senddatatoclipboard.description

```js
sendDataToClipboard(jsonData: string): void
```

/// html | div.result
//// define
`jsonData`：`string`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.senddatatoclipboard.jsondata.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.datatransfermanager.senddatatoclipboard.return


////

///

