# Tick World

> 文档版本：1.21.50.25

Defines if the entity ticks the world and the radius around it to tick.

## 架构

```mcschema
tick_world:
{
  number "distance_to_players" : opt
  boolean "never_despawn" : opt
  integer "radius" : opt
}

```

/// html | div.result
//// define
`distance_to_players`：<samp>number</samp>

- The distance at which the closest player has to be before this entity despawns. This option will be ignored if never_despawn is true. Min: 128 blocks.


////


//// define
`never_despawn`：<samp>boolean</samp>

- If true, this entity will not despawn even if players are far away. If false, distance_to_players will be used to determine when to despawn.


////


//// define
`radius`：<samp>integer</samp>

- The area around the entity to tick. Default: 2. Allowed range: 2-6.


////


///

