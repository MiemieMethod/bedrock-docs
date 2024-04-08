# <!-- md:samp LevelEventGenericPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelEventGenericPacket -->数据包，数字ID是`124`。

## 结构

```viz
digraph "LevelEventGenericPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4

0 [label="LevelEventGenericPacket",comment="name: \"LevelEventGenericPacket\", typeName: \"\", id: 0, branchId: 124, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 1, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: LevelEvent\""];
2 [label="varint",comment="name: \"varint\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event Data",comment="name: \"Event Data\", typeName: \"CompoundTag\", id: 3, branchId: 0, recurseId: -1, attributes: 256, notes: \"Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)\""];
4 [label="CompoundTag",comment="name: \"CompoundTag\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4}

}

```

## 字段

```title='LevelEventGenericPacket'
[event_id][event_data]
```

/// html | div.result
//// define
Event ID：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`9800`|`3617`||
  |`Undefined`|`0`||
  |`SoundClick`|`1000`||
  |`SoundClickFail`|`1001`||
  |`SoundLaunch`|`1002`||
  |`SoundOpenDoor`|`1003`||
  |`SoundFizz`|`1004`||
  |`SoundFuse`|`1005`||
  |`SoundPlayRecording`|`1006`||
  |`SoundGhastWarning`|`1007`||
  |`SoundGhastFireball`|`1008`||
  |`SoundBlazeFireball`|`1009`||
  |`SoundZombieWoodenDoor`|`1010`||
  |`SoundZombieDoorCrash`|`1012`||
  |`SoundZombieInfected`|`1016`||
  |`SoundZombieConverted`|`1017`||
  |`SoundEndermanTeleport`|`1018`||
  |`SoundAnvilBroken`|`1020`||
  |`SoundAnvilUsed`|`1021`||
  |`SoundAnvilLand`|`1022`||
  |`SoundInfinityArrowPickup`|`1030`||
  |`SoundTeleportEnderPearl`|`1032`||
  |`SoundAddItem`|`1040`||
  |`SoundItemFrameBreak`|`1041`||
  |`SoundItemFramePlace`|`1042`||
  |`SoundItemFrameRemoveItem`|`1043`||
  |`SoundItemFrameRotateItem`|`1044`||
  |`SoundExperienceOrbPickup`|`1051`||
  |`SoundTotemUsed`|`1052`||
  |`SoundArmorStandBreak`|`1060`||
  |`SoundArmorStandHit`|`1061`||
  |`SoundArmorStandLand`|`1062`||
  |`SoundArmorStandPlace`|`1063`||
  |`SoundPointedDripstoneLand`|`1064`||
  |`SoundDyeUsed`|`1065`||
  |`SoundInkSacUsed`|`1066`||
  |`SoundAmethystResonate`|`1067`||
  |`QueueCustomMusic`|`1900`||
  |`PlayCustomMusic`|`1901`||
  |`StopCustomMusic`|`1902`||
  |`SetMusicVolume`|`1903`||
  |`ParticlesShoot`|`2000`||
  |`ParticlesDestroyBlock`|`2001`||
  |`ParticlesPotionSplash`|`2002`||
  |`ParticlesEyeOfEnderDeath`|`2003`||
  |`ParticlesMobBlockSpawn`|`2004`||
  |`ParticleCropGrowth`|`2005`||
  |`ParticleSoundGuardianGhost`|`2006`||
  |`ParticleDeathSmoke`|`2007`||
  |`ParticleDenyBlock`|`2008`||
  |`ParticleGenericSpawn`|`2009`||
  |`ParticlesDragonEgg`|`2010`||
  |`ParticlesCropEaten`|`2011`||
  |`ParticlesCrit`|`2012`||
  |`ParticlesTeleport`|`2013`||
  |`ParticlesCrackBlock`|`2014`||
  |`ParticlesBubble`|`2015`||
  |`ParticlesEvaporate`|`2016`||
  |`ParticlesDestroyArmorStand`|`2017`||
  |`ParticlesBreakingEgg`|`2018`||
  |`ParticleDestroyEgg`|`2019`||
  |`ParticlesEvaporateWater`|`2020`||
  |`ParticlesDestroyBlockNoSound`|`2021`||
  |`ParticlesKnockbackRoar`|`2022`||
  |`ParticlesTeleportTrail`|`2023`||
  |`ParticlesPointCloud`|`2024`||
  |`ParticlesExplosion`|`2025`||
  |`ParticlesBlockExplosion`|`2026`||
  |`ParticlesVibrationSignal`|`2027`||
  |`ParticlesDripstoneDrip`|`2028`||
  |`ParticlesFizzEffect`|`2029`||
  |`WaxOn`|`2030`||
  |`WaxOff`|`2031`||
  |`Scrape`|`2032`||
  |`ParticlesElectricSpark`|`2033`||
  |`ParticleTurtleEgg`|`2034`||
  |`ParticlesSculkShriek`|`2035`||
  |`SculkCatalystBloom`|`2036`||
  |`SculkCharge`|`2037`||
  |`SculkChargePop`|`2038`||
  |`SonicExplosion`|`2039`||
  |`DustPlume`|`2040`||
  |`StartRaining`|`3001`||
  |`StartThunderstorm`|`3002`||
  |`StopRaining`|`3003`||
  |`StopThunderstorm`|`3004`||
  |`GlobalPause`|`3005`||
  |`SimTimeStep`|`3006`||
  |`SimTimeScale`|`3007`||
  |`ActivateBlock`|`3500`||
  |`CauldronExplode`|`3501`||
  |`CauldronDyeArmor`|`3502`||
  |`CauldronCleanArmor`|`3503`||
  |`CauldronFillPotion`|`3504`||
  |`CauldronTakePotion`|`3505`||
  |`CauldronFillWater`|`3506`||
  |`CauldronTakeWater`|`3507`||
  |`CauldronAddDye`|`3508`||
  |`CauldronCleanBanner`|`3509`||
  |`CauldronFlush`|`3510`||
  |`AgentSpawnEffect`|`3511`||
  |`CauldronFillLava`|`3512`||
  |`CauldronTakeLava`|`3513`||
  |`CauldronFillPowderSnow`|`3514`||
  |`CauldronTakePowderSnow`|`3515`||
  |`StartBlockCracking`|`3600`||
  |`StopBlockCracking`|`3601`||
  |`UpdateBlockCracking`|`3602`||
  |`ParticlesCrackBlockDown`|`3603`||
  |`ParticlesCrackBlockUp`|`3604`||
  |`ParticlesCrackBlockNorth`|`3605`||
  |`ParticlesCrackBlockSouth`|`3606`||
  |`ParticlesCrackBlockWest`|`3607`||
  |`ParticlesCrackBlockEast`|`3608`||
  |`ParticlesShootWhiteSmoke`|`3609`||
  |`ParticlesBreezeWindExplosion`|`3610`||
  |`ParticlesTrialSpawnerDetection`|`3611`||
  |`ParticlesTrialSpawnerSpawning`|`3612`||
  |`ParticlesTrialSpawnerEjecting`|`3613`||
  |`ParticlesWindExplosion`|`3614`||
  |`AllPlayersSleeping`|`3615`||
  |`deprecated`|`3616`||
  |`SleepingPlayers`|`9801`||
  |`JumpPrevented`|`9810`||
  |`AnimationVaultActivate`|`9811`||
  |`AnimationVaultDeactivate`|`9812`||
  |`AnimationVaultEjectItem`|`9813`||
  |`ParticleLegacyEvent`|`0x4000`||



////
//// define
Event Data：[<!-- md:samp CompoundTag -->](../types/compoundtag.md)

- 特殊类型。Note about Event ID: Legacy particles use the @enums.html#Particle Type@  enum |ed with ParticleLegacyEvent(0x4000)


////

///
