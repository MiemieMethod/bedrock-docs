# `TransactionManager`

> 文档版本：1.21.0.20

`TransactionManager`类。

## 方法

/// define
`addUserDefinedOperation`


///

```js
addUserDefinedOperation(transactionHandlerId: UserDefinedTransactionHandlerId, operationData: string, operationName?: string): void
```

/// html | div.result
//// define
`transactionHandlerId`：[`UserDefinedTransactionHandlerId`](./userdefinedtransactionhandlerid.md)

- 参数1。


////

//// define
`operationData`：`string`

- 参数2。


////

//// define
`operationName`：`string`|`undefined`

- 参数3。


////

//// define
返回值：`void`

- 返回值。


////

///


/// define
`commitOpenTransaction`


///

```js
commitOpenTransaction(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`commitTrackedChanges`


///

```js
commitTrackedChanges(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`createUserDefinedTransactionHandler`


///

```js
createUserDefinedTransactionHandler(undoClosure: (arg: string) => void, redoClosure: (arg: string) => void): UserDefinedTransactionHandlerId
```

/// html | div.result
//// define
`undoClosure`：<code>(string) =&gt; void</code>

- 参数1。


////

//// define
`redoClosure`：<code>(string) =&gt; void</code>

- 参数2。


////

//// define
返回值：[`UserDefinedTransactionHandlerId`](./userdefinedtransactionhandlerid.md)

- 返回值。


////

///


/// define
`discardOpenTransaction`


///

```js
discardOpenTransaction(): boolean
```

/// html | div.result
//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`discardTrackedChanges`


///

```js
discardTrackedChanges(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`openTransaction`


///

```js
openTransaction(name: string): boolean
```

/// html | div.result
//// define
`name`：`string`

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`redo`


///

```js
redo(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`redoSize`


///

```js
redoSize(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///


/// define
`trackBlockChangeArea`


///

```js
trackBlockChangeArea(from: Vector3, to: Vector3): boolean
```

/// html | div.result
//// define
`from`：[`Vector3`](../../server/beta/vector3.md)

- 参数1。


////

//// define
`to`：[`Vector3`](../../server/beta/vector3.md)

- 参数2。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`trackBlockChangeCompoundBlockVolume`


///

```js
trackBlockChangeCompoundBlockVolume(compoundBlockVolume: CompoundBlockVolume): boolean
```

/// html | div.result
//// define
`compoundBlockVolume`：[`CompoundBlockVolume`](../../server/beta/compoundblockvolume.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`trackBlockChangeList`


///

```js
trackBlockChangeList(locations: Vector3[]): boolean
```

/// html | div.result
//// define
`locations`：<code><a href="../../../server/beta/vector3/">Vector3</a>[]</code>

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`trackBlockChangeSelection`


///

```js
trackBlockChangeSelection(selection: Selection): boolean
```

/// html | div.result
//// define
`selection`：[`Selection`](./selection.md)

- 参数1。


////

//// define
返回值：`boolean`

- 返回值。


////

///


/// define
`undo`


///

```js
undo(): void
```

/// html | div.result
//// define
返回值：`void`

- 返回值。


////

///


/// define
`undoSize`


///

```js
undoSize(): int32
```

/// html | div.result
//// define
返回值：`int32`

- 返回值。


////

///

