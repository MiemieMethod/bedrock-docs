# Play Dead

> 文档版本：1.21.0.24

Allows the mob to play dead when attacked by other entities. When playing dead, other entities will not target this mob.

## 架构

```mcschema
play_dead:
{
  priority "priority"
  boolean "apply_regeneration" : opt
  number "duration" : opt
  filters "filters"
  integer "force_below_health" : opt
  number "random_start_chance" : opt
  array "random_damage_range" : opt
  {
    integer "0..0" : opt
    integer "1..1" : opt
  }
  entity_damage_source "damage_sources"
  array "damage_sources" : opt
  {
    entity_damage_source "<any array element>"
  }
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
`apply_regeneration`：<samp>boolean</samp>

- Whether the mob will receive the regeneration effect while playing dead.


////


//// define
`duration`：<samp>number</samp>

- The amount of time the mob will remain playing dead (in seconds).


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of other triggers that are required for the mob to activate play dead.


////


//// define
`force_below_health`：<samp>integer</samp>

- The amount of health at which damage will cause the mob to play dead.


////


//// define
`random_start_chance`：<samp>number</samp>

- The likelihood of this goal starting upon taking damage.


////


//// define
`random_damage_range`：<samp>array</samp>

- The range of damage that may cause the goal to start depending on randomness. Damage taken below the min will never cause the goal to start. Damage taken above the max will always cause the goal to start.


////

<div class="language-text highlight"><span class="filename"><code>random_damage_range</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>integer</samp>

- Minimum.


/////


///// define
`1..1`：<samp>integer</samp>

- Maximum.


/////


////


//// define
`damage_sources`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}

- The list of Entity Damage Sources that will cause this mob to play dead.


////

```mcschema
entity_damage_source:
string

```

//// html | div.result

////



//// define
`damage_sources`：<samp>array</samp>

- The list of Entity Damage Sources that will cause this mob to play dead.


////

<div class="language-text highlight"><span class="filename"><code>damage_sources</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>[entity_damage_source](#assets.schemas-blockception.general.entity.damage_source.json)</samp>


/////


////



///

