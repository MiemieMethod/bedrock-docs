# `Structure`

> 文档版本：1.21.0.20

`Structure`类。

## 属性

/// define
`id`


///

```js
read-only id: string;
```


/// define
`size`


///

```js
read-only size: Vector3;
```


## 方法

/// define
`getBlockPermutation`


///

```js
getBlockPermutation(location: Vector3): BlockPermutation | undefined
```


/// define
`getIsWaterlogged`


///

```js
getIsWaterlogged(location: Vector3): boolean
```


/// define
`isValid`


///

```js
isValid(): boolean
```


/// define
`saveAs`


///

```js
saveAs(identifier: string, saveMode: StructureSaveMode): Structure
```


/// define
`saveToWorld`


///

```js
saveToWorld(): void
```


/// define
`setBlockPermutation`


///

```js
setBlockPermutation(location: Vector3, blockPermutation?: BlockPermutation, waterlogged: boolean): void
```

