# Rideable

> 文档版本：1.21.0.24

Determines whether this entity can be ridden. Allows specifying the different seat positions and quantity.

## 架构

```mcschema
rideable:
{
  integer "controlling_seat" : opt
  boolean "crouching_skip_interact" : opt
  array "family_types" : opt
  {
    string "<any array element>" : opt
  }
  string "interact_text" : opt
  number "passenger_max_width" : opt
  boolean "pull_in_entities" : opt
  boolean "rider_can_interact" : opt
  integer "seat_count" : opt
  object "seats" : opt
  {
    number "lock_rider_rotation" : opt
    integer "max_rider_count" : opt
    integer "min_rider_count" : opt
    vector_of_3_items "position"
    0 "rotate_rider_by"
  }
  array "seats" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
}

```

/// html | div.result
//// define
`controlling_seat`：<samp>integer</samp>

- The seat that designates the driver of the entity.


////


//// define
`crouching_skip_interact`：<samp>boolean</samp>

- If true, this entity can't be interacted with if the entity interacting with it is crouching.


////


//// define
`family_types`：<samp>array</samp>

- List of entities that can ride this entity.


////

<div class="language-text highlight"><span class="filename"><code>family_types</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`interact_text`：<samp>string</samp>

- The text to display when the player can interact with the entity when playing with Touch-screen controls.


////


//// define
`passenger_max_width`：<samp>number</samp>

- The max width a mob can be to be a passenger. A value of 0 ignores this parameter.


////


//// define
`pull_in_entities`：<samp>boolean</samp>

- If true, this entity will pull in entities that are in the correct family_types into any available seats.


////


//// define
`rider_can_interact`：<samp>boolean</samp>

- If true, this entity will be picked when looked at by the rider.


////


//// define
`seat_count`：<samp>integer</samp>

- The number of entities that can ride this entity at the same time.


////


//// define
`seats`：<samp>object</samp>

- The list of positions and number of riders for each position for entities riding this entity.


////

<div class="language-text highlight"><span class="filename"><code>seats</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`lock_rider_rotation`：<samp>number</samp>

- Angle in degrees that a rider is allowed to rotate while riding this entity. Omit this property for no limit


/////


///// define
`max_rider_count`：<samp>integer</samp>

- Defines the maximum number of riders that can be riding this entity for this seat to be valid.


/////


///// define
`min_rider_count`：<samp>integer</samp>

- Defines the minimum number of riders that need to be riding this entity before this seat can be used.


/////


///// define
`position`：<samp>vector_of_3_items</samp> {#assets.schemas-blockception.general.vectors.number3.json}

- Position of this seat relative to this entity's position.


/////

```mcschema
vector_of_3_items:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
}

```

///// html | div.result
////// define
`0..0`：<samp>number</samp>

- The X component.


//////


////// define
`1..1`：<samp>number</samp>

- The Y component.


//////


////// define
`2..2`：<samp>number</samp>

- The Z component.


//////


/////



///// define
`rotate_rider_by`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Offset to rotate riders by.


/////

```mcschema
0:
string

```

///// html | div.result

/////


```mcschema
0:
number

```

///// html | div.result

/////




////


//// define
`seats`：<samp>array</samp>

- The list of positions and number of riders for each position for entities riding this entity.


////

<div class="language-text highlight"><span class="filename"><code>seats</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////



///

