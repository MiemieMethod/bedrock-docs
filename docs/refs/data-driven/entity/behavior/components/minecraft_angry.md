# minecraft:angry

> 文档版本：1.21.0.24

Defines the entity's 'angry' state using a timer.

## 架构

```mcschema
minecraft:angry:
{
  string "angry_sound" : opt
  boolean "broadcast_anger" : opt
  boolean "broadcast_anger_on_attack" : opt
  boolean "broadcast_anger_on_being_attacked" : opt
  entity_filters "broadcast_filters"
  integer "broadcast_range" : opt
  array "broadcast_targets" : opt
  {
    string "<any array element>" : opt
  }
  object "calm_event" : opt
  {
    string "event" : opt
    string "target" : opt
  }
  integer "duration" : opt
  integer "duration_delta" : opt
  entity_filters "filters"
  array "sound_interval" : opt
  {
    integer "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`angry_sound`：<samp>string</samp>

- The sound event to play when the mob is angry.


////


//// define
`broadcast_anger`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry.


////


//// define
`broadcast_anger_on_attack`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry whenever this mob attacks.


////


//// define
`broadcast_anger_on_being_attacked`：<samp>boolean</samp>

- If true, other entities of the same entity definition within the broadcastRange will also become angry whenever this mob is attacked.


////


//// define
`broadcast_filters`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}

- Conditions that make this entry in the list valid.


////

```mcschema
entity_filters:
{
  sub_filter "any_of"
  sub_filter "all_of"
  sub_filter "none_of"
}

```

//// html | div.result
///// define
`any_of`：<samp>sub_filter</samp> {#assets.schemas.common.definition.entity.sub_filter.json}


/////

```mcschema
sub_filter:
{
  string "test" : opt
  string "subject" : opt
  string "operator" : opt
  string "value" : opt
}

```

///// html | div.result
////// define
`test`：<samp>string</samp>


//////


////// define
`subject`：<samp>string</samp>


//////


////// define
`operator`：<samp>string</samp>


//////


////// define
`value`：<samp>string</samp>


//////


/////


```mcschema
sub_filter:
array
{
  object "<any array element>" : opt
  {
    string "test" : opt
    string "subject" : opt
    string "operator" : opt
    string "value" : opt
  }
}

```

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`test`：<samp>string</samp>


///////


/////// define
`subject`：<samp>string</samp>


///////


/////// define
`operator`：<samp>string</samp>


///////


/////// define
`value`：<samp>string</samp>


///////


//////


/////




///// define
`all_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


/////


///// define
`none_of`：<samp>[sub_filter](#assets.schemas.common.definition.entity.sub_filter.json)</samp>


/////


////



//// define
`broadcast_range`：<samp>integer</samp>

- Distance in blocks within which other entities of the same entity definition will become angry.


////


//// define
`broadcast_targets`：<samp>array</samp>

- A list of entity families to broadcast anger to.


////

<div class="language-text highlight"><span class="filename"><code>broadcast_targets</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`calm_event`：<samp>object</samp>

- Event to run after the number of seconds specified in duration expires (when the entity stops being 'angry').


////

<div class="language-text highlight"><span class="filename"><code>calm_event</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`event`：<samp>string</samp>


/////


///// define
`target`：<samp>string</samp>


/////


////


//// define
`duration`：<samp>integer</samp>

- The amount of time in seconds that the entity will be angry.


////


//// define
`duration_delta`：<samp>integer</samp>

- Variance in seconds added to the duration [-delta, delta].


////


//// define
`filters`：<samp>[entity_filters](#assets.schemas.common.definition.entity.entity_filters.json)</samp>

- Filter out mob types that it should not attack while angry (other Piglins).


////


//// define
`sound_interval`：<samp>array</samp>

- The range of time in seconds to randomly wait before playing the sound again.


////

<div class="language-text highlight"><span class="filename"><code>sound_interval</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////


///

