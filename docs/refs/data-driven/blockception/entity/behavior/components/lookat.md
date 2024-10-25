# Lookat

> 文档版本：1.21.50.25

Defines the behavior when another entity looks at this entity.

## 架构

```mcschema
lookat:
{
  boolean "allow_invulnerable" : opt
  filters "filters"
  range_number_type "look_cooldown"
  event_object "look_event"
  number "search_radius" : opt
  boolean "set_target" : opt
}

```

/// html | div.result
//// define
`allow_invulnerable`：<samp>boolean</samp>

- If true, invulnerable entities (e.g. Players in creative mode) are considered valid targets.


////


//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Defines the entities that can trigger this component.


////


//// define
`look_cooldown`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

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
`look_event`：<samp>event_object</samp> {#assets.schemas-blockception.behavior.entities.format.types.event_object.json}

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
`search_radius`：<samp>number</samp>

- Maximum distance this entity will look for another entity looking at it.


////


//// define
`set_target`：<samp>boolean</samp>

- If true, this entity will set the attack target as the entity that looked at it.


////


///

