# Healable

> 文档版本：1.21.0.24

Defines the interactions with this entity for healing it.

## 架构

```mcschema
healable:
{
  filters "filters"
  boolean "force_use" : opt
  array "items" : opt
  {
    object "<any array element>" : opt
    {
      filters "filters"
      integer "heal_amount" : opt
      descriptor "item"
      object "effects" : opt
      {
        string "name" : opt
        integer "duration" : opt
        integer "amplifier" : opt
      }
      array "effects" : opt
      {
        object "<any array element>" : opt
        {
        }
      }
    }
  }
}

```

/// html | div.result
//// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


////


//// define
`force_use`：<samp>boolean</samp>

- Determines if item can be used regardless of entity being at full health.


////


//// define
`items`：<samp>array</samp>

- The array of items that can be used to heal this entity.


////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。The filter group that defines the conditions for using this item to heal the entity.


//////


////// define
`heal_amount`：<samp>integer</samp>

- The amount of health this entity gains when fed this item.


//////


////// define
`item`：<samp>descriptor</samp> {#assets.schemas-blockception.general.item.descriptor.json}

- Item that can be used to heal this entity.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
  }
  0 "tags"
  string "item_tag" : opt
}

```

////// html | div.result
/////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


///////


/////// define
`item`：<samp>object</samp>

- An object that describes an item.


///////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////



/////// define
`tags`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- [UNDOCUMENTED] A Molang expression ran against item or block to match.


///////

```mcschema
0:
string

```

/////// html | div.result

///////



/////// define
`item_tag`：<samp>string</samp>

- [UNDOCUMENTED] A tag to lookup item or block by.


///////


//////


```mcschema
descriptor:
{
  identifier "item"
  object "item" : opt
  {
    identifier "item"
    object "item" : opt
    {
    }
    0 "tags"
    string "item_tag" : opt
  }
}

```

////// html | div.result
/////// define
`item`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>


///////


/////// define
`item`：<samp>object</samp>

- An object that describes an item.


///////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////



//////




////// define
`effects`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`name`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`duration`：<samp>integer</samp>

- The duration of the effect.


///////


/////// define
`amplifier`：<samp>integer</samp>

- The amplifier of the effect.


///////


//////


////// define
`effects`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////



/////


////


///

