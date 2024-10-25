# 自定义命令

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/custom-commands/](https://bridge-core.github.io/extension-docs/custom-commands/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-commands.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/custom-commands.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@608296630696fb37eb25ba52982c9c848aa2e5e4 -->
///

## 概述

bridge.允许你定义新命令，以便更轻松地编写长且复杂的函数。它们可以在`.mcfunction`文件和支持命令的JSON文件中使用。要开始使用，请导航到预设窗口中的“自定义命令”选项卡，并填写选项，包括你希望使用TypeScript还是JavaScript编写命令以及文件名。如果你在bridge.外部或在扩展中创建命令，则需要在`BP/commands`或`<扩展名称>/commands`文件夹中创建一个js或ts文件。

## 执行范围

### `defineCommand`

自定义命令可以访问`defineCommand`函数，其格式如下：

`#!ts defineCommand({ name: (name: string) => void, schema: (schema: any) => void, template: (templateFunction: (commandArgs: string[]) => string[] | string) => void }): void`

参数：

- `#!ts name(name: string): void`
  自定义命令的名称，将显示在自动补全中。

- `#!ts schema(schema: any): void`
  命令的架构。用于为自定义命令参数创建自动补全，应该按照[bridge.的命令架构](https://github.com/bridge-core/editor-packages/blob/main/packages/minecraftBedrock/language/mcfunction/schema/main.json)的`arguments`属性的形式编写，以定义命令的参数。你还可以通过`additionalData > schemaReference`属性访问bridge.的内置自动补全。它们可以在[这里](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/schema)找到，并应从`data`文件夹根目录引用，例如`#!ts additionalData: { schemaReference: '/data/packages/minecraftBedrock/schema/general/slotType.json' }`将访问槽位类型的自动补全。

  示例：

  ```js
  schema({
    arguments: [
      { type: 'string', additionalData: { values: ['1', '2', '3'] } },
      { type: 'string', additionalData: { values: ['4', '5', '6'] } },
    ],
  })
  ```

- `#!ts template(templateFunction: (componentArgs: string[]) => string[] | string): void`
  `templateFunction`接收一个字符串，表示用户在命令后输入的参数。它应返回一个命令或命令列表，表示在编译时替换自定义命令的命令。

## 扩展清单

在扩展中创建自定义命令时，你需要在扩展清单中使用[`contributeFiles`](./extension-manifest.md#contributefiles)字段指定它应安装的位置。

## 示例

```js
export default defineCommand(({ name, template, schema }) => {
  name('helloWorld')
  schema({
    arguments: [
      { type: 'string', additionalData: { values: ['1', '2', '3'] } },
    ],
  })

  template((names) => {
    return ['say Hello World!', ...names.map((name) => `say Hello ${name}`)]
  })
})
```