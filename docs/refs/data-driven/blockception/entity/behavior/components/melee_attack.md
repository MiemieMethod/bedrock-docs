# Melee Attack

> 文档版本：1.21.50.25

Allows the mob to use close combat melee attacks.

## 架构

```mcschema
melee_attack:
{
  priority "priority"
  speed_multiplier "speed_multiplier"
  boolean "attack_once" : opt
  string "attack_types" : opt
  boolean "can_spread_on_fire" : opt
  number "cooldown_time" : opt
  number "inner_boundary_time_increase" : opt
  number "max_dist" : opt
  number "max_path_time" : opt
  number "melee_fov" : opt
  number "min_path_time" : opt
  trigger "on_attack"
  trigger "on_kill"
  number "outer_boundary_time_increase" : opt
  number "path_fail_time_increase" : opt
  number "path_inner_boundary" : opt
  number "path_outer_boundary" : opt
  integer "random_stop_interval" : opt
  number "reach_multiplier" : opt
  boolean "require_complete_path" : opt
  boolean "set_persistent" : opt
  number "target_dist" : opt
  boolean "track_target" : opt
  number "x_max_rotation" : opt
  number "y_max_head_rotation" : opt
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
`attack_once`：<samp>boolean</samp>

- Allows the entity to use this attack behavior, only once EVER.


////


//// define
`attack_types`：<samp>string</samp>

- Defines the entity types this entity will attack.


////


//// define
`can_spread_on_fire`：<samp>boolean</samp>

- If the entity is on fire, this allows the entity's target to catch on fire after being hi


////


//// define
`cooldown_time`：<samp>number</samp>

- Cooldown time (in seconds) between attacks.


////


//// define
`inner_boundary_time_increase`：<samp>number</samp>

- Time (in seconds) to add to attack path recalculation when the target is beyond the "path_inner_boundary".


////


//// define
`max_dist`：<samp>number</samp>

- Unused. No effect on "minecraft:behavior.melee_attack".


////


//// define
`max_path_time`：<samp>number</samp>

- Maximum base time (in seconds) to recalculate new attack path to target (before increases applied).


////


//// define
`melee_fov`：<samp>number</samp>

- Field of view (in degrees) when using the sensing component to detect an attack target.


////


//// define
`min_path_time`：<samp>number</samp>

- Minimum base time (in seconds) to recalculate new attack path to target (before increases applied).


////


//// define
`on_attack`：<samp>trigger</samp> {#assets.schemas-blockception.behavior.entities.format.types.trigger.json}

- Defines the event to trigger when this entity successfully attacks.


////

```mcschema
trigger:
string

```

//// html | div.result

////


```mcschema
trigger:
{
  string "event" : opt
  filters "filters"
  subject "target"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>

- The event to run when the conditions for this trigger are met.


/////


///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The list of conditions for this trigger to execute.


/////


///// define
`target`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- The target of the event.


/////

```mcschema
subject:
string

```

///// html | div.result

/////



////


```mcschema
trigger:
array
{
  object "<any array element>" : opt
  {
    string "event" : opt
    filters "filters"
    subject "target"
  }
}

```

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////




//// define
`on_kill`：<samp>[trigger](#assets.schemas-blockception.behavior.entities.format.types.trigger.json)</samp>

- Defines the event to trigger when this entity successfully kills.


////


//// define
`outer_boundary_time_increase`：<samp>number</samp>

- Time (in seconds) to add to attack path recalculation when the target is beyond the "path_outer_boundary".


////


//// define
`path_fail_time_increase`：<samp>number</samp>

- Time (in seconds) to add to attack path recalculation when this entity cannot move along the current path.


////


//// define
`path_inner_boundary`：<samp>number</samp>

- Distance at which to increase attack path recalculation by "inner_boundary_tick_increase".


////


//// define
`path_outer_boundary`：<samp>number</samp>

- Distance at which to increase attack path recalculation by "outer_boundary_tick_increase".


////


//// define
`random_stop_interval`：<samp>integer</samp>

- This entity will have a 1 in N chance to stop it's current attack, where N = "random_stop_interval".


////


//// define
`reach_multiplier`：<samp>number</samp>

- Used with the base size of the entity to determine minimum target-distance before trying to deal attack damage.


////


//// define
`require_complete_path`：<samp>boolean</samp>

- Toggles (on/off) the need to have a full path from the entity to the target when using this melee attack behavior.


////


//// define
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`target_dist`：<samp>number</samp>

- Unused. No effect on "minecraft:behavior.melee_attack".


////


//// define
`track_target`：<samp>boolean</samp>

- Allows the entity to track the attack target, even if the entity has no sensing.


////


//// define
`x_max_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the X-axis, this entity can rotate while trying to look at the target.


////


//// define
`y_max_head_rotation`：<samp>number</samp>

- Maximum rotation (in degrees), on the Y-axis, this entity can rotate its head while trying to look at the target.


////


///

