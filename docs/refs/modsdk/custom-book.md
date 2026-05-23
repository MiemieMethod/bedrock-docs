# 自定义书本格式与接口<!-- md:flag china -->

本页整理中国版模组SDK自定义书本的文件格式、预置页面、脚本扩展对象和常用接口。该系统属于中国版Python模组SDK和中国版UI体系，不属于国际版附加包、国际版JSON UI或`@minecraft/server`脚本API。

/// warning | 中国版专用接口
本页中的`behavior_pack/customBooks`、`clientApi.GetBookManager()`、`BookManager`、`BasePage`和`BaseComp`均为中国版模组SDK概念。国际版脚本API没有这些对象。
///

## 文件结构

一本书本对应`behavior_pack/customBooks`下的一个文件夹。文件夹名是书本标识符。

/// html | div.treeview
- `behavior_pack`
    - `customBooks`
        - `bookName`
            - `book.json`
            - `category`
                - `categoryName.json`
            - `entry`
                - `entryName.json`
///

| 路径 | 固定性 | 说明 |
| --- | --- | --- |
| `customBooks` | 固定 | 保存全部自定义书本。 |
| `bookName` | 自定义 | 单本书本目录；目录名即书本标识符。 |
| `book.json` | 固定 | 书本首页与默认配置。 |
| `category` | 固定 | 保存目录文件。 |
| `entry` | 固定 | 保存章节文件。 |

## `book.json`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | `string` | 无 | 打开书本界面的物品标识符。 |
| `title1` | `string` | `""` | 书本首页主标题。 |
| `title2` | `string` | `""` | 书本首页副标题。 |
| `content` | `string` | `""` | 书本首页正文。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 首页正文文字大小，系统默认值为10。 |
| `titleArea` | `object` | 子字段默认值 | 主标题与副标题的排版配置。 |
| `pageConfig` | `object` | 无 | 页面配置默认值。 |
| `categoryConfig` | `object` | 无 | 目录配置默认值。 |
| `entryConfig` | `object` | 无 | 章节配置默认值。 |

`titleArea`字段：

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `offset` | `array(float)` | `[-10,0]` | 标题整体偏移。 |
| `textSize1` | `int` | `9` | 主标题文字大小。 |
| `textSize2` | `int` | `8` | 副标题文字大小。 |
| `padding` | `int` | `1` | 两个标题之间的垂直间隔。 |

## 目录文件

目录文件位于`category`文件夹。文件名去除`.json`后即目录标识符。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | `string` | 无 | 目录首页标题。 |
| `content` | `string` | `""` | 目录首页正文。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 目录首页正文文字大小，系统默认值为10。 |
| `icon` | `string` | `BookConfig.Images.categoryDefaultIcon` | 目录图标路径。 |
| `isLocked` | `bool` | `false` | 是否锁定目录。 |
| `lockIcon` | `string` | `BookConfig.Images.lockBtn_dark` | 锁定状态下显示的图标路径。 |
| `lockMsg` | `string` | `""` | 锁定状态下点击目录时显示的提示。为空时显示目录标题。 |
| `parent` | `string` | 书本 | 父目录标识符。不写时为一级目录。 |
| `sortnum` | `int` | 无 | 排列优先级，数值越小越靠前。 |

目录可以嵌套。一个目录下的子页组应保持同类；不应让同一目录同时作为子目录和章节的父级。

## 章节文件

章节文件位于`entry`文件夹。文件名去除`.json`后即章节标识符。

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `title` | `string` | 无 | 章节标题。 |
| `icon` | `string` | `BookConfig.Images.categoryDefaultIcon` | 章节图标路径。 |
| `isLocked` | `bool` | `false` | 是否锁定章节。 |
| `lockIcon` | `string` | `BookConfig.Images.lockBtn_dark` | 锁定状态下显示的图标路径。 |
| `lockMsg` | `string` | `""` | 锁定状态下点击章节时显示的提示。为空时显示章节标题。 |
| `parent` | `string` | 无 | 所属目录标识符。必须填写。 |
| `pages` | `array(object)` | 无 | 章节下的页面数组。 |
| `sortnum` | `int` | 无 | 排列优先级，数值越小越靠前。 |

