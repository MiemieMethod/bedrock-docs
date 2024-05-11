# minecraft:ageable

> 文档版本：1.21.0.24

Adds a timer for the entity to grow up. It can be accelerated by giving the entity the items it likes as defined by feedItems.

## 架构

```mcschema
minecraft:ageable:
{
  array "drop_items" : opt
  {
    string "<any array element>" : opt
  }
  array "feed_items" : opt
  {
    object "<any array element>" : opt
    {
      string "item" : opt
      number "growth" : opt
    }
    string "<any array element>" : opt
  }
  number "duration" : opt
  string "transform_to_item" : opt
  entity_filters "interact_filters"
  object "grow_up" : opt
  {
    string "target" : opt
    string "event" : opt
  }
}

```

/// html | div.result
//// define
`drop_items`：<samp>array</samp>

- List of items that the entity drops when it grows up.


////

<div class="language-text highlight"><span class="filename"><code>drop_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`feed_items`：<samp>array</samp>

- List of items that can be fed to the entity. Includes 'item' for the item name and 'growth' to define how much time it grows up by


////

<div class="language-text highlight"><span class="filename"><code>feed_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`item`：<samp>string</samp>


//////


////// define
`growth`：<samp>number</samp>


//////


/////


///// define
`<any array element>`：<samp>string</samp>


/////



////


//// define
`duration`：<samp>number</samp>

- Amount of time before the entity grows up, -1 for always a baby.


////


//// define
`transform_to_item`：<samp>string</samp>

- The feed item used will transform to this item upon successful interaction. Format: itemName:auxValue


////


//// define
`interact_filters`：<samp>entity_filters</samp> {#assets.schemas.common.definition.entity.entity_filters.json}

- List of conditions to meet so that the entity can be fed.


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
`grow_up`：<samp>object</samp>

- Event to run when this entity grows up.


////

<div class="language-text highlight"><span class="filename"><code>grow_up</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`target`：<samp>string</samp>


/////


///// define
`event`：<samp>string</samp>


/////


////


///

