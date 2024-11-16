---
title: 脚本监视器
category: 文档
tags:
  - 实验性
mentions:
  - JaylyDev
  - SmokeyStack
  - ThomasOrs
description: 脚本监视器是一个性能系统，默认在Minecraft脚本插件中启用。
---

脚本监视器是一个性能系统，默认在Minecraft脚本插件中启用。

## 脚本监视器配置

自1.19.20版本以来，有一组脚本监视器配置用于管理脚本环境的性能。这些选项无法在世界或领域中修改，但可以通过[专用服务器](https://www.minecraft.net/en-us/download/server/bedrock)中的`server.properties`进行修改。以下是默认的脚本监视器设置，这些设置在所有设备的世界和领域中都是相同的。

<CodeHeader>bedrock-server/server.properties</CodeHeader>

```ini
# 启用脚本监视器（默认 = true）
script-watchdog-enable=true

# 设置单次滴答挂起的监视器阈值（默认 = 3000 ms）
script-watchdog-hang-threshold=3000

# 设置单次滴答尖峰的监视器阈值（默认 = 100 ms）
script-watchdog-spike-threshold=100

# 设置多次滴答的慢脚本监视器阈值（默认 = 2ms）
script-watchdog-slow-threshold=2

# 当内存使用量超过给定阈值（以兆字节为单位）时保存并关闭世界。
# 将此值设置为0将禁用限制。（默认 = 250）
script-watchdog-memory-limit=250

# 当内存使用量超过给定阈值（以兆字节为单位）时生成内容日志警告。
# 将此值设置为0将禁用警告。（默认 = 100）
script-watchdog-memory-warning=100

# 通过events.beforeWatchdogTerminate事件启用监视器异常处理（默认 = true）
script-watchdog-enable-exception-handling=true

# 在发生未处理的监视器异常时启用服务器关闭（默认 = true）
script-watchdog-enable-shutdown=true

# 当发生挂起时抛出关键异常（默认 = true）
script-watchdog-hang-exception=true
```

## 脚本监视器消息

这些脚本监视器消息以`[Watchdog]`标签形式抛出，显示为警告或错误。这些错误绝不能被忽视。

### 在行为包'%s'中检测到慢运行脚本（平均x ms）

脚本运行时间延迟超过某个时间范围。

### 在行为包'%s'中检测到x ms脚本尖峰

脚本运行时间出现尖峰。

### 在行为包'%s'中检测到内存不足异常

当内存使用量超过限制时会发生此错误。

这将通过脚本监视器终止保存并关闭世界，无法通过`BeforeWatchdogTerminateEvent`取消。

### 在行为包'%s'中检测到x ms脚本挂起

脚本在某个位置冻结超过单次滴答的监视器阈值。

这通常是由于迭代造成的，例如`while`循环和`for`循环。

### 在行为包'%s'中检测到堆栈溢出

当存在没有出口的递归函数（调用自身的函数）时发生。

### 检测到高内存使用

当内存使用量超过给定阈值（以兆字节为单位）时生成内容日志警告。

### 在行为包'%s'中检测到未处理的关键异常'%s'

当发生未处理的关键异常时生成内容日志错误。

监视器决定终止行为包脚本执行的原因有多种。

-   `hang`：脚本由于挂起或无限循环而无响应。
-   `stackOverflow`：长时间且可能无限的函数调用链。

## 取消监视器终止

使用Minecraft的脚本API，你可以连接到一个回调，当脚本运行因违反性能监视器系统而被终止时将被调用。

此事件允许你取消脚本运行的终止，以防止监视器停止服务器运行。请注意，根据服务器配置设置，可能不允许取消终止。

```js
import { system } from '@minecraft/server';

system.events.beforeWatchdogTerminate.subscribe((event) => {
  event.cancel = true;
  console.warn(`[Watchdog] 取消了关键异常类型'${event.cancelationReason}'`);
});
```

## 脚本监视器命令

脚本监视器实现了Minecraft的斜杠命令，可以使用`/script watchdog`命令。

-   `/script watchdog exportstats`：导出脚本环境的性能分析，包括插件句柄和运行时信息。

---

[原始来源](https://github.com/JaylyDev/ScriptAPI/blob/main/docs/MinecraftApi/Watchdog.md)