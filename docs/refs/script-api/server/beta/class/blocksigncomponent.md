# `BlockSignComponent`

> 文档版本：1.21.0.20

`BlockSignComponent`类。

## 属性

/// define
`isWaxed`


///

```js
read-only isWaxed: boolean
```


## 方法

/// define
`getRawText`


///

```js
getRawText(side: SignSide): RawText | undefined
```


/// define
`getText`


///

```js
getText(side: SignSide): string | undefined
```


/// define
`getTextDyeColor`


///

```js
getTextDyeColor(side: SignSide): DyeColor | undefined
```


/// define
`setText`


///

```js
setText(message: RawMessage | RawText | string, side: SignSide): void
```


/// define
`setTextDyeColor`


///

```js
setTextDyeColor(color?: DyeColor, side: SignSide): void
```


/// define
`setWaxed`


///

```js
setWaxed(waxed: boolean): void
```

