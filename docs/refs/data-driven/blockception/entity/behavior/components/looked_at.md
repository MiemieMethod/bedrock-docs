# Looked At

> 文档版本：1.21.50.25

Defines the behavior when another entity looks at this entity.

## 架构

```mcschema
looked_at:
{
  number "field_of_view" : opt
  filters "filters"
  boolean "find_players_only" : opt
  string "line_of_sight_obstruction_type" : opt
  array "look_at_locations" : opt
  {
    string "<any array element>" : opt
  }
  range_number_type "looked_at_cooldown"
  event_object "looked_at_event"
  event_object "not_looked_at_event"
  boolean "scale_fov_by_distance" : opt
  number "search_radius" : opt
  string "set_target" : opt
}

```

/// html | div.result
//// define
`field_of_view`：<samp>number</samp>

- [Beta] Defines, in degrees, the width of the field of view for entities looking at the owner entity. If 'scale_fov_by_distance' is set to true, this value corresponds to the field of view at a distance of one block between the entities.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Defines the entities that can trigger this component.


////


//// define
`find_players_only`：<samp>boolean</samp>

- [Beta] Limits the search to only the nearest Player that meets the specified "filters" rather than all nearby entities.


////


//// define
`line_of_sight_obstruction_type`：<samp>string</samp>

- [Beta] Defines the type of block shape used to check for line of sight obstructions.


////


//// define
`look_at_locations`：<samp>array</samp>

- [Beta] A list of locations on the owner entity towards which line of sight checks are performed. At least one location must be unobstructed for the entity to be considered as looked at.


////

<div class="language-text highlight"><span class="filename"><code>look_at_locations</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`looked_at_cooldown`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- The range for the random amount of time during which the entity is `cooling down` and won't get angered or look for a target.


////

```mcschema
range_number_type:
number

```

//// html | div.result

////


```mcschema
range_number_type:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>number</samp>

- The first value of the range.


/////


///// define
`1..1`：<samp>number</samp>

- The second value of the range.


/////


////


```mcschema
range_number_type:
{
  number "range_min" : opt
  number "range_max" : opt
}

```

//// html | div.result
///// define
`range_min`：<samp>number</samp>

- The minimum value of the range.


/////


///// define
`range_max`：<samp>number</samp>

- The maximum value of the range.


/////


////




//// define
`looked_at_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

- The event identifier to run when the entities specified in filters look at this entity.


////

```mcschema
event_object:
{
  filters "filters"
  string "event" : opt
  string "target" : opt
}

```

//// html | div.result
///// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////


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
`not_looked_at_event`：<samp>[event_object](#assets.schemas-blockception.behavior.entities.format.types.event_object.json)</samp>

- [Beta] Defines the event to trigger when no entity is found looking at the owner entity.


////


//// define
`scale_fov_by_distance`：<samp>boolean</samp>

- [Beta] When true, the field of view narrows as the distance between the owner entity and the entity looking at it increases. This ensures that the width of the view cone remains somewhat constant towards the owner entity position, regardless of distance.


////


//// define
`search_radius`：<samp>number</samp>

- Maximum distance this entity will look for another entity looking at it.


////


//// define
`set_target`：<samp>string</samp>

- Defines if and how the owner entity will set entities that are looking at it as its combat targets. Valid values:
- "never", looking entities are never set as targets, but events are emitted.
- "once_and_stop_scanning", the first detected looking entity is set as target. Scanning and event emission is suspended if and until the owner entity has a target.
- [Beta] "once_and_keep_scanning", the first detected looking entity is set as target. Scanning and event emission continues.


////


///

