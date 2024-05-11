# Attribute

> 文档版本：1.21.0.24

Specifies the initial value of a specific attribute for an entity when spawned.

## 架构

```mcschema
attribute:
{
  number "min" : opt
  number "max" : opt
  range_number_type "value"
}

```

/// html | div.result
//// define
`min`：<samp>number</samp>

- The minimum starting health an entity has.


////


//// define
`max`：<samp>number</samp>

- The maximum starting health an entity has.


////


//// define
`value`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}

- The amount of health an entity to start with by default.


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




///

