# bridge.脚本模块

bridge.的脚本模块是扩展系统里最灵活的一部分。它允许你在扩展里写JavaScript，并把自定义Vue界面嵌入bridge.工作区。这样做出来的内容仍然是bridge.工具扩展，不是Minecraft原生功能。

## 先理解它在做什么

脚本模块主要解决两类事：

- 给bridge.增加新的界面，例如侧边栏页、内容标签页、输入窗口。
- 访问bridge.项目、文件系统、标签页和编译流程，做自动化或辅助工具。

文档说明这套系统基于Vue2。因此，如果你准备做复杂界面，先理解Vue单文件组件会省很多时间。

## 扩展的基础结构

开始写脚本模块之前，先准备一个合法的bridge.扩展。然后在扩展目录里创建`ui`和`scripts`两个文件夹：

/// html | div.treeview
- MyExtension
    - {/{file|manifest.json}}
    - ui
        - {/{file|Home.vue}}
    - scripts
        - {/{file|index.js}}
///

要注意两个限制：

- `ui`文件夹里只能放`.vue`文件。
- `scripts`文件夹里只能放`.js`文件。

如果扩展是在bridge.外部目录开发的，每次改完都要重新导入或执行**Tools**→**Reload Extensions**。

## 第一个侧边栏页面

最简单的入门方式，是做一个带按钮的侧边栏窗口。

### 第一步：写一个Vue组件

`ui/Home.vue`可以先写成一个最小计数器：

```vue
<template>
  <div style="padding:10px;">
    <h1>你已经点击了{/{counter}}次</h1>
    <v-btn block color="primary" @click="increment">点我</v-btn>
  </div>
</template>

<script>
export default {
  data: () => ({
    counter: 0
  }),
  methods: {
    increment() {
      this.counter += 1
    }
  }
}
</script>
```

### 第二步：在脚本里注册侧边栏按钮

`scripts/index.js`中导入`@bridge/sidebar`和`@bridge/ui`：

```javascript
import { create } from '@bridge/sidebar'
import { Home } from '@bridge/ui'

create({
  id: 'your_author.my_extension.home',
  displayName: '示例页面',
  icon: 'mdi-apple',
  component: Home
})
```

这里最容易出错的是`id`。它必须唯一，最好按“作者.扩展.功能”这样的格式写。

## 常用模块怎么分工

脚本模块很多，但做bridge.工具扩展时，最常用的大致是下面这些：

| 模块 | 适合做什么 |
| --- | --- |
| `@bridge/env` | 读取当前bridge.版本、当前项目、行为包路径、资源包路径、命名空间和目标版本。 |
| `@bridge/fs` | 读写bridge.可访问范围内的文件，创建目录，读取JSON。 |
| `@bridge/project` | 触发编译、检查包类型、监听项目切换。 |
| `@bridge/tab` | 新开标签页、打开文件、嵌入iframe页。 |
| `@bridge/sidebar` | 创建侧边栏入口。 |
| `@bridge/ui` | 导入扩展里`ui/`文件夹中的Vue组件。 |
| `@bridge/windows` | 弹出信息窗、输入窗、下拉窗和确认窗。 |

## 项目与路径信息：`@bridge/env`

`@bridge/env`最适合拿“当前上下文”：

```javascript
import { getCurrentBP, getCurrentRP, getCurrentProject, getProjectTargetVersion } from '@bridge/env'
```

常见用途包括：

- 用`getCurrentBP()`和`getCurrentRP()`拼接行为包、资源包路径。
- 用`getCurrentProject()`判断用户当前打开的是哪个项目。
- 用`getProjectTargetVersion()`或`getProjectPrefix()`决定界面里显示哪些选项。
- 用`resolvePackPath()`在项目配置改过包路径时仍然得到正确的真实路径。

如果扩展需要同时兼容不同版本项目，优先用这些函数，不要手写固定的`BP/`或`RP/`拼接逻辑。

## 读写文件：`@bridge/fs`

`@bridge/fs`提供的是bridge.可访问范围内的文件操作，不等于任意系统路径都能直接乱写。

最常用的函数通常是：

- `readFile(path)`：读取文件。
- `readJSON(path)`：按JSON5规则解析JSON文件。
- `mkdir(path)`：递归创建目录。
- `writeFile(path, data)`：直接按路径写文件。
- `readdir(path)`和`readFilesFromDir(path)`：遍历目录。

例如，读取当前资源包中的`manifest.json`：

```javascript
import { getCurrentRP } from '@bridge/env'
import { readJSON } from '@bridge/fs'

const rpPath = getCurrentRP()
const manifest = await readJSON(`${rpPath}/manifest.json`)
```

## 调用编译与监听项目：`@bridge/project`

`@bridge/project`适合把扩展接进bridge.项目工作流：

- `hasPacks()`：检查当前项目是否存在指定包类型。
- `compile(configFile)`：按某个编译配置强制执行Dash编译。
- `compileFiles(paths)`：只重编译一部分文件。
- `onProjectChanged(cb)`：用户切换项目时执行回调。

如果你的扩展会生成JSON、函数或其他需要立即进入输出目录的文件，这个模块会非常关键。

## 标签页与内容页：`@bridge/tab`

如果侧边栏不够用，可以改做真正的标签页。`@bridge/tab`里最重要的能力包括：

- `addTab(tab)`：把一个标签页对象加入当前标签系统。
- `openFilePath(filePath, selectTab)`：按项目内相对路径打开已有文件。
- `getCurrentTabSystem()`：拿到当前标签系统实例。

文档还保留了`openTab()`，但已经标记为弃用，优先使用`addTab()`。

## 界面导入：`@bridge/ui`

这个模块的作用很单纯：把`ui/`文件夹中的Vue组件变成可以在脚本里导入的对象。

```javascript
import { Main } from '@bridge/ui'
import { Nested: { Main: NestedMain } } from '@bridge/ui'
```

也就是说，`ui/Main.vue`会对应成`Main`，嵌套目录也能按对象结构导入。

## 弹窗：`@bridge/windows`

如果你只需要一个短流程输入，不必单独做完整页面。`@bridge/windows`已经提供了几种成品窗口：

- `createInformationWindow()`：显示说明。
- `createInputWindow()`：让用户输入文本。
- `createDropdownWindow()`：让用户在若干选项中二选一或多选一。
- `createConfirmWindow()`：做确认/取消流程。

它们很适合做导出前确认、命名输入、模式选择这类小交互。

## 什么时候改用iframe

如果你的工具本身已经是一个网页应用，或界面复杂到不想直接写在bridge.扩展里，就不要强行全用脚本模块。此时通常应改用iframe标签页，把已有网页嵌进bridge.，再通过通信层访问文件和项目数据。下一页就是[bridge.iframe API](bridge-iframe-api.md)。

## 实际建议

第一次写bridge.扩展时，不要一上来就做“自动生成完整附加包”。先做一个能：

1. 读取当前项目。
2. 让用户点一个按钮。
3. 生成或修改一个文件。
4. 触发一次编译。

这样的小工具最容易验证路径、权限、编译和界面是否都接对了。等这一步稳定了，再继续叠加更多模块。