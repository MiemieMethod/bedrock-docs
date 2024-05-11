# Flipbook Texture File

> 文档版本：1.21.0.24

The file that specifies animated textures.

## 架构

```mcschema
flipbook:
array
{
  object "<any array element>" : opt
  {
    integer "atlas_index" : opt
    string "atlas_tile" : opt
    integer "atlas_tile_variant" : opt
    boolean "blend_frames" : opt
    string "flipbook_texture" : opt
    array "frames" : opt
    {
      integer "<any array element>" : opt
    }
    integer "replicate" : opt
    integer "ticks_per_frame" : opt
  }
}

```

/// html | div.result
//// define
`<any array element>`：<samp>object</samp>

- A single flipbook texture.


////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`atlas_index`：<samp>integer</samp>

- UNDOCUMENTED.


/////


///// define
`atlas_tile`：<samp>string</samp>

- UNDOCUMENTED.


/////


///// define
`atlas_tile_variant`：<samp>integer</samp>

- UNDOCUMENTED.


/////


///// define
`blend_frames`：<samp>boolean</samp>

- UNDOCUMENTED.


/////


///// define
`flipbook_texture`：<samp>string</samp>

- A texture file.


/////


///// define
`frames`：<samp>array</samp>

- The collection of frame index to display.


/////

<div class="language-text highlight"><span class="filename"><code>frames</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>integer</samp>

- The index of the frame.


//////


/////


///// define
`replicate`：<samp>integer</samp>

- UNDOCUMENTED.


/////


///// define
`ticks_per_frame`：<samp>integer</samp>

- The amount of ticks to wait between frames.


/////


////


///

