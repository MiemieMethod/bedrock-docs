# 数据驱动

数据驱动就是用JSON、图片、声音、模型和其他静态文件告诉游戏“这个内容应该怎样工作”。从这一章开始，你会把附加包从“能加载”推进到“能添加玩法内容”。

## 先理解文件放在哪里

官方资料反复强调：基岩版只会在约定目录中读取约定类型的文件。文件内容写对了但放错位置，游戏通常会直接忽略它。

常用行为包目录如下：

/// html | div.treeview
- `demo_BP`
    - `blocks`：方块服务端定义。
    - `entities`：实体服务端定义。
    - `features`：地物定义。
    - `feature_rules`：地物规则。
    - `functions`：函数文件。
    - `items`：物品服务端定义。
    - `loot_tables`：战利品表。
    - `recipes`：配方。
    - `spawn_rules`：实体生成规则。
    - `structures`：结构文件。
    - `texts`：语言文件。
///

常用资源包目录如下：

/// html | div.treeview
- `demo_RP`
    - `animation_controllers`：客户端动画控制器。
    - `animations`：客户端动画。
    - `attachables`：附着物定义。
    - `entity`：客户端实体定义。
    - `fogs`：迷雾定义。
    - `models`：几何体。
    - `particles`：粒子特效。
    - `render_controllers`：渲染控制器。
    - `sounds`：声音文件和声音定义。
    - `textures`：纹理和图集定义。
///

## 本章的学习顺序

1. [认识格式版本](format-version.md)：先了解`format_version`字段的意义，避免后续踩坑。
2. [制作模型](creating-models.md)：学会用Blockbench导出几何体和纹理。
3. [认识Molang](understanding-molang.md)：理解动画、粒子和渲染条件中常见的表达式。
4. 自定义实体、方块、物品：学习最常见的三种内容。
5. 粒子、声音、配方、战利品表：给内容补上反馈和玩法循环。
6. 迷雾、地物、生物群系、维度、功能域：进入世界生成和环境效果。

## 每次新增内容都这样检查

- 标识符是否带命名空间。
- `format_version`是否与目标文件类型匹配。
- 文件夹名称是否正确。
- 资源包和行为包是否都已激活。
- 资源引用是否去掉扩展名，例如纹理路径写`textures/items/coin`而不是`textures/items/coin.png`。
- 语言键是否已经写入`texts/en_US.lang`。

如果你不确定一个组件或字段是否存在，先查参考文档或样例包，不要靠猜。很多数据驱动字段在旧版本中存在兼容写法，在新版本中又可能有新的推荐写法。