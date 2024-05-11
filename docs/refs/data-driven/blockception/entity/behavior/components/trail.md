# Trail

> 文档版本：1.21.0.24

Defines the entity's trail to carry items.

## 架构

```mcschema
trail:
{
  string "block_type" : opt
  filters "spawn_filter"
  array "spawn_offset" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
    number "2..2" : opt
  }
}

```

/// html | div.result
//// define
`block_type`：<samp>string</samp>

- The type of block you wish to be spawned by the entity as it move about the world. Solid blocks may not be spawned at an offset of ().


////


//// define
`spawn_filter`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。One or more conditions that must be met in order to cause the chosen block type to spawn.


////


//// define
`spawn_offset`：<samp>array</samp>

- The distance from the entities current position to spawn the block. Capped at up to 16 blocks away. The X value is left/right(-/+), the Z value is backward/forward(-/+), the Y value is below/above(-/+).


////

<div class="language-text highlight"><span class="filename"><code>spawn_offset</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`0..0`：<samp>number</samp>


/////


///// define
`1..1`：<samp>number</samp>


/////


///// define
`2..2`：<samp>number</samp>


/////


////


///

