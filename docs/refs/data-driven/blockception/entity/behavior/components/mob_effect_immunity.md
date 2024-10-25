# Mob Effect Immunity

> 文档版本：1.21.50.25

Entities with this component will have an immunity to the provided mob effects.

## 架构

```mcschema
mob_effect_immunity:
{
  array "mob_effects" : opt
  {
    effect "<any array element>"
  }
}

```

/// html | div.result
//// define
`mob_effects`：<samp>array</samp>

- List of names of effects the entity is immune to.


////

<div class="language-text highlight"><span class="filename"><code>mob_effects</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>effect</samp> {#assets.schemas-blockception.general.vanilla.effect.json}


/////

```mcschema
effect:
string

```

///// html | div.result

/////



////


///

