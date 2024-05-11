# 未命名

> 文档版本：1.21.0.24

Event trigger for when the item has completed its use duration.

## 架构

```mcschema
minecraft:chargeable:
{
  definition_trigger "on_complete"
  number "movement_modifier" : opt
}

```

/// html | div.result
//// define
`on_complete`：<samp>definition_trigger</samp> {#assets.schemas.common.definition.definition_trigger.json}

- Event trigger for when the item has completed its use duration.


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




//// define
`movement_modifier`：<samp>number</samp>

- Modifier value to scale the players movement speed when item is in use.


////


///

