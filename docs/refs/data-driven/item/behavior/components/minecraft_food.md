# minecraft:food

> 文档版本：1.21.0.24

When an item has a food component, it becomes edible to the player. Must have the 'minecraft:use_duration' component in order to function properly.

## 架构

```mcschema
minecraft:food:
{
  boolean "can_always_eat" : opt
  integer "nutrition" : opt
  number "saturation_modifier" : opt
  string "saturation_modifier" : opt
  item_descriptor "using_converts_to"
  string "on_use_action" : opt
  array "on_use_range" : opt
  {
    number "<any array element>" : opt
  }
  string "cooldown_type" : opt
  integer "cooldown_time" : opt
  array "effects" : opt
  {
    object "<any array element>" : opt
    {
      string "name" : opt
      integer "duration" : opt
      integer "amplifier" : opt
      number "chance" : opt
    }
  }
  array "remove_effects" : opt
  {
    string "<any array element>" : opt
  }
  definition_trigger "on_consume"
}

```

/// html | div.result
//// define
`can_always_eat`：<samp>boolean</samp>

- If true you can always eat this item (even when not hungry). Default is set to false.


////


//// define
`nutrition`：<samp>integer</samp>

- Value that is added to the entity's nutrition when the item is used. Default is set to 0.


////


//// define
`saturation_modifier`：<samp>number</samp>

- saturation_modifier is used in this formula: (nutrition * saturation_modifier * 2) when applying the saturation buff. Default is set to 0.6.


////


//// define
`saturation_modifier`：<samp>string</samp>


////



//// define
`using_converts_to`：<samp>item_descriptor</samp> {#assets.schemas.common.definition.item.item_descriptor.json}

- When used, converts to the item specified by the string in this field. Default does not convert item.


////

```mcschema
item_descriptor:
string

```

//// html | div.result

////


```mcschema
item_descriptor:
{
  string "<any object property>" : opt
}

```

//// html | div.result
///// define
`<any object property>`：<samp>string</samp>


/////


////




//// define
`on_use_action`：<samp>string</samp>


////


//// define
`on_use_range`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>on_use_range</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


//// define
`cooldown_type`：<samp>string</samp>


////


//// define
`cooldown_time`：<samp>integer</samp>


////


//// define
`effects`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>effects</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`name`：<samp>string</samp>


//////


////// define
`duration`：<samp>integer</samp>


//////


////// define
`amplifier`：<samp>integer</samp>


//////


////// define
`chance`：<samp>number</samp>


//////


/////


////


//// define
`remove_effects`：<samp>array</samp>


////

<div class="language-text highlight"><span class="filename"><code>remove_effects</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`on_consume`：<samp>definition_trigger</samp> {#assets.schemas.common.definition.definition_trigger.json}

- Event trigger for when the item is consumed.


////

```mcschema
definition_trigger:
string

```

//// html | div.result

////


```mcschema
definition_trigger:
{
  string "event" : opt
  string "target" : opt
  expression_node "condition"
}

```

//// html | div.result
///// define
`event`：<samp>string</samp>


/////


///// define
`target`：<samp>string</samp>


/////


///// define
`condition`：<samp>expression_node</samp> {#assets.schemas.common.molang.expression_node.json}


/////

```mcschema
expression_node:
string

```

///// html | div.result

/////


```mcschema
expression_node:
number

```

///// html | div.result

/////


```mcschema
expression_node:
{
  string "expression" : opt
  integer "version" : opt
}

```

///// html | div.result
////// define
`expression`：<samp>string</samp>


//////


////// define
`version`：<samp>integer</samp>


//////


/////




////




///

