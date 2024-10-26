---
title: 脚本表单
category: 教程
tags:
    - 实验性
mentions:
    - DrakPlay
    - cda94581
    - FrankyRay
    - MedicalJewel105
    - Worldwidebrine
    - Fabrimat
    - Axisander
    - JaylyDev
    - Herobrine643928
    - SmokeyStack
    - ThomasOrs
    - kumja1
description: 创建表单用户界面，无需处理 JSON 用户界面。
---

::: warning
脚本 API 目前正在积极开发中，破坏性更改频繁。此页面假设 Minecraft 版本为 1.20.60。
:::

在 1.18.30 版本中，Minecraft 发布了一个新的脚本模块 `@minecraft/server-ui`（之前称为 `mojang-minecraft-ui`）。通过这个模块，我们可以创建表单用户界面，无需处理 JSON 用户界面。

## 设置
与其他模块一样，您需要将依赖项添加到 `manifest.json` 中。

```json
{
	"dependencies": [
		{
			"module_name": "@minecraft/server-ui",
			"version": "1.2.0-beta"
		},
		{
			"module_name": "@minecraft/server",
			"version": "1.9.0-beta"
		}
	]
}
```

并在您的脚本文件中导入该模块。

```js
import {
  ActionFormData,
  MessageFormData,
  ModalFormData
} from "@minecraft/server-ui";
```

## 表单类型
`@minecraft/server-ui` 模块提供了 3 种表单类型：操作表单数据、消息表单数据和模态表单数据。

### ActionFormData
操作表单是包含多个按钮的表单。此表单非常适合商店用户界面、迷你游戏选择等。如果您看到一个特色服务器有很多按钮的用户界面，这就是该表单。

要使用该表单，您需要先创建它。

```js
let form = new ActionFormData();
```

该表单有 3 个函数/属性：标题、主体和按钮。

#### 标题
标题是表单顶部的文本。

```js
form.title("操作表单");
```

#### 主体
主体添加一些描述信息。您可以进一步解释表单的功能。

```js
form.body("这是操作表单的主体");
```

#### 按钮
按钮是表单的主要功能。表单可以有多个按钮供玩家选择。每个按钮有 2 个参数。第一个参数是标签，即显示在按钮上的文本。

第二个参数是可选的，是按钮图标，显示在按钮上的图片/图标。要使用它，您需要定义纹理路径。您可以使用原版资源包来显示图标（例如 `textures/items/compass`）。自定义纹理需要在路径末尾加上 `.png`，并且在世界中需要有有效的资源包。

```js
// 无图标
form.button("按钮 1");
// 使用原版纹理
form.button("按钮 2", "textures/items/compass");
// 使用自定义纹理
form.button("按钮 3", "textures/icon/btn_icon_3.png");
```

:::warning
按钮的最大数量为 256。更多可能导致表单崩溃。
:::

#### 示例
这是一个操作表单的示例。

```js
let form = new ActionFormData();
form.title("迷你游戏");
form.body("选择游戏");
form.button("雪仗", "textures/items/diamond_shovel");
form.button("谋杀之谜", "textures/items/iron_sword");
form.button("床战", "textures/minigames/bedwars.png");
```

![image](/assets/images/gametest/gametest-form/action-form.png)

### MessageFormData
消息表单是由 2 个按钮和一个大描述（主体）组成的表单。此表单非常适合是/否问题或确定/取消表单。

```js
let form = new MessageFormData();
```

消息表单与操作表单非常相似。主要区别在于按钮被称为按钮 1 和按钮 2。

#### 标题
标题是表单顶部的文本。

```js
form.title("消息表单");
```

#### 主体
主体添加一些描述信息。您可以进一步解释表单的功能。

消息表单的主体文本限制非常大，因此您可以放入 5 行以上的文本。要添加新行，请使用 `\n`。

```js
form.body("这是消息表单的主体");
```

#### 按钮 1 和 按钮 2
消息表单仅包含 2 个按钮，而操作表单可以有多个按钮。此表单用于向玩家发出警告或消息。

