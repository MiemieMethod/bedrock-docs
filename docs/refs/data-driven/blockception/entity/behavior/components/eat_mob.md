# Eat Mob

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] Allows the entity to eat a specified Mob.

## 架构

```mcschema
eat_mob:
{
  priority "priority"
  number "eat_animation_time" : opt
  sound_event "eat_mob_sound"
  string "loot_table" : opt
  number "pull_in_force" : opt
  number "reach_mob_distance" : opt
  number "run_speed" : opt
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
`eat_animation_time`：<samp>number</samp>

- Sets the time in seconds the eat animation should play for.


////


//// define
`eat_mob_sound`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Sets the sound that should play when eating a mob.


////

```mcschema
sound_event:
string

```

//// html | div.result

////



//// define
`loot_table`：<samp>string</samp>

- The loot table for loot to be dropped when eating a mob.


////


//// define
`pull_in_force`：<samp>number</samp>

- Sets the force which the mob-to-be-eaten is pulled towards the eating mob.


////


//// define
`reach_mob_distance`：<samp>number</samp>

- Sets the desired distance to be reached before eating the mob.


////


//// define
`run_speed`：<samp>number</samp>

- Sets the entity's speed when running toward the target.


////


///

