# 表单开发指南

LeviLamina提供了一套极简的表单API，允许开发者用几行代码实现复杂的表单功能。表单API的头文件被存放于`ll/api/form`中。

由于Minecraft的表单ID在运行时是唯一的，LeviLamina提供了**FormIdManager**用于获取Minecraft的表单ID，允许开发者自己实现一套表单API。

## FormIdManager

FormIdManager的头文件位于`ll/api/form/FormIdManager.h`，导出了`ll::form::FormIdManager::genFormId`方法，用于获取一个唯一的表单ID。

### 示例

```cpp
#include "ll/api/form/FormIdManager.h"

void test() { uint formId = ll::form::FormIdManager::genFormId(); }
```

## SimpleForm

SimpleForm是一个简单的表单，提供了标题、内容和按钮。SimpleForm的头文件位于`ll/api/form/SimpleForm.h`。由于SimpleForm的方法例如`appendButton`返回SimpleForm的引用，所以可以链式调用。

### 用法

1. 引用头文件`ll/api/form/SimpleForm.h`
2. 构造一个SimpleForm对象，可以使用带参数和不带参数的构造函数
3. 通过`appendButton`方法添加按钮，通过`appendHeader`、`appendLabel`和`appendDivider`方法添加仅视觉效果元素
4. 使用`sendTo`方法将表单发送给玩家，需要传入`Player`对象的引用和一个回调函数

/// tip | 提示
当按钮的索引为-1时代表玩家取消的表单。`FormCancelReason`的本质是`std::optional<ModalFormCancelReason>`，所以你需要先判断其是否有值才能使用。
///

### SimpleForm示例

```cpp
#include "ll/api/form/SimpleForm.h"
#include "magic_enum/magic_enum.hpp"

void sendSimpleFormToPlayer(Player& player) {
    ll::form::SimpleForm form("I'm title", "I'm content");
    form.appendHeader("header")
        .appendButton("Button1")
        .appendDivider()
        .appendHeader("header")
        .appendLabel("label")
        .appendButton("Button2")
        .sendTo(player, [](Player& player, int selected, ll::form::FormCancelReason reason) {
            switch (selected) {
            case 0: {
                player.sendMessage("You clicked Button1");
                break;
            }
            case 1: {
                player.sendMessage("You clicked Button2");
                break;
            }
            case -1: {
                player.sendMessage("You closed the form");
                break;
            }
            }
        });
}
```

## CustomForm

CustomForm是一个复杂的表单，提供了标题、标签(Label)、输入框(Input)、开关(Toggle)、下拉框(Dropdown)、滑块(Slider)和分段滑块(StepSlider)。

### 用法

1. 引用头文件`ll/api/form/CustomForm.h`
2. 构造一个CustomForm对象
3. 通过`appendInput`、`appendToggle`、`appendDropdown`、`appendSlider`和`appendStepSlider`方法添加各种自定义表单元素，通过`appendHeader`、`appendLabel`、`appendDivider`方法添加各种仅视觉效果元素
4. 使用`sendTo`方法将表单发送给玩家

/// tip | 提示
表单的结果`CustomFormResult`实际上是`std::optional<std::unordered_map<std::string, CustomFormElementResult>>`，一个存储了元素名称和结果的无序关联容器。你可以通过元素名称来获取对应的结果，结果的类型是`CustomFormElementResult`，是一个联合体(`std::variant<std::monostate, uint64, double, std::string>`)，所以你需要先使用`std::holds_alternative`判断其类型，通过`std::get`获取。
///

### CustomForm示例

