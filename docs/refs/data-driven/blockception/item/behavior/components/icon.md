# Icon

> 文档版本：1.21.0.24

The icon item componenent determines the icon to represent the item in the UI and elsewhere.

## 架构

```mcschema
minecraft:icon:
{
  object "textures" : opt
  {
    string "default" : opt
  }
}

```

/// html | div.result
//// define
`textures`：<samp>object</samp>

- Contains key-value pairs of textures used by the item


////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`default`：<samp>string</samp>

- The key from the resource_pack/textures/item_texture.json `texture_data` object associated with the texture file Example: blaze_powder.


/////


////


///

