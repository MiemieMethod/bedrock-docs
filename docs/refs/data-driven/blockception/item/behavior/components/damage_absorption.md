# Damage Absorption

> 文档版本：1.21.50.25

It allows an item to absorb damage that would otherwise be dealt to its wearer. For this to happen, the item needs to be equipped in an armor slot. The absorbed damage reduces the item's durability, with any excess damage being ignored. Because of this, the item also needs a `minecraft:durability` component.

## 架构

```mcschema
minecraft:damage_absorption:
{
  array "absorbable_causes" : opt
  {
    entity_damage_source "<any array element>"
  }
}

```

/// html | div.result
//// define
`absorbable_causes`：<samp>array</samp>

- List of damage causes that can be absorbed by the item. By default, no damage cause is absorbed.


////

<div class="language-text highlight"><span class="filename"><code>absorbable_causes</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>entity_damage_source</samp> {#assets.schemas-blockception.general.entity.damage_source.json}


/////

```mcschema
entity_damage_source:
string

```

///// html | div.result

/////



////


///

