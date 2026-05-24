# 国际化（i18n）指南

LeviLamina提供了内置的国际化系统，允许你的模组支持多语言。

## 基础概念

国际化（i18n）是使应用程序支持多种语言的过程。LeviLamina的i18n系统基于键值对的翻译文件。

## 使用翻译系统

### 1. 加载翻译文件

```cpp
#include "ll/api/i18n/I18nAPI.h"

void loadTranslations() {
    // 加载你的模组的翻译文件
    ll::i18n::getInstance().load("mods/my-mod/i18n");
}
```

### 2. 获取翻译字符串

```cpp
#include "ll/api/i18n/I18nAPI.h"

std::string getTranslatedText() {
    // 获取默认语言的翻译
    return ll::i18n::getInstance().get("key.my_text");
}

std::string getTranslatedTextForLang(const std::string& lang) {
    // 获取指定语言的翻译
    return ll::i18n::getInstance().get("key.my_text", lang);
}
```

## 翻译文件格式

翻译文件使用JSON格式存储键值对：

```json
{
  "ui.title": "My Mod",
  "command.help": "This is a help message",
  "message.welcome": "Welcome to my mod!",
  "error.invalid_input": "Invalid input provided"
}
```

### 文件组织

推荐的目录结构：

```
mods/my-mod/
├── i18n/
│   ├── en_US.json    # 美式英文
│   ├── zh_CN.json    # 简体中文
│   ├── ja_JP.json    # 日语
│   └── ...
└── tooth.json
```

## 在命令中使用翻译

```cpp
#include "ll/api/command/CommandRegistrar.h"
#include "ll/api/i18n/I18nAPI.h"

void registerTranslatedCommand() {
    using namespace ll::command;
    auto& command = CommandRegistrar::getInstance().getOrCreateCommand("hello");
    
    command.overload().execute([](CommandOrigin const& origin, CommandOutput& output) {
        auto text = ll::i18n::getInstance().get("message.welcome");
        output.success(text);
    });
}
```

## 在表单中使用翻译

```cpp
#include "ll/api/form/SimpleForm.h"
#include "ll/api/i18n/I18nAPI.h"

void showTranslatedForm(Player& player) {
    auto i18n = ll::i18n::getInstance();
    ll::form::SimpleForm form(
        i18n.get("ui.title"),
        i18n.get("ui.description")
    );
    
    form.appendButton(i18n.get("button.confirm"))
        .appendButton(i18n.get("button.cancel"))
        .sendTo(player, [](Player& p, int selected, auto reason) {
            // 处理选择
        });
}
```

## 最佳实践

/// note | 翻译键命名规范
使用点分符号组织翻译键，如：
- `ui.*` - 用户界面文本
- `command.*` - 命令帮助和反馈
- `message.*` - 游戏消息
- `error.*` - 错误消息
///

## 支持的语言

LeviLamina支持Minecraft支持的所有语言，包括但不限于：
- `en_US` - 美式英文
- `zh_CN` - 简体中文  
- `zh_TW` - 繁体中文
- `ja_JP` - 日语
- `ko_KR` - 韩语
- `ru_RU` - 俄语
- ...以及更多

## 下一步

- 回顾[表单开发](form-guide.md)
- 查看[LeviLamina API参考](../../refs/server/levilamina-api.md)中的i18n模块
- 参考[LeviLamina官方示例](https://github.com/LiteLDev/LeviLamina)获得更多实现细节
