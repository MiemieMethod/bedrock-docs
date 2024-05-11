# minecraft:icon

> 文档版本：1.21.0.24

Icon item component determines which icon graphic will be used to represent the item in the UI and elsewhere.

## 架构

```mcschema
minecraft:icon:
string

```

/// html | div.result

///


```mcschema
minecraft:icon:
{
  string "texture" : opt
  object "textures" : opt
  {
    object "textures" : opt
    {
      string "default" : opt
      string "<any object property>" : opt
    }
  }
}

```

/// html | div.result
//// define
`texture`：<samp>string</samp>

- The key from the resource_pack/textures/item_texture.json 'texture_data' object associated with the texture file.


////


//// define
`textures`：<samp>object</samp>

- This map contains the different textures that can be used for the item's icon. Default will contain the actual icon texture. Armor trim textures and palettes can be specified here too. The icon textures are the keys from the resource_pack/textures/item_texture.json 'texture_data' object associated with the texture file.


////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`textures`：<samp>object</samp>

- This map contains the different textures that can be used for the item's icon. Default will contain the actual icon texture. Armor trim textures and palettes can be specified here too. The icon textures are the keys from the resource_pack/textures/item_texture.json 'texture_data' object associated with the texture file.


/////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`default`：<samp>string</samp>

- The key from the resource_pack/textures/item_texture.json 'texture_data' object associated with the texture file.


//////


////// define
`<any object property>`：<samp>string</samp>


//////


/////


////


///


