# `BlockLocationIterator`

> 文档版本：1.21.0.24

`BlockLocationIterator`类，实现了<code>Iterator&lt;<a href="../vector3/">Vector3</a>&gt;</code>。一个方块坐标迭代器。

## 方法

/// define
`[Symbol.iterator]`


///

该迭代器的生成器函数。

```js
[Symbol.iterator](): Iterator<Vector3>
```

/// html | div.result
//// define
返回值：<code>Iterator&lt;<a href="../vector3/">Vector3</a>&gt;</code>

- 该迭代器的迭代器对象。


////

///


/// define
`next`


///

进行一次迭代并获取迭代结果。

```js
next(): IteratorResult<Vector3>
```

/// html | div.result
//// define
返回值：<code>IteratorResult&lt;<a href="../vector3/">Vector3</a>&gt;</code>

- 当前迭代结果对象。


////

///

