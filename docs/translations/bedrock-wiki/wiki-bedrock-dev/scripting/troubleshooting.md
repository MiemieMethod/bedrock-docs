---
title: JavaScript故障排除
category: 文档
mentions:
    - Herobrine643928
    - JaylyDev
    - SmokeyStack
    - ThomasOrs
description: JavaScript故障排除。
---

本文教你调试任何JavaScript问题的基本工作流程。

## 错误参考

这些错误在调试代码时可能会很有帮助，但报告的问题并不总是立即清晰。大多数这些错误在JavaScript引擎中很常见，因此可以通过搜索引擎（例如Google搜索）找到。

你可以通过点击每个错误名称下方的链接，了解更多关于每个错误类的信息。

- [`EvalError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/EvalError)
    - 创建一个实例，表示与全局函数`eval()`相关的错误。
- [`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
    - 创建一个实例，表示当数字变量或参数超出其有效范围时发生的错误。
- [`ReferenceError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError)
    - 创建一个实例，表示在解引用无效引用时发生的错误。在Minecraft脚本引擎中，有一个引用错误，原因不明确：
    - 绑定到原型的本地对象不存在。
- [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
    - 创建一个实例，表示语法错误。
- [`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)
    - 创建一个实例，表示当变量或参数不是有效类型时发生的错误。
- [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
    - 创建一个实例，表示当`encodeURI()`或`decodeURI()`传入无效参数时发生的错误。
- [`AggregateError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError)
    - 创建一个实例，表示当一个操作需要报告多个错误时，将多个错误封装在一个错误中，例如通过`Promise.any()`。
- [`InternalError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/InternalError)
    - 创建一个实例，表示当JavaScript引擎内部错误被抛出时发生的错误。在Minecraft JS中，错误如下：
        - 堆栈溢出
        - 内存不足

## Minecraft JS错误

由于Minecraft基岩版使用其自己的JavaScript版本，该版本基于QuickJS，因此存在一些仅在Minecraft中存在的错误，这些错误相当常见，因为API是基于本地C++构建的。

### InternalError: 内存不足

当组合内存使用超过250兆字节时，会发生此错误。

这会通过Watchdog终止保存并关闭世界，无法通过`BeforeWatchdogTerminateEvent`取消。

可以通过修改`server.properties`中的`script-watchdog-memory-limit`来调整内存限制。（将此值设置为0将禁用限制。）

### InternalError: 堆栈溢出

当存在一个没有退出点的递归函数（调用自身的函数）时发生。

示例代码：

```js
function loop(x) {
  // 缺少基本情况
  loop(x + 1); // 递归调用
}
loop(0);
// InternalError: 堆栈溢出
```

### InternalError: 中断

当运行时成本微不足道时发生。这取决于你的脚本设置。

### TypeError: 属性没有设置器

当尝试为仅定义了getter的属性设置新值时发生。

在尝试为本地模块中的本地对象设置属性时，这种情况很常见。

### TypeError: 值不可迭代

当对一个不是可迭代对象的值进行迭代时发生。

点击[**这里**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/is_not_iterable)获取更多信息。

### TypeError: 不是一个函数

当尝试调用一个值作为函数，但该值实际上不是函数时发生。这种情况非常常见，因为脚本API不断删除或重命名方法，而没有在Minecraft更新日志中提及它们。

点击[**这里**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Not_a_function)获取更多信息。

### TypeError: 本地类型转换失败

当你向本地方法的必需参数输入错误类型的值时，会发生此错误。

### TypeError: 本地变体类型转换失败

当你向本地方法的可选参数输入错误类型的值时，会发生此错误。

### TypeError: 对象没有本地句柄

::: warning
此错误未公开记录，因此解释是估计的。
:::

当脚本尝试从JavaScript对象获取本地句柄，但句柄实例已被清除时，会抛出此错误。

### ReferenceError: 绑定到原型的本地对象不存在。

::: warning
此错误未公开记录，因此解释是估计的。
:::

当由于意外原因而导致本地代码库不支持某个方法时，会抛出此错误。在某些情况下，重启游戏应该可以解决该问题。

## 调试

调试可以让你找到JavaScript代码中出错的确切位置。Minecraft具有内置的JavaScript调试器，你可以通过在`设置 > 创建者`中启用内容日志GUI来启用它。

### 日志级别

- **[脚本][信息]**

  你可以使用`console.log()`或`console.info()`来显示JavaScript值，但它们仅显示在[内容日志文件](/guide/troubleshooting#content-log-file)中，你可以在[这里](/guide/troubleshooting#content-log-file)查看它们。

  `00:00:00-[脚本][信息]-`: 当使用`console.log()`或`console.info()`时触发此文本。

- **[脚本][警告]**

  这会在内容日志GUI和内容日志文件中输出警告消息。当函数被触发时，以下文本会显示。

  `00:00:00-[脚本][警告]-`: 当使用`console.warn()`时触发此文本。

- **[脚本][错误]**

  这会在内容日志GUI和内容日志文件中输出错误消息。当函数被触发时，以下文本会显示。

  `00:00:00-[脚本][错误]-`: 当使用`console.error()`时触发此文本。

### 堆栈跟踪

堆栈跟踪是导致软件程序中的断点的函数列表，按顺序排列。

这对于查找代码中问题的原因非常有用。

示例：

```
[脚本][错误]-SyntaxError: 意外字符
    在 <anonymous> (index.js:16)
    在 parse (native)
    在 r (bundle.js)
    在 <anonymous> (bundle.js)
```
- 错误名称：SyntaxError
- 错误消息：意外字符
- 错误原因所在位置：`index.js`文件的第16行


---

[原始来源](https://github.com/JaylyDev/ScriptAPI/blob/main/docs/JavaScript/Error.md)