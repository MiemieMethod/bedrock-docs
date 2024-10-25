# 未命名

> 文档版本：1.21.0.24

The description identifier of the geometry to use to render this block. This identifier must match an existing geometry identifier in any of the loaded resource packs or be one of the currently supported Vanilla identifiers: minecraft:geometry.full_block or minecraft:geometry.cross.

## 架构

```mcschema
minecraft:geometry:
string

```

/// html | div.result

///


```mcschema
minecraft:geometry:
string

```

/// html | div.result

///


```mcschema
minecraft:geometry:
{
  string "identifier" : opt
  object "bone_visibility" : opt
  {
    boolean "^[a-zA-Z0-9]*$" : opt
  }
}

```

/// html | div.result
//// define
`identifier`：<samp>string</samp>

- This component is specified as an Identifier String, so it does not have a default value. You must provide a valid geometry identifier in order to use this component.


////


//// define
`bone_visibility`：<samp>object</samp>

- minecraft:bone_visibility is an optional array of Booleans that define the visibility of individual bones in the geometry file. In order to set up 'bone_visibility' the geometry file name must be entered as an identifier. After the identifier has been specified, bone_visibility can be defined based on the names of the bones in the specified geometry file on a true/false basis.

Note that all bones default to 'true,' so bones should only be defined if they are being set to 'false.' Including bones set to 'true' will work the same as the default.


////

<div class="language-text highlight"><span class="filename"><code>bone_visibility</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^[a-zA-Z0-9]*$`：<samp>boolean</samp>


/////


////


///