与操作表单的按钮一样，按钮 1 和按钮 2 也有 2 个参数，文本和图标。

```js
form.button1("按钮 1：否");
form.button2("按钮 2：是");
```

:::tip
由于消息表单只有 2 个按钮，建议在“按钮 2”上设置“是/确定”选项，在“按钮 1”上设置“否/取消”选项。您可以在“显示和响应”部分看到这个问题。
:::

#### 示例
这是一个消息表单的示例。

```js
let form = new MessageFormData();
form.title("高随机滴答警告");
form.body("您确定要运行此命令：\n/gamerule randomtickspeed 1000\n这可能会导致世界延迟");
form.button1("不，保持默认设置！");
form.button2("是的，执行！");
```

![image](/assets/images/gametest/gametest-form/message-form.png)

### ModalFormData
模态表单具有表单中可用的最多输入类型。它具有文本字段、滑块、下拉菜单和切换。模态表单适用于复杂的表单，例如效果生成器。模态表单没有主体属性。

```js
let form = new ModalFormData();
```

模态表单有 5 个属性：标题、文本字段、下拉菜单、滑块和切换。

#### 标题
标题是表单顶部的文本。

```js
form.title("模态表单");
```

#### 文本字段
文本字段是一个允许玩家输入文本的属性。它有 3 个参数。

1. 标签（`Str`），文本字段的标题。
2. 占位符文本（`Str`），文本字段的描述或信息。
3. 默认值（`Str`）[可选]，文本字段中的默认文本。默认值为空（`null`）。

```js
// 无默认值
form.textField("文本字段", "在这里输入一些内容");
// 有默认值
form.textField("文本字段", "在这里输入一些内容", "默认值");
```

#### 下拉菜单
下拉菜单是一个包含选项列表的属性。它有 3 个参数。

1. 标签（`Str`），下拉菜单的标题。
2. 选项（`List[String]`），供玩家选择的选项列表。
3. 默认值索引（`Int`）[可选]，默认值的索引。默认值为 `0`（列表中的第一个项目）。

```js
// 内部选项
form.dropdown("下拉菜单", [ "选项 1", "选项 2", "选项 3" ], 1);
// 默认索引 "1" 将选择第二个选项（"选项 2"）作为默认选项

// 外部选项（推荐）
let options = [ "选项 1", "选项 2", "选项 3" ];
form.dropdown("下拉菜单", options);
```

#### 滑块
滑块是一个可以保持数字范围的属性。它有 5 个参数。

1. 标签（`Str`），滑块的标题。
2. 最小数字（`Int`），范围的最低数字。
3. 最大数字（`Int`），范围的最高数字。
4. 值步长（`Int`），范围的步长值。
5. 默认值（`Int`）[可选]，滑块的默认数字。默认值为最低数字。

```js
// 从 1 到 100 的正常范围
form.slider("滑块", 1, 100, 1);
// 从 0 到 10 的偶数，默认值设置为 10
form.slider("滑块", 0, 10, 2, 10);
```

#### 切换
切换是一个仅具有真/假选项的属性。它有 2 个参数。

1. 标签（`Str`），切换的标题。
2. 默认值（`Bool`），切换的默认布尔值。默认值为 `false`。

```js
// 无默认值
form.toggle("切换");
// 有默认值
form.toggle("切换", true);
```

#### 示例
这是一个包含所有组件的模态表单示例。

```js
let form = new ModalFormData()
let effectList = [ "再生", "保护", "中毒", "凋零" ]
form.title("效果生成器");
form.textField("目标", "效果目标")
form.dropdown("效果类型", effectList)
form.slider("效果等级", 0, 255, 1)
form.toggle("隐藏效果粒子", true)
```

![image](/assets/images/gametest/gametest-form/modal-form.png)

## 显示和响应
创建表单后，我们需要向玩家显示表单并保存响应以执行其他任务。我们需要一些事件来显示我们的表单。最常用的事件是使用 `itemUse` 事件，它会在玩家使用（右键单击）物品时触发。

