# 未命名

> 文档版本：1.21.0.24

Weapon Item Component. Added to every weapon item such as axe, sword, trident, bow, crossbow.

## 架构

```mcschema
minecraft:weapon:
{
  definition_trigger "on_hurt_entity"
  definition_trigger "on_not_hurt_entity"
  definition_trigger "on_hit_block"
}

```

/// html | div.result
//// define
`on_hurt_entity`：<samp>definition_trigger</samp> {#assets.schemas.common.definition.definition_trigger.json}

- Trigger for letting you know when this item is used to hurt another mob


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
`on_not_hurt_entity`：<samp>[definition_trigger](#assets.schemas.common.definition.definition_trigger.json)</samp>

- Trigger for letting you know when this item hit another actor, but didn't do damage


////


//// define
`on_hit_block`：<samp>[definition_trigger](#assets.schemas.common.definition.definition_trigger.json)</samp>

- Trigger for letting you know when this item is used to hit a block


////


///

