# Particle Appearance Tinting Component For 1.10.0

> 文档版本：1.21.50.25

Color fields are special, they can be either an RGB, or a `#RRGGBB` field (or RGBA or `AARRGGBB`).  If RGB(A), the channels are from 0 to 1.  If the string `#AARRGGBB`, then the values are hex from 00 to ff.

## 架构

```mcschema
particle_appearance_tinting:
{
  array "color" : opt
  {
    0 "<any array element>"
  }
  string "color" : opt
  object "color" : opt
  {
    array "gradient" : opt
    {
      string "<any array element>" : opt
    }
    object "gradient" : opt
    {
      string "(^[\-0-9]+$|^[\-0-9]+\.[\-0-9]+$)" : opt
    }
    array "gradient" : opt
    {
      array "<any array element>" : opt
      {
        number "<any array element>" : opt
        string "<any array element>" : opt
      }
    }
    0 "interpolant"
  }
}

```

/// html | div.result
//// define
`color`：<samp>array</samp>

- Direct color field.


////

<div class="language-text highlight"><span class="filename"><code>color</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}


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
`color`：<samp>string</samp>

- Direct color field.


////


//// define
`color`：<samp>object</samp>

- Interpolation based color.


////

<div class="language-text highlight"><span class="filename"><code>color</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`gradient`：<samp>array</samp>

- An array of colors.


/////

<div class="language-text highlight"><span class="filename"><code>gradient</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>

- Color.


//////


/////


///// define
`gradient`：<samp>object</samp>

- An object of colors.


/////

<div class="language-text highlight"><span class="filename"><code>gradient</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`(^[\-0-9]+$|^[\-0-9]+\.[\-0-9]+$)`：<samp>string</samp>

- Color.


//////


/////


///// define
`gradient`：<samp>array</samp>

- An array of colors.


/////

<div class="language-text highlight"><span class="filename"><code>gradient</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>array</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>number</samp>

- Color.


///////


/////// define
`<any array element>`：<samp>string</samp>


///////



//////


/////



///// define
`interpolant`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: interpolant.


/////


////



///

