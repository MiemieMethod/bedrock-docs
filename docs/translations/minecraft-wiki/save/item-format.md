# 基岩版存档格式——物品格式

/// details-info | 来源信息
- 原文仓库：[中文Minecraft Wiki](https://zh.minecraft.wiki)
- 许可说明：以原仓库或原站点公开许可声明为准。
///

/// details-info | 译文信息
- 原文：[基岩版存档格式/物品格式 - 中文Minecraft Wiki](https://zh.minecraft.wiki/w/基岩版存档格式/物品格式)
- 作者或组织：Minecraft Wiki 编者
- 许可：[CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
///

本页面介绍基岩版中物品NBT结构的格式，物品NBT在玩家的物品栏和末影箱等容器物品栏中使用。

## 物品堆叠

所有物品的共通数据：

/// html | div.treeview
- {{nbt|compound}}：物品的根标签。
    - {{nbt|string|Name}}：物品的ID。
    - {{nbt|byte|Count}}：物品在单个槽位里的数量。
    - {{nbt|short|Damage}}：元数据。此标签并不储存物品的损害数据（例如剑和镐的损害情况）。
    - {{nbt|boolean|WasPickedUp}}：是否被捡起过。
    - {{nbt|compound|Block}}：（可能不存在）该物品的方块形式，在放置时使用。
        - （参见[方块格式](./save-format.md)）
    - {{nbt|compound|tag}}：（可能不存在）物品的附加数据。
    - {{nbt|list|CanDestroy}}：（可能不存在）用于控制在冒险模式下这个物品能够破坏什么类型的方块。
        - {{nbt|string}}：方块的ID。
    - {{nbt|list|CanPlaceOn}}：（可能不存在）用于控制在冒险模式下这个方块可以放置在什么类型的方块的上面。
        - {{nbt|string}}：方块的ID。
///

## 常规标签

具有耐久度的物品，其伤害值存储在NBT中。此外，物品可以有自定义的显示名称及其描述。还有一个**RepairCost**标签可以跟踪物品的铁砧使用情况，使得每次使用铁砧的成本更高。

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|int|Damage}}：（可能不存在）此物品的损害数据（默认为0）。
    - {{nbt|compound|display}}：（可能不存在）显示的属性。
        - {{nbt|string|Name}}：（可能不存在）用于显示物品的JSON文本组件。
        - {{nbt|list|Lore}}：（可能不存在）显示为物品描述的字符串列表。
            - {{nbt|string}}：（可能不存在）物品的描述。
    - {{nbt|int|RepairCost}}：（可能不存在）使用铁砧修复、合并或重命名此物品时，要添加到基础等级成本中的经验等级数量。
    - {{nbt|byte|minecraft:item_lock}}：控制物品是否锁定在物品栏内，锁定的物品无法合成、丢弃、移除等。1与2分别代表锁定在槽位里无法取出与锁定在物品栏里。
    - {{nbt|byte|minecraft:keep_on_death}}：1为死后不会掉落。
    - {{nbt|byte|Unbreakable}}：（可能不存在）该值为1时，物品不会消耗耐久度。和Java版不同，存在该值的物品不会在提示框中显示"无法破坏"，在不使用外部工具的情况下无法正常获取。
///

## 附魔标签

与Java版不同，基岩版只有一种办法储存物品的魔咒NBT：已经附魔的物品都共享一个{{nbt|list|ench}}标签。它存储了物品的魔咒。

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|list|ench}}：包含了物品附有的魔咒。
        - {{nbt|compound}}：单个魔咒。
            - {{nbt|short|id}}：魔咒的ID。参见魔咒ID。
            - {{nbt|short|lvl}}：魔咒的等级。
///

## 生物桶

生物桶的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|boolean|AppendCustomName}}：实体颜色、状态和ID是否用于生成桶物品的名称，默认为true。
    - {{nbt|string|CustomName}}：（可能不存在）桶内实体的自定义名称，用于生成桶的名称。
    - {{nbt|string|ColorID}}：（可能不存在）颜色的本地化键名，用于生成桶的名称。
    - {{nbt|string|Color2ID}}：（可能不存在）第二种颜色的本地化键名，用于生成桶的名称。
    - {{nbt|string|BodyID}}：（可能不存在）桶内实体的状态，用于生成桶的名称。
    - {{nbt|string|GroupName}}：（可能不存在）未知。用于生成桶的名称。
    - （参见[实体格式](./entity-format.md)）
    - 鱼或美西螈实体特有的附加标签。
