# Variable Max Auto Step

> 文档版本：1.21.50.25

Entities with this component will have a maximum auto step height that is different depending on wether they are on a block that prevents jumping. Incompatible with "runtime_identifier": "minecraft:horse".

## 架构

```mcschema
variable_max_auto_step:
{
  number "base_value" : opt
  number "controlled_value" : opt
  number "jump_prevented_value" : opt
}

```

/// html | div.result
//// define
`base_value`：<samp>number</samp>

- The maximum auto step height when on any other block.


////


//// define
`controlled_value`：<samp>number</samp>

- The maximum auto step height when on any other block and controlled by the player.


////


//// define
`jump_prevented_value`：<samp>number</samp>

- The maximum auto step height when on a block that prevents jumping.


////


///

