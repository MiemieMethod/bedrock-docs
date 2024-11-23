# <!-- md:samp SetLastHurtByPacket -->

> 文档版本：r/21_u4<br/>协议版本：748

<!-- md:samp SetLastHurtByPacket -->数据包，数字ID是`96`。该数据包用于protocol.packet.setlasthurtbypacket.description

## 结构

```viz
digraph "SetLastHurtByPacket" {
rankdir = LR
0
0 -> 1
1 -> 2

0 [label="SetLastHurtByPacket",comment="name: \"SetLastHurtByPacket\", typeName: \"\", id: 0, branchId: 96, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Last Hurt By",comment="name: \"Last Hurt By\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 基本类型枚举。protocol.packet.setlasthurtbypacket.last_hurt_by.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`1`|protocol.enum.undefined|
  |`TypeMask`|`0x000000ff`|protocol.enum.typemask|
  |`Mob`|`0x00000100`|protocol.enum.mob|
  |`PathfinderMob`|`0x00000200 | Mob`|protocol.enum.pathfindermob|
  |`Monster`|`0x00000800 | PathfinderMob`|protocol.enum.monster|
  |`Animal`|`0x00001000 | PathfinderMob`|protocol.enum.animal|
  |`TamableAnimal`|`0x00004000 | Animal`|protocol.enum.tamableanimal|
  |`Ambient`|`0x00008000 | Mob`|protocol.enum.ambient|
  |`UndeadMob`|`0x00010000 | Monster`|protocol.enum.undeadmob|
  |`ZombieMonster`|`0x00020000 | UndeadMob`|protocol.enum.zombiemonster|
  |`Arthropod`|`0x00040000 | Monster`|protocol.enum.arthropod|
  |`Minecart`|`0x00080000`|protocol.enum.minecart|
  |`SkeletonMonster`|`0x00100000 | UndeadMob`|protocol.enum.skeletonmonster|
  |`EquineAnimal`|`0x00200000 | TamableAnimal`|protocol.enum.equineanimal|
  |`Projectile`|`0x00400000`|protocol.enum.projectile|
  |`AbstractArrow`|`0x00800000`|protocol.enum.abstractarrow|
  |`WaterAnimal`|`0x00002000 | PathfinderMob`|protocol.enum.wateranimal|
  |`VillagerBase`|`0x01000000 | PathfinderMob`|protocol.enum.villagerbase|
  |`Chicken`|`10 | Animal`|protocol.enum.chicken|
  |`Cow`|`11 | Animal`|protocol.enum.cow|
  |`Pig`|`12 | Animal`|protocol.enum.pig|
  |`Sheep`|`13 | Animal`|protocol.enum.sheep|
  |`Wolf`|`14 | TamableAnimal`|protocol.enum.wolf|
  |`Villager`|`15 | VillagerBase`|protocol.enum.villager|
  |`MushroomCow`|`16 | Animal`|protocol.enum.mushroomcow|
  |`Squid`|`17 | WaterAnimal`|protocol.enum.squid|
  |`Rabbit`|`18 | Animal`|protocol.enum.rabbit|
  |`Bat`|`19 | Ambient`|protocol.enum.bat|
  |`IronGolem`|`20 | PathfinderMob`|protocol.enum.irongolem|
  |`SnowGolem`|`21 | PathfinderMob`|protocol.enum.snowgolem|
  |`Ocelot`|`22 | TamableAnimal`|protocol.enum.ocelot|
  |`Horse`|`23 | EquineAnimal`|protocol.enum.horse|
  |`PolarBear`|`28 | Animal`|protocol.enum.polarbear|
  |`Llama`|`29 | Animal`|protocol.enum.llama|
  |`Parrot`|`30 | TamableAnimal`|protocol.enum.parrot|
  |`Dolphin`|`31 | WaterAnimal`|protocol.enum.dolphin|
  |`Donkey`|`24 | EquineAnimal`|protocol.enum.donkey|
  |`Mule`|`25 | EquineAnimal`|protocol.enum.mule|
  |`SkeletonHorse`|`26 | EquineAnimal | UndeadMob`|protocol.enum.skeletonhorse|
  |`ZombieHorse`|`27 | EquineAnimal | UndeadMob`|protocol.enum.zombiehorse|
  |`Zombie`|`32 | ZombieMonster`|protocol.enum.zombie|
  |`Creeper`|`33 | Monster`|protocol.enum.creeper|
  |`Skeleton`|`34 | SkeletonMonster`|protocol.enum.skeleton|
  |`Spider`|`35 | Arthropod`|protocol.enum.spider|
  |`PigZombie`|`36 | UndeadMob`|protocol.enum.pigzombie|
  |`Slime`|`37 | Monster`|protocol.enum.slime|
  |`EnderMan`|`38 | Monster`|protocol.enum.enderman|
  |`Silverfish`|`39 | Arthropod`|protocol.enum.silverfish|
  |`CaveSpider`|`40 | Arthropod`|protocol.enum.cavespider|
  |`Ghast`|`41 | Monster`|protocol.enum.ghast|
  |`LavaSlime`|`42 | Monster`|protocol.enum.lavaslime|
  |`Blaze`|`43 | Monster`|protocol.enum.blaze|
  |`ZombieVillager`|`44 | ZombieMonster`|protocol.enum.zombievillager|
  |`Witch`|`45 | Monster`|protocol.enum.witch|
  |`Stray`|`46 | SkeletonMonster`|protocol.enum.stray|
  |`Husk`|`47 | ZombieMonster`|protocol.enum.husk|
  |`WitherSkeleton`|`48 | SkeletonMonster`|protocol.enum.witherskeleton|
  |`Guardian`|`49 | Monster`|protocol.enum.guardian|
  |`ElderGuardian`|`50 | Monster`|protocol.enum.elderguardian|
  |`Npc`|`51 | Mob`|protocol.enum.npc|
  |`WitherBoss`|`52 | UndeadMob`|protocol.enum.witherboss|
  |`Dragon`|`53 | Monster`|protocol.enum.dragon|
  |`Shulker`|`54 | Monster`|protocol.enum.shulker|
  |`Endermite`|`55 | Arthropod`|protocol.enum.endermite|
  |`Agent`|`56 | Mob`|protocol.enum.agent|
  |`Vindicator`|`57 | Monster`|protocol.enum.vindicator|
  |`Phantom`|`58 | UndeadMob`|protocol.enum.phantom|
  |`IllagerBeast`|`59 | Monster`|protocol.enum.illagerbeast|
  |`ArmorStand`|`61 | Mob`|protocol.enum.armorstand|
  |`TripodCamera`|`62 | Mob`|protocol.enum.tripodcamera|
  |`Player`|`63 | Mob`|protocol.enum.player|
  |`ItemEntity`|`64`|protocol.enum.itementity|
  |`PrimedTnt`|`65`|protocol.enum.primedtnt|
  |`FallingBlock`|`66`|protocol.enum.fallingblock|
  |`MovingBlock`|`67`|protocol.enum.movingblock|
  |`ExperiencePotion`|`68 | Projectile`|protocol.enum.experiencepotion|
  |`Experience`|`69`|protocol.enum.experience|
  |`EyeOfEnder`|`70`|protocol.enum.eyeofender|
  |`EnderCrystal`|`71`|protocol.enum.endercrystal|
  |`FireworksRocket`|`72`|protocol.enum.fireworksrocket|
  |`Trident`|`73 | Projectile | AbstractArrow`|protocol.enum.trident|
  |`Turtle`|`74 | Animal`|protocol.enum.turtle|
  |`Cat`|`75 | TamableAnimal`|protocol.enum.cat|
  |`ShulkerBullet`|`76 | Projectile`|protocol.enum.shulkerbullet|
  |`FishingHook`|`77`|protocol.enum.fishinghook|
  |`Chalkboard`|`78`|protocol.enum.chalkboard|
  |`DragonFireball`|`79 | Projectile`|protocol.enum.dragonfireball|
  |`Arrow`|`80 | Projectile | AbstractArrow`|protocol.enum.arrow|
  |`Snowball`|`81 | Projectile`|protocol.enum.snowball|
  |`ThrownEgg`|`82 | Projectile`|protocol.enum.thrownegg|
  |`Painting`|`83`|protocol.enum.painting|
  |`LargeFireball`|`85 | Projectile`|protocol.enum.largefireball|
  |`ThrownPotion`|`86 | Projectile`|protocol.enum.thrownpotion|
  |`Enderpearl`|`87 | Projectile`|protocol.enum.enderpearl|
  |`LeashKnot`|`88`|protocol.enum.leashknot|
  |`WitherSkull`|`89 | Projectile`|protocol.enum.witherskull|
  |`BoatRideable`|`90`|protocol.enum.boatrideable|
  |`WitherSkullDangerous`|`91 | Projectile`|protocol.enum.witherskulldangerous|
  |`LightningBolt`|`93`|protocol.enum.lightningbolt|
  |`SmallFireball`|`94 | Projectile`|protocol.enum.smallfireball|
  |`AreaEffectCloud`|`95`|protocol.enum.areaeffectcloud|
  |`LingeringPotion`|`101 | Projectile`|protocol.enum.lingeringpotion|
  |`LlamaSpit`|`102 | Projectile`|protocol.enum.llamaspit|
  |`EvocationFang`|`103 | Projectile`|protocol.enum.evocationfang|
  |`EvocationIllager`|`104 | Monster`|protocol.enum.evocationillager|
  |`Vex`|`105 | Monster`|protocol.enum.vex|
  |`MinecartRideable`|`84 | Minecart`|protocol.enum.minecartrideable|
  |`MinecartHopper`|`96 | Minecart`|protocol.enum.minecarthopper|
  |`MinecartTNT`|`97 | Minecart`|protocol.enum.minecarttnt|
  |`MinecartChest`|`98 | Minecart`|protocol.enum.minecartchest|
  |`MinecartFurnace`|`99 | Minecart`|protocol.enum.minecartfurnace|
  |`MinecartCommandBlock`|`100 | Minecart`|protocol.enum.minecartcommandblock|
  |`IceBomb`|`106 | Projectile`|protocol.enum.icebomb|
  |`Balloon`|`107`|protocol.enum.balloon|
  |`Pufferfish`|`108 | WaterAnimal`|protocol.enum.pufferfish|
  |`Salmon`|`109 | WaterAnimal`|protocol.enum.salmon|
  |`Drowned`|`110 | ZombieMonster`|protocol.enum.drowned|
  |`Tropicalfish`|`111 | WaterAnimal`|protocol.enum.tropicalfish|
  |`Fish`|`112 | WaterAnimal`|protocol.enum.fish|
  |`Panda`|`113 | Animal`|protocol.enum.panda|
  |`Pillager`|`114 | Monster`|protocol.enum.pillager|
  |`VillagerV2`|`115 | VillagerBase`|protocol.enum.villagerv2|
  |`ZombieVillagerV2`|`116 | ZombieMonster`|protocol.enum.zombievillagerv2|
  |`Shield`|`117`|protocol.enum.shield|
  |`WanderingTrader`|`118 | PathfinderMob`|protocol.enum.wanderingtrader|
  |`Lectern`|`119`|protocol.enum.lectern|
  |`ElderGuardianGhost`|`120 | Monster`|protocol.enum.elderguardianghost|
  |`Fox`|`121 | Animal`|protocol.enum.fox|
  |`Bee`|`122 | Mob`|protocol.enum.bee|
  |`Piglin`|`123 | Mob`|protocol.enum.piglin|
  |`Hoglin`|`124 | Animal`|protocol.enum.hoglin|
  |`Strider`|`125 | Animal`|protocol.enum.strider|
  |`Zoglin`|`126 | UndeadMob`|protocol.enum.zoglin|
  |`PiglinBrute`|`127 | Mob`|protocol.enum.piglinbrute|
  |`Goat`|`128 | Animal`|protocol.enum.goat|
  |`GlowSquid`|`129 | WaterAnimal`|protocol.enum.glowsquid|
  |`Axolotl`|`130 | Animal`|protocol.enum.axolotl|
  |`Warden`|`131 | Monster`|protocol.enum.warden|
  |`Frog`|`132 | Animal`|protocol.enum.frog|
  |`Tadpole`|`133 | WaterAnimal`|protocol.enum.tadpole|
  |`Allay`|`134 | Mob`|protocol.enum.allay|
  |`ChestBoatRideable`|`136 | BoatRideable`|protocol.enum.chestboatrideable|
  |`TraderLlama`|`137 | Llama`|protocol.enum.traderllama|
  |`Camel`|`138 | Animal`|protocol.enum.camel|
  |`Sniffer`|`139 | Animal`|protocol.enum.sniffer|
  |`Breeze`|`140 | Monster`|protocol.enum.breeze|
  |`BreezeWindChargeProjectile`|`141 | Projectile`|protocol.enum.breezewindchargeprojectile|
  |`Armadillo`|`142 | Animal`|protocol.enum.armadillo|
  |`WindChargeProjectile`|`143 | Projectile`|protocol.enum.windchargeprojectile|
  |`Bogged`|`144 | SkeletonMonster`|protocol.enum.bogged|
  |`OminousItemSpawner`|`145`|protocol.enum.ominousitemspawner|



////

///

