# Block Culling

> 文档版本：1.21.0.24

A resource pack file that helps the system determine how to change the appearance of this block.

## 架构

```mcschema
block_culling:
{
  format_version "format_version"
  object "minecraft:block_culling_rules" : opt
  {
    object "description" : opt
    {
      identifier "identifier"
    }
    array "rules" : opt
    {
      object "<any array element>" : opt
      {
        object "geometry_part" : opt
        {
          string "bone" : opt
          integer "cube" : opt
          string "face" : opt
        }
        string "direction" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



//// define
`minecraft:block_culling_rules`：<samp>object</samp>

- JSON container used for descriptions, especially the identifier for the name of the culled version of the block.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:block_culling_rules</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- Contains the identifier used by minecraft:geometry block components to refer to this culling data


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.block_culling.identifier.json}

- Sets the identifier for this rule's description.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



/////


///// define
`rules`：<samp>array</samp>

- List of all components used to identify geometry parts used in culling.


/////

<div class="language-text highlight"><span class="filename"><code>rules</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- The rules that specifies a "geometry_part" and "direction"


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`geometry_part`：<samp>object</samp>

- Specifies the bone, cube, and face that the block will be culled. The cube and face fields are optional to allow culling a specific face. Omitting these fields will cull the whole bone.


///////

<div class="language-text highlight"><span class="filename"><code>geometry_part</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`bone`：<samp>string</samp>

- The bone within the geometry part


////////


//////// define
`cube`：<samp>integer</samp>

- The cube within the geometry part


////////


//////// define
`face`：<samp>string</samp>

- The face within the geometry part


////////


///////


/////// define
`direction`：<samp>string</samp>

- Specifies the direction of the neighbor block to check for culling. This direction rotates with a block's Transform component.


///////


//////


/////


////


///

