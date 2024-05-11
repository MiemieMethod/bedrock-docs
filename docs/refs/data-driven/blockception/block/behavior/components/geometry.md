# Geometry

> 文档版本：1.21.0.24

The description identifier of the geometry file to use to render this block. This identifier must match an existing geometry identifier in any of the currently loaded resource packs.

## 架构

```mcschema
geometry:
string

```

/// html | div.result

///


```mcschema
geometry:
{
  string "identifier" : opt
  object "bone_visibility" : opt
  {
    ['boolean', 'string'] "<any object property>" : opt
  }
  string "culling" : opt
}

```

/// html | div.result
//// define
`identifier`：<samp>string</samp>

- The description identifier of the geometry file to use to render this block. This identifier must match an existing geometry identifier in any of the currently loaded resource packs.


////


//// define
`bone_visibility`：<samp>object</samp>

- A list of bones that should be visible when rendering this block. If not specified, all bones will be visible.


////

<div class="language-text highlight"><span class="filename"><code>bone_visibility</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any object property>`：<samp>['boolean', 'string']</samp>

- Whether or not the bone should be visible. Can be defined as a boolean or a molang expression resulting in a boolean.


/////


////


//// define
`culling`：<samp>string</samp>

- The description identifer of the block culling rule used to cull this block. This identifier must match an existing geometry identifier in any of the currently loaded resource packs.


////


///


