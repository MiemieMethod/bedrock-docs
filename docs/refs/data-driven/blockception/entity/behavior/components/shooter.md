# Shooter

> 文档版本：1.21.50.25

Defines the entity's ranged attack behavior.

## 架构

```mcschema
shooter:
{
  integer "aux_val" : opt
  string "def" : opt
  boolean "magic" : opt
  number "power" : opt
  array "projectiles" : opt
  {
    string "<any array element>" : opt
    object "<any array element>" : opt
    {
      integer "aux_val" : opt
      string "def" : opt
      filters "filters"
    }
  }
  string "sound" : opt
}

```

/// html | div.result
//// define
`aux_val`：<samp>integer</samp>

- ID of the Potion effect to be applied on hit.


////


//// define
`def`：<samp>string</samp>

- Actor definition to use as projectile for the ranged attack. The actor definition must have the projectile component to be able to be shot as a projectile


////


//// define
`magic`：<samp>boolean</samp>

- Sets whether the projectiles being used are flagged as magic. If set, the ranged attack goal will not be used at the same time as other magic goals, such as minecraft:behavior.drink_potion.


////


//// define
`power`：<samp>number</samp>

- Velocity in which the projectiles will be shot. A power of 0 will be overwritten by the default projectile throw power.


////


//// define
`projectiles`：<samp>array</samp>

- List of projectiles that can be used by the shooter. Projectiles are evaluated in the order of the list; after a projectile is chosen, the rest of the list is ignored.


////

<div class="language-text highlight"><span class="filename"><code>projectiles</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>

- Projectiles that can be used by the shooter


/////


///// define
`<any array element>`：<samp>object</samp>

- A projectile defintion


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`aux_val`：<samp>integer</samp>

- ID of the Potion effect to be applied on hit.


//////


////// define
`def`：<samp>string</samp>

- Actor definition to use as projectile for the ranged attack. The actor definition must have the projectile component to be able to be shot as a projectile


//////


////// define
`filters`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


//////


/////



////


//// define
`sound`：<samp>string</samp>

- Sound that is played when the shooter shoots a projectile.


////


///

