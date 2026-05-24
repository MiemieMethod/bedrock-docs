# 脚本错误排查<!-- md:flag vanilla -->

在开发脚本API时，错误消息和调试手段是排查问题的核心工具。本页面汇总了常见JavaScript错误类型及其在脚本API中的具体含义，并介绍如何读取调用栈。

## 启用内容日志

在正式排查前，请确保内容日志已开启，否则大多数脚本错误不会显示在屏幕上。进入设置 → 创作者 → 启用**内容日志GUI**和**内容日志文件**。错误将以红色显示在屏幕左下角。

## 常见JavaScript错误类型

/// define
`EvalError`

- `eval()`函数相关错误。脚本API的运行环境默认禁用`eval()`，如需动态执行代码应使用`Function()`构造函数，但同样不建议使用。

`RangeError`

- 数值超出允许范围，或数组/字符串操作参数越界。常见情况：
    - `new Array(-1)` — 创建负长度数组
    - `string.repeat(-1)` — 重复次数为负
    - 向`setInterval`传入负数延迟

`ReferenceError`

- 访问了未声明的变量或不存在的标识符。常见情况：
    - 拼写了不存在的变量名
    - 在变量声明前访问（暂时性死区）
    - **`ReferenceError: Native function [X::Y] does not have required privileges`** — 这是脚本API独有的错误，代表当前执行上下文处于受限执行模式，调用的API不被允许。请参阅[脚本执行权限](./privileges.md)。

`SyntaxError`

- JavaScript语法错误，通常在脚本加载阶段就会抛出，导致整个模块无法运行。常见情况：
    - 括号不匹配
    - 非法的变量名
    - `import`语句位置错误（必须在模块顶层）

`TypeError`

- 对不合适类型的值进行了操作。常见情况：
    - 调用了`undefined`或`null`上的属性/方法（最常见）
    - 向函数传递了错误类型的参数
    - 对常量重新赋值（`const`赋值错误在某些环境下抛出`TypeError`）
    - **`TypeError: Cannot read properties of undefined (reading 'X')`** — 表示你尝试访问`undefined.X`，通常是链式调用中某一步返回了`undefined`

`URIError`

- `decodeURIComponent()`等URI函数处理格式错误的URI时抛出。在脚本API中较少见。

`InternalError`（非标准）

- JavaScript引擎内部错误，通常是递归过深（堆栈溢出）。检查代码中是否有无限递归。

///

## 脚本API特有错误

### 权限不足

```
ReferenceError: Native function [World::sendMessage] does not have required privileges.
```

原因：在前置事件的回调（受限执行模式）或世界未加载时（早期执行模式）调用了不被允许的API。
解决：参阅[脚本执行权限](./privileges.md)。

### 实体已失效

```
TypeError: This native object (of type 'EntityImpl') is no longer valid.
TypeError: The object 'Entity' is no longer valid.
```

原因：持有的实体引用在实体从世界中移除后仍被使用。
解决：在执行实体操作前用`entity.isValid()`检查有效性：

```javascript
if (entity.isValid()) {
    entity.sendMessage("你还在线！");
}
```

### 模块版本不匹配

脚本文件导入的模块版本与`manifest.json`中声明的版本不一致时，模块加载会静默失败或产生运行时错误。请确保脚本的`import`语句和`manifest.json`中的`dependencies`使用相同的版本字符串。

## 读取调用栈

内容日志中的错误会附带调用栈：

```
[Scripting][error] Error: 这是一个错误
  at myFunction (BP/scripts/Main.js:10:5)
  at world.afterEvents.playerSpawn.subscribe (BP/scripts/Main.js:20:9)
```

每一行格式为`at 函数名 (文件路径:行号:列号)`，从上到下代表函数调用链（最近的在最上面）。找到自己编写的文件路径对应的行，即可定位出错位置。

/// tip | 使用console.error输出带调用栈的错误
在`catch`块中，将`error.stack`一起输出，可以看到完整的调用链：

```javascript
try {
    // ...
} catch (error) {
    console.error(error, error.stack);
}
```
///

## 常用调试技巧

- 使用`console.log(JSON.stringify(obj))`输出复杂对象（脚本API的`console.log`不支持深层对象打印）。
- 用`typeof`检查变量类型，排查意外的`undefined`。
- 在事件订阅前加日志确认事件是否触发。
- 如果脚本完全不执行，检查`manifest.json`中的脚本入口文件路径是否正确。