# Nearest Attackable Target

> 文档版本：1.21.0.24

Allows an entity to attack the closest target within a given subset of specific target types.

## 架构

```mcschema
nearest_attackable_target:
{
  priority "priority"
  entity_types "entity_types"
  integer "attack_interval" : opt
  number "attack_interval_min" : opt
  boolean "attack_owner" : opt
  boolean "must_reach" : opt
  boolean "must_see" : opt
  number "must_see_forget_duration" : opt
  number "persist_time" : opt
  boolean "reselect_targets" : opt
  integer "scan_interval" : opt
  boolean "set_persistent" : opt
  number "target_invisible_multiplier" : opt
  number "target_search_height" : opt
  number "target_sneak_visibility_multiplier" : opt
  number "within_radius" : opt
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
`entity_types`：<samp>entity_types</samp> {#assets.schemas-blockception.behavior.entities.format.types.entity_types.json}

- Filters which types of targets are valid for this entity


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
`attack_interval`：<samp>integer</samp>

- Time range (in seconds) between searching for an attack target, range is in (0, `attack_interval`]. Only used if `attack_interval` is greater than 0, otherwise `scan_interval` is used.


////


//// define
`attack_interval_min`：<samp>number</samp>

- Alias for `attack_interval`; provides the same functionality as `attack_interval`.


////


//// define
`attack_owner`：<samp>boolean</samp>

- If true, this entity can attack its owner.


////


//// define
`must_reach`：<samp>boolean</samp>

- If true, this entity requires a path to the target.


////


//// define
`must_see`：<samp>boolean</samp>

- Determines if target-validity requires this entity to be in range only, or both in range and in sight.


////


//// define
`must_see_forget_duration`：<samp>number</samp>

- Time (in seconds) the target must not be seen by this entity to become invalid. Used only if `must_see` is true.


////


//// define
`persist_time`：<samp>number</samp>

- Time (in seconds) this entity can continue attacking the target after the target is no longer valid.


////


//// define
`reselect_targets`：<samp>boolean</samp>

- Allows the attacking entity to update the nearest target, otherwise a target is only reselected after each `scan_interval` or `attack_interval`.


////


//// define
`scan_interval`：<samp>integer</samp>

- If `attack_interval` is 0 or isn't declared, then between attacks: scanning for a new target occurs every amount of ticks equal to `scan_interval`, minimum value is 1. Values under 10 can affect performance.


////


//// define
`set_persistent`：<samp>boolean</samp>

- Allows the actor to be set to persist upon targeting a player.


////


//// define
`target_invisible_multiplier`：<samp>number</samp>

- Multiplied with the target's armor coverage percentage to modify `max_dist` when detecting an invisible target.


////


//// define
`target_search_height`：<samp>number</samp>

- Maximum vertical target-search distance, if it's greater than the target type's `max_dist`. A negative value defaults to `entity_types` greatest `max_dist`.


////


//// define
`target_sneak_visibility_multiplier`：<samp>number</samp>

- Multiplied with the target type's `max_dist` when trying to detect a sneaking target.


////


//// define
`within_radius`：<samp>number</samp>

- Maximum distance this entity can be from the target when following it, otherwise the target becomes invalid. This value is only used if the entity doesn't declare `minecraft:follow_range`.


////


///

