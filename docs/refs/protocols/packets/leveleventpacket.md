# <!-- md:samp LevelEventPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp LevelEventPacket -->数据包，数字ID是`25`。该数据包用于protocol.packet.leveleventpacket.description

## 结构

```viz
digraph "LevelEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="LevelEventPacket",comment="name: \"LevelEventPacket\", typeName: \"\", id: 0, branchId: 25, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Position",comment="name: \"Position\", typeName: \"Vec3\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\""];
4 [label="Vec3",comment="name: \"Vec3\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='LevelEventPacket'
[event_id][position][data]
```

/// html | div.result
//// define
Event ID：<!-- md:samp varint -->

- 基本类型枚举。protocol.packet.leveleventpacket.event_id.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`9800`|`3619`|protocol.enum.9800|
  |`Undefined`|`0`|protocol.enum.undefined|
  |`SoundClick`|`1000`|protocol.enum.soundclick|
  |`SoundClickFail`|`1001`|protocol.enum.soundclickfail|
  |`SoundLaunch`|`1002`|protocol.enum.soundlaunch|
  |`SoundOpenDoor`|`1003`|protocol.enum.soundopendoor|
  |`SoundFizz`|`1004`|protocol.enum.soundfizz|
  |`SoundFuse`|`1005`|protocol.enum.soundfuse|
  |`SoundPlayRecording`|`1006`|protocol.enum.soundplayrecording|
  |`SoundGhastWarning`|`1007`|protocol.enum.soundghastwarning|
  |`SoundGhastFireball`|`1008`|protocol.enum.soundghastfireball|
  |`SoundBlazeFireball`|`1009`|protocol.enum.soundblazefireball|
  |`SoundZombieWoodenDoor`|`1010`|protocol.enum.soundzombiewoodendoor|
  |`SoundZombieDoorCrash`|`1012`|protocol.enum.soundzombiedoorcrash|
  |`SoundZombieInfected`|`1016`|protocol.enum.soundzombieinfected|
  |`SoundZombieConverted`|`1017`|protocol.enum.soundzombieconverted|
  |`SoundEndermanTeleport`|`1018`|protocol.enum.soundendermanteleport|
  |`SoundAnvilBroken`|`1020`|protocol.enum.soundanvilbroken|
  |`SoundAnvilUsed`|`1021`|protocol.enum.soundanvilused|
  |`SoundAnvilLand`|`1022`|protocol.enum.soundanvilland|
  |`SoundInfinityArrowPickup`|`1030`|protocol.enum.soundinfinityarrowpickup|
  |`SoundTeleportEnderPearl`|`1032`|protocol.enum.soundteleportenderpearl|
  |`SoundAddItem`|`1040`|protocol.enum.soundadditem|
  |`SoundItemFrameBreak`|`1041`|protocol.enum.sounditemframebreak|
  |`SoundItemFramePlace`|`1042`|protocol.enum.sounditemframeplace|
  |`SoundItemFrameRemoveItem`|`1043`|protocol.enum.sounditemframeremoveitem|
  |`SoundItemFrameRotateItem`|`1044`|protocol.enum.sounditemframerotateitem|
  |`SoundExperienceOrbPickup`|`1051`|protocol.enum.soundexperienceorbpickup|
  |`SoundTotemUsed`|`1052`|protocol.enum.soundtotemused|
  |`SoundArmorStandBreak`|`1060`|protocol.enum.soundarmorstandbreak|
  |`SoundArmorStandHit`|`1061`|protocol.enum.soundarmorstandhit|
  |`SoundArmorStandLand`|`1062`|protocol.enum.soundarmorstandland|
  |`SoundArmorStandPlace`|`1063`|protocol.enum.soundarmorstandplace|
  |`SoundPointedDripstoneLand`|`1064`|protocol.enum.soundpointeddripstoneland|
  |`SoundDyeUsed`|`1065`|protocol.enum.sounddyeused|
  |`SoundInkSacUsed`|`1066`|protocol.enum.soundinksacused|
  |`SoundAmethystResonate`|`1067`|protocol.enum.soundamethystresonate|
  |`QueueCustomMusic`|`1900`|protocol.enum.queuecustommusic|
  |`PlayCustomMusic`|`1901`|protocol.enum.playcustommusic|
  |`StopCustomMusic`|`1902`|protocol.enum.stopcustommusic|
  |`SetMusicVolume`|`1903`|protocol.enum.setmusicvolume|
  |`ParticlesShoot`|`2000`|protocol.enum.particlesshoot|
  |`ParticlesDestroyBlock`|`2001`|protocol.enum.particlesdestroyblock|
  |`ParticlesPotionSplash`|`2002`|protocol.enum.particlespotionsplash|
  |`ParticlesEyeOfEnderDeath`|`2003`|protocol.enum.particleseyeofenderdeath|
  |`ParticlesMobBlockSpawn`|`2004`|protocol.enum.particlesmobblockspawn|
  |`ParticleCropGrowth`|`2005`|protocol.enum.particlecropgrowth|
  |`ParticleSoundGuardianGhost`|`2006`|protocol.enum.particlesoundguardianghost|
  |`ParticleDeathSmoke`|`2007`|protocol.enum.particledeathsmoke|
  |`ParticleDenyBlock`|`2008`|protocol.enum.particledenyblock|
  |`ParticleGenericSpawn`|`2009`|protocol.enum.particlegenericspawn|
  |`ParticlesDragonEgg`|`2010`|protocol.enum.particlesdragonegg|
  |`ParticlesCropEaten`|`2011`|protocol.enum.particlescropeaten|
  |`ParticlesCrit`|`2012`|protocol.enum.particlescrit|
  |`ParticlesTeleport`|`2013`|protocol.enum.particlesteleport|
  |`ParticlesCrackBlock`|`2014`|protocol.enum.particlescrackblock|
  |`ParticlesBubble`|`2015`|protocol.enum.particlesbubble|
  |`ParticlesEvaporate`|`2016`|protocol.enum.particlesevaporate|
  |`ParticlesDestroyArmorStand`|`2017`|protocol.enum.particlesdestroyarmorstand|
  |`ParticlesBreakingEgg`|`2018`|protocol.enum.particlesbreakingegg|
  |`ParticleDestroyEgg`|`2019`|protocol.enum.particledestroyegg|
  |`ParticlesEvaporateWater`|`2020`|protocol.enum.particlesevaporatewater|
  |`ParticlesDestroyBlockNoSound`|`2021`|protocol.enum.particlesdestroyblocknosound|
  |`ParticlesKnockbackRoar`|`2022`|protocol.enum.particlesknockbackroar|
  |`ParticlesTeleportTrail`|`2023`|protocol.enum.particlesteleporttrail|
  |`ParticlesPointCloud`|`2024`|protocol.enum.particlespointcloud|
  |`ParticlesExplosion`|`2025`|protocol.enum.particlesexplosion|
  |`ParticlesBlockExplosion`|`2026`|protocol.enum.particlesblockexplosion|
  |`ParticlesVibrationSignal`|`2027`|protocol.enum.particlesvibrationsignal|
  |`ParticlesDripstoneDrip`|`2028`|protocol.enum.particlesdripstonedrip|
  |`ParticlesFizzEffect`|`2029`|protocol.enum.particlesfizzeffect|
  |`WaxOn`|`2030`|protocol.enum.waxon|
  |`WaxOff`|`2031`|protocol.enum.waxoff|
  |`Scrape`|`2032`|protocol.enum.scrape|
  |`ParticlesElectricSpark`|`2033`|protocol.enum.particleselectricspark|
  |`ParticleTurtleEgg`|`2034`|protocol.enum.particleturtleegg|
  |`ParticlesSculkShriek`|`2035`|protocol.enum.particlessculkshriek|
  |`SculkCatalystBloom`|`2036`|protocol.enum.sculkcatalystbloom|
  |`SculkCharge`|`2037`|protocol.enum.sculkcharge|
  |`SculkChargePop`|`2038`|protocol.enum.sculkchargepop|
  |`SonicExplosion`|`2039`|protocol.enum.sonicexplosion|
  |`DustPlume`|`2040`|protocol.enum.dustplume|
  |`StartRaining`|`3001`|protocol.enum.startraining|
  |`StartThunderstorm`|`3002`|protocol.enum.startthunderstorm|
  |`StopRaining`|`3003`|protocol.enum.stopraining|
  |`StopThunderstorm`|`3004`|protocol.enum.stopthunderstorm|
  |`GlobalPause`|`3005`|protocol.enum.globalpause|
  |`SimTimeStep`|`3006`|protocol.enum.simtimestep|
  |`SimTimeScale`|`3007`|protocol.enum.simtimescale|
  |`ActivateBlock`|`3500`|protocol.enum.activateblock|
  |`CauldronExplode`|`3501`|protocol.enum.cauldronexplode|
  |`CauldronDyeArmor`|`3502`|protocol.enum.cauldrondyearmor|
  |`CauldronCleanArmor`|`3503`|protocol.enum.cauldroncleanarmor|
  |`CauldronFillPotion`|`3504`|protocol.enum.cauldronfillpotion|
  |`CauldronTakePotion`|`3505`|protocol.enum.cauldrontakepotion|
  |`CauldronFillWater`|`3506`|protocol.enum.cauldronfillwater|
  |`CauldronTakeWater`|`3507`|protocol.enum.cauldrontakewater|
  |`CauldronAddDye`|`3508`|protocol.enum.cauldronadddye|
  |`CauldronCleanBanner`|`3509`|protocol.enum.cauldroncleanbanner|
  |`CauldronFlush`|`3510`|protocol.enum.cauldronflush|
  |`AgentSpawnEffect`|`3511`|protocol.enum.agentspawneffect|
  |`CauldronFillLava`|`3512`|protocol.enum.cauldronfilllava|
  |`CauldronTakeLava`|`3513`|protocol.enum.cauldrontakelava|
  |`CauldronFillPowderSnow`|`3514`|protocol.enum.cauldronfillpowdersnow|
  |`CauldronTakePowderSnow`|`3515`|protocol.enum.cauldrontakepowdersnow|
  |`StartBlockCracking`|`3600`|protocol.enum.startblockcracking|
  |`StopBlockCracking`|`3601`|protocol.enum.stopblockcracking|
  |`UpdateBlockCracking`|`3602`|protocol.enum.updateblockcracking|
  |`ParticlesCrackBlockDown`|`3603`|protocol.enum.particlescrackblockdown|
  |`ParticlesCrackBlockUp`|`3604`|protocol.enum.particlescrackblockup|
  |`ParticlesCrackBlockNorth`|`3605`|protocol.enum.particlescrackblocknorth|
  |`ParticlesCrackBlockSouth`|`3606`|protocol.enum.particlescrackblocksouth|
  |`ParticlesCrackBlockWest`|`3607`|protocol.enum.particlescrackblockwest|
  |`ParticlesCrackBlockEast`|`3608`|protocol.enum.particlescrackblockeast|
  |`ParticlesShootWhiteSmoke`|`3609`|protocol.enum.particlesshootwhitesmoke|
  |`ParticlesBreezeWindExplosion`|`3610`|protocol.enum.particlesbreezewindexplosion|
  |`ParticlesTrialSpawnerDetection`|`3611`|protocol.enum.particlestrialspawnerdetection|
  |`ParticlesTrialSpawnerSpawning`|`3612`|protocol.enum.particlestrialspawnerspawning|
  |`ParticlesTrialSpawnerEjecting`|`3613`|protocol.enum.particlestrialspawnerejecting|
  |`ParticlesWindExplosion`|`3614`|protocol.enum.particleswindexplosion|
  |`ParticlesTrialSpawnerDetectionCharged`|`3615`|protocol.enum.particlestrialspawnerdetectioncharged|
  |`ParticlesTrialSpawnerBecomeCharged`|`3616`|protocol.enum.particlestrialspawnerbecomecharged|
  |`AllPlayersSleeping`|`3617`|protocol.enum.allplayerssleeping|
  |`deprecated`|`3618`|protocol.enum.deprecated|
  |`SleepingPlayers`|`9801`|protocol.enum.sleepingplayers|
  |`JumpPrevented`|`9810`|protocol.enum.jumpprevented|
  |`AnimationVaultActivate`|`9811`|protocol.enum.animationvaultactivate|
  |`AnimationVaultDeactivate`|`9812`|protocol.enum.animationvaultdeactivate|
  |`AnimationVaultEjectItem`|`9813`|protocol.enum.animationvaultejectitem|
  |`AnimationSpawnCobweb`|`9814`|protocol.enum.animationspawncobweb|
  |`ParticleSmashAttackGroundDust`|`9815`|protocol.enum.particlesmashattackgrounddust|
  |`ParticleLegacyEvent`|`0x4000`|protocol.enum.particlelegacyevent|



////
//// define
Position：[<!-- md:samp Vec3 -->](../types/vec3.md)

- 特殊类型。protocol.packet.leveleventpacket.position.descriptionNote about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)


////
//// define
Data：<!-- md:samp varint -->

- 基本类型。protocol.packet.leveleventpacket.data.description


////

///