假设我们的表单必须通过一个名为“表单开启器”的棒子打开。您可以使用任何事件和任何配置来打开自己的表单。

```js
world.beforeEvents.itemUse.subscribe(event => {
	if (event.itemStack.typeId === "minecraft:stick" && event.itemStack.nameTag === "表单开启器") {
		// 表单
	};
});
```

:::warning
这些表单仅在没有其他用户界面打开时才能打开。如果您想通过自定义命令/聊天消息打开表单，则无法做到，因为聊天用户界面已打开。您需要使用 `/damage` 关闭聊天用户界面，然后打开表单。最佳选择是使用另一个事件。
:::

在 if 语句内部是我们将显示表单的地方。使用 `.show()`，表单将打开。在 show 函数内部，您需要一个玩家类作为参数。显示表单后，我们可以使用 `.then()` 来保存玩家的响应。

```js
form.show(event.source).then(r => {
	// 玩家响应/关闭表单时的代码
}).catch((e) => {
	console.error(e, e.stack);
});
```

当玩家关闭表单时，`.then()` 内的函数将运行，即使没有输入。这可能会导致玩家仅关闭表单时意外执行代码。为防止这种情况，您需要使用 `.canceled` 取消脚本。

```js
form.show(event.source).then(r => {
	// 玩家关闭表单时停止代码
	if (r.canceled) return;

	// 玩家响应表单时的代码
}).catch(e => {
	console.error(e, e.stack);
});
```

最后，我们可以处理玩家的输入。每种表单都有自己的玩家返回输入。

### ActionFormData
操作表单将输入保存在 `.selection` 中。它返回按钮索引的数字，从 0 开始为按钮 1。您可以使用 switch-case 来为每个按钮运行特定的代码。

```js
form.show(event.source).then(r => {
	// 玩家关闭表单时停止代码
	if (r.canceled) return;

	let response = r.selection;
	switch (response) {
		case 0:
			// 按钮 1 被按下时执行某些操作
			// 不要忘记在每个 case 后使用 "break"
			break;

		case 1:
			// 按钮 2 被按下时执行某些操作
			break;

			// 您可以为每个按钮添加 case
		default:
			// 当您的按钮尚未定义功能时使用此项
			// 默认 case 不需要使用 "break"
			// 请记得将默认项放在最后
	}
}).catch(e => {
	console.error(e, e.stack);
});
```

### MessageFormData
与操作表单类似，消息表单将输入保存在 `.selection` 中。点击 `.button1` 将返回 0，点击 `.button2` 将返回 1。虽然没有关闭按钮，但按“Escape”将关闭表单。我们可以使用 `.canceled` 来处理此事件。

```js
form.show(event.source).then(r => {
	if(r.canceled || r.selection == 0){
		// 玩家关闭表单或按下“按钮 1”时执行某些操作
		return
	}
	//我们不需要测试 "r.selection == 1"，因为这是唯一未处理的情况。
	// 玩家按下“按钮 2”时执行某些操作

}).catch(e => {
	console.error(e, e.stack);
});
```

### ModalFormData
模态表单将输入保存在 `.formValues` 中，作为输入列表。输入按从上到下的组件顺序排列。

例如：
```js
let form = new ModalFormData();
form.textField(...);
form.dropdown(...);
form.slider(...);
form.toggle(...);

// ...
console.warn(r.formValues);
// 输出: [ <文本字段输入>, <下拉菜单输入>, <滑块输入>, <切换输入> ]
```

由于表单的输出基于顶部组件的顺序，您可以将每个输入分配给自己的变量。

```js
let form = new ModalFormData();
form.textField(...);
form.dropdown(...);
form.slider(...);
form.toggle(...);

form.show(event.source).then(r => {
	// 玩家关闭表单时停止代码
	if (r.canceled) return;

	// 将每个输入分配给自己的变量
	let [ textField, dropdown, slider, toggle ] = r.formValues;

	// 执行某些操作
}).catch(e => {
	console.error(e, e.stack);
});
```