# Horse Jump Strength

> 文档版本：1.21.0.24

Allows this mob to jump higher when being ridden by a player.

## 架构

```mcschema
jump_strength:
{
  object "value" : opt
  {
    number "range_min" : opt
    number "range_max" : opt
  }
  number "value" : opt
}

```

/// html | div.result
//// define
`value`：<samp>object</samp>

- The multiplier to apply to the jumping height.


////

<div class="language-text highlight"><span class="filename"><code>value</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`range_min`：<samp>number</samp>


/////


///// define
`range_max`：<samp>number</samp>


/////


////


//// define
`value`：<samp>number</samp>

- The multiplier to apply to the jumping height.


////



///

