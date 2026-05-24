# 中国版ModAPI枚举值索引<!-- md:flag china -->


/// warning | 使用边界
这些枚举值用于中国版模组SDK接口参数与返回值。不要将其直接映射为国际版脚本API的枚举对象。
///

## 使用入口

资料索引指出，枚举值可通过`GetMinecraftEnum`接口获取。该能力属于中国版模组SDK通用工具接口体系。

## 枚举值分组

| 分组 | 代表枚举值 |
| --- | --- |
| 实体与玩家 | `ActorDamageCause`、`AttrType`、`AttributeBuffType`、`EntityType`、`EntityComponentType`、`PlayerActionType`、`GameType`、`GameDiffculty` |
| 方块与物品 | `BlockBreathability`、`ContainerType`、`ItemCategory`、`ItemPosType`、`SetBlockType`、`RedstoneModeType`、`CommandBlockType` |
| 渲染与动画 | `RenderLayer`、`RenderControllerArrayType`、`AnimationModeType`、`UseAnimation`、`MirrorModeType`、`TimeEaseType` |
| UI与输入 | `UICategory`、`UiBaseLayer`、`OriginGUIName`、`OpenContainerId`、`PlayerUISlot`、`ButtonEventType`、`TouchEvent`、`GamepadKeyType`、`KeyBoardType` |
| 世界与结构 | `BiomeType`、`StructureFeatureType`、`Facing`、`VirtualWorldObjectType` |
| 物理与反作弊 | `PxActorFlag`、`PxEventMask`、`PxForceMode`、`PxRigidBodyFlag`、`PxRigidDynamicLockFlag`、`AniCheatMove`、`AniCheatMoveRewind` |

## 完整枚举名录（按资料索引顺序）

`ActorDamageCause`、`AniCheatBlockBreak`、`AniCheatConsts`、`AniCheatMove`、`AniCheatMoveRewind`、`AnimationModeType`、`ArmorSlotType`、`AttrType`、`AttributeBuffType`、`BiomeType`、`BlockBreathability`、`BrewingStandSlotType`、`ButtonEventType`、`ButtonState`、`CatVariantType`、`Change`、`ColorCode`、`CommandBlockType`、`ConditionType`、`ContainerType`、`EffectType`、`EnchantSlotType`、`EnchantType`、`EntityColorType`、`EntityComponentType`、`EntityTeleportCause`、`EntityType`、`Facing`、`FoxType`、`GameDiffculty`、`GameType`、`GamepadKeyType`、`HorseSpotType`、`HorseType`、`InputMode`、`InventoryType`、`ItemAcquisitionMethod`、`ItemCategory`、`ItemColor`、`ItemPosType`、`ItemUseMethodEnum`、`KeyBoardType`、`MirrorModeType`、`OpenContainerId`、`OptionId`、`OriginGUIName`、`PermissionChangeCause`、`PlayerActionType`、`PlayerExhauseRatioType`、`PlayerUISlot`、`PxActorFlag`、`PxEventMask`、`PxForceMode`、`PxRigidBodyFlag`、`PxRigidDynamicLockFlag`、`RayFilterType`、`RedstoneModeType`、`RenderControllerArrayType`、`RenderLayer`、`SetBlockType`、`ShapeType`、`SliderOptionId`、`StructureFeatureType`、`TimeEaseType`、`TouchEvent`、`TradeLevelType`、`TransferServerFailReason`、`UICategory`、`UiBaseLayer`、`UseAnimation`、`VillagerClothingType`、`VirtualWorldObjectType`、`WalkState`。

## 相关页面

- 接口域总览：见[中国版ModAPI接口域索引](modapi-interface-index.md)。
- 事件域总览：见[中国版ModAPI事件域索引](modapi-event-index.md)。
- 世界控制接口：见[世界控制接口](world-control.md)。