## 页面通用字段

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `type` | `string` | 无 | 页面类型。可为预置类型或脚本注册的自定义页面类型。 |
| `subtitle` | `string` | 无 | 页面副标题。不写时页面内容通常直接置顶；章节首页通常使用章节标题。 |
| `title` | `string`或`object` | 无 | `TitlePage`可使用的标题数据。对象形式可含`icon`和`text`。 |

书本界面使用以左上角为原点的UI坐标系，默认界面大小为`(268,200)`像素。脚本中部分提示或按钮位置使用全局坐标系，即屏幕坐标系。

## 预置页面类型

### `textPage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `content` | `string` | `""` | 文本内容，支持格式化文本。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 文本字体大小。 |

### `imagePage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `image` | `string` | 无 | 图片路径，例如`textures/ui/myCustomBook/testImage_1`。 |
| `imageSize` | `array(float)` | `[80.0,80.0]` | 图片显示大小。 |
| `info` | `string` | 无 | 图片备注文本。 |
| `content` | `string` | `""` | 正文文本。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 正文文字大小。 |

### `highlightPage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `itemData` | `array(object)` | 无 | 轮播物品数据。 |
| `itemSize` | `array(float)` | `[30.0,30.0]` | 物品显示大小。 |
| `info` | `string` | 无 | 备注文本。 |
| `content` | `string` | `""` | 正文文本。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 正文文字大小。 |

`itemData`元素：

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `item` | `string` | 无 | 物品标识符。 |
| `data` | `int` | `0` | 物品附加值。 |

### `tableRecipePage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `recipeId` | `string` | 无 | 合成配方ID，通常为输出物品标识符。仍需要配置。 |
| `recipeShapeId` | `string` | 无 | 配方JSON的`identifier`字段。与`recipeId`同时存在时优先使用。 |
| `tag` | `string` | `crafting_table` | 配方标签。支持工作台、自定义工作台、制图台和切石机配方。 |
| `recipeSize` | `array(float)` | `[90.0,48.0]` | 合成表显示大小。 |
| `aux` | `int` | `0` | 合成物品附加值。 |
| `info` | `string` | 无 | 备注文本。 |
| `content` | `string` | `""` | 正文文本。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 正文文字大小。 |

### `entityPage`

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `entity` | `object` | 无 | 实体展示数据。 |
| `entitySize` | `array(float)` | `[100.0,100.0]` | 实体显示大小。 |
| `info` | `string` | 无 | 备注文本。 |
| `content` | `string` | `""` | 正文文本。 |
| `contentTextSize` | `int` | `BookConfig.TextSize.content` | 正文文字大小。 |

`entity`字段：

| 字段 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| `name` | `string` | 无 | 实体标识符。 |
| `offset` | `array(float)` | 无 | 实体相对于外框的偏移。无偏移时填写`[0,0]`。 |
| `molang_dict` | `dict` | `{}` | Molang表达式字典。 |

## `BookConfig`

`BookConfig`是书本系统默认值的静态配置对象。官方资料要求不要在程序运行期间修改该对象属性。

获取方式：

```python
import mod.client.extraClientApi as clientApi

bookManager = clientApi.GetBookManager()
bcf = bookManager.GetBookConfig()
```

| 属性 | 说明 | 常见成员 |
| --- | --- | --- |
| `TextSize` | 字体大小。 | `infotext=6`、`footprint=8`、`content=10`、`smallTitle=12`、`middleTitle=14`、`title=16` |
| `Colors` | 颜色。 | `TextDefault`、`BookTitle`、`SubTitle` |
| `TextAlign` | 文本对齐方式。 | `Left`、`Center`、`Right`、`Fit_Left`、`Fit_Center`、`Fit_Right` |
| `ImageReszieRule` | 图片缩放方式。 | `Ninesliced`、`Fit` |
| `Images` | 预设图片路径。 | `blank`、`categoryDefaultIcon`、`lockBtn_dark`、`sqrtPanel_light`、`progressBar_light`、`progressBar_dark` |

