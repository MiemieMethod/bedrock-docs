# Defend Trusted Target

> 文档版本：1.21.0.24

Allows the mob to target another mob that hurts an entity it trusts.

## 架构

```mcschema
defend_trusted_target:
{
  priority "priority"
  sound_event "aggro_sound"
  integer "attack_interval" : opt
  boolean "must_see" : opt
  number "must_see_forget_duration" : opt
  event "on_defend_start"
  number "within_radius" : opt
  entity_types "entity_types"
  number "sound_chance" : opt
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
`aggro_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sound to occasionally play while defending.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`attack_interval`：<samp>integer</samp>

- Time in seconds between attacks.


////


//// define
`must_see`：<samp>boolean</samp>

- If true, only entities in this mob's viewing range can be selected as targets.


////


//// define
`must_see_forget_duration`：<samp>number</samp>

- Determines the amount of time in seconds that this mob will look for a target before forgetting about it and looking for a new one when the target isn't visible any more.


////


//// define
`on_defend_start`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- The event to run when this mob starts to defend the entity it trusts.


////

```mcschema
event:
string

```

//// html | div.result

////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to fire.


/////


///// define
`target`：<samp>string</samp>

- The target of the event.


/////


////




//// define
`within_radius`：<samp>number</samp>

- Distance in blocks that the target can be within to launch an attack.


////


//// define
`entity_types`：<samp>entity_types</samp> {#assets.schemas-blockception.behavior.entities.format.types.entity_types.json}

- List of entity types that this mob considers valid targets.


////

```mcschema
entity_types:
array
{
  object "<any array element>" : opt
  {
    filters "filters"
    number "cooldown" : opt
    number "max_dist" : opt
    number "max_height" : opt
    number "max_flee" : opt
    number "priority" : opt
    number "within_default" : opt
    boolean "check_if_outnumbered" : opt
    boolean "must_see" : opt
    number "must_see_forget_duration" : opt
    boolean "reevaluate_description" : opt
    number "sprint_speed_multiplier" : opt
    number "walk_speed_multiplier" : opt
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The entity type.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


////// define
`cooldown`：<samp>number</samp>

- The amount of time in seconds that the mob has to wait before selecting a target of the same type again


//////


////// define
`max_dist`：<samp>number</samp>

- Maximum distance this mob can be away to be a valid choice.


//////


////// define
`max_height`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`max_flee`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`priority`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`within_default`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`check_if_outnumbered`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


////// define
`must_see`：<samp>boolean</samp>

- If true, the mob has to be visible to be a valid choice.


//////


////// define
`must_see_forget_duration`：<samp>number</samp>

- Determines the amount of time in seconds that this mob will look for a target before forgetting about it and looking for a new one when the target isn't visible any more.


//////


////// define
`reevaluate_description`：<samp>boolean</samp>

- If true, the mob will stop being targeted if it stops meeting any conditions.


//////


////// define
`sprint_speed_multiplier`：<samp>number</samp>

- Multiplier for the running speed. A value of 1.0 means the speed is unchanged


//////


////// define
`walk_speed_multiplier`：<samp>number</samp>

- Multiplier for the walking speed. A value of 1.0 means the speed is unchanged


//////


/////


////


```mcschema
entity_types:
{
  filters "filters"
  number "cooldown" : opt
  number "max_dist" : opt
  number "max_height" : opt
  number "max_flee" : opt
  number "priority" : opt
  number "within_default" : opt
  boolean "check_if_outnumbered" : opt
  boolean "must_see" : opt
  number "must_see_forget_duration" : opt
  boolean "reevaluate_description" : opt
  number "sprint_speed_multiplier" : opt
  number "walk_speed_multiplier" : opt
}

```

//// html | div.result

////




//// define
`sound_chance`：<samp>number</samp>

- Probability that a sound will play.


////


///

