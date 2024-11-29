# Home

> 文档版本：1.21.50.25

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
  string "restriction_type" : opt
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


//// define
`restriction_type`：<samp>string</samp>

- Defines how the the entity will be restricted to its home position. The possible values are:
- 'none', which poses no restriction.
- 'random_movement', which restricts randomized movement to be around the home position.
- [Beta] 'all_movement', which restricts any kind of movement to be around the home position. However, entities that somehow got too far away from their home will always be able to move closer to it, if prompted to do so.


////


///

