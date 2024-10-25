# 未命名

> 文档版本：1.21.50.25



## 架构

```mcschema
texture_set:
{
  format_version "format_version"
  object "minecraft:texture_set" : opt
  {
    string "color" : opt
    array "color" : opt
    {
      integer "0..0" : opt
      integer "1..1" : opt
      integer "2..2" : opt
      integer "3..3" : opt
    }
    string "heightmap" : opt
    integer "heightmap" : opt
    string "metalness_emissive_roughness" : opt
    array "metalness_emissive_roughness" : opt
    {
      integer "0..0" : opt
      integer "1..1" : opt
      integer "2..2" : opt
    }
    string "normal" : opt
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
`minecraft:texture_set`：<samp>object</samp>

- Texture Sets are used to define multiple PBR layers for a texture resource.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:texture_set</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`color`：<samp>string</samp>

- This is an RGB 3-channel image (defaults to uniform alpha of 1.0), or an RGBA 4-channel image, or a 4 value array for a uniform color with alpha.


/////


///// define
`color`：<samp>array</samp>

- This is an RGB 3-channel image (defaults to uniform alpha of 1.0), or an RGBA 4-channel image, or a 4 value array for a uniform color with alpha.


/////

<div class="language-text highlight"><span class="filename"><code>color</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>integer</samp>


//////


////// define
`1..1`：<samp>integer</samp>


//////


////// define
`2..2`：<samp>integer</samp>


//////


////// define
`3..3`：<samp>integer</samp>


//////


/////



///// define
`heightmap`：<samp>string</samp>

- 1-channel layer image or a single value in this JSON file for a uniform heightmap. This layer and the "normal" layer should not both be defined at the same time.


/////


///// define
`heightmap`：<samp>integer</samp>

- 1-channel layer image or a single value in this JSON file for a uniform heightmap. This layer and the "normal" layer should not both be defined at the same time.


/////



///// define
`metalness_emissive_roughness`：<samp>string</samp>

- This is a 3-channel image (or 4-channel where the 4th channel is ignored) or a 3-value array for a uniform MER. RGB images map Red to Metalness, Green to Emissive, and Blue to Roughness.


/////


///// define
`metalness_emissive_roughness`：<samp>array</samp>

- This is a 3-channel image (or 4-channel where the 4th channel is ignored) or a 3-value array for a uniform MER. RGB images map Red to Metalness, Green to Emissive, and Blue to Roughness.


/////

<div class="language-text highlight"><span class="filename"><code>metalness_emissive_roughness</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>integer</samp>


//////


////// define
`1..1`：<samp>integer</samp>


//////


////// define
`2..2`：<samp>integer</samp>


//////


/////



///// define
`normal`：<samp>string</samp>

- This is a 3-channel normal map image (or 4-channel where the 4th channel is ignored). This layer and the "heightmap" layer should not both be defined at the same time.


/////


////


///