```cpp
#include "ll/api/form/CustomForm.h"
#include "magic_enum/magic_enum.hpp"

void sendCustomFormToPlayer(Player& player) {
    ll::form::CustomForm form;
    form.setTitle("CustomForm")
        .appendHeader("header")
        .appendLabel("label")
        .appendInput("input1", "input")
        .appendToggle("toggle", "toggle")
        .appendSlider("slider", "slider", 0, 100, 1)
        .appendDivider()
        .appendStepSlider("stepSlider", "stepSlider", {"a", "b", "c"})
        .appendDropdown("dropdown", "dropdown", {"a", "b", "c"})
        .appendLabel("label")
        .setSubmitButton("Apply")
        .sendTo(
            player,
            [](Player& player, ll::form::CustomFormResult const& data, ll::form::FormCancelReason reason) {
                if (!data) {
                    player.sendMessage("CustomForm callback canceled");
                    return;
                }
                for (auto [name, result] : *data) {
                    if (std::holds_alternative<uint64_t>(result)) {
                        player.sendMessage(fmt::format("CustomForm callback {} = {}", name, std::get<uint64_t>(result)));
                    } else if (std::holds_alternative<double>(result)) {
                        player.sendMessage(fmt::format("CustomForm callback {} = {}", name, std::get<double>(result)));
                    } else if (std::holds_alternative<std::string>(result)) {
                        player.sendMessage(fmt::format("CustomForm callback {} = {}", name, std::get<std::string>(result)));
                    }
                }
            }
        );
}
```

## ModalForm

ModalForm是一个模态表单，提供了标题、内容和两个按钮，通常用于实现二项选择。

### 用法

1. 引用头文件`ll/api/form/ModalForm.h`
2. 构造一个ModalForm对象
3. 使用`sendTo`方法将表单发送给玩家

/// tip | 提示
`ModalFormResult`实际上是`std::optional<ModalFormSelectedButton>`的别名，而`ModalFormSelectedButton`是一个Bool枚举，有`Upper = true`和`Lower = false`两个值。
///

### ModalForm示例

```cpp
#include "ll/api/form/ModalForm.h"

void sendModalFormToPlayer(Player& player) {
    ll::form::ModalForm form;
    form.setTitle("ModalForm")
        .setContent("Select an option")
        .setUpperButton("Upper")
        .setLowerButton("Lower")
        .sendTo(
            player,
            [](Player& player, ll::form::ModalFormResult selected, ll::form::FormCancelReason reason) {
                if (!selected) {
                    player.sendMessage("ModalForm callback canceled");
                    return;
                }
                player.sendMessage(fmt::format("ModalForm callback {}", (bool)*selected));
            }
        );
}
```

## 动态更新表单

玩家处于表单打开状态时，可以使用`SimpleForm::sendUpdate`、`CustomForm::sendUpdate`和`ModalForm::sendUpdate`更新表单，且不限制更新的表单内容和类型。这些方法需要保证玩家处于表单打开中的状态，否则无效果。

### 动态更新示例

```cpp
#include "ll/api/chrono/GameChrono.h"
#include "ll/api/coro/CoroTask.h"
#include "ll/api/form/CustomForm.h"
#include "ll/api/service/Bedrock.h"
#include "ll/api/thread/ServerThreadExecutor.h"
#include "mc/server/ServerLevel.h"

std::unique_ptr<ll::form::CustomForm> buildStatusWindow() {
    auto form = std::make_unique<ll::form::CustomForm>("Status");
    auto ticks = ll::service::getLevel()
        .transform([](auto& level) { return level.getCurrentServerTick().tickID; })
        .value_or(-1);
    form->appendHeader("System Info")
        .appendLabel(fmt::format("Ticks: {}", ticks))
        .setSubmitButton("Close");
    return form;
}

void openStatusWindow(Player& player) {
    ll::coro::keepThis([uid = player.getOrCreateUniqueID()]() -> ll::coro::CoroTask<void> {
        auto closed = std::make_shared<bool>(false);
        auto callback = [closed](auto const&...) { *closed = true; };

        auto player = ll::service::getLevel().transform([uid](auto& level) { return level.getPlayer(uid); });
        if (!player || *closed) co_return;
        buildStatusWindow()->sendTo(*player, callback);

        while (true) {
            co_await ll::chrono::ticks{20};
            player = ll::service::getLevel().transform([uid](auto& level) { return level.getPlayer(uid); });
            if (!player || *closed) co_return;
            buildStatusWindow()->sendUpdate(*player, callback);
        }
    }).launch(ll::thread::ServerThreadExecutor::getDefault());
}
```

## 下一步

- 了解更多关于[钩子系统](hook-guide.md)
- 查看[LeviLamina API参考](../../../refs/server/levilamina-api.md)中的表单模块
- 参考[创建第一个模组](../levilamina.md#创建第一个模组)获得完整示例