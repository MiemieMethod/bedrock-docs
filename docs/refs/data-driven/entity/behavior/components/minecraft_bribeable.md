# minecraft:bribeable

> 文档版本：1.21.0.24

Defines the way an entity can get into the 'bribed' state.

## 架构

```mcschema
minecraft:bribeable:
{
  number "bribe_cooldown" : opt
  array "bribe_items" : opt
  {
    item_descriptor "<any array element>"
  }
}

```

/// html | div.result
//// define
`bribe_cooldown`：<samp>number</samp>

- Time in seconds before the Entity can be bribed again.


////


//// define
`bribe_items`：<samp>array</samp>

- The list of items that can be used to bribe the entity.


////

<div class="language-text highlight"><span class="filename"><code>bribe_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}


/////

```mcschema
item_descriptor:
string

```

///// html | div.result

/////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

///// html | div.result
////// define
`<any object property>`：<samp>string</samp>


//////


/////




////


///

