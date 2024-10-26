---
title: 引擎环境
category: 文档
mentions:
    - ConsoleTerm
    - JaylyDev
    - ThomasOrs
    - MuhammadRestu999
description: Minecraft基岩版脚本引擎环境。
---

Minecraft：基岩版使用其自有版本的JavaScript，该版本基于QuickJS。它使用ECMAScript模块（ESM）系统来组织和加载代码，这使得编写游戏脚本的方式更加模块化和有序。

## 常见问题

-   **SetTimeout支持**

在开始使用Minecraft脚本时，人们常常会遇到与时间相关的问题。您可能知道，时间代码的标准是`setTimeout`和`setInterval`函数及其取消函数。

这些标准化的方法被帧系统使用，您可以将延迟设置为毫秒精度，但Minecraft使用tick来处理世界中的变化。这就是为什么这些方法不可用且将不会可用的原因。Minecraft则使用[`system.runTimeout`](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/system#runtimeout)和[`system.runInterval`](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/system#runinterval)系统方法，这些方法在1.19.70版本中首次添加，延迟精度为一个tick。您可以在[Microsoft Docs](https://learn.microsoft.com/en-us/minecraft/creator/scriptapi/minecraft/server/system)或[Wiki教程](/scripting/script-server#scheduling)中了解更多信息。

-   **Eval权限**

并不是每个人都会遇到这个问题，因为使用eval和Function方法以字符串格式运行代码并不是很好。

一些浏览器也禁止使用这些方法，主要是eval方法，因为使用eval存在恶意代码的风险，因此默认情况下被禁用。

要启用这些评估代码的方法，您必须在清单中添加它。这项功能还增加了`Function()`构造函数的使用。

<CodeHeader>BP/manifest.json</CodeHeader>

```json
{
    "capabilities": ["script_eval"]
}
```

## 支持

-   **_支持的内容_**

    -   `Object` - 对象的标准函数构造器
    -   `Function` - 函数的标准函数构造器
    -   `Error` - (`EvalError`, `RangeError`, `ReferenceError`, `SyntaxError`, `TypeError`, `URIError`, `InternalError`, `AggregateError`) - 错误构造的类
    -   `Array` - (`Int8Array`, `UInt8Array`, `Int16Array`, `UInt16Array`, `Int32Array`, `UInt32Array`, `Float32Array`, `Float64Array`, `SharedArrayBuffer`, `ArrayBuffer`, `UInt8ClampedArray`) 数组对象的标准函数构造器
    -   `parseInt`, `parseFloat` - 将字符串解析为数字的标准方法
    -   `isNaN`, `isFinite` - 检查数字类型的标准方法
    -   `decodeURI`, `encodeURI` - 解码和编码URI路径的标准方法
    -   `decodeURIComponent`, `encodeURIComponent` - 解码和编码URI组件的标准方法
    -   `escape`, `unescape` - 非标准方法！如果可能，请使用decodeURI/encodeURI
    -   `NaN`, `Infinity`, `undefined` - 用于代码中的标准变量
    -   `__date_clock` - 获取当前时间的内置QuickJS方法
    -   `Number`, `Boolean`, `String`, `Symbol` - JS原始类型的标准函数构造器
    -   `Math` - 具有基本数学函数的标准对象，例如三角比和幂
    -   `Reflect` - 具有内置方法的标准对象
    -   `eval` - 将字符串作为代码进行评估的标准方法。请注意，必须在清单中添加此功能。
    -   `globalThis` - 访问全局作用域变量的标准对象
    -   `Date` - 日期实例的标准函数构造器
    -   `RegExp` - 正则表达式实例的标准函数构造器
    -   `JSON` - 具有JSON交互的字符串化和解析方法的标准对象
    -   `Proxy` - 内置代理处理程序的标准函数构造器
    -   `Map`, `Set`, `WeakMap`, `WeakSet` - 数据组织对象的标准函数构造器
    -   `DataView` - 二进制数组交互的标准函数构造器
    -   `Promise` - 异步交互的标准函数构造器
    -   `console` - 具有基本输出方法（`log`，`warn`，`error`，`info`）的标准对象

-   **_不支持的内容_**

    -   `setTimeout` - 用于计时代码运行的标准函数
    -   `setInterval` - 用于计时代码以间隔运行的标准函数
    -   `clearTimeout` - 取消setTimeout运行的标准函数
    -   `clearInterval` - 取消setInterval运行的标准函数

-   **扩展方法**
    我们有一堆QuickJS暴露的附加方法，但不要指望有什么改变游戏的东西！我们确实有一些附加的字符串方法，可以将字符串包装在HTML格式中。例如：`"text".bolt() -> "<b>text<b>"`。这些方法是无用的且没有文档，我们也不会提供。