/// note | 官方字段拼写
官方资料中的图片缩放枚举名写作`ImageReszieRule`。编写脚本时应以实际接口名称为准，不要按英文习惯自行改为`ImageResizeRule`。
///

## `BookManager`

`BookManager`管理全部书本对象、浏览历史、跳转地址、消息显示和页面注册。通过客户端API获取：

```python
import mod.client.extraClientApi as clientApi

bookManager = clientApi.GetBookManager()
```

| 接口 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `GetBookConfig()` | 无 | `BookConfig` | 获取书本配置常量。 |
| `GetBookInstance(bookName)` | `bookName:str` | `NormalBook`或`None` | 根据书本名称获取书本管理对象。 |
| `GetOpeningBookInstance()` | 无 | `NormalBook`或`None` | 获取当前打开的书本管理对象。 |
| `ShowMsg(position,msg)` | `position:tuple(int,int)`、`msg:str` | 无 | 在全局坐标显示提示文本，默认约2秒后隐藏。 |
| `HideMsg()` | 无 | 无 | 隐藏全局提示文本。 |
| `AddPageType(pageName,pageCls)` | `pageName:str`、`pageCls:classobj` | 无 | 注册自定义页面类型。只能在客户端系统初始化时调用。 |
| `UpdateScreen()` | 无 | 无 | 刷新书本界面。 |
| `To(addr)` | `addr:str` | `PageGroup` | 按地址跳转到书本页面。 |
| `GetBaseCompCls()` | 无 | `type(BaseComp)` | 获取组件基类。 |
| `GetButtonCompCls()` | 无 | `type(ButtonComp)` | 获取按钮组件类。 |
| `GetEntityCompCls()` | 无 | `type(EntityComp)` | 获取实体展示组件类。 |
| `GetHighlightCompCls()` | 无 | `type(HighlightComp)` | 获取轮播物品组件类。 |
| `GetImageCompCls()` | 无 | `type(ImageComp)` | 获取图片组件类。 |
| `GetTextCompCls()` | 无 | `type(TextComp)` | 获取文本组件类。 |
| `GetProgressBarCompCls()` | 无 | `type(ProgressBarComp)` | 获取进度条组件类。 |
| `GetBasePageCls()` | 无 | `type(BasePage)` | 获取页面基类。 |
| `GetTitlePageCls()` | 无 | `type(TitlePage)` | 获取带标题处理的页面类。 |

`AddPageType`的页面名称建议采用`模组名:页面名称`格式，避免与系统预置页面或其他模组页面重名。

## 页面地址

书本页面跳转地址分为绝对路径和相对路径。

| 类型 | 格式 | 说明 |
| --- | --- | --- |
| 绝对路径 | `/书本/目录/章节/页号` | 以`/`开头，从书本根级解析。 |
| 相对路径 | `页号`或`子页组/页号` | 不以`/`开头，从当前页组解析。 |

页号从0开始。如果路径中不写页号，默认跳转到目标页组的第0页。系统支持同章节、跨章节、同目录和跨目录跳转；不支持从当前书本跳转到另一本书。

## `NormalBook`

`NormalBook`表示已经成功创建的书本管理对象。

