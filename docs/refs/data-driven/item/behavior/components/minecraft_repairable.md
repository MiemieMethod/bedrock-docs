# minecraft:repairable

> 文档版本：1.21.0.24

The repairable item component specifies which items can be used to repair this item, along with how much durability is gained.

## 架构

```mcschema
minecraft:repairable:
{
  array "repair_items" : opt
  {
    array "<any array element>" : opt
    {
      item_descriptor "<any array element>"
    }
    object "<any array element>" : opt
    {
      array "items" : opt
      {
        item_descriptor "<any array element>"
      }
      expression_node "repair_amount"
    }
    string "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`repair_items`：<samp>array</samp>

- List of repair item entries. Each entry needs to define a list of strings for `items` that can be used for the repair and an optional `repair_amount` for how much durability is gained.


////

<div class="language-text highlight"><span class="filename"><code>repair_items</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}


//////

```mcschema
item_descriptor:
string

```

////// html | div.result

//////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>


///////


//////




/////


///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`items`：<samp>array</samp>

- Items that may be used to repair an item.


//////

<div class="language-text highlight"><span class="filename"><code>items</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[item_descriptor](#assets.schemas.common.definition.item.item_descriptor.json)</samp>


///////


//////


////// define
`repair_amount`：<samp>expression_node</samp> {#assets.schemas.common.molang.expression_node.json}

- How much the item is repaired.


//////

```mcschema
expression_node:
string

```

////// html | div.result

//////


```mcschema
expression_node:
number

```

////// html | div.result

//////


```mcschema
expression_node:
{
  string "expression" : opt
  integer "version" : opt
}

```

////// html | div.result
/////// define
`expression`：<samp>string</samp>


///////


/////// define
`version`：<samp>integer</samp>


///////


//////




/////


///// define
`<any array element>`：<samp>string</samp>


/////



////


///

