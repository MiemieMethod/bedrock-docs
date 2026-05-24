# 制作自定义书本<!-- md:flag china -->

自定义书本是中国版模组SDK提供的界面化内容系统。它把一个物品与一套书本界面绑定，使玩家可以像翻阅书一样阅读模组说明、玩法图鉴、合成提示、实体展示或任务说明。该功能依赖中国版行为包目录、资源包资源和Python脚本扩展，不属于国际版附加包或`@minecraft/server`脚本API。

/// warning | 不要与国际版书与笔混用
本页所说的自定义书本不是原版物品“书与笔”，也不是国际版脚本API中的对象。它使用`behavior_pack/customBooks`、`clientApi.GetBookManager()`和中国版UI控件体系，只能在支持中国版模组SDK的环境中使用。
///

## 准备书本物品

一本自定义书本首先是一种物品。中国版官方资料要求先在行为包和资源包的`netease_items_res`目录下定义一个自定义物品，再把这个物品写入书本配置的`item`字段。物品本身的定义属于自定义物品系统；本页只说明书本系统如何引用它。

```json title="book.json"
{
    "item": "custombooks:test0",
    "title1": "自定义书本的一级标题",
    "title2": "自定义书本的二级标题",
    "content": "第一页为书本首页，第二页为书本目录显示页。",
    "pageConfig": {
        "subtitle": "默认的副标题"
    }
}
```

`item`的值必须指向可用的物品标识符。玩家使用该物品时，系统会打开与该书本对应的界面。

## 建立目录结构

每一本书对应`behavior_pack/customBooks`下的一个文件夹。文件夹名就是书本名称，也会成为脚本接口中的书本标识。

/// html | div.treeview
- `behavior_pack`
    - `customBooks`
        - `customBook`
            - `book.json`
            - `category`
                - `pages.json`
            - `entry`
                - `imageEntry.json`
///

`book.json`描述书本首页和全局默认配置；`category`保存目录文件；`entry`保存章节文件。目录和章节都通过文件名取得标识符，例如`pages.json`的目录标识符为`pages`，`imageEntry.json`的章节标识符为`imageEntry`。

## 编写书本首页

`book.json`的首页内容由标题、正文和可选的默认配置组成。

| 字段 | 作用 |
| --- | --- |
| `item` | 打开书本的物品标识符。 |
| `title1` | 书本首页主标题。 |
| `title2` | 书本首页副标题。 |
| `content` | 书本首页正文。正文区域高度有限，过长文本不会完整显示。 |
| `titleArea` | 主标题与副标题的排版配置。可设置`offset`、`textSize1`、`textSize2`和`padding`。 |
| `contentTextSize` | 首页正文的字体大小。 |
| `pageConfig` | 页面字段的配置默认值。 |
| `categoryConfig` | 目录字段的配置默认值。 |
| `entryConfig` | 章节字段的配置默认值。 |

默认值分为系统默认值和配置默认值。若在`book.json`中写入`pageConfig`、`categoryConfig`或`entryConfig`，后续页面、目录或章节缺省相应字段时会优先使用这些配置默认值；若没有配置默认值，才会使用系统默认值。

/// tip | 只给可默认的字段设置默认值
官方资料提示，不应在配置默认值中写入本身没有默认值的字段，否则可能产生意外结果。适合放入默认配置的字段通常是字体大小、图标路径或锁图标等显示选项。
///

## 编写目录

目录文件放在`category`文件夹中。一个目录表示书本中的一组主题入口，可以位于书本首页下，也可以位于其他目录下。

```json title="category/pages.json"
{
    "title": "页面类型",
    "content": "该目录下的每个章节分别展示一种页面类型",
    "isLocked": false
}
```

常用字段如下：

| 字段 | 作用 |
| --- | --- |
| `title` | 目录首页标题。 |
| `content` | 目录首页正文。 |
| `contentTextSize` | 目录首页正文的字体大小。 |
| `icon` | 目录在上级页面和目录首页中显示的图标路径，例如`textures/items/apple`。 |
| `isLocked` | 是否锁定目录。锁定后玩家不能查看目录下的内容。 |
| `lockIcon` | 锁定状态下显示的锁图标路径。 |
| `lockMsg` | 玩家点击锁定目录时显示的提示文本。 |
| `parent` | 父目录文件名。不写时表示一级目录，父级为书本。 |
| `sortnum` | 排列优先级。数值越小越靠前；未设置时优先级最低。 |

目录支持多层嵌套，但同一个目录下不应同时放置子目录和章节。官方资料指出，如果某个目录既被子目录作为`parent`，又被章节作为`parent`，会造成冲突报错。

## 编写章节与页面

章节文件放在`entry`文件夹中。一个章节属于某个目录，并包含若干页。

```json title="entry/imageEntry.json"
{
    "parent": "pages",
    "icon": "textures/items/sign",
    "title": "图片",
    "pages": [
        {
            "type": "textPage",
            "content": "该章节为图片页的介绍"
        },
        {
            "type": "imagePage",
            "subtitle": "内容页的标题",
            "image": "textures/ui/myCustomBook/testImage_1",
            "info": "图片说明",
            "content": "图片页正文"
        }
    ]
}
```

章节常用字段如下：

| 字段 | 作用 |
| --- | --- |
| `title` | 章节标题。 |
| `icon` | 章节在目录首页中显示的图标路径。 |
| `isLocked` | 是否锁定章节。 |
| `lockIcon` | 章节锁定状态下显示的锁图标路径。 |
| `lockMsg` | 玩家点击锁定章节时显示的提示文本。 |
| `parent` | 章节所属目录的标识符。该字段必须填写。 |
| `pages` | 章节中的页面数组。 |
| `sortnum` | 排列优先级。 |

