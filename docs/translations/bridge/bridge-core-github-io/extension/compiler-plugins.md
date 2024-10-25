# 编译器插件

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/compiler-plugins/](https://bridge-core.github.io/extension-docs/compiler-plugins/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/compiler-plugins.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/compiler-plugins.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@1369b0935a07d852d4ff7c1b32661e8a607c1ab5 -->
///

bridge.的编译器架构允许任何人创建强大的插件，以几乎任何方式修改编译器输出。

## 编译器配置

编译器配置告诉编译器在编译时使用哪些插件。它应放在`<项目名称>/.bridge/compiler`目录中，并可以命名为任何名称。`dev`编译模式使用`default.json`编译器配置，而`dist`编译模式允许你从可用模式中进行选择。

默认情况下，`default.json`配置应如下所示：

```json
{
  "icon": "mdi-cogs",
  "name": "[默认脚本]",
  "description": "[将\"bridge.\"文件夹结构转换为\"com.mojang\"。\"bridge.\"在后台自动以开发模式运行，以支持快速增量构建进行测试。]",
  "plugins": [
    "typeScript",
    "entityIdentifierAlias",
    "customEntityComponents",
    "customItemComponents",
    "customBlockComponents",
    "customCommands",
    "moLang",
    [
      "simpleRewrite",
      {
        "packName": "BridgeTest"
      }
    ]
  ]
}
```

- `icon`
  指定在bridge.的UI中显示的[图标](https://materialdesignicons.com/)。

- `name`
  在bridge.的UI中显示的编译器配置名称。

- `description`
  在bridge.的UI中显示的编译器配置描述。

**注意：`name`和`description`周围有方括号，以便bridge.不会尝试翻译这些字符串。**

- `plugins`
  一个值的数组，指定要使用的编译器插件的ID。值可以是字符串，以简单地将插件添加到编译器，或者可以是一个数组，数组的第一个值是编译器插件的ID，第二个值是插件的选项对象。例如，上面的`"simpleRewrite"`插件包含一个参数`"packName"`，该参数传递给插件并在其中使用。

## 内置编译器插件

默认情况下，bridge.包含6个不同的内置编译器插件：

- `typeScript`
  将项目中的任何TypeScript文件编译为JavaScript。这使你可以在Minecraft的GameTests、脚本API和bridge.的自定义组件和命令中使用TypeScript。

- `entityIdentifierAlias`
  注册实体标识符，以便通过编译器插件中的`getAlias()`函数获取。

- `customEntityComponents`、`customItemComponents`、`customBlockComponents`
  为实体、物品和区块提供自定义组件功能。[文档](./custom-components.md)。

  **参数：**

  - `#!ts v1CompatMode: boolean` 启用v1自定义组件。仅推荐用于兼容性。

- `customCommands`
  为`.mcfunction`文件和支持命令的json文件提供自定义命令功能。[文档](./custom-commands.md)

  **参数：**

  - `#!ts v1CompatMode: boolean` 启用v1自定义命令。仅推荐用于兼容性。

- `moLang`
  提供自定义MoLang功能。这使你可以创建`.molang`文件并注册可在项目中使用的函数，适用于MoLang有效的地方。

- `simpleRewrite`
  重新结构化编译器输出，并将项目结构重写为Minecraft能够理解的结构。

  **参数：**

  - `#!ts packName: string` 包的名称。默认值：`Bridge`

  - `#!ts rewriteToComMojang: boolean` 项目是否写入com.mojang文件夹。默认值：true

  - `#!ts buildName: string` 构建的名称。默认值（取决于编译模式）：`dev`|`dist`

## 创建编译器插件

### 注册编译器插件

编译器插件应通过将其放入扩展的`<扩展名称>/compiler`文件夹中来添加。然后可以通过扩展清单注册该插件。

在扩展清单中，你需要一个[`"compiler"`](./extension-manifest.md#compiler)属性。

### 编译器插件文件结构

编译器插件应将`module.exports`设置为一个函数，该函数返回你正在使用的编译器钩子，并在其中包含逻辑。

示例：

```js
module.exports = () => {
  const blockPath = 'BP/blocks'

  return {
    transform(filePath, fileContent) {
      // 这将为每个区块文件的末尾添加"test"。
      if (filePath.startsWith(blockPath)) return `${fileContent}test`
      else return
    },
  }
}
```

此函数接收上下文参数以供插件使用。这些参数包括：

- `#!ts fileSystem: FileSystem`
  返回[FileSystem](https://github.com/bridge-core/editor/blob/main/src/components/FileSystem/FileSystem.ts)实例。

- `#!ts outputFileSystem: FileSystem`
  返回输出[FileSystem](https://github.com/bridge-core/editor/blob/main/src/components/FileSystem/FileSystem.ts)实例。

- `#!ts hasComMojangDirectory: boolean`
  允许你检查com.mojang文件夹是否已链接。

- `#!ts compileFiles: (files: string[]) => Promise<void>`
  一个允许你强制编译文件路径列表的函数。

- `#!ts getAliases: (filePath: string) => string[]`
  返回在给定文件路径的`registerAliases()`钩子中注册的所有别名。

- `#!ts targetVersion: string`
  允许你读取项目目标版本。

- `#!ts options: { mode: 'dev' | 'build', isFileRequest: boolean, restartDevServer: boolean, [key: string]: any}`

  - `#!ts mode: 'dev' | 'build'`
    允许你读取当前编译模式。

  - `#!ts isFileRequest: boolean`
    bridge.的某些核心组件手动请求编译文件。
    这些文件请求不一定需要表示你磁盘上的基础文件。
    （示例：粒子预览请求编译未保存的粒子文件）

  - `#!ts restartDevServer: boolean`
    此编译是否是开发服务器的重启。

  - `#!ts [key: string]: any`
    允许你访问在编译器配置中传递给插件的任何参数。

### 编译器钩子

```ts
  /**
   * 在构建过程开始之前运行一次
   */
  buildStart(): Promise<void> | void
  /**
   * 注册也应加载的文件
   */
  include(): Maybe<string[]>

  /**
   * 转换文件路径
   * - 例如：调整文件路径以指向构建文件夹
   * - 返回null以省略构建输出中的文件
   */
  transformPath(filePath: string | null): Maybe<string>

  /**
   * 读取`filePath`处的文件并返回其内容
   * - 返回null/undefined以仅复制文件
   */
  read(
    filePath: string,
    fileHandle?: { getFile(): Promise<File> | File }
  ): Promise<any> | any

  /**
   * 加载文件内容并将其转换为可用形式
   */
  load(filePath: string, fileContent: any): Promise<any> | any

  /**
   * 为文件提供替代查找
   * - 例如：自定义组件名称
   */
  registerAliases(source: string, fileContent: any): Maybe<string[]>

  /**
   * 注册文件依赖于其他文件
   */
  require(source: string, fileContent: any): Maybe<string[]>

  /**
   * 转换文件内容
   */
  transform(
    filePath: string,
    fileContent: any,
    dependencies?: Record<string, any>
  ): Promise<any> | any

  /**
   * 在数据写入磁盘之前准备数据
   */
  finalizeBuild(
    filePath: string,
    fileContent: any
  ): Maybe<string | Uint8Array | ArrayBuffer | Blob>

  /**
   * 在构建过程结束后运行一次
   */
  buildEnd(): Promise<void> | void
```

## 示例

- [纹理列表生成器](https://github.com/bridge-core/plugins/tree/master/plugins/textureList)

- [JSON编码器](https://github.com/bridge-core/plugins/tree/master/plugins/jsonEncoder)

- [自定义实体语法](https://github.com/bridge-core/plugins/tree/master/plugins/CustomEntitySyntax) **此插件使用[**rollup.js**](https://www.rollupjs.org/)将第三方包捆绑到插件中。**