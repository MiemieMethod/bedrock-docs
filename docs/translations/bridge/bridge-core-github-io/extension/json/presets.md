# 预设

/// details-info | 署名信息
- 该页面翻译自[https://bridge-core.github.io/extension-docs/json/presets/](https://bridge-core.github.io/extension-docs/json/presets/)
- 该页面仓库地址为[https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/presets.md](https://github.com/bridge-core/bridge-core.github.io/blob/master/content/docs/extension-docs/json/presets.md)
- 该页面的版本为<!-- md:samp bridge-core/bridge-core.github.io@70527ef12369f094f81fe6cd210f24e5da5114ec -->
///

## 概述

预设是一组文件，可以通过预设接口创建，只需输入一个标识符并点击“创建！”按钮。它们有助于快速设置新的物品、实体或类似功能。本页涵盖API第2版中的预设。

## 扩展集成

扩展也可以通过在`<扩展名称>/presets`文件夹中提供新预设来添加。为每个要添加的预设创建一个文件夹。每个文件夹应包含一个`manifest.json`文件和所有预设应创建的文件模板。

## 清单格式

### 主体

| 名称               | 类型                                     | 描述                                         |
| ------------------ | ---------------------------------------- | -------------------------------------------- |
| `name`             | `String`                                 | 在预设窗口中显示的名称                      |
| `description`      | `String`                                 | 预设描述                                    |
| `icon`             | `String`                                 | 在预设窗口中显示的图标                      |
| `category`         | `String`                                 | 预设的类别（实体、物品等）                  |
| `packTypes`        | `Array`                                  | 预设所需的包类型                            |
| `additionalModels` | `Object`                                  | 预设脚本的高级可选功能                      |
| `targetVersion`    | `Array`                                  | 有条件地改变预设的可用性                    |
| `createFiles`      | `Array<string, string, IPresetFileOpts>` | 要创建的JSON文件或要执行的预设脚本名称     |
| `expandFiles`      | `Array<string, string, IPresetFileOpts>` | 要添加数据或扩展的文件                      |
| `fields`           | `Array`                                  | 创建新的输入框                              |

### 创建、扩展文件

清单的两个组件`createFiles`和`expandFiles`需要3个要素：

- 模板文件名
- 创建或扩展的文件路径
- 创建文件时的其他选项

模板文件名是一个字符串，包含文件名及其扩展名，如`.json`或`.lang`，将被创建或扩展。
文件路径将定义指定模板文件的创建位置。如果文件需要扩展，则路径需要定义正在扩展的文件。例如：`RP/texts/en_US.lang`。
将包含在指定模板文件中的变量也需要“注入”，以便桥接知道哪些变量需要替换为相应的值。

## 选项

```ts
interface IPresetFileOpts {
  /*
   * 注入到文件中的变量。
   */
  inject: string[]
  /*
   * 创建预设时是否打开文件。
   */
  openFile?: boolean
  /**
   * 创建文件的包类型。
   */
  packPath?: 'behaviorPack' | 'resourcePack' | 'skinPack' | 'worldTemplate'
}
```

### 字段

字段在预设窗口中创建输入框，用户可以在其中输入某种类型的数据，如图像或文本，这些数据将分配给输入框名称后指定的变量。输入类型包括：

- 文本
- 文件
- 选择框
- 数字
- 开关

#### 输入类型

输入类型是“框”，用户可以在其中输入不同类型的数据值，如`text`、`image`、`models`等。输入类型在预设的清单中每个输入框的属性中定义。要创建新的输入框，请在`fields`数组中创建一个新数组，并为框定义一个显示名称和一个变量，以便将用户的输入分配给该变量。属性可以在输入框中的`object`内定义。

###### 文本

`textInput`是默认的输入类型。要创建它，请创建一个数组，第一个元素为文本框的名称（字符串），第二个元素为分配给用户输入的变量（字符串）。

###### 文件

`fileInput`输入类型将要求用户输入一个文件。要创建该字段，将`type`属性设置为`fileInput`。将可选的`multiple`属性设置为`true`以选择多个文件。使用`accept`属性限制输入为一种文件类型。使用`icon`属性设置输入框的图标。

###### 选择框

`selectInput`是一种输入类型，创建一个选择框或下拉列表选项。要创建选择框，请创建一个输入框并分配一个变量，然后创建一个属性对象并将输入框的类型定义为`selectInput`，再设置一个`default`值，这是输入框的默认选项。创建一个名为`options`的数组，然后为每个选项创建一个对象，定义显示的`text`和`value`。

`options`还允许一个对象，包含`cacheKey`和`fileType`，其中文件类型是[文件定义](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/presetScript)的ID，缓存键是获取值的闪电缓存键。

###### 数字输入

`numberInput`是一种输入类型，创建一个滑块，该滑块从定义的`min`数字到定义的`max`数字。此滑块将以定义的`step`数字向上或向下计数。要创建它，请创建一个新的输入框，将`numberInput`作为输入`type`，然后设置`min`、`max`和`step`数字。

###### 开关

`switch`是最简单的输入类型，它是一个可以打开或关闭的开关。分配给输入的变量将根据开关状态获得`true`或`false`。要创建它，请将输入`type`设置为`switch`。

#### 输入属性

输入属性是可以在输入框中的 `object` 内定义的属性。属性根据所选的输入类型而变化。所有输入类型都有 3 个通用属性：

| 名称       | 类型      | 描述                                   |
| ---------- | --------- | -------------------------------------- |
| `type`     | `String`  | 输入类型。                             |
| `default`  | `String`  | 输入的默认值。                         |
| `optional` | `Boolean`  | 输入是否为可选。                       |

### 图标

图标在预设窗口中显示。预设使用[Material Design Icons](https://materialdesignicons.com/)，这是一个可以在`manifest.json`中通过输入`mdi-`后跟图标名称来定义的图标集合。

### 变量

变量可以在清单的`createFiles`和`expandFile`组件中使用，也可以在预设的任何其他文件中使用，只要它们被“注入”到文件中。

变量可以通过在两个大括号中使用它们来引用：`{{VARIABLE}}`。桥接会自动用当前相应的变量值替换变量。

注意：变量`PROJECT_PREFIX`已预定义，并包含项目的命名空间（不包括冒号）。

## 预设脚本

### 用法

预设脚本是JavaScript文件，可以在创建预设时处理文件创建。

它们可以通过将文件路径添加到`createFiles`数组中在预设中引用。如果你创建自己的脚本，可以将其放在预设的文件夹中，并使用相对路径引用，例如`<扩展名称>/presets/<预设名称>/myScript.js`可以用`./myScript.js`从同一预设文件夹引用。

另外，你可以使用`presetScript/<SCRIPT_NAME>`引用[内置预设脚本](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/presetScript)。

## 创建

要创建预设脚本，请在你的`presets`文件夹中创建一个JavaScript文件。内部应将`module.exports`分配为在创建预设时运行的函数。

此函数传入以下内容：

| 标识符         | 类型                                                                                               | 描述                                                                                               |
| -------------- |--------------------------------------------------------------------------------------------------| -------------------------------------------------------------------------------------------------- |
| `createFile`     | <code>(filePath: string, data: any, opts: [IPresetFileOpts](#选项)) => Promise\<void\></code>      | 在给定路径创建文件                                                                                 |
| `expandFile`     | <code>(filePath: string, data: any, opts: [IPresetFileOpts](#选项)) => Promise\<void\></code> | 在给定路径的文件中添加数据                                                                         |
| `createJSONFile` | <code>(filePath: string, data: any, opts: [IPresetFileOpts](#选项)) => Promise\<void\></code> | 在给定路径创建JSON文件。应将数据作为对象传递，以便转换为JSON字符串                             |
| `loadPresetFile` | `(filePath: string) => Promise<File>`                                                            | 从预设文件夹返回指定文件                                                                           |
| `models`         | `Object`                                                                                         | 表示用户输入的模型或在`additionalModels`中定义的对象                                               |

## 示例

### 清单

```json
{
  "name": "蝙蝠",
  "icon": "mdi-bat",
  "description": "创建一个新的蝙蝠实体。",
  "category": "fileType.entity",
  "targetVersion": [">=", "1.8.0"],
  "fields": [
    ["标识符", "IDENTIFIER"],
    ["显示名称", "IDENTIFIER_NAME"]
  ],

  "createFiles": [
    "./myPresetScript.js",
    [
      "entity.json",
      "BP/entities/{{IDENTIFIER}}.json",
      { "inject": ["IDENTIFIER", "PROJECT_PREFIX"] }
    ],
    [
      "animation.json",
      "RP/animations/{{IDENTIFIER}}.json",
      { "inject": ["IDENTIFIER"] }
    ]
  ],
  "expandFiles": [
    [
      "en_US.lang",
      "RP/texts/en_US.lang",
      { "inject": ["IDENTIFIER", "IDENTIFIER_NAME", "PROJECT_PREFIX"] }
    ]
  ]
}
```

### 变量

```json
{
  "texture_data": {
    "{{IDENTIFIER}}": {
      "textures": ["textures/items/{{IDENTIFIER}}"]
    }
  }
}
```

### 字段

```json
["文本", "TEXT"]
```

```json
[
  "文件",
  "FILE",
  {
    "type": "fileInput",
    "accept": "image/png"
  }
]
```

```json
[
  "多个文件",
  "FILES",
  {
    "type": "fileInput",
    "accept": "image/png",
    "multiple": true
  }
]
```

```json
[
  "选择框",
  "SELECT",
  {
    "type": "selectInput",
    "default": "select1",
    "options": [
      { "text": "select1", "value": "select1" },
      { "text": "select2", "value": "select2" },
      { "text": "select3", "value": "select3" }
    ]
  }
]
```

```json
[
  "实体事件选择",
  "EVENT",
  {
    "type": "selectInput",
    "options": {
      "fileType": "entity",
      "cacheKey": "event"
    }
  }
]
```

```json
[
  "数字滑块",
  "NUM_SLIDE",
  {
    "type": "numberInput",
    "min": 0,
    "max": 10,
    "step": 1
  }
]
```

```json
[
  "开关我！",
  "BOOLEAN",
  {
    "type": "switch"
  }
]
```

### 预设脚本

```js
module.exports = async ({ createFile, loadPresetFile, models, expandFile }) => {
  let { TEXTURE, IDENTIFIER, PROJECT_PREFIX, DEFAULT_TEXTURE, PRESET_PATH } =
    models
  let fileName = `${IDENTIFIER}.png`

  if (!TEXTURE) TEXTURE = await loadPresetFile(DEFAULT_TEXTURE)
  else fileName = TEXTURE.name
  const fileNameNoExtension = fileName.replace(/.png|.tga|.jpg|.jpeg/gi, '')

  await createFile(`textures/blocks/${PRESET_PATH}${fileName}`, TEXTURE, {
    packPath: 'resourcePack',
  })
  await expandFile(
    'textures/terrain_texture.json',
    {
      texture_data: {
        [`${PROJECT_PREFIX}_${IDENTIFIER}`]: {
          textures: `textures/blocks/${PRESET_PATH}${fileNameNoExtension}`,
        },
      },
    },
    { packPath: 'resourcePack' }
  )
}
```

### 更多示例

- [`bridge.原生预设`](https://github.com/bridge-core/editor-packages/tree/main/packages/minecraftBedrock/preset)
- [`更多原生实体预设`](https://github.com/bridge-core/plugins/tree/master/plugins/MoreVanillaEntityPresets)
- [`预设架构`](https://github.com/bridge-core/editor-packages/blob/main/packages/common/schema/bridge/preset/main.json)