| 接口 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `GetOriginJsonData()` | 无 | `dict` | 获取从书本JSON文件读取的原始数据。 |
| `GetCurrentJsonData()` | 无 | `dict` | 获取经过书本系统预处理后的当前数据。 |
| `GetBook()` | 无 | `Book` | 获取书本首页所在的页组对象。 |
| `GetCategory(identifier)` | `identifier:str` | `Category` | 根据目录标识符获取目录对象。 |
| `GetEntry(identifier)` | `identifier:str` | `Entry` | 根据章节标识符获取章节对象。 |
| `LockCategory(identifier)` | `identifier:str` | 无 | 锁定目录。 |
| `UnlockCategory(identifier)` | `identifier:str` | 无 | 解锁目录。 |
| `LockEntry(identifier)` | `identifier:str` | 无 | 锁定章节。 |
| `UnlockEntry(identifier)` | `identifier:str` | 无 | 解锁章节。 |

## 页组对象

`Book`、`Category`和`Entry`均继承`PageGroup`。`PageGroup`管理一组页面，并提供公共接口。

| 接口 | 对象 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| `GetAddr()` | `PageGroup` | 无 | `str` | 获取该页组的绝对路径。 |
| `GetPages()` | `PageGroup` | 无 | `list(BasePage)` | 获取该页组的全部页面对象。 |
| `GetPagesCount()` | `PageGroup` | 无 | `int` | 获取该页组的页面数量。 |
| `GetSons()` | `Book` | 无 | `list(Category)` | 获取书本的一级目录。 |
| `GetProgressValue()` | `Book`、`Category` | 无 | `float` | 获取子页组解锁进度，范围为0至1。 |
| `GetSons()` | `Category` | 无 | `PageGroup`列表 | 获取子目录或章节。 |
| `GetParent()` | `Category` | 无 | `PageGroup` | 获取父页组。 |
| `isLocked()` | `Category`、`Entry` | 无 | `bool` | `True`表示未解锁，`False`表示已解锁。 |
| `Lock()` | `Category`、`Entry` | 无 | 无 | 锁定该目录或章节。 |
| `Unlock()` | `Category`、`Entry` | 无 | 无 | 解锁该目录或章节。 |
| `GetParent()` | `Entry` | 无 | `Category` | 获取所属目录。 |

## `BasePage`

所有自定义页面都继承`BasePage`。页面负责保存数据、显示自身，并排版页内组件。

### 重写方法

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__(size=None,position=None)` | `size:tuple(int,int)`、`position:tuple(int,int)` | `BasePage` | 初始化页面。自定义页面必须重写，并调用父类方法。 |
| `Show()` | 无 | `BasePage` | 显示页面。自定义页面通常需要重写并调用父类方法。 |
| `Hide()` | 无 | `BasePage` | 隐藏页面。可按需重写；重写时应主动调用父类方法。 |

### 排版与工具方法

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `GetPosition()` | 无 | `tuple(int,int)` | 获取页面在书本坐标系中的位置。 |
| `GetSize()` | 无 | `tuple(int,int)` | 获取页面大小。 |
| `Center()` | 无 | `tuple(int,int)` | 获取页面中心坐标。 |
| `Left()`、`Right()` | 无 | `int` | 获取页面左右边界的X值。 |
| `Top()`、`Bottom()` | 无 | `int` | 获取页面上下边界的Y值。 |
| `ResetCompsPosition()` | 无 | `BasePage` | 将所有组件位置重置为页面当前位置。 |
| `GetPageGroup()` | 无 | `PageGroup`或`None` | 获取页面所在页组。 |
| `AddComps(*comps)` | `BaseComp`可变参数 | `BasePage` | 向页面添加组件。 |
| `Call(callbackDict)` | `callbackDict:dict` | `object` | 调用回调函数。 |

`callbackDict`通常包含`func`和可选的`args`。

## `TitlePage`

`TitlePage`继承`BasePage`，提供标题处理。它会根据当前页面是否为章节首页，以及页面数据中的`title`或`subtitle`字段决定显示标题。

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `SetTitleData()` | 无 | `TitlePage` | 向标题组件注入数据。 |
| `LayoutTitle()` | 无 | `int` | 排版标题并返回标题下边界Y值。 |

`title`可以写作字符串，也可以写作对象：

```json
{
    "title": {
        "icon": "textures/items/apple",
        "text": "带图标的标题"
    }
}
```

## `BaseComp`

所有书本组件均继承`BaseComp`。组件把数据和UI控件对象封装在一起，负责把页面传入的数据渲染到UI控件节点。

### 重写方法

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__(compName,jsonFile,compNodeName,recycled=False)` | `compName:str`、`jsonFile:str`、`compNodeName:str`、`recycled:bool` | `BaseComp` | 初始化组件。自定义组件必须重写并调用父类方法。 |
| `Show()` | 无 | `BaseComp` | 显示组件。重写时应调用父类方法。 |
| `Hide()` | 无 | `BaseComp` | 隐藏组件。可按需重写；重写时应调用父类方法。 |
| `Reset()` | 无 | `BaseComp` | 组件回收时重置UI控件节点属性。可回收组件建议重写。 |

