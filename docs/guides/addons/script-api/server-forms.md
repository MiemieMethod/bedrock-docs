# 服务端表单<!-- md:flag vanilla -->

`@minecraft/server-ui`模块提供了三种可以直接从脚本弹出的表单界面，无需编写任何JSON UI配置。自1.18.30版本起可以使用。

## 准备依赖

在`manifest.json`中添加依赖：

```json title="BP/manifest.json（依赖部分）"
{
    "dependencies": [
        {
            "module_name": "@minecraft/server",
            "version": "2.0.0"
        },
        {
            "module_name": "@minecraft/server-ui",
            "version": "2.0.0"
        }
    ]
}
```

在脚本中导入对应类：

```javascript
import { ActionFormData, MessageFormData, ModalFormData } from "@minecraft/server-ui";
```

## 表单类型

### 动作表单（ActionFormData）

动作表单由若干按钮组成，适合商店界面、小游戏选择等场景。

```javascript
const form = new ActionFormData();
form.title("小游戏选择");
form.body("选择要参与的小游戏");
form.button("Spleef", "textures/items/diamond_shovel");         // 带图标按钮
form.button("Murder Mystery", "textures/items/iron_sword");
form.button("Bedwars", "textures/wiki/minigames/bedwars");      // 自定义纹理需加.png并提供资源包
```

/// warning | 按钮数量上限
动作表单最多支持256个按钮，超过可能导致表单异常。
///

### 消息表单（MessageFormData）

消息表单固定有两个按钮和一个大段文字主体，适合确认/取消对话框。

```javascript
const form = new MessageFormData();
form.title("随机刻速度警告");
form.body(
    "你确定要运行以下命令吗？\n/gamerule randomtickspeed 1000\n这可能会造成卡顿。"
);
form.button1("不，保持默认");
form.button2("确定");
```

/// tip | 按钮布局建议
建议将"确认"操作放在`button2`、"取消"操作放在`button1`。按下Escape关闭表单时效果等同于`button1`被取消。
///

### 模态表单（ModalFormData）

模态表单支持文本输入框、下拉菜单、滑块和开关，适合参数化操作。

```javascript
const effectList = ["生命恢复", "防护", "中毒", "凋零"];
const form = new ModalFormData();
form.title("效果生成器");
form.textField("目标", "输入目标名称");
form.dropdown("效果类型", effectList);
form.slider("效果等级", 0, 255, { defaultValue: 1 });
form.toggle("隐藏粒子效果", { defaultValue: true });
```

**文本输入框**参数：
1. 标签（标题文字）
2. 占位符文字（提示信息）
3. 可选：默认值（默认为空）

**下拉菜单**参数：
1. 标签
2. 选项数组
3. 可选：默认选中索引（默认为0）

**滑块**参数：
1. 标签
2. 最小值
3. 最大值
4. 选项对象（包含`defaultValue`和`step`）

**开关**参数：
1. 标签
2. 可选：选项对象（包含`defaultValue`）

## 显示表单并处理响应

使用`.show(player)`向玩家显示表单，返回一个`Promise`。

```javascript
import { world } from "@minecraft/server";
import { ActionFormData } from "@minecraft/server-ui";

world.beforeEvents.itemUse.subscribe((event) => {
    if (
        event.itemStack.typeId === "minecraft:stick" &&
        event.itemStack.nameTag === "表单打开器"
    ) {
        const player = event.source;
        const form = new ActionFormData();
        form.title("选择模式");
        form.button("生存");
        form.button("创造");

        form.show(player)
            .then((response) => {
                if (response.canceled) return; // 玩家关闭了表单

                switch (response.selection) {
                    case 0:
                        player.runCommand("gamemode survival @s");
                        break;
                    case 1:
                        player.runCommand("gamemode creative @s");
                        break;
                }
            })
            .catch((error) => {
                console.error(error, error.stack);
            });
    }
});
```

/// warning | 表单显示限制
表单只能在没有其他界面打开时显示。通过聊天消息触发时，因为聊天框已打开，无法立即显示表单；建议改用物品使用事件或其他不涉及UI的事件来触发表单。
///

### 动作表单响应

`response.selection`返回被点击按钮的索引（从0开始）：

```javascript
form.show(player).then((response) => {
    if (response.canceled) return;
    const index = response.selection;
    // 根据index执行对应逻辑
});
```

### 消息表单响应

`response.selection`返回0（`button1`）或1（`button2`）；按Escape关闭时`response.canceled`为`true`：

```javascript
form.show(player).then((response) => {
    if (response.canceled || response.selection === 0) {
        // 取消或选择了button1
        return;
    }
    // 选择了button2，执行确认逻辑
});
```

### 模态表单响应

`response.formValues`是一个数组，按照表单控件从上到下的顺序返回各控件的值：

```javascript
form.show(player).then((response) => {
    if (response.canceled) return;

    const [target, effectIndex, level, hideParticles] = response.formValues;
    // target: 字符串（文本输入框）
    // effectIndex: 数字（下拉菜单选中项的索引）
    // level: 数字（滑块当前值）
    // hideParticles: 布尔值（开关状态）
});
```
