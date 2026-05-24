---
title: 常见问题
---

# 常见问题

## LeviLamina来自哪里？

LeviLamina源自Minecraft基岩版服务端的逆向分析与注入式模组加载生态，最初继承自LiteLoaderBDS。

## 为什么LiteLoaderBDS更名为LeviLamina？

因为旧项目逐渐膨胀、耦合度提高，维护成本上升，所以项目从头重构，并保留`ll`缩写后更名为LeviLamina。

## LeviLamina属于官方BDS吗？

不属于。它是运行在BDS进程内的第三方模组加载器，依赖BDS版本、平台、网络协议和二进制接口，但并不是Mojang提供的原生插件系统。

## 为什么要先看版本支持表？

因为LeviLamina与BDS或客户端版本强绑定。版本不匹配通常会直接表现为启动失败、依赖诊断报错或连接兼容性错误。
