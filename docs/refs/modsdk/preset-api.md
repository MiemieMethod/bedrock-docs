# 中国版PresetAPI参考<!-- md:flag china -->


## 目录覆盖

| 子目录 | 文件数 | 说明 |
| --- | ---: | --- |
| `预设管理` | 1 | `PresetApi`入口函数。 |
| `预设对象\零件` | 9 | 零件生命周期、触发器、导航点、相机轨迹等。 |
| `预设对象\通用` | 5 | 变换、游戏对象、素材数据和SDK封装。 |
| `预设对象\预设` | 11 | 实体、玩家、方块、特效、界面和文字面板相关预设对象。 |
| `更新信息` | 13 | `1.23.0`至`2.4.0`版本变更记录。 |

## PresetApi入口接口


| 接口 | 作用 |
| --- | --- |
| `CreateTransform` | 构造坐标变换对象。 |
| `GetAllPresets` | 获取预设列表。 |
| `GetBlockPresetByPosition` | 获取指定位置的方块预设。 |
| `GetGameObjectByEntityId` / `GetGameObjectById` | 按实体ID或对象ID查询游戏对象。 |
| `GetGameObjectByTypeName` / `GetGameObjectsByTypeName` | 按类型与名称查询单个或多个游戏对象。 |
| `GetPartApi` | 获取零件API入口。 |
| `GetPresetByName` / `GetPresetsByName` | 按名称查询单个或多个预设。 |
| `GetPresetByType` / `GetPresetsByType` | 按类型查询单个或多个预设。 |
| `GetPresetSize` | 按预设ID查询包围盒大小。 |
| `GetTickCount` | 获取当前帧数。 |
| `LoadPartByModulePath` / `LoadPartByType` | 通过模块路径或类型名加载零件。 |
| `SpawnPreset` | 在指定维度与变换位置生成预设。 |

## 预设对象模型

### 零件对象

| 对象文件 | 接口数（不含“概述/索引”） | 说明 |
| --- | ---: | --- |
| `零件PartBase.md` | 43 | 零件生命周期、事件收发、组件创建、调试与对象查询主入口。 |
| `零件事件PartEvent.md` | 3 | 触发器进入、停留、离开事件定义。 |
| `触发器零件TriggerPart.md` | 1 | 触发器内实体查询。 |
| `导航路径零件NavPointsPart.md` | 2 | 导航点列表与导航半径读取。 |
| `相机轨迹CameraTrackPart.md` | 4 | 相机轨迹播放、暂停、继续与停止。 |
| `实体零件EntityBasePart.md` | 2 | 虚拟实体创建与销毁。 |

### 通用对象

| 对象文件 | 接口数（不含“概述/索引”） | 说明 |
| --- | ---: | --- |
| `变换对象TransformObject.md` | 44 | 预设树节点变换、节点遍历、父子关系操作。 |
| `SDK接口封装SdkInterface.md` | 330 | 面向模组SDK的高密度封装接口集合。 |
| `坐标变换Transform.md` | 5 | 位置、旋转、缩放叠加与变换矩阵计算。 |
| `游戏对象GameObject.md` | 2 | 对象基础加载与字典构造。 |

### 预设对象

| 对象文件 | 接口数（不含“概述/索引”） | 说明 |
| --- | ---: | --- |
| `实体对象EntityObject.md` | 94 | 实体对象的位置、旋转、状态、行为与外观控制。 |
| `玩家对象PlayerObject.md` | 38 | 玩家对象属性、动作、视角、输入与状态接口。 |
| `预设基类PresetBase.md` | 22 | 预设树管理、子预设操作、素材绑定与复制。 |
| `文字面板对象TextboardObject.md` | 9 | 文本、颜色、缩放与绑定对象控制。 |
| `特效对象EffectObject.md` | 7 | 特效播放、绑定、循环与深度测试控制。 |
| `界面预设UIPreset.md` | 5 | UI激活、显示与界面节点访问。 |

## 更新信息概览


| 版本 | 新增条目数 | 调整条目数 | 说明 |
| --- | ---: | ---: | --- |
| `1.23.0` | 126 | 0 | 初始大规模接口投放阶段。 |
| `1.23.1` | 382 | 0 | 扩展`SdkInterface`与对象能力。 |
| `1.23.2` | 9 | 0 | 小规模增量扩展。 |
| `1.23.3` | 8 | 0 | 小规模增量扩展。 |
| `1.23.4` | 110 | 0 | 功能密集补充。 |
| `1.24.0` | 12 | 0 | 增加玩家、实体与系统事件相关能力。 |
| `1.24.1` | 14 | 0 | 增量扩展。 |
| `1.25.0` | 9 | 0 | 增量扩展。 |
| `2.0.1` | 3 | 0 | 2.x初始补充。 |
| `2.0.2` | 36 | 0 | 明显扩展阶段。 |
| `2.0.3` | 17 | 0 | 增量扩展。 |
| `2.2.0` | 1 | 0 | 小规模补丁。 |
| `2.4.0` | 3 | 9 | 引入`dimension`参数与`GetPresetSize`等接口调整。 |

## 相关页面

- [中国版ModAPI接口域索引](modapi-interface-index.md)
- [中国版ModAPI事件域索引](modapi-event-index.md)
- [中国版ModAPI枚举值索引](modapi-enum-index.md)
- [模组SDK版本更新索引](version-update.md)