---
comments: true
---

# 表单开发

表单是一个Minecraft基岩版中的特殊功能，允许玩家以用户友好的方式读取和输入数据。Allay提供了一个强大的表单API，允许插件轻松创建和处理表单。

## 创建和发送表单

假设你想在玩家加入服务器时向他们显示一个简单表单。关于如何注册事件监听器，请参阅[事件系统](event-guide.md)。

```java linenums="1" hl_lines="8-11"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerJoinEvent;
import org.allaymc.api.form.Forms;
import org.allaymc.api.utils.TextFormat;

public class MyEventListener {
    @EventHandler
    private void onPlayerJoin(PlayerJoinEvent event) {
        Forms.simple()
                .title(TextFormat.BLUE + "欢迎")
                .content(TextFormat.GREEN + "欢迎来到服务器！")
                .sendTo(event.getPlayer());
    }
}
```

**完成了！**[构建并安装你的插件](first-plugin.md#构建插件)，当玩家加入服务器时，他们会看到一个内容为"欢迎来到服务器！"的表单。

## 处理表单响应

你可能想问玩家是否喜欢你的服务器，并根据玩家的选择用不同的内容回复。以下是做法：

```java linenums="1" hl_lines="12-14"
import org.allaymc.api.eventbus.EventHandler;
import org.allaymc.api.eventbus.event.server.PlayerJoinEvent;
import org.allaymc.api.form.Forms;
import org.allaymc.api.utils.TextFormat;

public class MyEventListener {
    @EventHandler
    private void onPlayerJoin(PlayerJoinEvent event) {
        var player = event.getPlayer();
        Forms.modal() /*(1)!*/
                .title(TextFormat.YELLOW + "你喜欢Allay吗？")
                .content(TextFormat.GREEN + "请告诉我们你是否喜欢Allay！")
                .trueButton(TextFormat.GREEN + "是的", () -> player.sendMessage("谢谢！"))
                .falseButton(TextFormat.RED + "不", () -> player.sendMessage("遗憾听到那！"))
                .sendTo(player);
    }
}
```

1. :star: 模态表单是只有两个按钮的表单类型。

当玩家加入服务器时，他们会看到一个标题为"你喜欢Allay吗？"、有两个按钮"是的"和"不"的表单。当玩家点击"是的"按钮时，他们会收到消息"谢谢！"，当他们点击"不"按钮时，他们会收到消息"遗憾听到那！"。

## 使用自定义表单

自定义表单是最强大的表单类型，允许你从玩家收集各种类型的数据。它们支持多个元素类型，非常适合设置页面、注册表单或任何你需要结构化输入的场景。

### 基本自定义表单示例

让我们创建一个简单的反馈表单，要求玩家输入他们的名字和评论：

```java linenums="1"
import org.allaymc.api.entity.interfaces.EntityPlayer;
import org.allaymc.api.form.Forms;
import org.allaymc.api.utils.TextFormat;

public void showFeedbackForm(EntityPlayer player) {
    Forms.custom()
            .title(TextFormat.GOLD + "玩家反馈")
            .input("你的名字", "输入你的名字...", "")
            .input("评论", "告诉我们你的想法...", "")
            .onResponse(responses -> {
                String name = responses.get(0);
                String comments = responses.get(1);
                player.sendMessage("感谢" + name + "的反馈！");
            })
            .sendTo(player);
}
```

### 可用的自定义表单元素

自定义表单支持各种元素类型来收集不同类型的数据：

| 元素类型 | 方法 | 描述 |
|---------|------|------|
| 标签 | `.label(text)` | 显示纯文本标签 |
| 输入 | `.input(label, placeholder, default)` | 单行文本输入 |
| 下拉列表 | `.dropdown(label, options)` | 下拉选择列表 |
| 切换 | `.toggle(label, default)` | 开关/复选框 |
| 滑块 | `.slider(label, min, max, step, default)` | 数值滑块 |

### 表单类型

Allay提供三种主要表单类型：

| 表单类型 | 用途 | 方法 |
|---------|------|------|
| 简单表单 | 显示信息和基本选项 | `Forms.simple()` |
| 模态表单 | 是/否选择 | `Forms.modal()` |
| 自定义表单 | 复杂数据收集 | `Forms.custom()` |

## 处理未闭合的表单

有时玩家可能会关闭表单而不填写。你可以使用`onClose()`处理这种情况：

```java linenums="1"
Forms.custom()
        .title("表单标题")
        .input("名字", "输入...", "")
        .onResponse(responses -> {
            // 玩家提交了表单
        })
        .onClose(() -> {
            // 玩家关闭了表单
        })
        .sendTo(player);
```

## 接下来

现在你已经了解了表单系统的基础。建议继续学习：

- [方块API](block-guide.md) - 与方块交互
- [物品API](item-guide.md) - 管理物品