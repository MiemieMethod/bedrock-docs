# Home

> 文档版本：1.21.0.24

Saves a home pos for when the the entity is spawned.

## 架构

```mcschema
home:
{
  integer "restriction_radius" : opt
  array "home_block_list" : opt
  {
    identifier "<any array element>"
  }
}

```

/// html | div.result
//// define
`restriction_radius`：<samp>integer</samp>

- The radius that the entity will be restricted to in relation to its home.


////


//// define
`home_block_list`：<samp>array</samp>

- Optional block list that the home position will be associated with. If any of the blocks no longer exist at that position, the home restriction is removed. Example syntax: minecraft:sand. Not supported: minecraft:sand:1


////

<div class="language-text highlight"><span class="filename"><code>home_block_list</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- Optional block that the home position will be associated with. If any of the blocks no longer exist at that position, the home restriction is removed. Example syntax: minecraft:sand. Not supported: minecraft:sand:1


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



////


///

