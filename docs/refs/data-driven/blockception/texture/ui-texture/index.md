# UI Texture File

> 文档版本：1.21.50.25

The file that specifies either 9slice texture or Aseprite flipbook.

## 架构

```mcschema
nine_slice:
{
  number "nineslice_size" : opt
  array "nineslice_size" : opt
  {
    number "<any array element>" : opt
  }
  array "base_size" : opt
  {
    number "<any array element>" : opt
  }
}

```

/// html | div.result
//// define
`nineslice_size`：<samp>number</samp>

- Offset from left, top, right and bottom of the texture file.


////


//// define
`nineslice_size`：<samp>array</samp>

- Offsets from left, top, right and bottom of the texture file (in this exact order).


////

<div class="language-text highlight"><span class="filename"><code>nineslice_size</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////



//// define
`base_size`：<samp>array</samp>

- Width and height of the texture (in this exact order).


////

<div class="language-text highlight"><span class="filename"><code>base_size</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>number</samp>


/////


////


///



```mcschema
aseprite_flipbook:
{
  object "meta" : opt
  {
    object "size" : opt
    {
      integer "w" : opt
      integer "h" : opt
    }
    string "image" : opt
  }
  array "frames" : opt
  {
    object "<any array element>" : opt
    {
      integer "duration" : opt
      object "frame" : opt
      {
        integer "x" : opt
        integer "y" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`meta`：<samp>object</samp>

- The meta data of the flipbook.


////

<div class="language-text highlight"><span class="filename"><code>meta</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`size`：<samp>object</samp>

- The size of the flipbook sprite sheet.


/////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`w`：<samp>integer</samp>

- The width of the sprite sheet.


//////


////// define
`h`：<samp>integer</samp>

- The height of the sprite sheet.


//////


/////


///// define
`image`：<samp>string</samp>

- The path to the sprite sheet. The value is required, but not used.


/////


////


//// define
`frames`：<samp>array</samp>

- The frames of the flipbook.


////

<div class="language-text highlight"><span class="filename"><code>frames</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- A frame of the flipbook.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`duration`：<samp>integer</samp>

- The duration of the frame in milliseconds.


//////


////// define
`frame`：<samp>object</samp>

- The position of the frame in the sprite sheet (UV).


//////

<div class="language-text highlight"><span class="filename"><code>frame</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`x`：<samp>integer</samp>

- The x position of the frame in the sprite sheet.


///////


/////// define
`y`：<samp>integer</samp>

- The y position of the frame in the sprite sheet.


///////


//////


/////


////


///



