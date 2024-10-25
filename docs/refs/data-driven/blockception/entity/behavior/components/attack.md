# Attack

> 文档版本：1.21.50.25

Defines an entity's melee attack and any additional effects on it.

## 架构

```mcschema
attack:
{
  range_number_type "damage"
  effect "effect_name"
  number "effect_duration" : opt
}

```

/// html | div.result
//// define
`damage`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- Range of the random amount of damage the melee attack deals. A negative value can heal the entity instead of hurting it.


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
`effect_name`：<samp>effect</samp> {#assets.schemas-blockception.general.vanilla.effect.json}

- Identifier of the status ailment to apply to an entity attacked by this entity's melee attack.


////

```mcschema
effect:
string

```

//// html | div.result

////



//// define
`effect_duration`：<samp>number</samp>

- Duration in seconds of the status ailment applied to the damaged entity.


////


///

