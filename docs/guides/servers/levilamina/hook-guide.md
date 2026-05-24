# 钩子系统指南

Hook是一种在运行时修改函数行为的技术，允许你在不修改源代码的情况下修改函数行为。

更多信息请参考：[Wikipedia Hooking](https://en.wikipedia.org/wiki/Hooking)

在LeviLamina中，我们提供了封装好的Hook API，使得你可以快速便捷地对Minecraft基岩专用服务器（BDS）中的游戏函数进行行为修改。

## Hook的类型

在`ll/api/memory/Hook.h`中定义了以下几种Hook宏：

| 宏 | 用途 |
|-----|------|
| `LL_TYPE_STATIC_HOOK` | 针对静态函数的Hook（手动注册） |
| `LL_STATIC_HOOK` | 简化版静态函数Hook（手动注册） |
| `LL_TYPE_INSTANCE_HOOK` | 针对成员函数的Hook（手动注册） |
| `LL_INSTANCE_HOOK` | 简化版成员函数Hook（手动注册） |
| `LL_AUTO_TYPE_STATIC_HOOK` | 自动注册的静态函数Hook |
| `LL_AUTO_STATIC_HOOK` | 简化自动静态函数Hook |
| `LL_AUTO_TYPE_INSTANCE_HOOK` | 自动注册的成员函数Hook |
| `LL_AUTO_INSTANCE_HOOK` | 简化自动成员函数Hook |

其中，AUTO标注的Hook会自动注册；TYPE标注的Hook会给你定义的类型继承到你指定的类型。

## Hook参数说明

| 参数 | 说明 |
|------|------|
| `DEF_TYPE` | 你给这个Hook起的类型名 |
| `PRIORITY` | Hook的优先级，如`ll::memory::HookPriority::Normal` |
| `TYPE` | 你定义的`DEF_TYPE`继承到的类型 |
| `IDENTIFIER` | Hook的查询函数使用的标识符（函数修饰名、字节码或函数定义） |
| `RET_TYPE` | Hook函数的返回值类型 |
| `...` | Hook函数的参数列表 |

## 简单的Hook示例

```cpp
#include "ll/api/memory/Hook.h"
#include "ll/api/io/LoggerRegistry.h"
#include "mc/server/DedicatedServer.h"

auto dedicatedServerLogger = ll::io::LoggerRegistry::getInstance().getOrCreate("DedicatedServer");

LL_AUTO_TYPE_INSTANCE_HOOK(
    DedicatedServerCtorHook,
    ll::memory::HookPriority::Normal,
    DedicatedServer,
    &DedicatedServer::$ctor,
    void*
) {
    dedicatedServerLogger->info("DedicatedServer::DedicatedServer");
    return origin();
}
```

这段代码会Hook DedicatedServer的构造函数，并在构造函数被调用时打印一条日志。

### 示例解析

1. 使用了`INSTANCE_HOOK`类型，因为构造函数是类的成员函数
2. 使用了`AUTO`标注，使得Hook在模组被加载时自动注册
3. 使用了`TYPE`标注，便于在函数体内调用DedicatedServer类型下的函数

## Hook的查询

你可以查阅LeviLamina提供的[Fake Headers](https://github.com/LiteLDev/LeviLamina/tree/develop/src/mc)来获取你想要Hook的函数的定义。

## Hook的注册和卸载

### 注册

针对非自动注册的Hook，需要在需要注册Hook的时机调用`hook()`函数进行注册。

### 卸载

所有的Hook都会在BDS卸载时自动卸载，你也可以在需要卸载Hook时调用`unhook()`函数进行卸载。

## 最佳实践

/// note | 优先级建议
一般不是特殊需求，我们不推荐过高的优先级，`Normal`即可。
///

## 写在最后

Hook是一种非常强大的技术，但也是一把双刃剑。如果使用不当，可能会导致BDS本体崩溃、模组崩溃，甚至影响存档。

因此，在使用Hook时务必谨慎，仔细检查代码，避免引入不必要的错误。

## 下一步

- 了解更多关于[协程使用](coro-guide.md)
- 查看[LeviLamina API参考](../../../refs/server/levilamina-api.md)中的内存&钩子模块
- 参考[官方Hook示例](https://github.com/LiteLDev/LeviLamina/blob/develop/src/ll/api/memory/Hook.h)
