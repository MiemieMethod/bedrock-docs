# JSON组件

## format_version

基岩版自定义方块的json结构曾经过多次调整，当填写format_version时，需要按照对应版本的json结构编写components。

你可以在以下两个版本进行选择：

- 1.16.0

  该版本的components结构详见[bedrock.dev](https://bedrock.dev/zh/docs/1.16.0.0/1.16.0.66/Blocks)。

- 1.10.0

  该版本的components结构详见[bedrock.dev](https://bedrock.dev/zh/docs/1.12.0.0/1.12.0.28/Blocks)。该版本相比于1.16.0，component的值为一个Json Object，例如`minecraft:destroy_time`，在1.10.0中为

  ```json
  "minecraft:destroy_time": {
      "value": 4.0
  }
  ```

  而在更高的版本中为

  ```json
  "minecraft:destroy_time": 4.0
  ```

  

## description

| 键                      | 类型 | 默认值 | 解释                                                         |
| ----------------------- | ---- | ------ | ------------------------------------------------------------ |
| identifier              | str  |        | 包括命名空间及物品名。需要全局唯一。<br>建议使用mod名称作为命名空间 |
| register_to_create_menu | bool | false  | 是否注册到创造栏                                             |
| category                | str  | Nature | 注册到创造栏的分类，可选的值有：<br>Construction<br>Nature<br>Equipment<br>Items |
| custom_item_type        | str  |        | 自定义物品类别，可选值有：<br/>weapon<br/>armor<br/>egg<br/>ranged_weapon<br/>projectile_item |

## components

目前行为包中自定义方块json中支持的component包括原版component和网易独有的component。minecraft开头的为原版component，netease开头的为网易独有component。

对于原版component，你可以在上方的format_version解释中找到更多的参数及解释。

<span id="minecraft_loot"></span>

### minecraft:loot

可用于使用loot table控制掉落物

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks:customblocks_test_ore方块

<span id="minecraft_destroy_time"></span>

### minecraft:destroy_time

可用于控制挖掘所需的时间。该值的含义与[官方wiki](https://minecraft-zh.gamepedia.com/%E6%8C%96%E6%8E%98#.E6.96.B9.E5.9D.97.E7.A1.AC.E5.BA.A6)的“硬度”一致

主要用于[挖掘](./2-功能.md#wajue)的功能

<span id="minecraft_block_light_emission"></span>

### minecraft:block_light_emission

可用于设置方块亮度。关于亮度及方块光源可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6)

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_explosion_resistance"></span>

### minecraft:explosion_resistance

可用于设置爆炸抗性。原版方块的爆炸抗性见[官方wiki](https://minecraft-zh.gamepedia.com/%E7%88%86%E7%82%B8#.E7.88.86.E7.82.B8.E6.8A.97.E6.80.A7)

<span id="minecraft_block_light_absorption"></span>

### minecraft:block_light_absorption

可用于设置方块的透光率。具体可参考[官方wiki](https://minecraft-zh.gamepedia.com/%E4%BA%AE%E5%BA%A6#.E9.98.BB.E7.A2.8D.E5.85.89.E7.85.A7.E7.9A.84.E6.96.B9.E5.9D.97)

默认为不透光。

主要用于[亮度](./2-功能.md#liangdu)的功能

<span id="minecraft_map_color"></span>

### minecraft:map_color

可用于设置方块显示在地图上的颜色

<span id="netease_tier"></span>

### netease:tier

用于设置与挖掘相关的属性

主要用于[挖掘](./2-功能.md#wajue)的功能

|       键        |  类型  | 默认值 | 解释                                                         |
| :-------------: | :----: | :----: | :----------------------------------------------------------- |
|     digger      | string |        | 必须设置。表示方块使用此工具挖掘时有速度加成。<br>可选的值有：<br>    shovel：铲<br>    pickaxe：镐<br>    hatchet：斧 |
| destroy_special |  bool  | false  | 可选。<br>当设置为true时，表示只有使用digger设置的工具进行挖掘才会产生掉落物。 |
|      level      |  int   |   0    | 可选。<br>当destroy_special为true时才会生效。表示挖掘所需的工具等级，若手持工具等级小于该值，则不会产生掉落物。<br>原版工具的等级：<br>    空手/其他非工具物品：0<br>    木制/金制工具：0<br>    石制工具：1<br>    铁制工具：2<br>    钻石工具：3 |

<span id="netease_aabb"></span>

### netease:aabb

用于设置方块的碰撞盒

**注意事项：**

1. 无碰撞箱的方块请将collision的每个项都设置为0
2. 有碰撞箱的方块，clip的范围需要小于或等于collision的范围，否则弹射物命中时会异常
3. aabb的min不要小于[-1, -1, -1]，max不要大于[2, 2, 2]

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks_model_flower及customblocks_model_wire方块。

| 键        | 类型          | 默认值 | 解释                                                         |
| --------- | ------------- | ------ | ------------------------------------------------------------ |
| collision | object或array |        | 计算与物体碰撞时用的碰撞盒                                   |
| clip      | object或array |        | 计算射线检测时用的碰撞盒。如准心选取及弹射物碰撞。<br>（那么当该AABB没有体积时，准心与弹射物都会无视这个方块） |

当collision或clip为object时，用于表示恒定大小的单一碰撞盒，结构为：

| 键   | 类型         | 默认值    | 解释                               |
| ---- | ------------ | --------- | ---------------------------------- |
| min  | array(float) | [0, 0, 0] | min的三个值必须小于等于max的三个值 |
| max  | array(float) | [1, 1, 1] |                                    |

当collision或clip为array时，用于可变化的多个碰撞盒的组合，通常用于可变化的自定义方块模型。元素的结构为：

|        | 类型         | 默认值    | 解释                                                         |
| ------ | ------------ | --------- | ------------------------------------------------------------ |
| enable | molang       | true      | 控制是否开启该碰撞箱<br/>目前仅支持is_connect查询，详见[netease:connection](#netease_connection) |
| min    | array(float) | [0, 0, 0] | min的三个值必须小于等于max的三个值                           |
| max    | array(float) | [1, 1, 1] |                                                              |

<span id="netease_face_directional"></span>

### netease:face_directional

用于设置方块的多面向

主要用于[多面向](./2-功能.md#duomianxiang)的功能

| 键   | 类型   | 默认值 | 解释                                                  |
| ---- | ------ | ------ | ----------------------------------------------------- |
| type | string |        | direction：四面向方块<br>facing_direction：六面向方块 |

<span id="netease_render_layer"></span>

### netease:render_layer

用于设置方块渲染时使用的材质

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型   | 默认值 | 解释                                                         |
| ----- | ------ | ------ | ------------------------------------------------------------ |
| value | string |        | 目前支持的材质有：<br>opaque：不透明，即“terrain_opaque”材质。默认为此项<br>alpha：全透明，即“terrain_alpha”材质，如火焰，树叶。<br>blend：半透明，即“terrain_blend”材质，如彩色玻璃 |

<span id="netease_solid"></span>

### netease:solid

用于设置方块是否为实心方块主要与生物在方块内时是否受到窒息伤害有关。

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型 | 默认值 | 解释                                                         |
| ----- | ---- | ------ | ------------------------------------------------------------ |
| value | bool | true   | 为true时，生物在方块内会受到窒息伤害<br>为false时，生物在方块内不会受到窒息伤害 |

<span id="netease_pathable"></span>

### netease:pathable

用于设置游戏内AI在进行寻路时，方块是否被当作障碍物。

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks:customblocks_model_flower方块。

| 键    | 类型 | 默认值 | 解释                                                         |
| ----- | ---- | ------ | ------------------------------------------------------------ |
| value | bool | false  | 为true时，寻路时被当作空气<br>为false时，寻路时被当作障碍物，并且可在其上方行走 |

<span id="netease_block_entity"></span>
### netease:block_entity

用于给自定义方块添加[自定义方块实体](./4-自定义方块实体.md)。

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks:customblocks_test_block_entity方块。

| 键      | 类型 | 默认值 | 解释                                                         |
| ------- | ---- | ------ | ------------------------------------------------------------ |
| tick    | bool | false  | 为true时，当玩家进入方块tick范围时，该方块每秒会发送**20次**ServerBlockEntityTickEvent事件<br>为false时，该方块不会发送ServerBlockEntityTickEvent事件 |
| movable | bool | true   | 为true时，该方块可被粘性活塞拉回<br>为false时，该方块不可被粘性活塞拉回 |

<span id="netease_random_tick"></span>

### netease:random_tick

用于给自定义方块定义是否可以随机tick，并且设置该tick事件是否发送到脚本层。

| 键             | 类型 | 默认值 | 解释                                                         |
| -------------- | ---- | ------ | ------------------------------------------------------------ |
| enable         | bool | false  | 方块是否随机tick                                             |
| tick_to_script | bool | false  | 是否发送事件[BlockRandomTickServerEvent](../../02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#blockrandomtickserverevent)到python脚本 |

### netease:redstone_property

用于给自定义方块设置红石属性

| 键    | 类型 | 默认值 | 解释                                                         |
| ----- | ---- | ------ | ------------------------------------------------------------ |
| value | str  | None   | 目前只支持break_on_push，设置之后，方块可以被活塞破坏变成掉落物，否则，方块会被活塞推动而不破坏 |

### netease:neighborchanged_sendto_script

| 键    | 类型 | 默认值 | 解释                                                         |
| ----- | ---- | ------ | ------------------------------------------------------------ |
| value | bool | false  | 方块周围环境变化是否发送事件[BlockNeighborChangedServerEvent](../../02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#blockneighborchangedserverevent)到脚本层 |

<span id="netease_connection"></span>

### netease:connection

用于给自定义方块定义“连接”属性

使用枚举的方式配置该方块与哪些方块具有“连接”属性，并且此属性是单向的。不支持附加值。

由于方块更新的特性，“床”和“旗帜”方块在区块边缘放置时，与其他方块会出现连接失败。

可参考[CustomBlocksMod](../../../4-DEMO示例/示例简介.html#CustomBlocksMod)的customblocks_model_wire方块。

| 键     | 类型          | 解释                       |
| ------ | ------------- | -------------------------- |
| blocks | array(string) | 数组元素为方块的identifier |

目前该属性只用于[netease:aabb](#netease_aabb)及[自定义方块模型](./5-自定义方块模型.md)的is_connect查询：

| 名称             | 解释                                                         |
| ---------------- | ------------------------------------------------------------ |
| query.is_connect | 传入一个参数，返回该方块与对应临面上的方块是否有connection属性<br/>参数取值与对应的面：<br>0-down面，1-up面，2-north面，3-south面，4-west面，5-east面。 |

<span id="netease_redstone"></span>

### netease:redstone

用于配置自定义红石源与自定义红石机械元件；

可以配置自定义红石的类型，如红石源或者红石机械元件；

可以配置初始信号强度，默认为15。

| 键       | 类型 | 默认值 | 说明                                                       |
| -------- | ---- | ------ | ---------------------------------------------------------- |
| type     | str  |        | 红石类型：<br/>producer：红石源<br/>consumer：红石机械元件 |
| strength | int  | 15     | 红石信号值，范围[0,15]                                     |



<span id="listen_block_remove"></span>

### netease:listen_block_remove

用于配置自定义方块是否监听方块的[BlockRemoveServerEvent](../../02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.md#blockremoveserverevent)事件

| 键    | 类型 | 默认值 | 说明         |
| ----- | ---- | ------ | ------------ |
| value | bool | false  | 是否监听事件 |

<span id="netease_may_place_on"></span>

### netease:may_place_on

用于配置自定义方块可存在于哪些方块的上面。

会生效于玩家右键放置方块时；以及已存在的方块下方的方块发生改变时。

可参考CustomBlocksMod示例中的customblocks_model_flower

| 键              | 类型         | 默认值 | 说明                                                         |
| --------------- | ------------ | ------ | ------------------------------------------------------------ |
| block           | list(str)    |        | 方块identifier的列表。这些方块的所有[方块状态](../../02-Python脚本开发/99-ModAPI/0-名词解释.html)都可放置 |
| block_state     | list(object) |        | [方块状态](../../02-Python脚本开发/99-ModAPI/0-名词解释.html)的列表。<br>每个元素只对应一个特定的方块状态，如果方块有多个种类的状态，需要考虑排列组合的所有情况<br>最终可在上面放置的方块是block字段与block_state字段的并集 |
| spawn_resources | bool         | true   | 已存在的方块因下方的方块发生改变而被破坏时，是否生成掉落物   |

<span id="netease_fire_resistant"></span>

### netease:fire_resistant

用于配置自定义方块是否防火。

设置为防火时，方块的掉落物会与下界合金一样，不会被火烧毁，掉进岩浆时会弹走。

可参考CustomBlocksMod示例中的customblocks_test_ore

| 键    | 类型 | 默认值 | 说明     |
| ----- | ---- | ------ | -------- |
| value | bool |        | 是否防火 |