# Material

> 文档版本：1.21.0.24

A collection of material specifications for the render engine of minecraft.

## 架构

```mcschema
materials:
{
  object "materials" : opt
  {
    string "version" : opt
    object "<any object property>" : opt
    {
      string "alphaDst" : opt
      object "backFace" : opt
      {
        string "stencilDepthFailOp" : opt
        string "stencilFailOp" : opt
        string "stencilFunc" : opt
        string "stencilPass" : opt
        string "stencilPassOp" : opt
      }
      string "blendDst" : opt
      string "blendSrc" : opt
      array "defines" : opt
      {
        string "<any array element>" : opt
      }
      array "+defines" : opt
      array "-defines" : opt
      number "depthBias" : opt
      number "depthBiasOGL" : opt
      string "depthFunc" : opt
      string "fragmentShader" : opt
      object "frontFace" : opt
      {
      }
      integer "isAnimatedTexture" : opt
      string "msaaSupport" : opt
      string "primitiveMode" : opt
      array "samplerStates" : opt
      {
        object "<any array element>" : opt
        {
          integer "samplerIndex" : opt
          string "textureFilter" : opt
          string "textureWrap" : opt
        }
      }
      array "+samplerStates" : opt
      number "slopeScaledDepthBias" : opt
      number "slopeScaledDepthBiasOGL" : opt
      array "states" : opt
      {
        string "<any array element>" : opt
      }
      array "+states" : opt
      array "-states" : opt
      integer "stencilRef" : opt
      integer "stencilRefOverride" : opt
      integer "stencilReadMask" : opt
      integer "stencilWriteMask" : opt
      array "variants" : opt
      {
        object "<any array element>" : opt
        {
          object "<any object property>" : opt
          {
            array "+defines" : opt
            array "vertexFields" : opt
            {
              object "<any array element>" : opt
              {
                string "field" : opt
              }
            }
            array "states" : opt
            array "+states" : opt
            array "-states" : opt
          }
        }
      }
      array "+variants" : opt
      array "vertexFields" : opt
      string "vertexShader" : opt
      string "vrGeometryShader" : opt
    }
  }
}

```

/// html | div.result
//// define
`materials`：<samp>object</samp>

- The collection of materials, each property key is the identification key of the material, and what it implements if : are used.


////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`version`：<samp>string</samp>

- UNDOCUMENTED.


/////


///// define
`<any object property>`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`alphaDst`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`backFace`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>backFace</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`stencilDepthFailOp`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`stencilFailOp`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`stencilFunc`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`stencilPass`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`stencilPassOp`：<samp>string</samp>

- UNDOCUMENTED.


///////


//////


////// define
`blendDst`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`blendSrc`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`defines`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>defines</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


///////


//////


////// define
`+defines`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>+defines</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`-defines`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>-defines</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`depthBias`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`depthBiasOGL`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`depthFunc`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`fragmentShader`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`frontFace`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>frontFace</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`isAnimatedTexture`：<samp>integer</samp>

- UNDOCUMENTED, think its a boolean value as a number, so 1 and 0????.


//////


////// define
`msaaSupport`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`primitiveMode`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`samplerStates`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>samplerStates</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`samplerIndex`：<samp>integer</samp>

- UNDOCUMENTED.


////////


//////// define
`textureFilter`：<samp>string</samp>

- UNDOCUMENTED.


////////


//////// define
`textureWrap`：<samp>string</samp>

- UNDOCUMENTED.


////////


///////


//////


////// define
`+samplerStates`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>+samplerStates</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`slopeScaledDepthBias`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`slopeScaledDepthBiasOGL`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`states`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


///////


//////


////// define
`+states`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>+states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`-states`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>-states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`stencilRef`：<samp>integer</samp>

- UNDOCUMENTED.


//////


////// define
`stencilRefOverride`：<samp>integer</samp>

- UNDOCUMENTED.


//////


////// define
`stencilReadMask`：<samp>integer</samp>

- UNDOCUMENTED.


//////


////// define
`stencilWriteMask`：<samp>integer</samp>

- UNDOCUMENTED.


//////


////// define
`variants`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>variants</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`+defines`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>+defines</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`vertexFields`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>vertexFields</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


//////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`field`：<samp>string</samp>

- UNDOCUMENTED.


///////////


//////////


/////////


///////// define
`states`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`+states`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>+states</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`-states`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>-states</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


////////


///////


//////


////// define
`+variants`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>+variants</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`vertexFields`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>vertexFields</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`vertexShader`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`vrGeometryShader`：<samp>string</samp>

- UNDOCUMENTED.


//////


/////


////


///