开启组件回收后，隐藏组件时拷贝出的UI控件节点不会立即删除，而会进入空闲队列供后续同名组件复用。因此，`Show`中修改过的位置、大小、文本、颜色或层级需要被重置。

### 排版方法

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `GetPosition()` | 无 | `tuple(int,int)` | 获取组件位置。 |
| `SetPosition(newPosition)` | `newPosition:tuple(int,int)` | `BaseComp` | 设置组件位置。 |
| `GetSize()` | 无 | `tuple(int,int)` | 获取组件大小。 |
| `SetSize(newSize)` | `newSize:tuple(int,int)` | `BaseComp` | 设置组件大小。 |
| `Center()` | 无 | `tuple(int,int)` | 获取组件中心坐标。 |
| `Left()`、`Right()` | 无 | `int` | 获取左右边界X值。 |
| `Top()`、`Bottom()` | 无 | `int` | 获取上下边界Y值。 |
| `MoveToX(x)`、`MoveToY(y)` | `int` | `BaseComp` | 单独设置位置坐标中的X或Y。 |
| `MoveX(x)`、`MoveY(y)` | `int` | `BaseComp` | 沿指定轴移动。 |
| `AlignCenterToX(x)`、`AlignCenterToY(y)` | `int` | `BaseComp` | 将组件中心对齐到指定坐标。 |
| `AlignCenterToPosition(position)` | `position:tuple(int,int)` | `BaseComp` | 将组件中心对齐到指定位置。 |
| `AlignLeftToX(x)`、`AlignRightToX(x)` | `int` | `BaseComp` | 将左右边界对齐到指定X值。 |
| `AlignTopToY(y)`、`AlignBottomToY(y)` | `int` | `BaseComp` | 将上下边界对齐到指定Y值。 |

调用对齐或移动方法前，通常应先调用`SetSize`，否则排版可能不符合预期。

### UI控件节点方法

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `GetRootUINode()` | 无 | `BaseUIControl` | 获取组件封装的UI控件根节点。仅组件可见时可用。 |
| `HasRootUINode()` | 无 | `bool` | 判断组件是否拥有UI控件根节点。 |
| `SetNodeOffset(node,offset)` | `node:BaseUIControl`、`offset:tuple(int,int)` | `BaseComp` | 偏移节点，并在隐藏时复原，适合解决回收复用问题。 |
| `SetNodeSize(node,newSize)` | `node:BaseUIControl`、`newSize:tuple(int,int)` | `BaseComp` | 设置节点大小，并处理回收复用。 |
| `SetNodeText(node,text)` | `node:BaseUIControl`、`text:str` | `BaseComp` | 设置文本控件文本并刷新界面。 |
| `SetNodeTextFontSize(node,originFontSize,newFontSize)` | `node:BaseUIControl`、`originFontSize:int`、`newFontSize:int` | `BaseComp` | 设置文本控件字号。 |
| `GetNodeCenterGlobal(node)` | `node:BaseUIControl` | `tuple(int,int)` | 获取指定UI控件节点中心的全局坐标。 |
| `SetLayer(layer)` | `layer:int` | `BaseComp` | 设置组件根节点UI层级。 |
| `Call(callbackDict)` | `callbackDict:dict` | `object` | 调用回调函数。 |
| `GetPage()` | 无 | `BasePage`或`None` | 获取组件当前所在页面。 |

