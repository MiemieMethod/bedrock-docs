# <!-- md:samp SetLastHurtByPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp SetLastHurtByPacket -->数据包，数字ID是`96`。

## 结构

```viz
digraph "SetLastHurtByPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetLastHurtByPacket",comment="name: \"SetLastHurtByPacket\", typeName: \"\", id: 0, branchId: 96, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Last Hurt By",comment="name: \"Last Hurt By\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2}

}

```

## 字段

```title='SetLastHurtByPacket'
[last_hurt_by]
```

/// html | div.result
//// define
Last Hurt By：<!-- md:samp varint -->

- 类型：<!-- md:samp varint -->。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`||
  |`TypeMask`|`0x000000ff`||
  |`Mob`|`0x00000100`||
  |`PathfinderMob`|`0x00000200 | Mob`||
  |`Monster`|`0x00000800 | PathfinderMob`||
  |`Animal`|`0x00001000 | PathfinderMob`||
  |`TamableAnimal`|`0x00004000 | Animal`||
  |`Ambient`|`0x00008000 | Mob`||
  |`UndeadMob`|`0x00010000 | Monster`||
  |`ZombieMonster`|`0x00020000 | UndeadMob`||
  |`Arthropod`|`0x00040000 | Monster`||
  |`Minecart`|`0x00080000`||
  |`SkeletonMonster`|`0x00100000 | UndeadMob`||
  |`EquineAnimal`|`0x00200000 | TamableAnimal`||
  |`Projectile`|`0x00400000`||
  |`AbstractArrow`|`0x00800000`||
  |`WaterAnimal`|`0x00002000 | PathfinderMob`||
  |`VillagerBase`|`0x01000000 | PathfinderMob`||
  |`Chicken`|`10 | Animal`||
  |`Cow`|`11 | Animal`||
  |`Pig`|`12 | Animal`||
  |`Sheep`|`13 | Animal`||
  |`Wolf`|`14 | TamableAnimal`||
  |`Villager`|`15 | VillagerBase`||
  |`MushroomCow`|`16 | Animal`||
  |`Squid`|`17 | WaterAnimal`||
  |`Rabbit`|`18 | Animal`||
  |`Bat`|`19 | Ambient`||
  |`IronGolem`|`20 | PathfinderMob`||
  |`SnowGolem`|`21 | PathfinderMob`||
  |`Ocelot`|`22 | TamableAnimal`||
  |`Horse`|`23 | EquineAnimal`||
  |`PolarBear`|`28 | Animal`||
  |`Llama`|`29 | Animal`||
  |`Parrot`|`30 | TamableAnimal`||
  |`Dolphin`|`31 | WaterAnimal`||
  |`Donkey`|`24 | EquineAnimal`||
  |`Mule`|`25 | EquineAnimal`||
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`||
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`||
  |`Zombie`|`32 | ZombieMonster`||
  |`Creeper`|`33 | Monster`||
  |`Skeleton`|`34 | SkeletonMonster`||
  |`Spider`|`35 | Arthropod`||
  |`PigZombie`|`36 | UndeadMob`||
  |`Slime`|`37 | Monster`||
  |`EnderMan`|`38 | Monster`||
  |`Silverfish`|`39 | Arthropod`||
  |`CaveSpider`|`40 | Arthropod`||
  |`Ghast`|`41 | Monster`||
  |`LavaSlime`|`42 | Monster`||
  |`Blaze`|`43 | Monster`||
  |`ZombieVillager`|`44 | ZombieMonster`||
  |`Witch`|`45 | Monster`||
  |`Stray`|`46 | SkeletonMonster`||
  |`Husk`|`47 | ZombieMonster`||
  |`WitherSkeleton`|`48 | SkeletonMonster`||
  |`Guardian`|`49 | Monster`||
  |`ElderGuardian`|`50 | Monster`||
  |`Npc`|`51 | Mob`||
  |`WitherBoss`|`52 | UndeadMob`||
  |`Dragon`|`53 | Monster`||
  |`Shulker`|`54 | Monster`||
  |`Endermite`|`55 | Arthropod`||
  |`Agent`|`56 | Mob`||
  |`Vindicator`|`57 | Monster`||
  |`Phantom`|`58 | UndeadMob`||
  |`IllagerBeast`|`59 | Monster`||
  |`ArmorStand`|`61 | Mob`||
  |`TripodCamera`|`62 | Mob`||
  |`Player`|`63 | Mob`||
  |`ItemEntity`|`64`||
  |`PrimedTnt`|`65`||
  |`FallingBlock`|`66`||
  |`MovingBlock`|`67`||
  |`ExperiencePotion`|`68 | Projectile`||
  |`Experience`|`69`||
  |`EyeOfEnder`|`70`||
  |`EnderCrystal`|`71`||
  |`FireworksRocket`|`72`||
  |`Trident`|`73 | Projectile | AbstractArrow`||
  |`Turtle`|`74 | Animal`||
  |`Cat`|`75 | TamableAnimal`||
  |`ShulkerBullet`|`76 | Projectile`||
  |`FishingHook`|`77`||
  |`Chalkboard`|`78`||
  |`DragonFireball`|`79 | Projectile`||
  |`Arrow`|`80 | Projectile | AbstractArrow`||
  |`Snowball`|`81 | Projectile`||
  |`ThrownEgg`|`82 | Projectile`||
  |`Painting`|`83`||
  |`LargeFireball`|`85 | Projectile`||
  |`ThrownPotion`|`86 | Projectile`||
  |`Enderpearl`|`87 | Projectile`||
  |`LeashKnot`|`88`||
  |`WitherSkull`|`89 | Projectile`||
  |`BoatRideable`|`90`||
  |`WitherSkullDangerous`|`91 | Projectile`||
  |`LightningBolt`|`93`||
  |`SmallFireball`|`94 | Projectile`||
  |`AreaEffectCloud`|`95`||
  |`LingeringPotion`|`101 | Projectile`||
  |`LlamaSpit`|`102 | Projectile`||
  |`EvocationFang`|`103 | Projectile`||
  |`EvocationIllager`|`104 | Monster`||
  |`Vex`|`105 | Monster`||
  |`MinecartRideable`|`84 | Minecart`||
  |`MinecartHopper`|`96 | Minecart`||
  |`MinecartTNT`|`97 | Minecart`||
  |`MinecartChest`|`98 | Minecart`||
  |`MinecartFurnace`|`99 | Minecart`||
  |`MinecartCommandBlock`|`100 | Minecart`||
  |`IceBomb`|`106 | Projectile`||
  |`Balloon`|`107`||
  |`Pufferfish`|`108 | WaterAnimal`||
  |`Salmon`|`109 | WaterAnimal`||
  |`Drowned`|`110 | ZombieMonster`||
  |`Tropicalfish`|`111 | WaterAnimal`||
  |`Fish`|`112 | WaterAnimal`||
  |`Panda`|`113 | Animal`||
  |`Pillager`|`114 | Monster`||
  |`VillagerV2`|`115 | VillagerBase`||
  |`ZombieVillagerV2`|`116 | ZombieMonster`||
  |`Shield`|`117`||
  |`WanderingTrader`|`118 | PathfinderMob`||
  |`Lectern`|`119`||
  |`ElderGuardianGhost`|`120 | Monster`||
  |`Fox`|`121 | Animal`||
  |`Bee`|`122 | Mob`||
  |`Piglin`|`123 | Mob`||
  |`Hoglin`|`124 | Animal`||
  |`Strider`|`125 | Animal`||
  |`Zoglin`|`126 | UndeadMob`||
  |`PiglinBrute`|`127 | Mob`||
  |`Goat`|`128 | Animal`||
  |`GlowSquid`|`129 | WaterAnimal`||
  |`Axolotl`|`130 | Animal`||
  |`Warden`|`131 | Monster`||
  |`Frog`|`132 | Animal`||
  |`Tadpole`|`133 | WaterAnimal`||
  |`Allay`|`134 | Mob`||
  |`ChestBoatRideable`|`136 | BoatRideable`||
  |`TraderLlama`|`137 | Llama`||
  |`Camel`|`138 | Animal`||
  |`Sniffer`|`139 | Animal`||
  |`Breeze`|`140 | Monster`||
  |`BreezeWindChargeProjectile`|`141 | Projectile`||
  |`Armadillo`|`142 | Animal`||
  |`WindChargeProjectile`|`143 | Projectile`||
  |`Bogged`|`144| SkeletonMonster`||



////

///