每个页面至少需要`type`字段。系统预置的页面类型包括：

| 类型 | 用途 | 关键字段 |
| --- | --- | --- |
| `textPage` | 纯文本页。 | `content`、`contentTextSize` |
| `imagePage` | 图片和文字页。 | `image`、`imageSize`、`info`、`content` |
| `highlightPage` | 轮播物品页。 | `itemData`、`itemSize`、`info`、`content` |
| `tableRecipePage` | 工作台合成表页。 | `recipeId`、`recipeShapeId`、`tag`、`recipeSize`、`aux`、`info`、`content` |
| `entityPage` | 实体展示页。 | `entity`、`entitySize`、`info`、`content` |

`highlightPage`中的`itemData`是物品数组，每个元素通常包含`item`和可选的`data`。`entityPage`中的`entity`对象通常包含`name`、`offset`和`molang_dict`。`tableRecipePage`仍需要配置`recipeId`；如果同时配置`recipeId`和`recipeShapeId`，系统会优先尝试使用`recipeShapeId`获取配方，失败后再使用`recipeId`。

## 用脚本扩展页面

如果预置页面不能满足需求，可以用Python脚本注册自定义页面。页面类通常继承`BasePage`或`TitlePage`，并实现初始化、`SetData`和`Show`。`BasePage`不处理标题；`TitlePage`会帮助处理章节首页标题、`title`和`subtitle`。

```python
import mod.client.extraClientApi as clientApi

bookManager = clientApi.GetBookManager()
BasePage = bookManager.GetBasePageCls()
TextComp = bookManager.GetTextCompCls()
ImageComp = bookManager.GetImageCompCls()

class MyNoTitlePage(BasePage):

    def __init__(self, size=None, position=None):
        BasePage.__init__(self, size, position)
        self.title = TextComp()
        self.image = ImageComp()
        self.AddComps(self.title, self.image)
        self.data = None

    def SetData(self, data):
        self.data = data
        return self

    def Show(self):
        if not self.data:
            return self
        self.title.SetDataBeforeShow(self.data["testTitle"])
        self.image.SetDataBeforeShow(self.data["image"])
        BasePage.Show(self)
        self.ResetCompsPosition()
        self.title.AlignTopToY(self.Top()).AlignCenterToX(self.Center()[0])
        self.image.SetSize((80, 80)).AlignTopToY(self.title.Bottom()).MoveY(5)
        return self
```

自定义页面需要在客户端系统初始化时注册。页面类型名称建议使用`模组名:页面类名`格式，以避免与其他模组或系统预置类型冲突。

```python
class TutorialClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        from tutorialScripts.pages.myNoTitlePage import MyNoTitlePage
        bookManager = clientApi.GetBookManager()
        bookManager.AddPageType("CustomMod:MyNoTitlePage", MyNoTitlePage)
```

注册后即可在章节页面中使用该类型：

```json
{
    "type": "CustomMod:MyNoTitlePage",
    "testTitle": "标题文本",
    "image": "textures/ui/myCustomBook/testImage"
}
```

## 用脚本扩展组件

页面由组件组成。预置组件包括文本、图片、轮播物品、合成表、实体预览、进度条和按钮。更复杂的界面可以通过自定义组件实现。

自定义组件需要一个UI模板。模板文件中必须存在名为`main`的根层级和名为`comps`的面板节点，组件要封装的UI根节点放在`comps`下。`comps`的大小应覆盖整个界面区域，组件根节点的锚点应位于左上角，以便和书本坐标系一致。

组件类通常继承`BaseComp`，并在初始化时把组件名称、UI模板路径和根节点名称传给父类。

```python
import mod.client.extraClientApi as clientApi

bookManager = clientApi.GetBookManager()
BaseComp = bookManager.GetBaseCompCls()

class MyCustomComp(BaseComp):

    def __init__(self):
        BaseComp.__init__(self, "CustomMod:MyCustomComp", "CustomComp.main", "testComp")
        self.text = None

    def SetDataBeforeShow(self, text):
        self.text = text
        return self

    def Show(self):
        BaseComp.Show(self)
        textNode = self.GetRootUINode().GetChildByPath("/text").asLabel()
        self.SetNodeText(textNode, self.text)
        return self
```

/// note | 组件回收需要重置状态
组件可以设置为可回收，以减少UI控件节点的重复拷贝。开启回收后，节点会被复用；如果`Show`中修改了位置、大小、文本、颜色或层级，就需要在`Reset`中恢复状态，或使用`SetNodeOffset`、`SetNodeSize`等辅助方法。
///

## 跳转与解锁

自定义书本内部的跳转类似浏览器地址。以`/`开头的是绝对路径，不以`/`开头的是相对路径。路径由书本、目录、章节和页号组成，例如`/customBook/pages/imageEntry/1`可以表示`customBook`书本中`pages`目录下`imageEntry`章节的第1页。页号从0开始；如果省略页号，默认跳转到第0页。

```python
import mod.client.extraClientApi as clientApi

bookManager = clientApi.GetBookManager()
bookManager.To("/customBook/pages/imageEntry/1")
```

脚本还可以获取当前打开的书本，并动态锁定或解锁目录与章节：

```python
book = clientApi.GetBookManager().GetOpeningBookInstance()
if book:
    book.LockCategory("pages")
    book.UnlockEntry("imageEntry")
```

页面跳转只在当前打开的书本内有效，不支持从一本书直接跳转到另一本书。