# <span id="Minecraft枚举值文档"></span>Minecraft枚举值文档


Minecraft中不同的枚举类型，使用GetMinecraftEnum接口获取

<span id="ActorDamageCause"></span>
## ActorDamageCause

- 描述

    描述实体伤害来源枚举值，及实体被伤害的原因。

```python
class ActorDamageCause(object):
	NONE                = "none"               # 其他
	Override            = "override"           # 非正常方式（如脚本直接设置血量为0）
	Contact             = "contact"            # 接触伤害（如仙人掌）
	EntityAttack        = "entity_attack"      # 生物攻击
	Projectile          = "projectile"         # 抛射物攻击
	Suffocation         = "suffocation"        # 窒息（密封空间）
	Fall                = "fall"               # 掉落
	Fire                = "fire"               # 着火
	FireTick            = "fire_tick"          # 连续着火（生物着火、在火中）
	Lava                = "lava"               # 熔岩
	Drowning            = "drowning"           # 溺水
	BlockExplosion      = "block_explosion"    # 方块爆炸
	EntityExplosion     = "entity_explosion"   # 生物爆炸
	Void                = "void"               # 虚空
	Suicide             = "suicide"            # 自杀（kill命令）
	Magic               = "magic"              # 尖牙对生物造成的伤害、守卫者对生物造成的魔法伤害和药水伤害等
	Wither              = "wither"             # 凋零 poison
	Starve              = "starve"             # 饥饿
	Anvil               = "anvil"              # 下落的铁砧
	Thorns              = "thorns"             # 荆棘反弹伤害
	FallingBlock        = "falling_block"      # 下落的方块（除了铁砧）
	Piston              = "piston"             # 活塞
	FlyIntoWall         = "fly_into_wall"      # 滑翔（撞墙）
	Magma               = "magma"              # 岩浆（如站在岩浆方块上）
	Fireworks           = "fireworks"          # 烟花
	Lightning           = "lightning"          # 闪电
``` 

<span id="ArmorSlotType"></span>
## ArmorSlotType

- 描述

    描述盔甲槽位枚举值

```python
class ArmorSlotType(object):
	DEFAULT = -1
	HEAD = 0
	BODY = 1
	LEG = 2
	FOOT = 3
``` 

<span id="AttrType"></span>
## AttrType

