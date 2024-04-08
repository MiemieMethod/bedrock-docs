# <!-- md:samp LevelSoundEventPacketV1 -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelSoundEventPacketV1 -->类型，数字ID是`24`。

## 结构

```viz
digraph "LevelSoundEventPacketV1" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6
0 -> 7
7 -> 8
0 -> 9
9 -> 10
0 -> 11
11 -> 12

0 [label="LevelSoundEventPacketV1",comment="name: \"LevelSoundEventPacketV1\", typeName: \"\", id: 0, branchId: 24, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Puv::Legacy::LevelSoundEvent\""];
2 [label="byte",comment="name: \"byte\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
7 [label="Actor Type",comment="name: \"Actor Type\", typeName: \"\", id: 7, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorType\""];
8 [label="varint",comment="name: \"varint\", typeName: \"\", id: 8, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
9 [label="Baby Mob",comment="name: \"Baby Mob\", typeName: \"\", id: 9, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
10 [label="bool",comment="name: \"bool\", typeName: \"\", id: 10, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
11 [label="Global",comment="name: \"Global\", typeName: \"\", id: 11, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
12 [label="bool",comment="name: \"bool\", typeName: \"\", id: 12, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6;8;10;12}

}

```

## 字段

```title='LevelSoundEventPacketV1'
[event_id][position][data][actor_type][baby_mob][global]
```