///

## 磁石指针

磁石指针的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|int|trackingHandle}}：磁石指针所跟踪的磁石的ID。
///

## 填充的地图

填充的地图的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|boolean|map_is_init}}：是否为创建世界时提供的初始地图。
    - {{nbt|long|map_uuid}}：地图的UUID。
    - {{nbt|int|map_name_index}}：地图名称的索引。
    - {{nbt|boolean|map_display_players}}：（可能不存在）地图是否显示玩家标记。
    - {{nbt|int|map_scale}}：地图的缩放等级。值为0-3。
    - {{nbt|boolean|map_is_scaling}}：地图是否经过缩放处理。
///

## 马铠

马铠的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|int|customColor}}：（可能不存在）皮革马铠的自定义颜色。
///

## 荧光棒

荧光棒的附加字段：

/// html | div.treeview
- {{nbt|compound}}：父级标签。
    - {{nbt|long|active_time}}：（可能不存在）荧光棒激活后的剩余发光时间。
///

## 旗帜

旗帜的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|int|Type}}：（可能不存在）0为普通旗帜，1为不祥旗帜。
    - {{nbt|list|Patterns}}：旗帜的图案列表。
        - {{nbt|compound}}：单个图案。
            - {{nbt|string|Pattern}}：图案的ID。参见方块实体。
            - {{nbt|int|Color}}：图案的颜色。参见方块实体。
///

## 盾牌

盾牌的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|int|Base}}：（可能不存在）盾牌上旗帜的颜色。参见物品数据。
    - {{nbt|list|Patterns}}：盾牌上旗帜的图案列表。
        - {{nbt|compound}}：单个图案。
            - {{nbt|string|Pattern}}：图案的ID。
            - {{nbt|int|Color}}：图案的颜色。
///

## 烟花火箭

烟花火箭的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|compound|Fireworks}}：烟花火箭的效果。
        - {{nbt|list|Explosions}}：烟花火箭的爆裂组合的组件列表。
            - {{nbt|compound}}：爆裂效果。
                - （参见[其他数据格式——烟花火箭爆裂](./other-data-format.md)）
        - {{nbt|byte|Flight}}：表示烟花的飞行时间（等于合成烟花火箭所用的火药数量）。可以是-128到127之间的任何值。
///

## 烟火之星

烟火之星的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|compound|FireworksItem}}：烟火之星提供的爆裂效果。
        - （参见[其他数据格式——烟花火箭爆裂](./other-data-format.md)）
    - {{nbt|int|customColor}}：烟火之星的颜色。
///

## 成书

成书的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|string|author}}：书的作者。
    - {{nbt|string|title}}：书的标题。
    - {{nbt|long|xuid}}：书的ID。
    - {{nbt|list|pages}}：书的页码列表。
        - {{nbt|compound}}：书的单页。
            - {{nbt|string|text}}：此页的文本内容。
            - {{nbt|string|photoname}}：书上的图片的名称。
    - {{nbt|int|generation}}：书的副本。0表示原本，1表示副本，2表示副本的副本，3表示残损副本。
///

## 书与笔

书与笔的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|list|pages}}：书的页码列表。
        - {{nbt|compound}}：书的单页。
            - {{nbt|string|text}}：此页的文本内容。
            - {{nbt|string|photoname}}：书上的图片的名称。
///

## 容器

容器的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|list|Items}}：容器内的物品列表。
        - {{nbt|compound}}：物品及其槽位标签。
            - {{nbt|byte|Slot}}：物品所在的槽位编号。
            - （参见[物品堆叠](#物品堆叠)）
///

## 弩

弩的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|compound|chargedItem}}：弩所装填的物品。
        - （参见[物品堆叠](#物品堆叠)）
///

## 药水

药水的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|boolean|wasJustBrewed}}：（可能不存在）药水是否通过酿造获得。
///

## 盔甲纹饰

盔甲纹饰的附加字段：

/// html | div.treeview
- {{nbt|compound|tag}}：父级标签。
    - {{nbt|compound|Trim}}：盔甲纹饰的属性。
        - {{nbt|string|Material}}：盔甲纹饰的材料。
        - {{nbt|string|Pattern}}：盔甲纹饰的图案。
///
