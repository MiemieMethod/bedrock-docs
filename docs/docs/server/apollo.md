# Apollo网络服<!-- md:flag china -->

**Apollo网络服（Apollo Network Server）**是中国版《我的世界》历史上的一套网络游戏集群开发与部署体系。它把大厅服、游戏服、控制服、功能服、插件能力与运维入口整合在同一工作流中，用于支撑中国版网络游戏的开发、测试、审核与上架。

## 概述

Apollo面向的是“多服协同”的网络游戏形态，而非单进程的普通基岩版专用服务器。旧版，开发者通常通过MC Studio创建网络服工程，在开发机上部署多角色服务，再通过平台流程完成提审和上线。

Apollo是中国版独有生态能力，字段命名、部署流程、审核环节和接口分层均不适用于国际版BDS、Realm或国际版脚本API。

## 角色分层

Apollo旧版资料通常把服务分为以下角色：

| 角色 | 典型职责 |
| --- | --- |
| 大厅服 | 玩家登录落点、房间入口、玩法分流。 |
| 游戏服 | 承载具体玩法逻辑与地图实例。 |
| 控制服 | 管理配置、运维控制与部分平台能力。 |
| 功能服 | 承载共享业务能力与通用服务逻辑。 |
| 代理与通信层 | 负责跨服路由、消息转发与集群通信。 |

这种分层使网络游戏可以在功能、负载和运维上解耦，但也意味着工程复杂度和部署门槛显著高于单服方案。

## 生命周期

在旧版流程中，Apollo项目通常经历以下阶段：

1. 入驻并开通网络服开发权限。
2. 选择模板或导入工程，建立大厅服与游戏服结构。
3. 在开发机完成配置、部署、联调与性能观测。
4. 提交测试服审核并按反馈修正。
5. 申请正式服、演练发布并完成上架。
6. 在运营期持续维护日志、监控、插件与活动配置。

流程中的“提审”“正式服”“上架”属于中国版平台治理环节，不应外推到国际版教程。

## 与模组SDK

Apollo常与中国版模组SDK配合使用。旧版文档把接口拆分为事件域、接口域和枚举值，并按大厅服、游戏服、控制服、功能服与公共能力划分。相关接口清单见中国版模组SDK参考中的Apollo条目：

- [Apollo网络服事件](../../refs/modsdk/apollo-events.md)
- [Apollo控制服接口](../../refs/modsdk/apollo-control-api.md)
- [Apollo功能服接口](../../refs/modsdk/apollo-service-api.md)
- [Apollo大厅与游戏服接口](../../refs/modsdk/apollo-lobby-game-api.md)
- [Apollo公共接口](../../refs/modsdk/apollo-common-api.md)
- [Apollo服务器通信接口](../../refs/modsdk/apollo-communication-api.md)
- [Apollo运营指令](../../refs/modsdk/apollo-op-commands.md)
- [Apollo启动器信息接口](../../refs/modsdk/apollo-launcher-api.md)
- [Apollo插件生态](../../refs/modsdk/apollo-plugin-ecosystem.md)

## 与旧版资料维护

当旧工程中出现网络服模板目录、多角色服务配置、提审记录、运营指令路径或Apollo插件依赖时，通常需要按历史语境维护。若项目目标是当前国际版服务端生态，应优先评估迁移到BDS与对应插件生态，而不是直接复用Apollo旧流程。