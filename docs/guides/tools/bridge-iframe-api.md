# bridge.iframe API

如果你的工具本身已经是一个网页，bridge.的iframe API会比直接重写成脚本模块更省事。它允许你把第三方网页工具嵌进bridge.标签页，再通过通信通道访问部分文件系统、Dash和项目数据。

## 什么时候用iframe API

它尤其适合下面这些情况：

- 工具本来就是一个网页应用。
- 需要复杂界面，但不想把全部逻辑改写成Vue2扩展。
- 想把贴图编辑器、表单生成器、预览器之类的独立网页接进bridge.。

要注意，iframe API调用的仍然是bridge.工具能力，不是Minecraft原生API。

## 第一步：在扩展里创建iframe标签页

在bridge.扩展脚本中，可以通过`@bridge/tab`创建`IframeTab`：

```typescript
import { IframeTab, addTab, getCurrentTabSystem } from '@bridge/tab'

const tab = new IframeTab(await getCurrentTabSystem(), {
  url: 'https://my-embedded-tool.example',
  name: 'My Embedded Tool',
  icon: 'mdi-book-outline',
  iconColor: 'behaviorPack'
})

addTab(tab)
```

其中最重要的几个字段是：

| 字段 | 用途 |
| --- | --- |
| `url` | 要嵌入的网页地址。 |
| `name` | 标签页标题。 |
| `icon` | 标签页图标。 |
| `iconColor` | 标签页图标颜色。 |

如果你的工具要“打开某个文件并接管它”，还要补上`openWithPayload`：

```typescript
const tab = new IframeTab(await getCurrentTabSystem(), {
  url: 'https://my-embedded-tool.example',
  name: 'My Embedded Tool',
  icon: 'mdi-book-outline',
  iconColor: 'behaviorPack',
  openWithPayload: {
    filePath,
    fileHandle
  }
})
```

## 第二步：在网页侧建立通信

被嵌入的网页要通过`bridge-iframe-api`建立通信通道。官方示例直接从CDN导入：

```typescript
import { Channel } from 'https://cdn.jsdelivr.net/npm/bridge-iframe-api@0.4.11/dist/bridge-iframe-api.es.js'

const api = new Channel()
await api.connect()
```

连接成功后，就可以监听事件和触发动作。

/// tip | 有些事件要先监听再连接
文档提醒，部分事件应先注册监听器再执行`connect()`，否则可能错过第一次触发。
///

## 监听事件

iframe页可以通过`api.on()`监听bridge.发来的事件：

```typescript
api.on('<event>', (data) => {
  // 处理数据
})
```

当前最关键的事件是`tab.openFile`。当底层iframe标签页被用于打开某个文件时，这个事件会触发，并给出：

- `filePath`：文件路径，可能为空。
- `fileReference`：底层文件引用。只要接口接受文件路径，一般也能使用这个引用。
- `isReadOnly`：是否只读。

如果你做的是自定义编辑器，这个事件通常就是入口。

## 触发bridge.动作

iframe页可以通过`api.trigger()`调用bridge.内部动作：

```typescript
const result = await api.trigger('<action>', payload)
```

官方当前文档里，比较实用的动作主要有这几组。

### Dash相关

`dash.updateFile`会重新编译某个文件：

```typescript
await api.trigger('dash.updateFile', filePath)
```

它适合用在网页工具改写了某个源文件之后，要求bridge.马上更新输出。

### 文件系统相关

iframe可以读取或写入文件：

- `fs.readAsDataUrl`
- `fs.readFile`
- `fs.readTextFile`
- `fs.writeFile`

例如，把字符串写回某个文件：

```typescript
await api.trigger('fs.writeFile', {
  filePath: myFilePath,
  data: myData
})
```

### 包索引相关

如果你想在当前项目里按文件类型和缓存键查数据，可以用：

- `packIndexer.find`
- `packIndexer.getFile`

例如，按标识符查客户端实体文件：

```typescript
const filePaths = await api.trigger('packIndexer.find', {
  findFileType: 'clientEntity',
  whereCacheKey: 'identifier',
  matchesOneOf: ['minecraft:player']
})
```

这类接口非常适合做“按标识符跳转”“查资源引用”“做项目内选择器”。

### 项目与标签页状态

- `project.getItemPreview`：获取某个物品标识符的预览图。
- `tab.setIsLoading`：设置iframe标签页是否处于加载状态。
- `tab.setIsUnsaved`：标记当前标签页是否有未保存更改。
- `util.platform`：获取当前平台，返回`win32`、`darwin`或`linux`。

其中`tab.setIsUnsaved`尤其重要。只要你的网页工具会让用户修改内容，就应该在内容脏了之后把它设为`true`，避免用户误关标签页。

## 权限与边界

桥接层允许iframe页接触bridge.文件和项目，但部分调用仍会触发权限提示。也就是说：

- 不是所有动作都能无提示执行。
- 工具必须在bridge.可嵌入的iframe环境中运行。
- 真正写入游戏可读文件前，仍然要经过bridge.项目或Dash流程。

因此，iframe API最适合拿来做“项目内网页工具”，而不是绕开bridge.项目系统。

## 一个适合基岩版工作的例子

假设你已经有一个网页做物品图集或动画状态可视化，那么最自然的流程通常是：

1. 在bridge.扩展里把这个网页嵌成一个`IframeTab`。
2. 用`tab.openFile`接住被打开的文件。
3. 用`fs.readTextFile`读取源数据。
4. 在网页里编辑。
5. 用`fs.writeFile`写回。
6. 调用`dash.updateFile`刷新编译结果。

这样，网页仍然负责自己的复杂界面，bridge.则负责项目上下文、文件访问和编译。