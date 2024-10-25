# <!-- md:samp ActorEventPacket -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp ActorEventPacket -->数据包，数字ID是`27`。该数据包用于通信活动对象事件。

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
3 [label="Event ID",comment="name: \"Event ID\", typeName: \"\", id: 3, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
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

- 特殊类型。目标活动对象的运行时标识符。


////
//// define
Event ID：<!-- md:samp byte -->

- 基本类型枚举。事件标识符。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NONE`|`0`|无|
  |`JUMP`|`1`|protocol.enum.jump|
  |`HURT`|`2`|protocol.enum.hurt|
  |`DEATH`|`3`|protocol.enum.death|
  |`START_ATTACKING`|`4`|protocol.enum.start_attacking|
  |`STOP_ATTACKING`|`5`|protocol.enum.stop_attacking|
  |`TAMING_FAILED`|`6`|protocol.enum.taming_failed|
  |`TAMING_SUCCEEDED`|`7`|protocol.enum.taming_succeeded|
  |`SHAKE_WETNESS`|`8`|protocol.enum.shake_wetness|
  |`EAT_GRASS`|`10`|protocol.enum.eat_grass|
  |`FISHHOOK_BUBBLE`|`11`|protocol.enum.fishhook_bubble|
  |`FISHHOOK_FISHPOS`|`12`|protocol.enum.fishhook_fishpos|
  |`FISHHOOK_HOOKTIME`|`13`|protocol.enum.fishhook_hooktime|
  |`FISHHOOK_TEASE`|`14`|protocol.enum.fishhook_tease|
  |`SQUID_FLEEING`|`15`|protocol.enum.squid_fleeing|
  |`ZOMBIE_CONVERTING`|`16`|protocol.enum.zombie_converting|
  |`PLAY_AMBIENT`|`17`|protocol.enum.play_ambient|
  |`SPAWN_ALIVE`|`18`|protocol.enum.spawn_alive|
  |`START_OFFER_FLOWER`|`19`|protocol.enum.start_offer_flower|
  |`STOP_OFFER_FLOWER`|`20`|protocol.enum.stop_offer_flower|
  |`LOVE_HEARTS`|`21`|protocol.enum.love_hearts|
  |`VILLAGER_ANGRY`|`22`|protocol.enum.villager_angry|
  |`VILLAGER_HAPPY`|`23`|protocol.enum.villager_happy|
  |`WITCH_HAT_MAGIC`|`24`|protocol.enum.witch_hat_magic|
  |`FIREWORKS_EXPLODE`|`25`|protocol.enum.fireworks_explode|
  |`IN_LOVE_HEARTS`|`26`|protocol.enum.in_love_hearts|
  |`SILVERFISH_MERGE_ANIM`|`27`|protocol.enum.silverfish_merge_anim|
  |`GUARDIAN_ATTACK_SOUND`|`28`|protocol.enum.guardian_attack_sound|
  |`DRINK_POTION`|`29`|protocol.enum.drink_potion|
  |`THROW_POTION`|`30`|protocol.enum.throw_potion|
  |`PRIME_TNTCART`|`31`|protocol.enum.prime_tntcart|
  |`PRIME_CREEPER`|`32`|protocol.enum.prime_creeper|
  |`AIR_SUPPLY`|`33`|protocol.enum.air_supply|
  |`ADD_PLAYER_LEVELS`|`34`|protocol.enum.add_player_levels|
  |`GUARDIAN_MINING_FATIGUE`|`35`|protocol.enum.guardian_mining_fatigue|
  |`AGENT_SWING_ARM`|`36`|protocol.enum.agent_swing_arm|
  |`DRAGON_START_DEATH_ANIM`|`37`|protocol.enum.dragon_start_death_anim|
  |`GROUND_DUST`|`38`|protocol.enum.ground_dust|
  |`SHAKE`|`39`|protocol.enum.shake|
  |`FEED`|`57`|protocol.enum.feed|
  |`BABY_AGE`|`60`|protocol.enum.baby_age|
  |`INSTANT_DEATH`|`61`|protocol.enum.instant_death|
  |`NOTIFY_TRADE`|`62`|protocol.enum.notify_trade|
  |`LEASH_DESTROYED`|`63`|protocol.enum.leash_destroyed|
  |`CARAVAN_UPDATED`|`64`|protocol.enum.caravan_updated|
  |`TALISMAN_ACTIVATE`|`65`|protocol.enum.talisman_activate|
  |`DEPRECATED_UPDATE_STRUCTURE_FEATURE`|`66`|protocol.enum.deprecated_update_structure_feature|
  |`PLAYER_SPAWNED_MOB`|`67`|protocol.enum.player_spawned_mob|
  |`PUKE`|`68`|protocol.enum.puke|
  |`UPDATE_STACK_SIZE`|`69`|protocol.enum.update_stack_size|
  |`START_SWIMMING`|`70`|protocol.enum.start_swimming|
  |`BALLOON_POP`|`71`|protocol.enum.balloon_pop|
  |`TREASURE_HUNT`|`72`|protocol.enum.treasure_hunt|
  |`SUMMON_AGENT`|`73`|protocol.enum.summon_agent|
  |`FINISHED_CHARGING_ITEM`|`74`|protocol.enum.finished_charging_item|
  |`ACTOR_GROW_UP`|`76`|protocol.enum.actor_grow_up|
  |`VIBRATION_DETECTED`|`77`|protocol.enum.vibration_detected|
  |`DRINK_MILK`|`78`|protocol.enum.drink_milk|



////
//// define
Data：<!-- md:samp varint -->

- 基本类型。protocol.packet.actoreventpacket.data.description


////

///