/// html | div.result
//// define
Event ID：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ItemUseOn`|`0`||
  |`Hit`|`1`||
  |`Step`|`2`||
  |`Fly`|`3`||
  |`Jump`|`4`||
  |`Break`|`5`||
  |`Place`|`6`||
  |`HeavyStep`|`7`||
  |`Gallop`|`8`||
  |`Fall`|`9`||
  |`Ambient`|`10`||
  |`AmbientBaby`|`11`||
  |`AmbientInWater`|`12`||
  |`Breathe`|`13`||
  |`Death`|`14`||
  |`DeathInWater`|`15`||
  |`DeathToZombie`|`16`||
  |`Hurt`|`17`||
  |`HurtInWater`|`18`||
  |`Mad`|`19`||
  |`Boost`|`20`||
  |`Bow`|`21`||
  |`SquishBig`|`22`||
  |`SquishSmall`|`23`||
  |`FallBig`|`24`||
  |`FallSmall`|`25`||
  |`Splash`|`26`||
  |`Fizz`|`27`||
  |`Flap`|`28`||
  |`Swim`|`29`||
  |`Drink`|`30`||
  |`Eat`|`31`||
  |`Takeoff`|`32`||
  |`Shake`|`33`||
  |`Plop`|`34`||
  |`Land`|`35`||
  |`Saddle`|`36`||
  |`Armor`|`37`||
  |`ArmorPlace`|`38`||
  |`AddChest`|`39`||
  |`Throw`|`40`||
  |`Attack`|`41`||
  |`AttackNoDamage`|`42`||
  |`AttackStrong`|`43`||
  |`Warn`|`44`||
  |`Shear`|`45`||
  |`Milk`|`46`||
  |`Thunder`|`47`||
  |`Explode`|`48`||
  |`Fire`|`49`||
  |`Ignite`|`50`||
  |`Fuse`|`51`||
  |`Stare`|`52`||
  |`Spawn`|`53`||
  |`Shoot`|`54`||
  |`BreakBlock`|`55`||
  |`Launch`|`56`||
  |`Blast`|`57`||
  |`LargeBlast`|`58`||
  |`Twinkle`|`59`||
  |`Remedy`|`60`||
  |`Unfect`|`61`||
  |`LevelUp`|`62`||
  |`BowHit`|`63`||
  |`BulletHit`|`64`||
  |`ExtinguishFire`|`65`||
  |`ItemFizz`|`66`||
  |`ChestOpen`|`67`||
  |`ChestClosed`|`68`||
  |`ShulkerBoxOpen`|`69`||
  |`ShulkerBoxClosed`|`70`||
  |`EnderChestOpen`|`71`||
  |`EnderChestClosed`|`72`||
  |`PowerOn`|`73`||
  |`PowerOff`|`74`||
  |`Attach`|`75`||
  |`Detach`|`76`||
  |`Deny`|`77`||
  |`Tripod`|`78`||
  |`Pop`|`79`||
  |`DropSlot`|`80`||
  |`Note`|`81`||
  |`Thorns`|`82`||
  |`PistonIn`|`83`||
  |`PistonOut`|`84`||
  |`Portal`|`85`||
  |`Water`|`86`||
  |`LavaPop`|`87`||
  |`Lava`|`88`||
  |`Burp`|`89`||
  |`BucketFillWater`|`90`||
  |`BucketFillLava`|`91`||
  |`BucketEmptyWater`|`92`||
  |`BucketEmptyLava`|`93`||
  |`EquipChain`|`94`||
  |`EquipDiamond`|`95`||
  |`EquipGeneric`|`96`||
  |`EquipGold`|`97`||
  |`EquipIron`|`98`||
  |`EquipLeather`|`99`||
  |`EquipElytra`|`100`||
  |`Record13`|`101`||
  |`RecordCat`|`102`||
  |`RecordBlocks`|`103`||
  |`RecordChirp`|`104`||
  |`RecordFar`|`105`||
  |`RecordMall`|`106`||
  |`RecordMellohi`|`107`||
  |`RecordStal`|`108`||
  |`RecordStrad`|`109`||
  |`RecordWard`|`110`||
  |`Record11`|`111`||
  |`RecordWait`|`112`||
  |`RecordNull`|`113`||
  |`Flop`|`114`||
  |`GuardianCurse`|`115`||
  |`MobWarning`|`116`||
  |`MobWarningBaby`|`117`||
  |`Teleport`|`118`||
  |`ShulkerOpen`|`119`||
  |`ShulkerClose`|`120`||
  |`Haggle`|`121`||
  |`HaggleYes`|`122`||
  |`HaggleNo`|`123`||
  |`HaggleIdle`|`124`||
  |`ChorusGrow`|`125`||
  |`ChorusDeath`|`126`||
  |`Glass`|`127`||
  |`PotionBrewed`|`128`||
  |`CastSpell`|`129`||
  |`PrepareAttackSpell`|`130`||
  |`PrepareSummon`|`131`||
  |`PrepareWololo`|`132`||
  |`Fang`|`133`||
  |`Charge`|`134`||
  |`TakePicture`|`135`||
  |`PlaceLeashKnot`|`136`||
  |`BreakLeashKnot`|`137`||
  |`AmbientGrowl`|`138`||
  |`AmbientWhine`|`139`||
  |`AmbientPant`|`140`||
  |`AmbientPurr`|`141`||
  |`AmbientPurreow`|`142`||
  |`DeathMinVolume`|`143`||
  |`DeathMidVolume`|`144`||
  |`ImitateBlaze`|`145`||
  |`ImitateCaveSpider`|`146`||
  |`ImitateCreeper`|`147`||
  |`ImitateElderGuardian`|`148`||
  |`ImitateEnderDragon`|`149`||
  |`ImitateEnderman`|`150`||
  |`ImitateEndermite`|`151`||
  |`ImitateEvocationIllager`|`152`||
  |`ImitateGhast`|`153`||
  |`ImitateHusk`|`154`||
  |`ImitateIllusionIllager`|`155`||
  |`ImitateMagmaCube`|`156`||
  |`ImitatePolarBear`|`157`||
  |`ImitateShulker`|`158`||
  |`ImitateSilverfish`|`159`||
  |`ImitateSkeleton`|`160`||
  |`ImitateSlime`|`161`||
  |`ImitateSpider`|`162`||
  |`ImitateStray`|`163`||
  |`ImitateVex`|`164`||
  |`ImitateVindicationIllager`|`165`||
  |`ImitateWitch`|`166`||
  |`ImitateWither`|`167`||
  |`ImitateWitherSkeleton`|`168`||
  |`ImitateWolf`|`169`||
  |`ImitateZombie`|`170`||
  |`ImitateZombiePigman`|`171`||
  |`ImitateZombieVillager`|`172`||
  |`EnderEyePlaced`|`173`||
  |`EndPortalCreated`|`174`||
  |`AnvilUse`|`175`||
  |`BottleDragonBreath`|`176`||
  |`PortalTravel`|`177`||
  |`TridentHit`|`178`||
  |`TridentReturn`|`179`||
  |`TridentRiptide_1`|`180`||
  |`TridentRiptide_2`|`181`||
  |`TridentRiptide_3`|`182`||
  |`TridentThrow`|`183`||
  |`TridentThunder`|`184`||
  |`TridentHitGround`|`185`||
  |`Default`|`186`||
  |`FletchingTableUse`|`187`||
  |`ElemConstructOpen`|`188`||
  |`IceBombHit`|`189`||
  |`BalloonPop`|`190`||
  |`LTReactionIceBomb`|`191`||
  |`LTReactionBleach`|`192`||
  |`LTReactionElephantToothpaste`|`193`||
  |`LTReactionElephantToothpaste2`|`194`||
  |`LTReactionGlowStick`|`195`||
  |`LTReactionGlowStick2`|`196`||
  |`LTReactionLuminol`|`197`||
  |`LTReactionSalt`|`198`||
  |`LTReactionFertilizer`|`199`||
  |`LTReactionFireball`|`200`||
  |`LTReactionMagnesiumSalt`|`201`||
  |`LTReactionMiscFire`|`202`||
  |`LTReactionFire`|`203`||
  |`LTReactionMiscExplosion`|`204`||
  |`LTReactionMiscMystical`|`205`||
  |`LTReactionMiscMystical2`|`206`||
  |`LTReactionProduct`|`207`||
  |`SparklerUse`|`208`||
  |`GlowStickUse`|`209`||
  |`SparklerActive`|`210`||
  |`ConvertToDrowned`|`211`||
  |`BucketFillFish`|`212`||
  |`BucketEmptyFish`|`213`||
  |`BubbleColumnUpwards`|`214`||
  |`BubbleColumnDownwards`|`215`||
  |`BubblePop`|`216`||
  |`BubbleUpInside`|`217`||
  |`BubbleDownInside`|`218`||
  |`HurtBaby`|`219`||
  |`DeathBaby`|`220`||
  |`StepBaby`|`221`||
  |`SpawnBaby`|`222`||
  |`Born`|`223`||
  |`TurtleEggBreak`|`224`||
  |`TurtleEggCrack`|`225`||
  |`TurtleEggHatched`|`226`||
  |`LayEgg`|`227`||
  |`TurtleEggAttacked`|`228`||
  |`BeaconActivate`|`229`||
  |`BeaconAmbient`|`230`||
  |`BeaconDeactivate`|`231`||
  |`BeaconPower`|`232`||
  |`ConduitActivate`|`233`||
  |`ConduitAmbient`|`234`||
  |`ConduitAttack`|`235`||
  |`ConduitDeactivate`|`236`||
  |`ConduitShort`|`237`||
  |`Swoop`|`238`||
  |`BambooSaplingPlace`|`239`||
  |`PreSneeze`|`240`||
  |`Sneeze`|`241`||
  |`AmbientTame`|`242`||
  |`Scared`|`243`||
  |`ScaffoldingClimb`|`244`||
  |`CrossbowLoadingStart`|`245`||
  |`CrossbowLoadingMiddle`|`246`||
  |`CrossbowLoadingEnd`|`247`||
  |`CrossbowShoot`|`248`||
  |`CrossbowQuickChargeStart`|`249`||
  |`CrossbowQuickChargeMiddle`|`250`||
  |`CrossbowQuickChargeEnd`|`251`||
  |`AmbientAggressive`|`252`||
  |`AmbientWorried`|`253`||
  |`CantBreed`|`254`||
  |`ShieldBlock`|`255`||
  |`LecternBookPlace`|`256`||
  |`GrindstoneUse`|`257`||
  |`Bell`|`258`||
  |`CampfireCrackle`|`259`||
  |`Roar`|`260`||
  |`Stun`|`261`||
  |`SweetBerryBushHurt`|`262`||
  |`SweetBerryBushPick`|`263`||
  |`CartographyTableUse`|`264`||
  |`StonecutterUse`|`265`||
  |`ComposterEmpty`|`266`||
  |`ComposterFill`|`267`||
  |`ComposterFillLayer`|`268`||
  |`ComposterReady`|`269`||
  |`BarrelOpen`|`270`||
  |`BarrelClose`|`271`||
  |`RaidHorn`|`272`||
  |`LoomUse`|`273`||
  |`AmbientInRaid`|`274`||
  |`UICartographyTableUse`|`275`||
  |`UIStonecutterUse`|`276`||
  |`UILoomUse`|`277`||
  |`SmokerUse`|`278`||
  |`BlastFurnaceUse`|`279`||
  |`SmithingTableUse`|`280`||
  |`Screech`|`281`||
  |`Sleep`|`282`||
  |`FurnaceUse`|`283`||
  |`MooshroomConvert`|`284`||
  |`MilkSuspiciously`|`285`||
  |`Celebrate`|`286`||
  |`JumpPrevent`|`287`||
  |`AmbientPollinate`|`288`||
  |`BeehiveDrip`|`289`||
  |`BeehiveEnter`|`290`||
  |`BeehiveExit`|`291`||
  |`BeehiveWork`|`292`||
  |`BeehiveShear`|`293`||
  |`HoneybottleDrink`|`294`||
  |`AmbientCave`|`295`||
  |`Retreat`|`296`||
  |`ConvertToZombified`|`297`||
  |`Admire`|`298`||
  |`StepLava`|`299`||
  |`Tempt`|`300`||
  |`Panic`|`301`||
  |`Angry`|`302`||
  |`AmbientMoodWarpedForest`|`303`||
  |`AmbientMoodSoulsandValley`|`304`||
  |`AmbientMoodNetherWastes`|`305`||
  |`AmbientMoodBasaltDeltas`|`306`||
  |`AmbientMoodCrimsonForest`|`307`||
  |`RespawnAnchorCharge`|`308`||
  |`RespawnAnchorDeplete`|`309`||
  |`RespawnAnchorSetSpawn`|`310`||
  |`RespawnAnchorAmbient`|`311`||
  |`SoulEscapeQuiet`|`312`||
  |`SoulEscapeLoud`|`313`||
  |`RecordPigstep`|`314`||
  |`LinkCompassToLodestone`|`315`||
  |`UseSmithingTable`|`316`||
  |`EquipNetherite`|`317`||
  |`AmbientLoopWarpedForest`|`318`||
  |`AmbientLoopSoulsandValley`|`319`||
  |`AmbientLoopNetherWastes`|`320`||
  |`AmbientLoopBasaltDeltas`|`321`||
  |`AmbientLoopCrimsonForest`|`322`||
  |`AmbientAdditionWarpedForest`|`323`||
  |`AmbientAdditionSoulsandValley`|`324`||
  |`AmbientAdditionNetherWastes`|`325`||
  |`AmbientAdditionBasaltDeltas`|`326`||
  |`AmbientAdditionCrimsonForest`|`327`||
  |`SculkSensorPowerOn`|`328`||
  |`SculkSensorPowerOff`|`329`||
  |`BucketFillPowderSnow`|`330`||
  |`BucketEmptyPowderSnow`|`331`||
  |`PointedDripstoneCauldronDripWater`|`332`||
  |`PointedDripstoneCauldronDripLava`|`333`||
  |`PointedDripstoneDripWater`|`334`||
  |`PointedDripstoneDripLava`|`335`||
  |`CaveVinesPickBerries`|`336`||
  |`BigDripleafTiltDown`|`337`||
  |`BigDripleafTiltUp`|`338`||
  |`CopperWaxOn`|`339`||
  |`CopperWaxOff`|`340`||
  |`Scrape`|`341`||
  |`PlayerHurtDrown`|`342`||
  |`PlayerHurtOnFire`|`343`||
  |`PlayerHurtFreeze`|`344`||
  |`UseSpyglass`|`345`||
  |`StopUsingSpyglass`|`346`||
  |`AmethystBlockChime`|`347`||
  |`AmbientScreamer`|`348`||
  |`HurtScreamer`|`349`||
  |`DeathScreamer`|`350`||
  |`MilkScreamer`|`351`||
  |`JumpToBlock`|`352`||
  |`PreRam`|`353`||
  |`PreRamScreamer`|`354`||
  |`RamImpact`|`355`||
  |`RamImpactScreamer`|`356`||
  |`SquidInkSquirt`|`357`||
  |`GlowSquidInkSquirt`|`358`||
  |`ConvertToStray`|`359`||
  |`CakeAddCandle`|`360`||
  |`ExtinguishCandle`|`361`||
  |`AmbientCandle`|`362`||
  |`BlockClick`|`363`||
  |`BlockClickFail`|`364`||
  |`SculkCatalystBloom`|`365`||
  |`SculkShriekerShriek`|`366`||
  |`NearbyClose`|`367`||
  |`NearbyCloser`|`368`||
  |`NearbyClosest`|`369`||
  |`Agitated`|`370`||
  |`RecordOtherside`|`371`||
  |`Tongue`|`372`||
  |`CrackIronGolem`|`373`||
  |`RepairIronGolem`|`374`||
  |`Listening`|`375`||
  |`Heartbeat`|`376`||
  |`HornBreak`|`377`||
  |`SculkSpread`|`379`||
  |`SculkCharge`|`380`||
  |`SculkSensorPlace`|`381`||
  |`SculkShriekerPlace`|`382`||
  |`GoatCall0`|`383`||
  |`GoatCall1`|`384`||
  |`GoatCall2`|`385`||
  |`GoatCall3`|`386`||
  |`GoatCall4`|`387`||
  |`GoatCall5`|`388`||
  |`GoatCall6`|`389`||
  |`GoatCall7`|`390`||
  |`ImitateWarden`|`426`||
  |`ListeningAngry`|`427`||
  |`Item_Given`|`428`||
  |`Item_Taken`|`429`||
  |`Disappeared`|`430`||
  |`Reappeared`|`431`||
  |`DrinkMilk`|`432`||
  |`FrogspawnHatched`|`433`||
  |`LaySpawn`|`434`||
  |`FrogspawnBreak`|`435`||
  |`SonicBoom`|`436`||
  |`SonicCharge`|`437`||
  |`Item_Thrown`|`438`||
  |`Record5`|`439`||
  |`ConvertToFrog`|`440`||
  |`RecordPlaying`|`441`||
  |`EnchantingTableUse`|`442`||
  |`StepSand`|`443`||
  |`DashReady`|`444`||
  |`BundleDropContents`|`445`||
  |`BundleInsert`|`446`||
  |`BundleRemoveOne`|`447`||
  |`PressurePlateClickOff`|`448`||
  |`PressurePlateClickOn`|`449`||
  |`ButtonClickOff`|`450`||
  |`ButtonClickOn`|`451`||
  |`DoorOpen`|`452`||
  |`DoorClose`|`453`||
  |`TrapdoorOpen`|`454`||
  |`TrapdoorClose`|`455`||
  |`FenceGateOpen`|`456`||
  |`FenceGateClose`|`457`||
  |`Insert`|`458`||
  |`Pickup`|`459`||
  |`InsertEnchanted`|`460`||
  |`PickupEnchanted`|`461`||
  |`Brush`|`462`||
  |`BrushCompleted`|`463`||
  |`ShatterDecoratedPot`|`464`||
  |`BreakDecoratedPot`|`465`||
  |`SnifferEggCrack`|`466`||
  |`SnifferEggHatched`|`467`||
  |`WaxedSignInteractFail`|`468`||
  |`RecordRelic`|`469`||
  |`Bump`|`470`||
  |`PumpkinCarve`|`471`||
  |`ConvertHuskToZombie`|`472`||
  |`PigDeath`|`473`||
  |`HoglinConvertToZombified`|`474`||
  |`AmbientUnderwaterEnter`|`475`||
  |`AmbientUnderwaterExit`|`476`||
  |`BottleFill`|`477`||
  |`BottleEmpty`|`478`||
  |`CrafterCraft`|`479`||
  |`CrafterFail`|`480`||
  |`DecoratedPotInsert`|`481`||
  |`DecoratedPotInsertFail`|`482`||
  |`CrafterDisableSlot`|`483`||
  |`CopperBulbTurnOn`|`490`||
  |`CopperBulbTurnOff`|`491`||
  |`Undefined`|`492`||



////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。


////
//// define
Data：<!-- md:samp varint -->

- 基本类型。


////
//// define
Actor Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

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
//// define
Baby Mob：<!-- md:samp bool -->

- 基本类型。


////
//// define
Global：<!-- md:samp bool -->

- 基本类型。


////

///