- 描述

    描述属性枚举值，用于[attr属性组件](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#attr)

- 备注
    - ABSORPTION: 伤害吸收效果的量化值，详见wiki文档：[伤害吸收](https://minecraft-zh.gamepedia.com/index.php?title=%E4%BC%A4%E5%AE%B3%E5%90%B8%E6%94%B6&variant=zh)

```python
class AttrType(object):
	HEALTH = 0
	SPEED = 1
	DAMAGE = 2
	UNDERWATER_SPEED = 3
	HUNGER = 4
	SATURATION = 5
	ABSORPTION = 6
``` 

<span id="AttributeBuffType"></span>
## AttributeBuffType

- 描述

    Buff状态类型枚举值

```python
class AttributeBuffType(object):
	Hunger = 0
	Saturation = 1
	Regeneration = 2
	Heal = 3
	Harm = 4
	Magic = 5
	Wither = 6
	Poison = 7
	FatalPoison = 8
	SelfHeal = 9
``` 

<span id="BiomeType"></span>
## BiomeType

- 描述

    描述生物群系枚举值，主要用于API文档中的[mobSpawn组件](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#mobSpawn)，设置世界的生成生物规则

```python
class BiomeType:
	ocean = 0
	plains = 1
	desert = 2
	extreme_hills = 3
	forest = 4
	taiga = 5
	swampland = 6
	river = 7
	hell = 8
	the_end = 9
	legacy_frozen_ocean = 10
	frozen_river = 11
	ice_plains = 12
	ice_mountains = 13
	mushroom_island = 14
	mushroom_island_shore = 15
	beach = 16
	desert_hills = 17
	forest_hills = 18
	taiga_hills = 19
	extreme_hills_edge = 20
	jungle = 21
	jungle_hills = 22
	jungle_edge = 23
	deep_ocean = 24
	stone_beach = 25
	cold_beach = 26
	birch_forest = 27
	birch_forest_hills = 28
	roofed_forest = 29
	cold_taiga = 30
	cold_taiga_hills = 31
	mega_taiga = 32
	mega_taiga_hills = 33
	extreme_hills_plus_trees = 34
	savanna = 35
	savanna_plateau = 36
	mesa = 37
	mesa_plateau_stone = 38
	mesa_plateau = 39
	warm_ocean = 40
	deep_warm_ocean = 41
	lukewarm_ocean = 42
	deep_lukewarm_ocean = 43
	cold_ocean = 44
	deep_cold_ocean = 45
	frozen_ocean = 46
	deep_frozen_ocean = 47
	bamboo_jungle = 48
	bamboo_jungle_hills = 49
	sunflower_plains = 129
	desert_mutated = 130
	extreme_hills_mutated = 131
	flower_forest = 132
	taiga_mutated = 133
	swampland_mutated = 134
	ice_plains_spikes = 140
	jungle_mutated = 149
	jungle_edge_mutated = 151
	birch_forest_mutated = 155
	birch_forest_hills_mutated = 156
	roofed_forest_mutated = 157
	cold_taiga_mutated = 158
	redwood_taiga_mutated = 160
	redwood_taiga_hills_mutated = 161
	extreme_hills_plus_trees_mutated = 162
	savanna_mutated = 163
	savanna_plateau_mutated = 164
	mesa_bryce = 165
	mesa_plateau_stone_mutated = 166
	mesa_plateau_mutated = 167
``` 

<span id="ButtonEventType"></span>
## ButtonEventType

- 描述

    按钮事件枚举值

```python
class ButtonEventType(object):
	Clicked = 0
	Pressed = 1
	Released = 2
``` 

<span id="ButtonState"></span>
## ButtonState

- 描述

    按钮状态枚举值

```python
class ButtonState(object):
	Up = 0
	Down = 1
``` 

<span id="Change"></span>
## Change

- 描述

    刷怪设置参数枚举值，用于[mobSpawn组件](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#mobSpawn)

```python
class Change:
	Add = 0
	Remove = 1
``` 

<span id="EffectType"></span>
## EffectType

- 描述

    描述特效类型的枚举值

```python
class EffectType:
	EMPTY_EFFECT = "empty"
	MOVEMENT_SPEED = "speed"
	MOVEMENT_SLOWDOWN = "slowness"
	DIG_SPEED = "haste"
	DIG_SLOWDOWN = "mining_fatigue"
	DAMAGE_BOOST = "strength"
	HEAL = "instant_health"
	HARM = "instant_damage"
	JUMP = "jump_boost"
	CONFUSION = "nausea"
	REGENERATION = "regeneration"
	DAMAGE_RESISTANCE = "resistance"
	FIRE_RESISTANCE = "fire_resistance"
	WATER_BREATHING = "water_breathing"
	INVISIBILITY = "invisibility"
	BLINDNESS = "blindness"
	NIGHT_VISION = "night_vision"
	HUNGER = "hunger"
	WEAKNESS = "weakness"
	POISON = "poison"
	WITHER = "wither"
	HEALTH_BOOST = "health_boost"
	ABSORPTION = "absorption"
	SATURATION = "saturation"
	LEVITATION = "levitation"
	FATAL_POISON = "fatal_poison"
	CONDUIT_POWER = "conduit_power"
	SLOW_FALLING = "slow_falling"
	BAD_OMEN = "bad_omen"
	HERO_OF_THE_VILLAGE = "village_hero"
``` 

<span id="EnchantType"></span>
## EnchantType

- 描述

    附魔类型枚举值

```python
class EnchantType:
	ArmorAll = 0
	ArmorFire = 1
	ArmorFall = 2
	ArmorExplosive = 3
	ArmorProjectile = 4
	ArmorThorns = 5
	WaterBreath = 6
	WaterSpeed = 7
	WaterAffinity = 8
	WeaponDamage = 9
	WeaponUndead = 10
	WeaponArthropod = 11
	WeaponKnockback = 12
	WeaponFire = 13
	WeaponLoot = 14
	MiningEfficiency = 15
	MiningSilkTouch = 16
	MiningDurability = 17
	MiningLoot = 18
	BowDamage = 19
	BowKnockback = 20
	BowFire = 21
	BowInfinity = 22
	FishingLoot = 23
	FishingLure = 24
	FrostWalker = 25
	Mending = 26
	CurseBinding = 27
	CurseVanishing = 28
	TridentImpaling = 29
	TridentRiptide = 30
	TridentLoyalty = 31
	TridentChanneling = 32
	CrossbowMultishot = 33
	CrossbowPiercing = 34
	CrossbowQuickCharge = 35
	NumEnchantments = 36
	InvalidEnchantment = 37
``` 

<span id="EntityConst"></span>
## EntityConst

- 描述

    描述实体类型枚举值，主要用于API文档中的CreateEntity功能

```python
class EntityConst:
	TYPE_LVOBJ = "lvobj"
	TYPE_ENTITY = "entity"
	TYPE_MONSTER = "monster"
	TYPE_PLAYER = "player"
	TYPE_BULLET = "bullet"
	TYPE_SFX = "sfx"
	TYPE_BUFF = "buff"
	TYPE_PARTICLE = "particle"
	TYPE_EFFECT = "effect"
	TYPE_FONT = "font"
	TYPE_TEAM = "team"
	TYPE_ITEM_ENTITY = "item_entity"
	TYPE_NPC = "npc"
	TYPE_MOD_ENTITY = "mod_entity"
``` 

<span id="EntityTeleportCause"></span>
## EntityTeleportCause

- 描述

    传送理由枚举值，用于[WillTeleportToServerEvent事件](../02-Python脚本开发/99-ModAPI/3-事件/2-服务端事件.html#willteleporttoserverevent)

```python
class EntityTeleportCause(object):
	Unkown = "0"		# 尚未具体分类，末影人自体传送目前归为此类
	Projectile = "1"	# 飞射物，类似末影珍珠
	Command = "3"		# op指令，类似传送指令
	ChorusFruit = "2"	# 吃紫颂果传送
	Behavior = "4"		# 微软原生脚本组件
	Agent = "agent"		# 教育版指导传送
	Client = "client"	# 客户端发送的传送移动包
	GateWay = "gateway"	# 传送门
``` 

<span id="EntityType"></span>
## EntityType

- 描述

    描述生物类型枚举值，主要用于API文档中[EngineType组件](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#engineType)

```python
class EntityType:
	Undefined = 1
	TypeMask = 0x000000ff
	Mob = 0x00000100
	PathfinderMob = 0x00000200 | Mob
	Monster = 0x00000800 | PathfinderMob
	Animal = 0x00001000 | PathfinderMob
	TamableAnimal = 0x00004000 | Animal
	Ambient = 0x00008000 | Mob
	UndeadMob = 0x00010000 | Monster
	ZombieMonster = 0x00020000 | UndeadMob
	Arthropod = 0x00040000 | Monster
	Minecart = 0x00080000
	SkeletonMonster = 0x00100000 | UndeadMob
	EquineAnimal = 0x00200000 | TamableAnimal
	Projectile = 0x00400000
	AbstractArrow = 0x00800000
	WaterAnimal = 0x00002000 | PathfinderMob
	VillagerBase = 0x01000000 | PathfinderMob
	Chicken = 10 | Animal
	Cow = 11 | Animal
	Pig = 12 | Animal
	Sheep = 13 | Animal
	Wolf = 14 | TamableAnimal
	Villager = 15 | VillagerBase
	MushroomCow = 16 | Animal
	Squid = 17 | WaterAnimal
	Rabbit = 18 | Animal
	Bat = 19 | Ambient
	IronGolem = 20 | PathfinderMob
	SnowGolem = 21 | PathfinderMob
	Ocelot = 22 | TamableAnimal
	Horse = 23 | EquineAnimal
	PolarBear = 28 | Animal
	Llama = 29 | Animal
	Parrot = 30 | TamableAnimal
	Dolphin = 31 | WaterAnimal
	Donkey = 24 | EquineAnimal
	Mule = 25 | EquineAnimal
	SkeletonHorse = 26 | EquineAnimal | UndeadMob
	ZombieHorse = 27 | EquineAnimal | UndeadMob
	Zombie = 32 | ZombieMonster
	Creeper = 33 | Monster
	Skeleton = 34 | SkeletonMonster
	Spider = 35 | Arthropod
	PigZombie = 36 | UndeadMob
	Slime = 37 | Monster
	EnderMan = 38 | Monster
	Silverfish = 39 | Arthropod
	CaveSpider = 40 | Arthropod
	Ghast = 41 | Monster
	LavaSlime = 42 | Monster
	Blaze = 43 | Monster
	ZombieVillager = 44 | ZombieMonster
	Witch = 45 | Monster
	Stray = 46 | SkeletonMonster
	Husk = 47 | ZombieMonster
	WitherSkeleton = 48 | SkeletonMonster
	Guardian = 49 | Monster
	ElderGuardian = 50 | Monster
	Npc = 51 | Mob
	WitherBoss = 52 | UndeadMob
	Dragon = 53 | Monster
	Shulker = 54 | Monster
	Endermite = 55 | Arthropod
	Agent = 56 | Mob
	Vindicator = 57 | Monster
	Phantom = 58 | UndeadMob
	IllagerBeast = 59 | Monster
	ArmorStand = 61 | Mob
	TripodCamera = 62 | Mob
	Player = 63 | Mob
	ItemEntity = 64
	PrimedTnt = 65
	FallingBlock = 66
	MovingBlock = 67
	ExperiencePotion = 68 | Projectile
	Experience = 69
	EyeOfEnder = 70
	EnderCrystal = 71
	FireworksRocket = 72
	Trident = 73 | Projectile | AbstractArrow
	Turtle = 74 | Animal
	Cat = 75 | TamableAnimal
	ShulkerBullet = 76 | Projectile
	FishingHook = 77
	Chalkboard = 78
	DragonFireball = 79 | Projectile
	Arrow = 80 | Projectile | AbstractArrow
	Snowball = 81 | Projectile
	ThrownEgg = 82 | Projectile
	Painting = 83
	LargeFireball = 85 | Projectile
	ThrownPotion = 86 | Projectile
	Enderpearl = 87 | Projectile
	LeashKnot = 88
	WitherSkull = 89 | Projectile
	BoatRideable = 90
	WitherSkullDangerous = 91 | Projectile
	LightningBolt = 93
	SmallFireball = 94 | Projectile
	AreaEffectCloud = 95
	LingeringPotion = 101 | Projectile
	LlamaSpit = 102 | Projectile
	EvocationFang = 103 | Projectile
	EvocationIllager = 104 | Monster
	Vex = 105 | Monster
	MinecartRideable = 84 | Minecart
	MinecartHopper = 96 | Minecart
	MinecartTNT = 97 | Minecart
	MinecartChest = 98 | Minecart
	MinecartFurnace = 99 | Minecart
	MinecartCommandBlock = 100 | Minecart
	IceBomb = 106 | Projectile
	Balloon = 107
	Pufferfish = 108 | WaterAnimal
	Salmon = 109 | WaterAnimal
	Drowned = 110 | ZombieMonster
	Tropicalfish = 111 | WaterAnimal
	Fish = 112 | WaterAnimal
	Panda = 113 | Animal
	Pillager = 114 | Monster
	VillagerV2 = 115 | VillagerBase
	ZombieVillagerV2 = 116 | ZombieMonster
	Shield = 117
	WanderingTrader = 118 | PathfinderMob
	Lectern = 119
	ElderGuardianGhost = 120 | Monster
	Fox = 121 | Animal
	EntityExtension = 255
	MAX_ENTITY_ID = 256
``` 

<span id="Facing"></span>
## Facing

- 描述

    朝向枚举值

```python
class Facing(object):
	Down = 0
	Up = 1
	North = 2
	South = 3
	West = 4
	East = 5
``` 

<span id="GameDiffculty"></span>
## GameDiffculty

- 描述

    描述游戏难度的枚举值

```python
class GameDiffculty(object):
	Peaceful = 0
	Easy = 1
	Normal = 2
	Hard = 3
	Count = 4
	Unknown = 5
``` 

<span id="GameType"></span>
## GameType

- 描述

    描述游戏类型的枚举值

```python
class GameType(object):
	Undefined = -1
	Survival = 0
	Creative = 1
	Adventure = 2
	Default = Survival
``` 

<span id="ItemAcquisitionMethod"></span>
## ItemAcquisitionMethod

- 描述

    获得物品的方法枚举值

```python
class ItemAcquisitionMethod(object):
	Unknown = -1
	MethodNone = 0
	PickedUp = 1
	Crafted = 2
	TakenFromChest = 3
	TakenFromEnderchest = 4
	Bought = 5
	Anvil = 6
	Smelted = 7
	Brewed = 8
	Filled = 9
	Trading = 10
	Fishing = 11
	Container = 13
``` 

<span id="ItemColor"></span>
## ItemColor

- 描述

    物品的颜色枚举值

```python
class ItemColor(object):
	Black = 0
	Red = 1
	Green = 2
	Brown = 3
	Blue = 4
	Purple = 5
	Cyan = 6
	Silver = 7
	Gray = 8
	Pink = 9
	Lime = 10
	Yellow = 11
	LightBlue = 12
	Magenta = 13
	Orange = 14
	White = 15
``` 

<span id="ItemPosType"></span>
## ItemPosType

- 描述

    描述玩家物品位置

```python
class ItemPosType(object):
	INVENTORY = 0
	OFFHAND = 1
	CARRIED = 2
	ARMOR = 3
``` 

<span id="ItemUseMethodEnum"></span>
## ItemUseMethodEnum

- 描述

    使用物品的方法枚举值

```python
class ItemUseMethodEnum(object):
	Unknown		= -1
	EquipArmor	= 0	# Equipping armor
	Eat			= 1	# Eating food
	Attack		= 2	# Attacking (anything?)
	Consume		= 3	# Consuming potion
	Throw		= 4	# Thrown item (snowball, potion)
	Shoot		= 5	# Bow+Arrow
	Place		= 6	# Place an item (e.g. Sign)
	FillBottle	= 7	# Attempted to fill an empty bottle
	FillBucket	= 8	# Attempted to fill an empty bucket
	PourBucket	= 9	# Pour contents of a filled bucket
	UseTool		= 10	# Use right-click function of a tool (flint&steel, hoe, shovel, etc)
	Interact	= 11
	Retrieved	= 12	# Currently only for reeling in the fishing rod
``` 

<span id="KeyBoardType"></span>
## KeyBoardType

- 描述

    描述PC端点击键盘输入的按钮枚举值

```python
class KeyBoardType:
	KEY_GOBACK = 4

	KEY_BACKSPACE = 8
	KEY_TAB = 9
	KEY_RETURN = 13
	KEY_PAUSE = 19

	KEY_LSHIFT = 16
	KEY_CONTROL = 17
	KEY_MENU = 18
	KEY_CAPS_LOCK = 20
	KEY_ESCAPE = 27
	KEY_SPACE = 32
	KEY_PG_UP = 33
	KEY_PG_DOWN = 34
	KEY_END = 35
	KEY_HOME = 36

	KEY_LEFT = 37
	KEY_UP = 38
	KEY_RIGHT = 39
	KEY_DOWN = 40
	KEY_INSERT = 45
	KEY_DELETE = 46

	KEY_0 = 48
	KEY_1 = 49
	KEY_2 = 50
	KEY_3 = 51
	KEY_4 = 52
	KEY_5 = 53
	KEY_6 = 54
	KEY_7 = 55
	KEY_8 = 56
	KEY_9 = 57

	KEY_A = 65
	KEY_B = 66
	KEY_C = 67
	KEY_D = 68
	KEY_E = 69
	KEY_F = 70
	KEY_G = 71
	KEY_H = 72
	KEY_I = 73
	KEY_J = 74
	KEY_K = 75
	KEY_L = 76
	KEY_M = 77
	KEY_N = 78
	KEY_O = 79
	KEY_P = 80
	KEY_Q = 81
	KEY_R = 82
	KEY_S = 83
	KEY_T = 84
	KEY_U = 85
	KEY_V = 86
	KEY_W = 87
	KEY_X = 88
	KEY_Y = 89
	KEY_Z = 90

	KEY_NUMPAD0 = 96
	KEY_NUMPAD1 = 97
	KEY_NUMPAD2 = 98
	KEY_NUMPAD3 = 99
	KEY_NUMPAD4 = 100
	KEY_NUMPAD5 = 101
	KEY_NUMPAD6 = 102
	KEY_NUMPAD7 = 103
	KEY_NUMPAD8 = 104
	KEY_NUMPAD9 = 105
	KEY_MULTIPLY = 106
	KEY_ADD = 107

	KEY_SUBTRACT = 109
	KEY_DECIMAL = 110
	KEY_DIVIDE = 111
	KEY_F1 = 112
	KEY_F2 = 113
	KEY_F3 = 114
	KEY_F4 = 115
	KEY_F5 = 116
	KEY_F6 = 117
	KEY_F7 = 118
	KEY_F8 = 119
	KEY_F9 = 120
	KEY_F10 = 121
	KEY_F11 = 122
	KEY_F12 = 123
	KEY_F13 = 124

	KEY_NUM_LOCK = 144
	KEY_SCROLL = 145

	KEY_SEMICOLON = 186
	KEY_EQUALS = 187
	KEY_COMMA = 188
	KEY_MINUS = 189
	KEY_PERIOD = 190
	KEY_SLASH = 191
	KEY_GRAVE = 192

	KEY_LBRACKET = 219
	KEY_BACKSLASH = 220
	KEY_RBRACKET = 221
	KEY_APOSTRAPHE = 222

	KEY_ANDROID_MENU = 0xff
``` 

<span id="OptionId"></span>
## OptionId

- 描述

    可设置的枚举值

```python
class OptionId(object):
	Undefined = ""
	AUTO_JUMP = "AUTO_JUMP" 			#自动跳跃
	HIDE_PAPERDOLL = "HIDE_PAPERDOLL"	#隐藏纸娃娃
	HIDE_HAND = "HIDE_HAND" 			#隐藏手
	SPLIT_CONTROLS = "SPLIT_CONTROLS" 	#准心瞄准
``` 

<span id="StructureFeatureType"></span>
## StructureFeatureType

- 描述

    描述原版结构特征类型的枚举值，主要用于API文档中feature组件中[LocateStructureFeature](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#LocateNeteaseFeature)接口的传入参数

```python
class StructureFeatureType(object):
	Unknown = 0
	EndCity = 1
	Fortress = 2
	Mineshaft = 3
	Monument = 4
	Stronghold = 5
	Temple = 6
	Village = 7
	WoodlandMansion = 8
	Shipwreck = 9
	BuriedTreasure = 10
	Ruins = 11
	PillagerOutpost = 12
	RuinedPortal = 13
	Bastion = 14
``` 

<span id="SysSoundType"></span>
## SysSoundType

- 描述

    描述系统音效类型枚举值，主要用于API文档中[systemAudio组件](../02-Python脚本开发/99-ModAPI/4-组件/2-服务端组件.html#systemAudio)

```python
class SysSoundType:
	ItemUseOn = 0
	Hit = 1
	Step = 2
	Fly = 3
	Jump = 4
	Break = 5
	Place = 6
	HeavyStep = 7
	Gallop = 8
	Fall = 9
	Ambient = 10
	AmbientBaby = 11
	AmbientInWater = 12
	Breathe = 13
	Death = 14
	DeathInWater = 15
	DeathToZombie = 16
	Hurt = 17
	HurtInWater = 18
	Mad = 19
	Boost = 20
	Bow = 21
	SquishBig = 22
	SquishSmall = 23
	FallBig = 24
	FallSmall = 25
	Splash = 26
	Fizz = 27
	Flap = 28
	Swim = 29
	Drink = 30
	Eat = 31
	Takeoff = 32
	Shake = 33
	Plop = 34
	Land = 35
	Saddle = 36
	Armor = 37
	ArmorPlace = 38
	AddChest = 39
	Throw = 40
	Attack = 41
	AttackNoDamage = 42
	AttackStrong = 43
	Warn = 44
	Shear = 45
	Milk = 46
	Thunder = 47
	Explode = 48
	Fire = 49
	Ignite = 50
	Fuse = 51
	Stare = 52
	Spawn = 53
	Shoot = 54
	BreakBlock = 55
	Launch = 56
	Blast = 57
	LargeBlast = 58
	Twinkle = 59
	Remedy = 60
	Unfect = 61
	LevelUp = 62
	BowHit = 63
	BulletHit = 64
	ExtinguishFire = 65
	ItemFizz = 66
	ChestOpen = 67
	ChestClosed = 68
	ShulkerBoxOpen = 69
	ShulkerBoxClosed = 70
	EnderChestOpen = 71
	EnderChestClosed = 72
	PowerOn = 73
	PowerOff = 74
	Attach = 75
	Detach = 76
	Deny = 77
	Tripod = 78
	Pop = 79
	DropSlot = 80
	Note = 81
	Thorns = 82
	PistonIn = 83
	PistonOut = 84
	Portal = 85
	Water = 86
	LavaPop = 87
	Lava = 88
	Burp = 89
	BucketFillWater = 90
	BucketFillLava = 91
	BucketEmptyWater = 92
	BucketEmptyLava = 93
	EquipChain = 94
	EquipDiamond = 95
	EquipGeneric = 96
	EquipGold = 97
	EquipIron = 98
	EquipLeather = 99
	EquipElytra = 100
	Record13 = 101
	RecordCat = 102
	RecordBlocks = 103
	RecordChirp = 104
	RecordFar = 105
	RecordMall = 106
	RecordMellohi = 107
	RecordStal = 108
	RecordStrad = 109
	RecordWard = 110
	Record11 = 111
	RecordWait = 112
	RecordNull = 113
	Flop = 114
	GuardianCurse = 115
	MobWarning = 116
	MobWarningBaby = 117
	Teleport = 118
	ShulkerOpen = 119
	ShulkerClose = 120
	Haggle = 121
	HaggleYes = 122
	HaggleNo = 123
	HaggleIdle = 124
	ChorusGrow = 125
	ChorusDeath = 126
	Glass = 127
	PotionBrewed = 128
	CastSpell = 129
	PrepareAttackSpell = 130
	PrepareSummon = 131
	PrepareWololo = 132
	Fang = 133
	Charge = 134
	TakePicture = 135
	PlaceLeashKnot = 136
	BreakLeashKnot = 137
	AmbientGrowl = 138
	AmbientWhine = 139
	AmbientPant = 140
	AmbientPurr = 141
	AmbientPurreow = 142
	DeathMinVolume = 143
	DeathMidVolume = 144
	ImitateBlaze = 145
	ImitateCaveSpider = 146
	ImitateCreeper = 147
	ImitateElderGuardian = 148
	ImitateEnderDragon = 149
	ImitateEnderman = 150
	ImitateEndermite = 151
	ImitateEvocationIllager = 152
	ImitateGhast = 153
	ImitateHusk = 154
	ImitateIllusionIllager = 155
	ImitateMagmaCube = 156
	ImitatePolarBear = 157
	ImitateShulker = 158
	ImitateSilverfish = 159
	ImitateSkeleton = 160
	ImitateSlime = 161
	ImitateSpider = 162
	ImitateStray = 163
	ImitateVex = 164
	ImitateVindicationIllager = 165
	ImitateWitch = 166
	ImitateWither = 167
	ImitateWitherSkeleton = 168
	ImitateWolf = 169
	ImitateZombie = 170
	ImitateZombiePigman = 171
	ImitateZombieVillager = 172
	EnderEyePlaced = 173
	EndPortalCreated = 174
	AnvilUse = 175
	BottleDragonBreath = 176
	PortalTravel = 177
	TridentHit = 178
	TridentReturn = 179
	TridentRiptide_1 = 180
	TridentRiptide_2 = 181
	TridentRiptide_3 = 182
	TridentThrow = 183
	TridentThunder = 184
	TridentHitGround = 185
	Default = 186
	FletchingTableUse = 187
	ElemConstructOpen = 188
	IceBombHit = 189
	BalloonPop = 190
	LTReactionIceBomb = 191
	LTReactionBleach = 192
	LTReactionElephantToothpaste = 193
	LTReactionElephantToothpaste2 = 194
	LTReactionGlowStick = 195
	LTReactionGlowStick2 = 196
	LTReactionLuminol = 197
	LTReactionSalt = 198
	LTReactionFertilizer = 199
	LTReactionFireball = 200
	LTReactionMagnesiumSalt = 201
	LTReactionMiscFire = 202
	LTReactionFire = 203
	LTReactionMiscExplosion = 204
	LTReactionMiscMystical = 205
	LTReactionMiscMystical2 = 206
	LTReactionProduct = 207
	SparklerUse = 208
	GlowStickUse = 209
	SparklerActive = 210
	ConvertToDrowned = 211
	BucketFillFish = 212
	BucketEmptyFish = 213
	BubbleColumnUpwards = 214
	BubbleColumnDownwards = 215
	BubblePop = 216
	BubbleUpInside = 217
	BubbleDownInside = 218
	HurtBaby = 219
	DeathBaby = 220
	StepBaby = 221
	SpawnBaby = 222
	Born = 223
	TurtleEggBreak = 224
	TurtleEggCrack = 225
	TurtleEggHatched = 226
	LayEgg = 227
	TurtleEggAttacked = 228
	BeaconActivate = 229
	BeaconAmbient = 230
	BeaconDeactivate = 231
	BeaconPower = 232
	ConduitActivate = 233
	ConduitAmbient = 234
	ConduitAttack = 235
	ConduitDeactivate = 236
	ConduitShort = 237
	Swoop = 238
	BambooSaplingPlace = 239
	PreSneeze = 240
	Sneeze = 241
	AmbientTame = 242
	Scared = 243
	ScaffoldingClimb = 244
	CrossbowLoadingStart = 245
	CrossbowLoadingMiddle = 246
	CrossbowLoadingEnd = 247
	CrossbowShoot = 248
	CrossbowQuickChargeStart = 249
	CrossbowQuickChargeMiddle = 250
	CrossbowQuickChargeEnd = 251
	AmbientAggressive = 252
	AmbientWorried = 253
	CantBreed = 254
	ShieldBlock = 255
	LecternBookPlace = 256
	GrindstoneUse = 257
	Bell = 258
	CampfireCrackle = 259
	SweetBerryBushHurt = 262
	SweetBerryBushPick = 263
	Roar = 260
	Stun = 261
	CartographyTableUse = 264
	StonecutterUse = 265
	ComposterEmpty = 266
	ComposterFill = 267
	ComposterFillLayer = 268
	ComposterReady = 269
	BarrelOpen = 270
	BarrelClose = 271
	RaidHorn = 272
	LoomUse = 273
	AmbientInRaid = 274
	UICartographyTableUse = 275
	UIStonecutterUse = 276
	UILoomUse = 277
	SmokerUse = 278
	BlastFurnaceUse = 279
	SmithingTableUse = 280
	Screech = 281
	Sleep = 282
	FurnaceUse = 283
	MooshroomConvert = 284
	MilkSuspiciously = 285
	Celebrate = 286
	Undefined = 287
``` 

<span id="TouchEvent"></span>
## TouchEvent

- 描述

    触摸回调事件枚举值

```python
class TouchEvent:
	TouchUp = 0
	TouchDown = 1
	TouchCancel = 3
	TouchMove = 4
	TouchMoveIn  = 5
	TouchMoveOut = 6
``` 

<span id="UiBaseLayer"></span>
## UiBaseLayer

- 描述

    自定义UI界面的层次宏定义，用于在多个插件之间协调UI界面的遮挡关系

```python
class UiBaseLayer(object):
	Desk = 0				# 主界面常驻
	DeskFloat = 15000		# 主界面浮动提示（浮动提示信息）
	PopUpLv1 = 25000		# 一级弹出界面
	PopUpLv2 = 45000		# 二级弹出界面
	PopUpModal = 60000		# 模态弹出界面（弹出提示）
	PopUpFloat = 75000		# 模态弹出之上的浮动提示（大喇叭）
``` 

<span id="UseAnimation"></span>
## UseAnimation

- 描述

    使用物品时动画枚举值

```python
class UseAnimation(object):
	Undefined = 'none'
	Eat = 'eat'
	Drink = 'drink'
	Block = 'block'
	Bow = 'bow'
	Camera = 'camera'
	Crossbow = 'crossbow'
``` 

