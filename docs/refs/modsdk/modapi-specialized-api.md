# 中国版ModAPI特化接口<!-- md:flag china -->


## 覆盖范围

| 接口域 | 来源文件 | 说明 |
| --- | --- | --- |
| 成就 | `接口\成就.md` | 联机大厅成就存储读写接口。 |
| 联机大厅 | `接口\联机大厅.md` | 玩家UID、大厅存储与大厅商品信息接口。 |
| 商城 | `接口\商城.md` | 中国版商城入口与界面开关接口。 |
| 山头服务器 | `接口\山头服务器.md` | 山头服务器宿主玩家UID查询接口。 |
| 物理 | `接口\物理.md` | PhysX刚体、碰撞体、力学与射线接口。 |
| 模型 | `接口\模型.md` | 自由模型创建、绑定、动画与材质控制接口。 |
| 虚拟世界 | `接口\虚拟世界\*.md` | 客户端虚拟世界、相机、模型与对象绑定接口。 |

## 平台大厅与商城接口

| 接口域 | 代表接口 | 作用 |
| --- | --- | --- |
| 成就 | `LobbyGetAchievementStorage`、`LobbySetAchievementStorage` | 读取与写入大厅成就存储。 |
| 联机大厅 | `LobbyGetStorage`、`LobbyGetStorageBySort`、`LobbySetStorageAndUserItem`、`QueryLobbyUserItem` | 管理大厅侧玩家存储与大厅商品关联数据。 |
| 联机大厅 | `GetPlayerUid` | 从玩家实体ID查询平台UID。 |
| 商城 | `OpenShopWindow`、`OpenItemDetailWindow`、`CloseShopWindow`、`ShowShopGate`、`HideShopGate` | 控制商城界面与商城入口显示。 |
| 山头服务器 | `GetHostPlayerUid` | 获取山头服务器宿主玩家UID。 |

## 物理接口

`接口\物理.md`共收录15个接口，主要围绕PhysX活动对象生命周期与受力控制。

| 能力分组 | 代表接口 |
| --- | --- |
| 活动对象创建 | `CreatePxActor` |
| 几何体构建 | `AddBoxGeometry`、`AddSphereGeometry`、`AddCapsuleGeometry`、`AddBoxTrigger` |
| 施力与姿态 | `AddForce`、`AddForceAtPos`、`AddForceAtPosLocal`、`SetGlobalPose`、`SetKinematicTarget` |
| 标志位与约束 | `SetActorFlag`、`SetRigidBodyFlag`、`SetRigidDynamicLockFlags` |
| 计算工具 | `Raycast`、`GetQuaternion` |

## 自由模型接口

`接口\模型.md`为高密度接口页，包含模型创建、绑定、动画、材质、纹理、透明度与可见性控制。该页部分标题是“当需要自由模型时，建议使用LevelId”提示语，不是独立接口名称。

| 能力分组 | 代表接口 |
| --- | --- |
| 创建与销毁 | `CreateFreeModel`、`RemoveFreeModel`、`ResetModel` |
| 绑定关系 | `BindModelToEntity`、`BindModelToModel`、`BindItemToBone`、`UnBindModelToEntity`、`UnBindModelToModel` |
| 动画控制 | `PlayAnim`、`ModelPlayAni`、`ModelStopAni`、`SetAnimLayer`、`SetAnimSpeed` |
| 动画融合 | `RegisterAnim1DControlParam`、`RegisterAnim1DMultiControlParam`、`SetAnim1DControlParam`、`SetAnim1DMultiControlParam` |
| 外观与材质 | `SetModel`、`SetModelMaterial`、`SetModelTexture`、`SetTexture`、`SetBrightness`、`SetEntityOpacity` |
| 变换控制 | `SetFreeModelPos`、`SetFreeModelRot`、`SetFreeModelScale`、`SetModelOffset` |

## 虚拟世界接口

虚拟世界接口集中在客户端`CreateVirtualWorld(levelId)`组件，分为世界、相机、模型、对象四组。

### 世界

| 接口 | 作用 |
| --- | --- |
| `VirtualWorldCreate` / `VirtualWorldDestroy` | 创建或销毁虚拟世界。 |
| `VirtualWorldToggleVisibility` | 切换虚拟世界可见性。 |
| `VirtualWorldSetSkyBgColor` / `VirtualWorldSetSkyTexture` | 设置天空背景色与天空贴图。 |
| `VirtualWorldSetCollidersVisible` | 显示或隐藏模型包围盒（调试用途）。 |

### 相机

| 接口 | 作用 |
| --- | --- |
| `CameraSetPos`、`CameraGetPos` | 设置或读取相机位置。 |
| `CameraLookAt` | 设置相机朝向目标点。 |
| `CameraMoveTo`、`CameraStopActions` | 以插值方式移动相机并可中断。 |
| `CameraSetFov`、`CameraGetFov` | 设置或读取视野角。 |
| `CameraSetZoom`、`CameraGetZoom` | 设置或读取缩放值。 |
| `CameraGetClickModel` | 查询相机当前选中的模型ID。 |

### 模型与对象

| 接口域 | 代表接口 | 作用 |
| --- | --- | --- |
| 虚拟世界模型 | `ModelCreateObject`、`ModelCreateMinecraftObject`、`ModelRemove` | 创建或销毁虚拟世界模型。 |
| 模型变换 | `ModelSetPos`、`ModelSetRot`、`ModelSetScale`、`ModelMoveTo`、`ModelRotateTo` | 控制模型位置、旋转、缩放和插值移动。 |
| 模型动画 | `ModelPlayAnimation`、`ModelStopAnimation`、`ModelSetAnimLayer`、`ModelSetAnimBoneMask` | 控制虚拟世界模型动画播放与骨骼遮罩。 |
| 其他对象 | `BindModel`、`MoveToVirtualWorld` | 将序列帧、粒子、文字面板或模型绑定到模型，或移动到虚拟世界。 |

## 相关页面

- [中国版ModAPI接口域索引](modapi-interface-index.md)
- [UI与交互接口](modapi-ui-api.md)
- [特效接口](modapi-effects-api.md)
- [中国版PresetAPI参考](preset-api.md)