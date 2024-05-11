# Durability

> 文档版本：1.21.0.24

Durability item component: how much damage can this item take before breaking.

## 架构

```mcschema
minecraft:durability:
{
  object "damage_chance" : opt
  {
    integer "min" : opt
    integer "max" : opt
  }
  integer "max_durability" : opt
}

```

/// html | div.result
//// define
`damage_chance`：<samp>object</samp>

- Damage chance.


////

<div class="language-text highlight"><span class="filename"><code>damage_chance</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`min`：<samp>integer</samp>

- The minimum.


/////


///// define
`max`：<samp>integer</samp>

- The maximum.


/////


////


//// define
`max_durability`：<samp>integer</samp>

- Maximum durability is the amount of damage that this item can take before breaking.


////


///

