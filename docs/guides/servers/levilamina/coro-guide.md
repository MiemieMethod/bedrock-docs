# 协程使用指南

LeviLamina提供了C++20协程支持，允许你编写异步非阻塞的代码。

## 基础概念

协程(Coroutine)是一种编程工具，允许你暂停和恢复函数的执行。LeviLamina的协程支持基于C++20标准，提供了任务、生成器和执行器等高层抽象。

## 协程任务

`CoroTask`是最常用的协程类型，用于处理异步任务。

```cpp
#include "ll/api/coro/CoroTask.h"
#include "ll/api/thread/ServerThreadExecutor.h"

ll::coro::CoroTask<int> asyncTask() {
    // 异步操作
    co_return 42;
}

void startTask() {
    auto task = asyncTask();
    task.launch(ll::thread::ServerThreadExecutor::getDefault());
}
```

## 等待操作

使用`co_await`暂停协程执行，直到某个操作完成。

```cpp
#include "ll/api/chrono/GameChrono.h"
#include "ll/api/coro/CoroTask.h"

ll::coro::CoroTask<void> delayedTask() {
    // 等待20个游戏刻
    co_await ll::chrono::ticks{20};
    
    // 代码将在20刻后执行
}
```

## 线程安全

当访问Minecraft游戏对象时，必须在服务器线程中执行。使用`ServerThreadExecutor`确保线程安全。

```cpp
#include "ll/api/service/Bedrock.h"
#include "ll/api/thread/ServerThreadExecutor.h"

ll::coro::CoroTask<void> gameAwareTask() {
    // 在服务器线程中访问级别和玩家
    auto level = ll::service::getLevel();
    if (level) {
        auto players = level->getPlayers();
        // 处理玩家...
    }
    co_return;
}
```

## 常见模式

### 周期性任务

```cpp
#include "ll/api/chrono/GameChrono.h"

ll::coro::CoroTask<void> periodicTask() {
    while (true) {
        // 执行某些操作
        co_await ll::chrono::ticks{100};  // 每100刻执行一次
    }
}
```

### 错误处理

```cpp
ll::coro::CoroTask<void> errorHandlingTask() {
    try {
        // 异步操作
    } catch (const std::exception& e) {
        // 处理异常
    }
    co_return;
}
```

## 下一步

- 了解更多关于[国际化支持](i18n-guide.md)
- 查看[LeviLamina API参考](../../refs/server/levilamina-api.md)中的协程模块
- 参考[游戏时间](../../refs/server/levilamina-api.md)用于时间相关操作