## 预置组件

### `TextComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__(textAlign=BookConfig.TextAlign.Left)` | `textAlign:int` | `TextComp` | 初始化文本组件。 |
| `SetDataBeforeShow(text,textSize=BookConfig.TextSize.content)` | `text:str`、`textSize:int` | `TextComp` | 设置显示前数据。 |
| `SetAlpha(alpha)` | `alpha:float` | `TextComp` | 设置文本透明度。组件显示后可用。 |
| `SetColor(color)` | `color:tuple(float,float,float,float)` | `TextComp` | 设置文本颜色。组件显示后可用。 |

`Fit_`前缀的文本对齐方式会使UI控件根节点自适应文本内容，此时`SetSize`无效。

### `ImageComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__(imageResizeRule=BookConfig.ImageReszieRule.Ninesliced)` | `imageResizeRule:int` | `ImageComp` | 初始化图片组件。 |
| `SetDataBeforeShow(image)` | `image:str` | `ImageComp` | 设置图片路径。 |
| `SetAlpha(alpha)` | `alpha:float` | `ImageComp` | 设置图片透明度。 |

`Ninesliced`会改变图片长宽比以适应给定大小；`Fit`会保持图片长宽比。

### `HighlightComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__()` | 无 | `HighlightComp` | 初始化轮播物品组件。 |
| `SetDataBeforeShow(itemData)` | `itemData:list(dict)` | `HighlightComp` | 设置轮播物品数据。 |

`itemData`元素包含`item`和可选的`data`。

### `TableRecipeComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__()` | 无 | `TableRecipeComp` | 初始化工作台合成表组件。 |
| `SetDataBeforeShow(recipeId,aux=0)` | `recipeId:str`、`aux:int` | `TableRecipeComp` | 设置合成表数据。 |

### `EntityComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__()` | 无 | `EntityComp` | 初始化实体展示组件。 |
| `SetDataBeforeShow(entityName,molang_dict={},entityOffset=(0,0),backgroundImage=BookConfig.Images.sqrtPanel_light)` | `entityName:str`、`molang_dict:dict`、`entityOffset:tuple(int,int)`、`backgroundImage:str` | `EntityComp` | 设置展示实体数据。 |

### `ProgressBarComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__()` | 无 | `ProgressBarComp` | 初始化进度条组件。 |
| `SetDataBeforeShow(value=1,emptyImage=BookConfig.Images.progressBar_dark,fillImage=BookConfig.Images.progressBar_light)` | `value:float`、`emptyImage:str`、`fillImage:str` | `ProgressBarComp` | 设置进度条数据。`value`范围为0至1。 |

### `ButtonComp`

| 方法 | 参数 | 返回值 | 说明 |
| --- | --- | --- | --- |
| `__init__()` | 无 | `ButtonComp` | 初始化按钮组件。 |
| `SetDataBeforeShow(defaultImage=BookConfig.Images.blank,pressCallBack=None,moveInCallBack=None,text="",pressImage=None,hoverImage=None)` | 多参数 | `ButtonComp` | 设置按钮图片、回调和文本。 |
| `SetAlpha(alpha)` | `alpha:float` | `ButtonComp` | 设置按钮图片透明度。 |
| `SetTextColor(color)` | `color:tuple(float,float,float,float)` | `ButtonComp` | 设置按钮文字颜色。 |
| `SetTextSize(newSize)` | `newSize:int` | `ButtonComp` | 设置按钮文字大小。 |
| `SetTextAlpha(alpha)` | `alpha:float` | `ButtonComp` | 设置按钮文字透明度。 |

`pressCallBack`和`moveInCallBack`均为字典，通常包含`func`和可选的`args`。

