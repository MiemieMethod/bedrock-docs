# minecraft:area_attack

> 文档版本：1.21.0.24

A component that does damage to entities that get within range.

## 架构

```mcschema
minecraft:area_attack:
{
  string "cause" : opt
  number "damage_cooldown" : opt
  integer "damage_per_tick" : opt
  number "damage_range" : opt
  entity_filters "entity_filter"
  boolean "play_attack_sound" : opt
}

```

/// html | div.result
//// define
`cause`：<samp>string</samp>

- The type of damage that is applied to entities that enter the damage range.


////


//// define
`damage_cooldown`：<samp>number</samp>

- Attack cooldown (in seconds) for how often this entity can attack a target.


////


//// define
`damage_per_tick`：<samp>integer</samp>

- How much damage per tick is applied to entities that enter the damage range.


////


//// define
`damage_range`：<samp>number</samp>

- How close a hostile entity must be to have the damage applied.


////


//// define
`entity_filter`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}

- The set of entities that are valid to apply the damage to when within range.


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
`play_attack_sound`：<samp>boolean</samp>

- If the entity should play their attack sound when attacking a target.


////


///

