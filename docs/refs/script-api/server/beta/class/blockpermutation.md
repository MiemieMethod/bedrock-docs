# `BlockPermutation`

> 文档版本：1.21.0.20

`BlockPermutation`类。

## 属性

/// define
`type`


///

```js
read-only type: BlockType
```


## 方法

/// define
getAllStates

- ```js
getAllStates(): Record<string, boolean | int32 | string>
```



///


/// define
getItemStack

- ```js
getItemStack(amount: int32): ItemStack | undefined
```



///


/// define
getState

- ```js
getState(stateName: string): boolean | int32 | string | undefined
```



///


/// define
getTags

- ```js
getTags(): string[]
```



///


/// define
hasTag

- ```js
hasTag(tag: string): boolean
```



///


/// define
matches

- ```js
matches(blockName: string, states?: Record<string, boolean | int32 | string>): boolean
```



///


/// define
resolve

- ```js
static resolve(blockName: string, states?: Record<string, boolean | int32 | string>): BlockPermutation
```



///


/// define
withState

- ```js
withState(name: string, value: boolean | int32 | string): BlockPermutation
```



///

