# Blocks

> 文档版本：1.21.0.24

The minecraft block definition file.

## 架构

```mcschema
json:
{
  format_version "format_version"
  array "format_version" : opt
  {
    integer "<any array element>" : opt
  }
  object "^[\w_\-:\.]+$" : opt
  {
    number "brightness_gamma" : opt
    string "carried_textures" : opt
    object "carried_textures" : opt
    {
      string "down" : opt
      string "up" : opt
      string "side" : opt
      string "south" : opt
      string "north" : opt
      string "west" : opt
      string "east" : opt
    }
    boolean "isotropic" : opt
    object "isotropic" : opt
    {
      boolean "down" : opt
      boolean "up" : opt
      boolean "side" : opt
      boolean "south" : opt
      boolean "north" : opt
      boolean "west" : opt
      boolean "east" : opt
    }
    string "sound" : opt
     "textures" : opt
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
`format_version`：<samp>array</samp>

- A version that tells Minecraft what type of data format can be expected when reading this file.


////

<div class="language-text highlight"><span class="filename"><code>format_version</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////



//// define
`^[\w_\-:\.]+$`：<samp>object</samp>

- Block texture definition.


////

<div class="language-text highlight"><span class="filename"><code>^[\w_\-:\.]+$</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`brightness_gamma`：<samp>number</samp>

- Specifies the gamma brightness level to apply to the block texture.


/////


///// define
`carried_textures`：<samp>string</samp>

- Carried Textures.


/////


///// define
`carried_textures`：<samp>object</samp>

- Carried Textures.


/////

<div class="language-text highlight"><span class="filename"><code>carried_textures</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`down`：<samp>string</samp>


//////


////// define
`up`：<samp>string</samp>


//////


////// define
`side`：<samp>string</samp>


//////


////// define
`south`：<samp>string</samp>


//////


////// define
`north`：<samp>string</samp>


//////


////// define
`west`：<samp>string</samp>


//////


////// define
`east`：<samp>string</samp>


//////


/////



///// define
`isotropic`：<samp>boolean</samp>

- Marks if this block is isotropic or not, or which side are.


/////


///// define
`isotropic`：<samp>object</samp>

- Marks if this block is isotropic or not, or which side are.


/////

<div class="language-text highlight"><span class="filename"><code>isotropic</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`down`：<samp>boolean</samp>


//////


////// define
`up`：<samp>boolean</samp>


//////


////// define
`side`：<samp>boolean</samp>


//////


////// define
`south`：<samp>boolean</samp>


//////


////// define
`north`：<samp>boolean</samp>


//////


////// define
`west`：<samp>boolean</samp>


//////


////// define
`east`：<samp>boolean</samp>


//////


/////



///// define
`sound`：<samp>string</samp>

- The sound definition of this block.


/////


///// define
`textures`

- Textures.


/////


////


///

