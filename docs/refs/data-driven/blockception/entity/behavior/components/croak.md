# Croak

> 文档版本：1.21.0.24

[EXPERIMENTAL BEHAVIOR] Allows the entity to croak at a random time interval with configurable conditions.

## 架构

```mcschema
croak:
{
  priority "priority"
  duration "duration"
  filters "filters"
  interval "interval"
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
`duration`：<samp>number2orvalue</samp> {#assets.schemas-blockception.general.vectors.number2OrValue.json}

- Random range in seconds after which the croaking stops. Can also be a constant.


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



```mcschema
value:
number

```

//// html | div.result

////




//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。Conditions for the behavior to start and keep running. The interval between runs only starts after passing the filters.


////


//// define
`interval`：<samp>integer2orvalue</samp> {#assets.schemas-blockception.general.vectors.integer2OrValue.json}

- Random range in seconds between runs of this behavior. Can also be a constant.


////

```mcschema
vector_of_2_items:
array
{
  integer "0..0" : opt
  integer "1..1" : opt
}

```

//// html | div.result
///// define
`0..0`：<samp>integer</samp>

- The X component.


/////


///// define
`1..1`：<samp>integer</samp>

- The Y component.


/////


////



```mcschema
value:
integer

```

//// html | div.result

////




///

