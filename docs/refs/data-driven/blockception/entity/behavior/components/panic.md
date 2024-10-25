# Panic

> 文档版本：1.21.50.25

Allows the mob to enter the panic state, which makes it run around and away from the damage source that made it enter this state.

## 架构

```mcschema
panic:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  array "damage_sources" : opt
  {
    entity_damage_source "<any array element>"
  }
  boolean "force" : opt
  boolean "ignore_mob_damage" : opt
  boolean "prefer_water" : opt
  sound_event "panic_sound"
  object "sound_interval" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
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
`speed_multiplier`：<samp>speed_multiplier</samp> {#assets.schemas-blockception.behavior.entities.format.behaviors.types.speed_multiplier.json}


////

```mcschema
speed_multiplier:
number

```

//// html | div.result

////



//// define
`damage_sources`：<samp>array</samp>

- The list of Entity Damage Sources that will cause this mob to panic.


////

<div class="language-text highlight"><span class="filename"><code>damage_sources</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}


/////

```mcschema
entity_damage_source:
string

```

///// html | div.result

/////



////


//// define
`force`：<samp>boolean</samp>

- If true, this mob will not stop panicking until it can't move anymore or the goal is removed from it.


////


//// define
`ignore_mob_damage`：<samp>boolean</samp>

- If true, the mob will not panic in response to damage from other mobs. This overrides the damage types in `damage_sources`


////


//// define
`prefer_water`：<samp>boolean</samp>

- If true, the mob will prefer water over land.


////


//// define
`panic_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- The sound event to play when this mob is in panic.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`sound_interval`：<samp>object</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum time in seconds before the `panic_sound` plays.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum time in seconds before the `panic_sound` plays.


/////


////


///

