# `TransactionManager`

> 文档版本：1.21.60.21

`TransactionManager`类。script_api.@minecraft/server-editor-bindings.transactionmanager.description

## 方法

/// define
`addEntityOperation`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.addentityoperation.description

```js
addEntityOperation(entity: Entity, type: EntityOperationType): boolean
```

/// html | div.result
//// define
`entity`：[`Entity`](../../server/beta/entity.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.addentityoperation.entity.description


////

//// define
`type`：[`EntityOperationType`](./entityoperationtype.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.addentityoperation.type.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.addentityoperation.return


////

///


/// define
`addUserDefinedOperation`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.adduserdefinedoperation.description

```js
addUserDefinedOperation(transactionHandlerId: UserDefinedTransactionHandlerId, operationData: string, operationName?: string): void
```

/// html | div.result
//// define
`transactionHandlerId`：[`UserDefinedTransactionHandlerId`](./userdefinedtransactionhandlerid.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.adduserdefinedoperation.transactionhandlerid.description


////

//// define
`operationData`：`string`

- script_api.@minecraft/server-editor-bindings.transactionmanager.adduserdefinedoperation.operationdata.description


////

//// define
`operationName`?：`string`＝`null`

- script_api.@minecraft/server-editor-bindings.transactionmanager.adduserdefinedoperation.operationname.description


////

//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.transactionmanager.adduserdefinedoperation.return


////

///


/// define
`commitOpenTransaction`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.commitopentransaction.description

```js
commitOpenTransaction(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.commitopentransaction.return


////

///


/// define
`commitTrackedChanges`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.committrackedchanges.description

```js
commitTrackedChanges(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server-editor-bindings.transactionmanager.committrackedchanges.return


////

///


/// define
`createUserDefinedTransactionHandler`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.createuserdefinedtransactionhandler.description

```js
createUserDefinedTransactionHandler(undoClosure: (arg: string) => void, redoClosure: (arg: string) => void): UserDefinedTransactionHandlerId
```

/// html | div.result
//// define
`undoClosure`：<code>(string) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.transactionmanager.createuserdefinedtransactionhandler.undoclosure.description


////

//// define
`redoClosure`：<code>(string) =&gt; void</code>

- script_api.@minecraft/server-editor-bindings.transactionmanager.createuserdefinedtransactionhandler.redoclosure.description


////

//// define
返回值：[`UserDefinedTransactionHandlerId`](./userdefinedtransactionhandlerid.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.createuserdefinedtransactionhandler.return


////

///


/// define
`discardOpenTransaction`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.discardopentransaction.description

```js
discardOpenTransaction(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.discardopentransaction.return


////

///


/// define
`discardTrackedChanges`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.discardtrackedchanges.description

```js
discardTrackedChanges(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server-editor-bindings.transactionmanager.discardtrackedchanges.return


////

///


/// define
`openTransaction`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.opentransaction.description

```js
openTransaction(name: string): boolean
```

/// html | div.result
//// define
`name`：`string`

- script_api.@minecraft/server-editor-bindings.transactionmanager.opentransaction.name.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.opentransaction.return


////

///


/// define
`redo`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.redo.description

```js
redo(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.transactionmanager.redo.return


////

///


/// define
`redoSize`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.redosize.description

```js
redoSize(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server-editor-bindings.transactionmanager.redosize.return


////

///


/// define
`trackBlockChangeArea`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangearea.description

```js
trackBlockChangeArea(from: Vector3, to: Vector3): boolean
```

/// html | div.result
//// define
`from`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangearea.from.description


////

//// define
`to`：[`Vector3`](../../server/beta/vector3.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangearea.to.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangearea.return


////

///


/// define
`trackBlockChangeCompoundBlockVolume`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangecompoundblockvolume.description

```js
trackBlockChangeCompoundBlockVolume(compoundBlockVolume: CompoundBlockVolume): boolean
```

/// html | div.result
//// define
`compoundBlockVolume`：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangecompoundblockvolume.compoundblockvolume.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangecompoundblockvolume.return


////

///


/// define
`trackBlockChangeList`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangelist.description

```js
trackBlockChangeList(locations: Vector3[]): boolean
```

/// html | div.result
//// define
`locations`：<code><a href="../../../server/beta/vector3/">Vector3</a>[]</code>

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangelist.locations.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangelist.return


////

///


/// define
`trackBlockChangeSelection`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangeselection.description

```js
trackBlockChangeSelection(selection: Selection): boolean
```

/// html | div.result
//// define
`selection`：[`Selection`](./selection.md)

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangeselection.selection.description


////

//// define
返回值：`boolean`

- script_api.@minecraft/server-editor-bindings.transactionmanager.trackblockchangeselection.return


////

///


/// define
`undo`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.undo.description

```js
undo(): void
```

/// html | div.result
//// define
返回值：`void`

- script_api.@minecraft/server-editor-bindings.transactionmanager.undo.return


////

///


/// define
`undoSize`


///

script_api.@minecraft/server-editor-bindings.transactionmanager.undosize.description

```js
undoSize(): int32
```

/// html | div.result
//// define
返回值：`int32`

- script_api.@minecraft/server-editor-bindings.transactionmanager.undosize.return


////

///

