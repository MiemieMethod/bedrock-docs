# <!-- md:samp LevelSoundEventPacketV1 -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelSoundEventPacketV1 -->类型，数字ID是`24`。该类型用于protocol.packet.levelsoundeventpacketv1.description

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

- 基本类型枚举。protocol.packet.levelsoundeventpacketv1.event_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`ItemUseOn`|`0`|protocol.enum.itemuseon|
  |`Hit`|`1`|protocol.enum.hit|
  |`Step`|`2`|protocol.enum.step|
  |`Fly`|`3`|protocol.enum.fly|
  |`Jump`|`4`|protocol.enum.jump|
  |`Break`|`5`|protocol.enum.break|
  |`Place`|`6`|protocol.enum.place|
  |`HeavyStep`|`7`|protocol.enum.heavystep|
  |`Gallop`|`8`|protocol.enum.gallop|
  |`Fall`|`9`|protocol.enum.fall|
  |`Ambient`|`10`|protocol.enum.ambient|
  |`AmbientBaby`|`11`|protocol.enum.ambientbaby|
  |`AmbientInWater`|`12`|protocol.enum.ambientinwater|
  |`Breathe`|`13`|protocol.enum.breathe|
  |`Death`|`14`|protocol.enum.death|
  |`DeathInWater`|`15`|protocol.enum.deathinwater|
  |`DeathToZombie`|`16`|protocol.enum.deathtozombie|
  |`Hurt`|`17`|protocol.enum.hurt|
  |`HurtInWater`|`18`|protocol.enum.hurtinwater|
  |`Mad`|`19`|protocol.enum.mad|
  |`Boost`|`20`|protocol.enum.boost|
  |`Bow`|`21`|protocol.enum.bow|
  |`SquishBig`|`22`|protocol.enum.squishbig|
  |`SquishSmall`|`23`|protocol.enum.squishsmall|
  |`FallBig`|`24`|protocol.enum.fallbig|
  |`FallSmall`|`25`|protocol.enum.fallsmall|
  |`Splash`|`26`|protocol.enum.splash|
  |`Fizz`|`27`|protocol.enum.fizz|
  |`Flap`|`28`|protocol.enum.flap|
  |`Swim`|`29`|protocol.enum.swim|
  |`Drink`|`30`|protocol.enum.drink|
  |`Eat`|`31`|protocol.enum.eat|
  |`Takeoff`|`32`|protocol.enum.takeoff|
  |`Shake`|`33`|protocol.enum.shake|
  |`Plop`|`34`|protocol.enum.plop|
  |`Land`|`35`|protocol.enum.land|
  |`Saddle`|`36`|protocol.enum.saddle|
  |`Armor`|`37`|protocol.enum.armor|
  |`ArmorPlace`|`38`|protocol.enum.armorplace|
  |`AddChest`|`39`|protocol.enum.addchest|
  |`Throw`|`40`|protocol.enum.throw|
  |`Attack`|`41`|protocol.enum.attack|
  |`AttackNoDamage`|`42`|protocol.enum.attacknodamage|
  |`AttackStrong`|`43`|protocol.enum.attackstrong|
  |`Warn`|`44`|protocol.enum.warn|
  |`Shear`|`45`|protocol.enum.shear|
  |`Milk`|`46`|protocol.enum.milk|
  |`Thunder`|`47`|protocol.enum.thunder|
  |`Explode`|`48`|protocol.enum.explode|
  |`Fire`|`49`|protocol.enum.fire|
  |`Ignite`|`50`|protocol.enum.ignite|
  |`Fuse`|`51`|protocol.enum.fuse|
  |`Stare`|`52`|protocol.enum.stare|
  |`Spawn`|`53`|protocol.enum.spawn|
  |`Shoot`|`54`|protocol.enum.shoot|
  |`BreakBlock`|`55`|protocol.enum.breakblock|
  |`Launch`|`56`|protocol.enum.launch|
  |`Blast`|`57`|protocol.enum.blast|
  |`LargeBlast`|`58`|protocol.enum.largeblast|
  |`Twinkle`|`59`|protocol.enum.twinkle|
  |`Remedy`|`60`|protocol.enum.remedy|
  |`Unfect`|`61`|protocol.enum.unfect|
  |`LevelUp`|`62`|protocol.enum.levelup|
  |`BowHit`|`63`|protocol.enum.bowhit|
  |`BulletHit`|`64`|protocol.enum.bullethit|
  |`ExtinguishFire`|`65`|protocol.enum.extinguishfire|
  |`ItemFizz`|`66`|protocol.enum.itemfizz|
  |`ChestOpen`|`67`|protocol.enum.chestopen|
  |`ChestClosed`|`68`|protocol.enum.chestclosed|
  |`ShulkerBoxOpen`|`69`|protocol.enum.shulkerboxopen|
  |`ShulkerBoxClosed`|`70`|protocol.enum.shulkerboxclosed|
  |`EnderChestOpen`|`71`|protocol.enum.enderchestopen|
  |`EnderChestClosed`|`72`|protocol.enum.enderchestclosed|
  |`PowerOn`|`73`|protocol.enum.poweron|
  |`PowerOff`|`74`|protocol.enum.poweroff|
  |`Attach`|`75`|protocol.enum.attach|
  |`Detach`|`76`|protocol.enum.detach|
  |`Deny`|`77`|protocol.enum.deny|
  |`Tripod`|`78`|protocol.enum.tripod|
  |`Pop`|`79`|protocol.enum.pop|
  |`DropSlot`|`80`|protocol.enum.dropslot|
  |`Note`|`81`|protocol.enum.note|
  |`Thorns`|`82`|protocol.enum.thorns|
  |`PistonIn`|`83`|protocol.enum.pistonin|
  |`PistonOut`|`84`|protocol.enum.pistonout|
  |`Portal`|`85`|protocol.enum.portal|
  |`Water`|`86`|protocol.enum.water|
  |`LavaPop`|`87`|protocol.enum.lavapop|
  |`Lava`|`88`|protocol.enum.lava|
  |`Burp`|`89`|protocol.enum.burp|
  |`BucketFillWater`|`90`|protocol.enum.bucketfillwater|
  |`BucketFillLava`|`91`|protocol.enum.bucketfilllava|
  |`BucketEmptyWater`|`92`|protocol.enum.bucketemptywater|
  |`BucketEmptyLava`|`93`|protocol.enum.bucketemptylava|
  |`EquipChain`|`94`|protocol.enum.equipchain|
  |`EquipDiamond`|`95`|protocol.enum.equipdiamond|
  |`EquipGeneric`|`96`|protocol.enum.equipgeneric|
  |`EquipGold`|`97`|protocol.enum.equipgold|
  |`EquipIron`|`98`|protocol.enum.equipiron|
  |`EquipLeather`|`99`|protocol.enum.equipleather|
  |`EquipElytra`|`100`|protocol.enum.equipelytra|
  |`Record13`|`101`|protocol.enum.record13|
  |`RecordCat`|`102`|protocol.enum.recordcat|
  |`RecordBlocks`|`103`|protocol.enum.recordblocks|
  |`RecordChirp`|`104`|protocol.enum.recordchirp|
  |`RecordFar`|`105`|protocol.enum.recordfar|
  |`RecordMall`|`106`|protocol.enum.recordmall|
  |`RecordMellohi`|`107`|protocol.enum.recordmellohi|
  |`RecordStal`|`108`|protocol.enum.recordstal|
  |`RecordStrad`|`109`|protocol.enum.recordstrad|
  |`RecordWard`|`110`|protocol.enum.recordward|
  |`Record11`|`111`|protocol.enum.record11|
  |`RecordWait`|`112`|protocol.enum.recordwait|
  |`RecordNull`|`113`|protocol.enum.recordnull|
  |`Flop`|`114`|protocol.enum.flop|
  |`GuardianCurse`|`115`|protocol.enum.guardiancurse|
  |`MobWarning`|`116`|protocol.enum.mobwarning|
  |`MobWarningBaby`|`117`|protocol.enum.mobwarningbaby|
  |`Teleport`|`118`|protocol.enum.teleport|
  |`ShulkerOpen`|`119`|protocol.enum.shulkeropen|
  |`ShulkerClose`|`120`|protocol.enum.shulkerclose|
  |`Haggle`|`121`|protocol.enum.haggle|
  |`HaggleYes`|`122`|protocol.enum.haggleyes|
  |`HaggleNo`|`123`|protocol.enum.haggleno|
  |`HaggleIdle`|`124`|protocol.enum.haggleidle|
  |`ChorusGrow`|`125`|protocol.enum.chorusgrow|
  |`ChorusDeath`|`126`|protocol.enum.chorusdeath|
  |`Glass`|`127`|protocol.enum.glass|
  |`PotionBrewed`|`128`|protocol.enum.potionbrewed|
  |`CastSpell`|`129`|protocol.enum.castspell|
  |`PrepareAttackSpell`|`130`|protocol.enum.prepareattackspell|
  |`PrepareSummon`|`131`|protocol.enum.preparesummon|
  |`PrepareWololo`|`132`|protocol.enum.preparewololo|
  |`Fang`|`133`|protocol.enum.fang|
  |`Charge`|`134`|protocol.enum.charge|
  |`TakePicture`|`135`|protocol.enum.takepicture|
  |`PlaceLeashKnot`|`136`|protocol.enum.placeleashknot|
  |`BreakLeashKnot`|`137`|protocol.enum.breakleashknot|
  |`AmbientGrowl`|`138`|protocol.enum.ambientgrowl|
  |`AmbientWhine`|`139`|protocol.enum.ambientwhine|
  |`AmbientPant`|`140`|protocol.enum.ambientpant|
  |`AmbientPurr`|`141`|protocol.enum.ambientpurr|
  |`AmbientPurreow`|`142`|protocol.enum.ambientpurreow|
  |`DeathMinVolume`|`143`|protocol.enum.deathminvolume|
  |`DeathMidVolume`|`144`|protocol.enum.deathmidvolume|
  |`ImitateBlaze`|`145`|protocol.enum.imitateblaze|
  |`ImitateCaveSpider`|`146`|protocol.enum.imitatecavespider|
  |`ImitateCreeper`|`147`|protocol.enum.imitatecreeper|
  |`ImitateElderGuardian`|`148`|protocol.enum.imitateelderguardian|
  |`ImitateEnderDragon`|`149`|protocol.enum.imitateenderdragon|
  |`ImitateEnderman`|`150`|protocol.enum.imitateenderman|
  |`ImitateEndermite`|`151`|protocol.enum.imitateendermite|
  |`ImitateEvocationIllager`|`152`|protocol.enum.imitateevocationillager|
  |`ImitateGhast`|`153`|protocol.enum.imitateghast|
  |`ImitateHusk`|`154`|protocol.enum.imitatehusk|
  |`ImitateIllusionIllager`|`155`|protocol.enum.imitateillusionillager|
  |`ImitateMagmaCube`|`156`|protocol.enum.imitatemagmacube|
  |`ImitatePolarBear`|`157`|protocol.enum.imitatepolarbear|
  |`ImitateShulker`|`158`|protocol.enum.imitateshulker|
  |`ImitateSilverfish`|`159`|protocol.enum.imitatesilverfish|
  |`ImitateSkeleton`|`160`|protocol.enum.imitateskeleton|
  |`ImitateSlime`|`161`|protocol.enum.imitateslime|
  |`ImitateSpider`|`162`|protocol.enum.imitatespider|
  |`ImitateStray`|`163`|protocol.enum.imitatestray|
  |`ImitateVex`|`164`|protocol.enum.imitatevex|
  |`ImitateVindicationIllager`|`165`|protocol.enum.imitatevindicationillager|
  |`ImitateWitch`|`166`|protocol.enum.imitatewitch|
  |`ImitateWither`|`167`|protocol.enum.imitatewither|
  |`ImitateWitherSkeleton`|`168`|protocol.enum.imitatewitherskeleton|
  |`ImitateWolf`|`169`|protocol.enum.imitatewolf|
  |`ImitateZombie`|`170`|protocol.enum.imitatezombie|
  |`ImitateZombiePigman`|`171`|protocol.enum.imitatezombiepigman|
  |`ImitateZombieVillager`|`172`|protocol.enum.imitatezombievillager|
  |`EnderEyePlaced`|`173`|protocol.enum.endereyeplaced|
  |`EndPortalCreated`|`174`|protocol.enum.endportalcreated|
  |`AnvilUse`|`175`|protocol.enum.anviluse|
  |`BottleDragonBreath`|`176`|protocol.enum.bottledragonbreath|
  |`PortalTravel`|`177`|protocol.enum.portaltravel|
  |`TridentHit`|`178`|protocol.enum.tridenthit|
  |`TridentReturn`|`179`|protocol.enum.tridentreturn|
  |`TridentRiptide_1`|`180`|protocol.enum.tridentriptide_1|
  |`TridentRiptide_2`|`181`|protocol.enum.tridentriptide_2|
  |`TridentRiptide_3`|`182`|protocol.enum.tridentriptide_3|
  |`TridentThrow`|`183`|protocol.enum.tridentthrow|
  |`TridentThunder`|`184`|protocol.enum.tridentthunder|
  |`TridentHitGround`|`185`|protocol.enum.tridenthitground|
  |`Default`|`186`|protocol.enum.default|
  |`FletchingTableUse`|`187`|protocol.enum.fletchingtableuse|
  |`ElemConstructOpen`|`188`|protocol.enum.elemconstructopen|
  |`IceBombHit`|`189`|protocol.enum.icebombhit|
  |`BalloonPop`|`190`|protocol.enum.balloonpop|
  |`LTReactionIceBomb`|`191`|protocol.enum.ltreactionicebomb|
  |`LTReactionBleach`|`192`|protocol.enum.ltreactionbleach|
  |`LTReactionElephantToothpaste`|`193`|protocol.enum.ltreactionelephanttoothpaste|
  |`LTReactionElephantToothpaste2`|`194`|protocol.enum.ltreactionelephanttoothpaste2|
  |`LTReactionGlowStick`|`195`|protocol.enum.ltreactionglowstick|
  |`LTReactionGlowStick2`|`196`|protocol.enum.ltreactionglowstick2|
  |`LTReactionLuminol`|`197`|protocol.enum.ltreactionluminol|
  |`LTReactionSalt`|`198`|protocol.enum.ltreactionsalt|
  |`LTReactionFertilizer`|`199`|protocol.enum.ltreactionfertilizer|
  |`LTReactionFireball`|`200`|protocol.enum.ltreactionfireball|
  |`LTReactionMagnesiumSalt`|`201`|protocol.enum.ltreactionmagnesiumsalt|
  |`LTReactionMiscFire`|`202`|protocol.enum.ltreactionmiscfire|
  |`LTReactionFire`|`203`|protocol.enum.ltreactionfire|
  |`LTReactionMiscExplosion`|`204`|protocol.enum.ltreactionmiscexplosion|
  |`LTReactionMiscMystical`|`205`|protocol.enum.ltreactionmiscmystical|
  |`LTReactionMiscMystical2`|`206`|protocol.enum.ltreactionmiscmystical2|
  |`LTReactionProduct`|`207`|protocol.enum.ltreactionproduct|
  |`SparklerUse`|`208`|protocol.enum.sparkleruse|
  |`GlowStickUse`|`209`|protocol.enum.glowstickuse|
  |`SparklerActive`|`210`|protocol.enum.sparkleractive|
  |`ConvertToDrowned`|`211`|protocol.enum.converttodrowned|
  |`BucketFillFish`|`212`|protocol.enum.bucketfillfish|
  |`BucketEmptyFish`|`213`|protocol.enum.bucketemptyfish|
  |`BubbleColumnUpwards`|`214`|protocol.enum.bubblecolumnupwards|
  |`BubbleColumnDownwards`|`215`|protocol.enum.bubblecolumndownwards|
  |`BubblePop`|`216`|protocol.enum.bubblepop|
  |`BubbleUpInside`|`217`|protocol.enum.bubbleupinside|
  |`BubbleDownInside`|`218`|protocol.enum.bubbledowninside|
  |`HurtBaby`|`219`|protocol.enum.hurtbaby|
  |`DeathBaby`|`220`|protocol.enum.deathbaby|
  |`StepBaby`|`221`|protocol.enum.stepbaby|
  |`SpawnBaby`|`222`|protocol.enum.spawnbaby|
  |`Born`|`223`|protocol.enum.born|
  |`TurtleEggBreak`|`224`|protocol.enum.turtleeggbreak|
  |`TurtleEggCrack`|`225`|protocol.enum.turtleeggcrack|
  |`TurtleEggHatched`|`226`|protocol.enum.turtleegghatched|
  |`LayEgg`|`227`|protocol.enum.layegg|
  |`TurtleEggAttacked`|`228`|protocol.enum.turtleeggattacked|
  |`BeaconActivate`|`229`|protocol.enum.beaconactivate|
  |`BeaconAmbient`|`230`|protocol.enum.beaconambient|
  |`BeaconDeactivate`|`231`|protocol.enum.beacondeactivate|
  |`BeaconPower`|`232`|protocol.enum.beaconpower|
  |`ConduitActivate`|`233`|protocol.enum.conduitactivate|
  |`ConduitAmbient`|`234`|protocol.enum.conduitambient|
  |`ConduitAttack`|`235`|protocol.enum.conduitattack|
  |`ConduitDeactivate`|`236`|protocol.enum.conduitdeactivate|
  |`ConduitShort`|`237`|protocol.enum.conduitshort|
  |`Swoop`|`238`|protocol.enum.swoop|
  |`BambooSaplingPlace`|`239`|protocol.enum.bamboosaplingplace|
  |`PreSneeze`|`240`|protocol.enum.presneeze|
  |`Sneeze`|`241`|protocol.enum.sneeze|
  |`AmbientTame`|`242`|protocol.enum.ambienttame|
  |`Scared`|`243`|protocol.enum.scared|
  |`ScaffoldingClimb`|`244`|protocol.enum.scaffoldingclimb|
  |`CrossbowLoadingStart`|`245`|protocol.enum.crossbowloadingstart|
  |`CrossbowLoadingMiddle`|`246`|protocol.enum.crossbowloadingmiddle|
  |`CrossbowLoadingEnd`|`247`|protocol.enum.crossbowloadingend|
  |`CrossbowShoot`|`248`|protocol.enum.crossbowshoot|
  |`CrossbowQuickChargeStart`|`249`|protocol.enum.crossbowquickchargestart|
  |`CrossbowQuickChargeMiddle`|`250`|protocol.enum.crossbowquickchargemiddle|
  |`CrossbowQuickChargeEnd`|`251`|protocol.enum.crossbowquickchargeend|
  |`AmbientAggressive`|`252`|protocol.enum.ambientaggressive|
  |`AmbientWorried`|`253`|protocol.enum.ambientworried|
  |`CantBreed`|`254`|protocol.enum.cantbreed|
  |`ShieldBlock`|`255`|protocol.enum.shieldblock|
  |`LecternBookPlace`|`256`|protocol.enum.lecternbookplace|
  |`GrindstoneUse`|`257`|protocol.enum.grindstoneuse|
  |`Bell`|`258`|protocol.enum.bell|
  |`CampfireCrackle`|`259`|protocol.enum.campfirecrackle|
  |`Roar`|`260`|protocol.enum.roar|
  |`Stun`|`261`|protocol.enum.stun|
  |`SweetBerryBushHurt`|`262`|protocol.enum.sweetberrybushhurt|
  |`SweetBerryBushPick`|`263`|protocol.enum.sweetberrybushpick|
  |`CartographyTableUse`|`264`|protocol.enum.cartographytableuse|
  |`StonecutterUse`|`265`|protocol.enum.stonecutteruse|
  |`ComposterEmpty`|`266`|protocol.enum.composterempty|
  |`ComposterFill`|`267`|protocol.enum.composterfill|
  |`ComposterFillLayer`|`268`|protocol.enum.composterfilllayer|
  |`ComposterReady`|`269`|protocol.enum.composterready|
  |`BarrelOpen`|`270`|protocol.enum.barrelopen|
  |`BarrelClose`|`271`|protocol.enum.barrelclose|
  |`RaidHorn`|`272`|protocol.enum.raidhorn|
  |`LoomUse`|`273`|protocol.enum.loomuse|
  |`AmbientInRaid`|`274`|protocol.enum.ambientinraid|
  |`UICartographyTableUse`|`275`|protocol.enum.uicartographytableuse|
  |`UIStonecutterUse`|`276`|protocol.enum.uistonecutteruse|
  |`UILoomUse`|`277`|protocol.enum.uiloomuse|
  |`SmokerUse`|`278`|protocol.enum.smokeruse|
  |`BlastFurnaceUse`|`279`|protocol.enum.blastfurnaceuse|
  |`SmithingTableUse`|`280`|protocol.enum.smithingtableuse|
  |`Screech`|`281`|protocol.enum.screech|
  |`Sleep`|`282`|protocol.enum.sleep|
  |`FurnaceUse`|`283`|protocol.enum.furnaceuse|
  |`MooshroomConvert`|`284`|protocol.enum.mooshroomconvert|
  |`MilkSuspiciously`|`285`|protocol.enum.milksuspiciously|
  |`Celebrate`|`286`|protocol.enum.celebrate|
  |`JumpPrevent`|`287`|protocol.enum.jumpprevent|
  |`AmbientPollinate`|`288`|protocol.enum.ambientpollinate|
  |`BeehiveDrip`|`289`|protocol.enum.beehivedrip|
  |`BeehiveEnter`|`290`|protocol.enum.beehiveenter|
  |`BeehiveExit`|`291`|protocol.enum.beehiveexit|
  |`BeehiveWork`|`292`|protocol.enum.beehivework|
  |`BeehiveShear`|`293`|protocol.enum.beehiveshear|
  |`HoneybottleDrink`|`294`|protocol.enum.honeybottledrink|
  |`AmbientCave`|`295`|protocol.enum.ambientcave|
  |`Retreat`|`296`|protocol.enum.retreat|
  |`ConvertToZombified`|`297`|protocol.enum.converttozombified|
  |`Admire`|`298`|protocol.enum.admire|
  |`StepLava`|`299`|protocol.enum.steplava|
  |`Tempt`|`300`|protocol.enum.tempt|
  |`Panic`|`301`|protocol.enum.panic|
  |`Angry`|`302`|protocol.enum.angry|
  |`AmbientMoodWarpedForest`|`303`|protocol.enum.ambientmoodwarpedforest|
  |`AmbientMoodSoulsandValley`|`304`|protocol.enum.ambientmoodsoulsandvalley|
  |`AmbientMoodNetherWastes`|`305`|protocol.enum.ambientmoodnetherwastes|
  |`AmbientMoodBasaltDeltas`|`306`|protocol.enum.ambientmoodbasaltdeltas|
  |`AmbientMoodCrimsonForest`|`307`|protocol.enum.ambientmoodcrimsonforest|
  |`RespawnAnchorCharge`|`308`|protocol.enum.respawnanchorcharge|
  |`RespawnAnchorDeplete`|`309`|protocol.enum.respawnanchordeplete|
  |`RespawnAnchorSetSpawn`|`310`|protocol.enum.respawnanchorsetspawn|
  |`RespawnAnchorAmbient`|`311`|protocol.enum.respawnanchorambient|
  |`SoulEscapeQuiet`|`312`|protocol.enum.soulescapequiet|
  |`SoulEscapeLoud`|`313`|protocol.enum.soulescapeloud|
  |`RecordPigstep`|`314`|protocol.enum.recordpigstep|
  |`LinkCompassToLodestone`|`315`|protocol.enum.linkcompasstolodestone|
  |`UseSmithingTable`|`316`|protocol.enum.usesmithingtable|
  |`EquipNetherite`|`317`|protocol.enum.equipnetherite|
  |`AmbientLoopWarpedForest`|`318`|protocol.enum.ambientloopwarpedforest|
  |`AmbientLoopSoulsandValley`|`319`|protocol.enum.ambientloopsoulsandvalley|
  |`AmbientLoopNetherWastes`|`320`|protocol.enum.ambientloopnetherwastes|
  |`AmbientLoopBasaltDeltas`|`321`|protocol.enum.ambientloopbasaltdeltas|
  |`AmbientLoopCrimsonForest`|`322`|protocol.enum.ambientloopcrimsonforest|
  |`AmbientAdditionWarpedForest`|`323`|protocol.enum.ambientadditionwarpedforest|
  |`AmbientAdditionSoulsandValley`|`324`|protocol.enum.ambientadditionsoulsandvalley|
  |`AmbientAdditionNetherWastes`|`325`|protocol.enum.ambientadditionnetherwastes|
  |`AmbientAdditionBasaltDeltas`|`326`|protocol.enum.ambientadditionbasaltdeltas|
  |`AmbientAdditionCrimsonForest`|`327`|protocol.enum.ambientadditioncrimsonforest|
  |`SculkSensorPowerOn`|`328`|protocol.enum.sculksensorpoweron|
  |`SculkSensorPowerOff`|`329`|protocol.enum.sculksensorpoweroff|
  |`BucketFillPowderSnow`|`330`|protocol.enum.bucketfillpowdersnow|
  |`BucketEmptyPowderSnow`|`331`|protocol.enum.bucketemptypowdersnow|
  |`PointedDripstoneCauldronDripWater`|`332`|protocol.enum.pointeddripstonecauldrondripwater|
  |`PointedDripstoneCauldronDripLava`|`333`|protocol.enum.pointeddripstonecauldrondriplava|
  |`PointedDripstoneDripWater`|`334`|protocol.enum.pointeddripstonedripwater|
  |`PointedDripstoneDripLava`|`335`|protocol.enum.pointeddripstonedriplava|
  |`CaveVinesPickBerries`|`336`|protocol.enum.cavevinespickberries|
  |`BigDripleafTiltDown`|`337`|protocol.enum.bigdripleaftiltdown|
  |`BigDripleafTiltUp`|`338`|protocol.enum.bigdripleaftiltup|
  |`CopperWaxOn`|`339`|protocol.enum.copperwaxon|
  |`CopperWaxOff`|`340`|protocol.enum.copperwaxoff|
  |`Scrape`|`341`|protocol.enum.scrape|
  |`PlayerHurtDrown`|`342`|protocol.enum.playerhurtdrown|
  |`PlayerHurtOnFire`|`343`|protocol.enum.playerhurtonfire|
  |`PlayerHurtFreeze`|`344`|protocol.enum.playerhurtfreeze|
  |`UseSpyglass`|`345`|protocol.enum.usespyglass|
  |`StopUsingSpyglass`|`346`|protocol.enum.stopusingspyglass|
  |`AmethystBlockChime`|`347`|protocol.enum.amethystblockchime|
  |`AmbientScreamer`|`348`|protocol.enum.ambientscreamer|
  |`HurtScreamer`|`349`|protocol.enum.hurtscreamer|
  |`DeathScreamer`|`350`|protocol.enum.deathscreamer|
  |`MilkScreamer`|`351`|protocol.enum.milkscreamer|
  |`JumpToBlock`|`352`|protocol.enum.jumptoblock|
  |`PreRam`|`353`|protocol.enum.preram|
  |`PreRamScreamer`|`354`|protocol.enum.preramscreamer|
  |`RamImpact`|`355`|protocol.enum.ramimpact|
  |`RamImpactScreamer`|`356`|protocol.enum.ramimpactscreamer|
  |`SquidInkSquirt`|`357`|protocol.enum.squidinksquirt|
  |`GlowSquidInkSquirt`|`358`|protocol.enum.glowsquidinksquirt|
  |`ConvertToStray`|`359`|protocol.enum.converttostray|
  |`CakeAddCandle`|`360`|protocol.enum.cakeaddcandle|
  |`ExtinguishCandle`|`361`|protocol.enum.extinguishcandle|
  |`AmbientCandle`|`362`|protocol.enum.ambientcandle|
  |`BlockClick`|`363`|protocol.enum.blockclick|
  |`BlockClickFail`|`364`|protocol.enum.blockclickfail|
  |`SculkCatalystBloom`|`365`|protocol.enum.sculkcatalystbloom|
  |`SculkShriekerShriek`|`366`|protocol.enum.sculkshriekershriek|
  |`NearbyClose`|`367`|protocol.enum.nearbyclose|
  |`NearbyCloser`|`368`|protocol.enum.nearbycloser|
  |`NearbyClosest`|`369`|protocol.enum.nearbyclosest|
  |`Agitated`|`370`|protocol.enum.agitated|
  |`RecordOtherside`|`371`|protocol.enum.recordotherside|
  |`Tongue`|`372`|protocol.enum.tongue|
  |`CrackIronGolem`|`373`|protocol.enum.crackirongolem|
  |`RepairIronGolem`|`374`|protocol.enum.repairirongolem|
  |`Listening`|`375`|protocol.enum.listening|
  |`Heartbeat`|`376`|protocol.enum.heartbeat|
  |`HornBreak`|`377`|protocol.enum.hornbreak|
  |`SculkSpread`|`379`|protocol.enum.sculkspread|
  |`SculkCharge`|`380`|protocol.enum.sculkcharge|
  |`SculkSensorPlace`|`381`|protocol.enum.sculksensorplace|
  |`SculkShriekerPlace`|`382`|protocol.enum.sculkshriekerplace|
  |`GoatCall0`|`383`|protocol.enum.goatcall0|
  |`GoatCall1`|`384`|protocol.enum.goatcall1|
  |`GoatCall2`|`385`|protocol.enum.goatcall2|
  |`GoatCall3`|`386`|protocol.enum.goatcall3|
  |`GoatCall4`|`387`|protocol.enum.goatcall4|
  |`GoatCall5`|`388`|protocol.enum.goatcall5|
  |`GoatCall6`|`389`|protocol.enum.goatcall6|
  |`GoatCall7`|`390`|protocol.enum.goatcall7|
  |`ImitateWarden`|`426`|protocol.enum.imitatewarden|
  |`ListeningAngry`|`427`|protocol.enum.listeningangry|
  |`Item_Given`|`428`|protocol.enum.item_given|
  |`Item_Taken`|`429`|protocol.enum.item_taken|
  |`Disappeared`|`430`|protocol.enum.disappeared|
  |`Reappeared`|`431`|protocol.enum.reappeared|
  |`DrinkMilk`|`432`|protocol.enum.drinkmilk|
  |`FrogspawnHatched`|`433`|protocol.enum.frogspawnhatched|
  |`LaySpawn`|`434`|protocol.enum.layspawn|
  |`FrogspawnBreak`|`435`|protocol.enum.frogspawnbreak|
  |`SonicBoom`|`436`|protocol.enum.sonicboom|
  |`SonicCharge`|`437`|protocol.enum.soniccharge|
  |`Item_Thrown`|`438`|protocol.enum.item_thrown|
  |`Record5`|`439`|protocol.enum.record5|
  |`ConvertToFrog`|`440`|protocol.enum.converttofrog|
  |`RecordPlaying`|`441`|protocol.enum.recordplaying|
  |`EnchantingTableUse`|`442`|protocol.enum.enchantingtableuse|
  |`StepSand`|`443`|protocol.enum.stepsand|
  |`DashReady`|`444`|protocol.enum.dashready|
  |`BundleDropContents`|`445`|protocol.enum.bundledropcontents|
  |`BundleInsert`|`446`|protocol.enum.bundleinsert|
  |`BundleRemoveOne`|`447`|protocol.enum.bundleremoveone|
  |`PressurePlateClickOff`|`448`|protocol.enum.pressureplateclickoff|
  |`PressurePlateClickOn`|`449`|protocol.enum.pressureplateclickon|
  |`ButtonClickOff`|`450`|protocol.enum.buttonclickoff|
  |`ButtonClickOn`|`451`|protocol.enum.buttonclickon|
  |`DoorOpen`|`452`|protocol.enum.dooropen|
  |`DoorClose`|`453`|protocol.enum.doorclose|
  |`TrapdoorOpen`|`454`|protocol.enum.trapdooropen|
  |`TrapdoorClose`|`455`|protocol.enum.trapdoorclose|
  |`FenceGateOpen`|`456`|protocol.enum.fencegateopen|
  |`FenceGateClose`|`457`|protocol.enum.fencegateclose|
  |`Insert`|`458`|protocol.enum.insert|
  |`Pickup`|`459`|protocol.enum.pickup|
  |`InsertEnchanted`|`460`|protocol.enum.insertenchanted|
  |`PickupEnchanted`|`461`|protocol.enum.pickupenchanted|
  |`Brush`|`462`|protocol.enum.brush|
  |`BrushCompleted`|`463`|protocol.enum.brushcompleted|
  |`ShatterDecoratedPot`|`464`|protocol.enum.shatterdecoratedpot|
  |`BreakDecoratedPot`|`465`|protocol.enum.breakdecoratedpot|
  |`SnifferEggCrack`|`466`|protocol.enum.sniffereggcrack|
  |`SnifferEggHatched`|`467`|protocol.enum.snifferegghatched|
  |`WaxedSignInteractFail`|`468`|protocol.enum.waxedsigninteractfail|
  |`RecordRelic`|`469`|protocol.enum.recordrelic|
  |`Bump`|`470`|protocol.enum.bump|
  |`PumpkinCarve`|`471`|protocol.enum.pumpkincarve|
  |`ConvertHuskToZombie`|`472`|protocol.enum.converthusktozombie|
  |`PigDeath`|`473`|protocol.enum.pigdeath|
  |`HoglinConvertToZombified`|`474`|protocol.enum.hoglinconverttozombified|
  |`AmbientUnderwaterEnter`|`475`|protocol.enum.ambientunderwaterenter|
  |`AmbientUnderwaterExit`|`476`|protocol.enum.ambientunderwaterexit|
  |`BottleFill`|`477`|protocol.enum.bottlefill|
  |`BottleEmpty`|`478`|protocol.enum.bottleempty|
  |`CrafterCraft`|`479`|protocol.enum.craftercraft|
  |`CrafterFail`|`480`|protocol.enum.crafterfail|
  |`DecoratedPotInsert`|`481`|protocol.enum.decoratedpotinsert|
  |`DecoratedPotInsertFail`|`482`|protocol.enum.decoratedpotinsertfail|
  |`CrafterDisableSlot`|`483`|protocol.enum.crafterdisableslot|
  |`CopperBulbTurnOn`|`490`|protocol.enum.copperbulbturnon|
  |`CopperBulbTurnOff`|`491`|protocol.enum.copperbulbturnoff|
  |`Undefined`|`492`|protocol.enum.undefined|



////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.levelsoundeventpacketv1.position.description


////
//// define
Data：<!-- md:samp varint -->

- 基本类型。protocol.packet.levelsoundeventpacketv1.data.description


////
//// define
Actor Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.levelsoundeventpacketv1.actor_type.description枚举值如下：

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
  |`Bogged`|`144| SkeletonMonster`|protocol.enum.bogged|



////
//// define
Baby Mob：<!-- md:samp bool -->

- 基本类型。protocol.packet.levelsoundeventpacketv1.baby_mob.description


////
//// define
Global：<!-- md:samp bool -->

- 基本类型。protocol.packet.levelsoundeventpacketv1.global.description


////

///

