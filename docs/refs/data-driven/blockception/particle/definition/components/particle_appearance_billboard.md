# Particle Appearance Billboard Component For 1.10.0

> 文档版本：1.21.50.25

UNDOCUMENTED.

## 架构

```mcschema
particle_appearance_billboard:
{
  array "size" : opt
  {
    0 "<any array element>"
  }
  string "facing_camera_mode" : opt
  object "direction" : opt
  {
    string "mode" : opt
    array "custom_direction" : opt
    {
      0 "<any array element>"
    }
    number "min_speed_threshold" : opt
  }
  object "uv" : opt
  {
    integer "texture_width" : opt
    integer "texture_height" : opt
    object "flipbook" : opt
    {
      array "base_UV" : opt
      {
        0 "<any array element>"
      }
      array "size_UV" : opt
      {
        0 "<any array element>"
      }
      array "step_UV" : opt
      {
        0 "<any array element>"
      }
      0 "frames_per_second"
      0 "max_frame"
      boolean "stretch_to_lifetime" : opt
      boolean "loop" : opt
    }
    array "uv" : opt
    {
      0 "<any array element>"
    }
    array "uv_size" : opt
    {
      0 "<any array element>"
    }
  }
}

```

/// html | div.result
//// define
`size`：<samp>array</samp>

- UNDOCUMENTED: size.


////

<div class="language-text highlight"><span class="filename"><code>size</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- UNDOCUMENTED: size.


/////

```mcschema
0:
string

```

///// html | div.result

/////


```mcschema
0:
number

```

///// html | div.result

/////




////


//// define
`facing_camera_mode`：<samp>string</samp>

- Used to orient the billboard.


////


//// define
`direction`：<samp>object</samp>

- UNDOCUMENTED


////

<div class="language-text highlight"><span class="filename"><code>direction</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`mode`：<samp>string</samp>

- Specified how to calculate the billboard direction of a particle.


/////


///// define
`custom_direction`：<samp>array</samp>

- The facing direction of emitted particles.


/////

<div class="language-text highlight"><span class="filename"><code>custom_direction</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED.


//////


/////


///// define
`min_speed_threshold`：<samp>number</samp>

- The direction is set if the speed of the particle is above the threshold.


/////


////


//// define
`uv`：<samp>object</samp>

- UNDOCUMENTED: uv.


////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`texture_width`：<samp>integer</samp>

- UNDOCUMENTED: texture width.


/////


///// define
`texture_height`：<samp>integer</samp>

- UNDOCUMENTED: texture height.


/////


///// define
`flipbook`：<samp>object</samp>

- UNDOCUMENTED: flipbook.


/////

<div class="language-text highlight"><span class="filename"><code>flipbook</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`base_UV`：<samp>array</samp>

- UNDOCUMENTED: base UV.


//////

<div class="language-text highlight"><span class="filename"><code>base_UV</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: base UV.


///////


//////


////// define
`size_UV`：<samp>array</samp>

- UNDOCUMENTED: size UV.


//////

<div class="language-text highlight"><span class="filename"><code>size_UV</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: size UV.


///////


//////


////// define
`step_UV`：<samp>array</samp>

- UNDOCUMENTED: step UV.


//////

<div class="language-text highlight"><span class="filename"><code>step_UV</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: step UV.


///////


//////


////// define
`frames_per_second`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: frames per second.


//////


////// define
`max_frame`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: Maximum frame.


//////


////// define
`stretch_to_lifetime`：<samp>boolean</samp>

- UNDOCUMENTED: stretch to lifetime.


//////


////// define
`loop`：<samp>boolean</samp>

- UNDOCUMENTED: loop.


//////


/////


///// define
`uv`：<samp>array</samp>

- UNDOCUMENTED: uv.


/////

<div class="language-text highlight"><span class="filename"><code>uv</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: uv.


//////


/////


///// define
`uv_size`：<samp>array</samp>

- UNDOCUMENTED: uv size.


/////

<div class="language-text highlight"><span class="filename"><code>uv_size</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: uv size.


//////


/////


////


///

