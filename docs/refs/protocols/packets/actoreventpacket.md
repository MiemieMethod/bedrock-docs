# <!-- md:samp ActorEventPacket -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp ActorEventPacket -->数据包，数字ID是`27`。

## 结构

```viz
digraph "ActorEventPacket" {
rankdir = LR
0
0 -> 1
1 -> 2
0 -> 3
3 -> 4
0 -> 5
5 -> 6

0 [label="ActorEventPacket",comment="name: \"ActorEventPacket\", typeName: \"\", id: 0, branchId: 27, recurseId: -1, attributes: 0, notes: \"\""];
1 [label="Target Runtime ID",comment="name: \"Target Runtime ID\", typeName: \"ActorRuntimeID\", id: 1, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
2 [label="ActorRuntimeID",comment="name: \"ActorRuntimeID\", typeName: \"\", id: 2, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
3 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ActorEvent\""];
4 [label="byte",comment="name: \"byte\", typeName: \"\", id: 4, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
5 [label="Data",comment="name: \"Data\", typeName: \"\", id: 5, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
6 [label="varint",comment="name: \"varint\", typeName: \"\", id: 6, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;2;4;6}

}

```

## 字段

```title='ActorEventPacket'
[target_runtime_id][event_id][data]
```

/// html | div.result
//// define
Target Runtime ID：[<!-- md:samp ActorRuntimeID -->](../types/actorruntimeid.md)

- <!-- md:samp ActorRuntimeID -->类型。


////
//// define
Event ID：<!-- md:samp byte -->

- <!-- md:samp byte -->类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NONE`|`0`||
  |`JUMP`|`1`||
  |`HURT`|`2`||
  |`DEATH`|`3`||
  |`START_ATTACKING`|`4`||
  |`STOP_ATTACKING`|`5`||
  |`TAMING_FAILED`|`6`||
  |`TAMING_SUCCEEDED`|`7`||
  |`SHAKE_WETNESS`|`8`||
  |`EAT_GRASS`|`10`||
  |`FISHHOOK_BUBBLE`|`11`||
  |`FISHHOOK_FISHPOS`|`12`||
  |`FISHHOOK_HOOKTIME`|`13`||
  |`FISHHOOK_TEASE`|`14`||
  |`SQUID_FLEEING`|`15`||
  |`ZOMBIE_CONVERTING`|`16`||
  |`PLAY_AMBIENT`|`17`||
  |`SPAWN_ALIVE`|`18`||
  |`START_OFFER_FLOWER`|`19`||
  |`STOP_OFFER_FLOWER`|`20`||
  |`LOVE_HEARTS`|`21`||
  |`VILLAGER_ANGRY`|`22`||
  |`VILLAGER_HAPPY`|`23`||
  |`WITCH_HAT_MAGIC`|`24`||
  |`FIREWORKS_EXPLODE`|`25`||
  |`IN_LOVE_HEARTS`|`26`||
  |`SILVERFISH_MERGE_ANIM`|`27`||
  |`GUARDIAN_ATTACK_SOUND`|`28`||
  |`DRINK_POTION`|`29`||
  |`THROW_POTION`|`30`||
  |`PRIME_TNTCART`|`31`||
  |`PRIME_CREEPER`|`32`||
  |`AIR_SUPPLY`|`33`||
  |`ADD_PLAYER_LEVELS`|`34`||
  |`GUARDIAN_MINING_FATIGUE`|`35`||
  |`AGENT_SWING_ARM`|`36`||
  |`DRAGON_START_DEATH_ANIM`|`37`||
  |`GROUND_DUST`|`38`||
  |`SHAKE`|`39`||
  |`FEED`|`57`||
  |`BABY_AGE`|`60`||
  |`INSTANT_DEATH`|`61`||
  |`NOTIFY_TRADE`|`62`||
  |`LEASH_DESTROYED`|`63`||
  |`CARAVAN_UPDATED`|`64`||
  |`TALISMAN_ACTIVATE`|`65`||
  |`UPDATE_STRUCTURE_FEATURE`|`66`||
  |`PLAYER_SPAWNED_MOB`|`67`||
  |`PUKE`|`68`||
  |`UPDATE_STACK_SIZE`|`69`||
  |`START_SWIMMING`|`70`||
  |`BALLOON_POP`|`71`||
  |`TREASURE_HUNT`|`72`||
  |`SUMMON_AGENT`|`73`||
  |`FINISHED_CHARGING_ITEM`|`74`||
  |`ACTOR_GROW_UP`|`76`||
  |`VIBRATION_DETECTED`|`77`||
  |`DRINK_MILK`|`78`||



////
//// define
Data：<!-- md:samp varint -->

- <!-- md:samp varint -->类型。


////

///

