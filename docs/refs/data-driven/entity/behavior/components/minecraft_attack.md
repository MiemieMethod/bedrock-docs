# minecraft:attack

> 文档版本：1.21.0.24

Defines an entity's melee attack and any additional effects on it.

## 架构

```mcschema
minecraft:attack:
{
  integer "damage" : opt
  array "damage" : opt
  {
    integer "<any array element>" : opt
  }
  number "effect_duration" : opt
  string "effect_name" : opt
}

```

/// html | div.result
//// define
`damage`：<samp>integer</samp>


////


//// define
`damage`：<samp>array</samp>

- Range of the random amount of damage the melee attack deals. A negative value can heal the entity instead of hurting it.


////

<div class="language-text highlight"><span class="filename"><code>damage</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////



//// define
`effect_duration`：<samp>number</samp>

- Duration in seconds of the status ailment applied to the damaged entity.


////


//// define
`effect_name`：<samp>string</samp>

- Identifier of the status ailment to apply to an entity attacked by this entity's melee attack.


////


///

