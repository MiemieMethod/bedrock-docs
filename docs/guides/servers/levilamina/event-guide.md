# 事件系统指南

LeviLamina内置了一套事件系统，提供简单事件和供模组发布自己的事件。所有的内置事件都被放在了`ll/api/event/`目录下，并且被分类放置在`command`、`entity`、`player`、`world`等子目录下。

## 监听事件

### 基本用法

监听事件的基本步骤：

1. 引入事件总线和相应的事件类
2. 从事件总线获取实例
3. 使用`emplaceListener`方法注册监听器

### 示例：服务端启动完成事件

```cpp
#include "ll/api/event/EventBus.h"
#include "ll/api/event/server/ServerStartedEvent.h"

void ListenEvents() {
    using namespace ll::event;
    EventBus& bus = EventBus::getInstance();
    bus.emplaceListener<ServerStartedEvent>([](ServerStartedEvent& event) {
        // 服务端启动完成后要执行的代码
    });
}
```

## 发布事件

如果你想为你的模组或其他模组发布自己的事件，需要以下步骤：

### 1. 创建事件类

创建一个名为`ServerStartedEvent.h`的头文件，定义`ServerStartedEvent`类，继承自`ll::event::Event`：

```cpp
#pragma once

#include "ll/api/event/Event.h"
#include "mc/server/ServerInstance.h"

namespace ll::event::inline server {
class ServerStartedEvent final : public Event {
    ServerInstance& mInstance;

public:
    constexpr explicit ServerStartedEvent(ServerInstance& server) : mInstance(server) {}

    LLAPI void serialize(CompoundTag&) const override;

    LLNDAPI ServerInstance& server() const;
};
} // namespace ll::event::inline server
```

/// tip | 关于可取消的事件
如果你希望你的事件是可取消的，就继承`ll::event::Cancellable<ll::event::Event>`类。
///

### 2. 关于LLAPI宏

LeviLamina中的`LLAPI`宏本质是通过在`xmake.lua`中使用`add_defines("LL_EXPORT")`预定义`LL_EXPORT`，以实现在LeviLamina编译时`LLAPI`表示`__declspec(dllexport)`，在其他模组引用时变为`__declspec(dllimport)`。以下是一个实现这样的宏的简单示例，在实际使用中你需要将`MOD_EXPORT`和`MODAPI`改名以避免与其他模组的宏产生冲突：

```cpp
#ifdef MOD_EXPORT
#define MODAPI __declspec(dllexport)
#else
#define MODAPI __declspec(dllimport)
#endif
```

你只需要在你的模组的`xmake.lua`中添加`add_defines("MOD_EXPORT")`，然后在需要被导出的方法前面添加`MODAPI`即可导出你的模组的方法。

### 3. 实现事件类

在`ServerStartedEvent.cpp`中实现`ServerStartedEvent`类的`serialize`和`server`方法，并在事件应该被触发时调用`EventBus::publish`方法：

```cpp
#include "ll/api/event/server/ServerStartedEvent.h"
#include "ll/api/event/Emitter.h"
#include "ll/api/event/EventRefObjSerializer.h"
#include "ll/api/memory/Hook.h"

#include "mc/deps/nbt/CompoundTag.h"
#include "mc/scripting/ServerScriptManager.h"

namespace ll::event::inline server {

void ServerStartedEvent::serialize(CompoundTag& nbt) const {
    Event::serialize(nbt);
    nbt["server"] = serializeRefObj(server());
}

ServerInstance& ServerStartedEvent::server() const { return mInstance; }

LL_TYPE_INSTANCE_HOOK(
    ServerStartedEventHook,
    ll::memory::HookPriority::Normal,
    ServerScriptManager,
    &ServerScriptManager::$onServerThreadStarted,
    EventResult,
    ::ServerInstance& ins
) {
    auto result = origin(ins);
    EventBus::getInstance().publish(ServerStartedEvent(ins));
    return result;
}

static std::unique_ptr<EmitterBase> emitterFactory();
class ServerStartedEventEmitter : public Emitter<emitterFactory, ServerStartedEvent> {
    memory::HookRegistrar<ServerStartedEventHook> hook;
};

static std::unique_ptr<EmitterBase> emitterFactory() { return std::make_unique<ServerStartedEventEmitter>(); }
} // namespace ll::event::inline server
```

/// tip | 关于可取消的事件处理
如果你的事件是可取消的，你还需要通过判断`Event::isCancelled`方法的返回值来决定是否执行取消该事件的操作。
///

### 4. 注册事件发射器

如果其他模组需要在不链接你的模组的情况下使用你的模组提供的事件，可以直接将事件的成员设为`public`，或直接在头文件中实现获取方法。另外，最好在事件中声明并实现一个`serialize`方法，以方便在控制台中输出该事件的信息。

## 下一步

- 了解更多关于[表单开发](form-guide.md)
- 查看[LeviLamina API参考](../../../refs/server/levilamina-api.md)中的事件模块
- 参考[创建第一个模组](../levilamina.md#创建第一个模组)获得完整示例
