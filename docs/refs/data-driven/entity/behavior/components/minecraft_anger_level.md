# minecraft:anger_level

> 文档版本：1.21.0.24

Allows this entity to track anger towards a set of nuisances.

## 架构

```mcschema
minecraft:anger_level:
{
  number "anger_decrement_interval" : opt
  integer "angry_boost" : opt
  integer "angry_threshold" : opt
  integer "default_annoyingness" : opt
  integer "default_projectile_annoyingness" : opt
  integer "max_anger" : opt
  entity_filters "nuisance_filter"
  array "on_increase_sounds" : opt
  {
    object "<any array element>" : opt
    {
      expression_node_no_version "condition"
      string "sound" : opt
    }
  }
  boolean "remove_targets_below_angry_threshold" : opt
}

```

/// html | div.result
//// define
`anger_decrement_interval`：<samp>number</samp>

- Anger level will decay over time. Defines how often anger towards all nuisances will be decreased by one.


////


//// define
`angry_boost`：<samp>integer</samp>

- Anger boost applied to angry threshold when mob gets angry.


////


//// define
`angry_threshold`：<samp>integer</samp>

- Threshold that define when the mob is considered angry at a nuisance.


////


//// define
`default_annoyingness`：<samp>integer</samp>

- Specifies the amount to raise anger level with each provocation.


////


//// define
`default_projectile_annoyingness`：<samp>integer</samp>

- Specifies the amount to raise anger level with each projectile hit.


////


//// define
`max_anger`：<samp>integer</samp>

- The maximum anger level that can be reached. Applies to any nuisance.


////


//// define
`nuisance_filter`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}

- Filter that is applied to determine if a mob can be a nuisance.


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
`on_increase_sounds`：<samp>array</samp>

- Sounds to play when the entity is getting provoked. Evaluated in order; the first matching condition wins.


////

<div class="language-text highlight"><span class="filename"><code>on_increase_sounds</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`condition`：<samp>expression_node_no_version</samp> {#assets.schemas.common.molang.expression_node_no_version.json}


//////

```mcschema
expression_node_no_version:
string

```

////// html | div.result

//////


```mcschema
expression_node_no_version:
boolean

```

////// html | div.result

//////


```mcschema
expression_node_no_version:
number

```

////// html | div.result

//////




////// define
`sound`：<samp>string</samp>


//////


/////


////


//// define
`remove_targets_below_angry_threshold`：<samp>boolean</samp>

- Defines if the entity should remove target if it falls below 'angry' threshold.


////


///

