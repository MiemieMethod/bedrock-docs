# 自定义MoLang

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/custom-molang/](https://bridge-core.github.io/extension-docs/custom-molang/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-molang.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-molang.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@6afe1b719fb8f7665ee34ee1c7e9eabbc138dc7a -->
///

自定义MoLang允许你编写可以在整个项目中使用的MoLang函数，适用于所有MoLang有效的地方。

## 创建

要开始，请打开预设窗口并选择`Molang`选项卡，输入文件名并点击“创建”。在bridge.之外，你可以在`BP/molang`目录中创建一个`.molang`文件。

在此文件中，你可以像这样定义函数：

```javascript
function('sq', 'base', {
    return math.pow(arg.base, 3);
});
```

`function()`的第一个参数应为函数名称，其他参数为函数参数，可以在函数内通过`arg.<argName>`访问。

## 使用

使用自定义MoLang函数就像在MoLang有效的地方写`#!js f.funcName('arg1', 'arg2')`一样简单。这个例子将用`arg1`和`arg2`替换`funcName`函数中的输入。