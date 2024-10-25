# Sniff

> 文档版本：1.21.50.25

Sniff compels this entity to detect the nearest player within "sniffing_radius" and update its minecraft:suspect_tracking component state.

## 架构

```mcschema
sniff:
{
  priority "priority"
  vector_of_2_items "cooldown_range"
  number "duration" : opt
  number "sniffing_radius" : opt
  number "suspicion_radius_horizontal" : opt
  number "suspicion_radius_vertical" : opt
}

```

/// html | div.result
//// define
`priority`：<samp>priority</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.priority.json}


////

```mcschema
priority:
integer

```

//// html | div.result

////



//// define
`cooldown_range`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- Cooldown range between sniffs in seconds.


////

```mcschema
vector_of_2_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The X component.


/////


///// define
`1..1`：<samp>number</samp>

- The Y component.


/////


////



//// define
`duration`：<samp>number</samp>

- Sniffing duration in seconds


////


//// define
`sniffing_radius`：<samp>number</samp>

- Mob detection radius.


////


//// define
`suspicion_radius_horizontal`：<samp>number</samp>

- Mob suspicion horizontal radius. When a player is within this radius horizontally, the anger level towards that player is increased.


////


//// define
`suspicion_radius_vertical`：<samp>number</samp>

- Mob suspicion vertical radius. When a player is within this radius vertically, the anger level towards that player is increased.


////


///

