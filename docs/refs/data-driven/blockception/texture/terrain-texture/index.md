# Terrain Texture File

> 文档版本：1.21.0.24

An collection of texture definitions.

## 架构

```mcschema
terrain_texture:
{
  integer "num_mip_levels" : opt
  integer "padding" : opt
  string "resource_pack_name" : opt
  object "texture_data" : opt
  {
    object "^[\w_\-\.]+$" : opt
    {
      string "textures" : opt
      object "textures" : opt
      {
         "overlay_color" : opt
        string "path" : opt
        string "tint_color" : opt
        array "variations" : opt
        {
          object "<any array element>" : opt
          {
            string "path" : opt
            integer "weight" : opt
          }
        }
      }
      array "textures" : opt
      {
         "<any array element>" : opt
      }
    }
  }
  string "texture_name" : opt
}

```

/// html | div.result
//// define
`num_mip_levels`：<samp>integer</samp>

- UNDOCUMENTED.


////


//// define
`padding`：<samp>integer</samp>

- UNDOCUMENTED.


////


//// define
`resource_pack_name`：<samp>string</samp>

- UNDOCUMENTED.


////


//// define
`texture_data`：<samp>object</samp>

- UNDOCUMENTED.


////

<div class="language-text highlight"><span class="filename"><code>texture_data</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^[\w_\-\.]+$`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>^[\w_\-\.]+$</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`textures`：<samp>string</samp>

- A texture file.


//////


////// define
`textures`：<samp>object</samp>

- A collection of texture files.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`overlay_color`

- The color to apply to the texture.


///////


/////// define
`path`：<samp>string</samp>

- A texture file.


///////


/////// define
`tint_color`：<samp>string</samp>

- The tint color to be applied to the texture.


///////


/////// define
`variations`：<samp>array</samp>

- The possible variations to use for this texture.


///////

<div class="language-text highlight"><span class="filename"><code>variations</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- One of the variantions, specified along with a possible weight.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`path`：<samp>string</samp>

- A texture file.


/////////


///////// define
`weight`：<samp>integer</samp>

- The weight of the texture.


/////////


////////


///////


//////



////// define
`textures`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`


///////


//////



/////


////


//// define
`texture_name`：<samp>string</samp>

- UNDOCUMENTED.


////


///

