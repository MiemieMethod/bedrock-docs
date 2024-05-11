# Entity Sensor

> 文档版本：1.21.0.24

A component that fires an event when a set of conditions are met by other entities within the defined range.

## 架构

```mcschema
entity_sensor:
{
  number "cooldown" : opt
  filters "event_filters"
  string "event" : opt
  integer "maximum_count" : opt
  integer "minimum_count" : opt
  vector_of_2_items "range"
  number "range" : opt
  boolean "require_all" : opt
  number "sensor_range" : opt
}

```

/// html | div.result
//// define
`cooldown`：<samp>number</samp>

- How many seconds should elapse before the subsensor can once again sense for entities. The cooldown is applied on top of the base 1 tick (0.05 seconds) delay. Negative values will result in no cooldown being used.


////


//// define
`event_filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


////


//// define
`event`：<samp>string</samp>

- event.


////


//// define
`maximum_count`：<samp>integer</samp>

- The maximum number of entities that must pass the filter conditions for the event to send.


////


//// define
`minimum_count`：<samp>integer</samp>

- The minimum number of entities that must pass the filter conditions for the event to send.


////


//// define
`range`：<samp>vector_of_2_items</samp> {#assets.schemas-blockception.general.vectors.number2.json}

- The maximum distance another entity can be from this and have the filters checked against it.


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



//// define
`range`：<samp>number</samp>

- The maximum distance another entity can be from this and have the filters checked against it.


////



//// define
`require_all`：<samp>boolean</samp>

- If true requires all nearby entities to pass the filter conditions for the event to send.


////


//// define
`sensor_range`：<samp>number</samp>

- The maximum distance another entity can be from this and have the filters checked against it.


////


///


```mcschema
entity_sensor:
{
  boolean "relative_range" : opt
}

```

/// html | div.result
//// define
`relative_range`：<samp>boolean</samp>

- If true the sensor range is additive on top of the entity's size.


////


///



```mcschema
entity_sensor:
{
  array "subsensors" : opt
  {
    object "<any array element>" : opt
    {
      number "cooldown" : opt
      filters "event_filters"
      string "event" : opt
      integer "maximum_count" : opt
      integer "minimum_count" : opt
      vector_of_2_items "range"
      number "range" : opt
      boolean "require_all" : opt
      number "sensor_range" : opt
    }
  }
  boolean "relative_range" : opt
}

```

/// html | div.result
//// define
`subsensors`：<samp>array</samp>

- The list of subsensors.


////

<div class="language-text highlight"><span class="filename"><code>subsensors</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////


//// define
`relative_range`：<samp>boolean</samp>

- If true the sensor range is additive on top of the entity's size.


////


///


