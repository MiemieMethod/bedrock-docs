---
comments: true
---

# 国际化

Allay自带完整的国际化系统，所以插件没有必要把所有提示都写死成中文或英文。只要把文本改成翻译键，再把语言文件打进JAR里，同一套插件就能按玩家语言输出不同文本。

## 翻译键长什么样

Allay使用的翻译键格式是：

```text
namespace:path.to.key
```

例如：

- `minecraft:commands.generic.syntax`
- `allay:command.gc.completed`
- `myplugin:greeting.welcome`

建议你始终使用自己的插件命名空间，避免和别的插件撞键。

## 在代码里翻译文本

最基础的入口是`I18n.get().tr()`：

```java linenums="1"
import org.allaymc.api.message.I18n;

String text = I18n.get().tr("myplugin:greeting.welcome");
String hello = I18n.get().tr("myplugin:greeting.hello", player.getDisplayName());
```

如果你想指定语言，也可以显式传语言代码：

```java linenums="1"
import org.allaymc.api.message.I18n;
import org.allaymc.api.message.LangCode;

String zh = I18n.get().tr(LangCode.zh_CN, "myplugin:greeting.welcome");
String ja = I18n.get().tr(LangCode.ja_JP, "myplugin:greeting.welcome");
```

## 把语言文件放进插件

语言文件要放在插件JAR里的`assets/lang/`目录下：

```text
your-plugin.jar
├── plugin.json
└── assets
    └── lang
        ├── en_US.json
        └── zh_CN.json
```

一个最小示例如下：

```json title="assets/lang/en_US.json"
{
  "myplugin:greeting.welcome": "Welcome to our server!",
  "myplugin:greeting.hello": "Hello, %1!"
}
```

```json title="assets/lang/zh_CN.json"
{
  "myplugin:greeting.welcome": "欢迎来到服务器！",
  "myplugin:greeting.hello": "你好，%1！"
}
```

## 占位符怎么写

Allay给出了三类常见占位符：

| 占位符 | 用途 |
|--------|------|
| `%1`、`%2`、`%3` | 有序参数，推荐使用。 |
| `%s` | 无序字符串参数。 |
| `%d` | 无序数字参数。 |

实践里优先使用`%1`、`%2`这类有序参数，因为不同语言的语序经常不一样。

```json
{
  "myplugin:message.trade": "%1与%3交易了%2个物品，换来%4个绿宝石"
}
```

```java
I18n.get().tr("myplugin:message.trade", "Steve", 5, "Alex", 10);
```

## 直接发给玩家

如果消息最终是给玩家看的，通常可以直接用`sendTranslatable()`：

```java linenums="1"
player.sendTranslatable("myplugin:greeting.welcome");
player.sendTranslatable("myplugin:greeting.hello", player.getDisplayName());
```

这样消息会按玩家当前语言设置翻译，而不是按服务器默认语言固定输出。

## 命令里也可以用翻译键

命令描述和输出都可以直接写翻译键：

```java linenums="1"
import org.allaymc.api.command.Command;
import org.allaymc.api.command.tree.CommandTree;

public class GreetCommand extends Command {
    public GreetCommand() {
        super("greet", "myplugin:command.greet.description", "myplugin.command.greet");
    }

    @Override
    public void prepareCommandTree(CommandTree tree) {
        tree.getRoot()
                .playerTarget("player")
                .exec(context -> {
                    var players = context.getResult(0);
                    for (var player : players) {
                        context.addOutput("myplugin:command.greet.success", player.getDisplayName());
                    }
                    return context.success();
                });
    }
}
```

## 回退语言

如果指定语言找不到某个键，Allay会回退到`en_US`。所以不管你主力维护哪种语言，都建议至少保证`en_US.json`完整。

## 实战建议

- 键名尽量按功能分层，例如`myplugin:command.home.success`。
- 玩家可见文本尽量全部进语言文件，不要在代码里硬拼整句。
- 描述文字、按钮文字和报错也都可以走翻译键。
- 如果你已经开始做可翻译的菜单和提示，再结合[表单开发](form-guide.md)会很顺手。