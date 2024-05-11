# Render Controllers

> 文档版本：1.21.0.24

A collection of render controllers to apply.

## 架构

```mcschema
render_controllers:
{
  format_version "format_version"
  object "render_controllers" : opt
  {
    object "^controller\.render\.[a-z\.]+" : opt
    {
      object "arrays" : opt
      {
        object "geometries" : opt
        {
          array "<any object property>" : opt
          {
            string "<any array element>" : opt
          }
        }
        object "materials" : opt
        {
          array "<any object property>" : opt
          {
            string "<any array element>" : opt
          }
        }
        object "textures" : opt
        {
          array "<any object property>" : opt
          {
            string "<any array element>" : opt
          }
        }
      }
      object "color" : opt
      {
        number "r" : opt
        string "r" : opt
         "g" : opt
         "b" : opt
         "a" : opt
      }
      boolean "filter_lighting" : opt
      0 "geometry"
      boolean "ignore_lighting" : opt
      object "is_hurt_color" : opt
      {
         "r" : opt
         "g" : opt
         "b" : opt
         "a" : opt
      }
      0 "light_color_multiplier"
      array "materials" : opt
      {
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
        }
      }
      object "on_fire_color" : opt
      {
         "r" : opt
         "g" : opt
         "b" : opt
         "a" : opt
      }
      object "overlay_color" : opt
      {
         "r" : opt
         "g" : opt
         "b" : opt
         "a" : opt
      }
      array "part_visibility" : opt
      {
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
          boolean "<any object property>" : opt
          number "<any object property>" : opt
        }
      }
      boolean "rebuild_animation_matrices" : opt
      array "textures" : opt
      {
        0 "<any array element>"
      }
      object "uv_anim" : opt
      {
        array "offset" : opt
        {
          0 "<any array element>"
        }
        array "scale" : opt
        {
          0 "<any array element>"
        }
      }
    }
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
`render_controllers`：<samp>object</samp>

- The collection of render controllers, each property is the identifier of a render controller.


////

<div class="language-text highlight"><span class="filename"><code>render_controllers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^controller\.render\.[a-z\.]+`：<samp>object</samp>

- A single render_controller.


/////

<div class="language-text highlight"><span class="filename"><code>^controller\.render\.[a-z\.]+</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`arrays`：<samp>object</samp>

- A collection of definition of arrays.


//////

<div class="language-text highlight"><span class="filename"><code>arrays</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`geometries`：<samp>object</samp>

- A collection of Geometry array.


///////

<div class="language-text highlight"><span class="filename"><code>geometries</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>array</samp>

- A geometry array definition.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- A geometry item, must be defined in the entity.


/////////


////////


///////


/////// define
`materials`：<samp>object</samp>

- A collection of materials array.


///////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>array</samp>

- A material array definition.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- A material item, must be defined in the entity.


/////////


////////


///////


/////// define
`textures`：<samp>object</samp>

- A collection of texture array.


///////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>array</samp>

- Textures.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- An texture item.


/////////


////////


///////


//////


////// define
`color`：<samp>object</samp>

- The color to apply.


//////

<div class="language-text highlight"><span class="filename"><code>color</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`r`：<samp>number</samp>

- A color definition as number, between 0 and 1.


///////


/////// define
`r`：<samp>string</samp>

- A color definition in molang, between 0 and 1.


///////



/////// define
`g`

- The value of green, between 0 and 1.


///////


/////// define
`b`

- The value of blue, between 0 and 1.


///////


/////// define
`a`

- The value of alpha, between 0 and 1.


///////


//////


////// define
`filter_lighting`：<samp>boolean</samp>

- Whenever or not to apply enviroment lighting to this object.


//////


////// define
`geometry`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- The model data to use.


//////

```mcschema
0:
string

```

////// html | div.result

//////



////// define
`ignore_lighting`：<samp>boolean</samp>

- Whenever or not to apply enviroment lighting to this object.


//////


////// define
`is_hurt_color`：<samp>object</samp>

- The color to overlay on the entity when hurt.


//////

<div class="language-text highlight"><span class="filename"><code>is_hurt_color</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`r`

- The value of red, between 0 and 1.


///////


/////// define
`g`

- The value of green, between 0 and 1.


///////


/////// define
`b`

- The value of blue, between 0 and 1.


///////


/////// define
`a`

- The value of alpha, between 0 and 1.


///////


//////


////// define
`light_color_multiplier`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- The amount of light that blends into what is being rendered, lower values gives darker rendering, (1 = 100%).


//////

```mcschema
0:
string

```

////// html | div.result

//////


```mcschema
0:
number

```

////// html | div.result

//////




////// define
`materials`：<samp>array</samp>

- The specification where to apply materials to.


//////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- The definitions of what material to apply to what set of bones, can be done through specific names, or patterns using * as a wildcard.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- The material to apply, or patterns using * as a wildcard.


////////


///////


//////


////// define
`on_fire_color`：<samp>object</samp>

- The color that will be overlayed when the object is on fire.


//////

<div class="language-text highlight"><span class="filename"><code>on_fire_color</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`r`

- The value of red, must result in a float between 0 and 1.


///////


/////// define
`g`

- The value of green, must result in a float between 0 and 1.


///////


/////// define
`b`

- The value of blue, must result in a float between 0 and 1.


///////


/////// define
`a`

- The value of alpha, must result in a float between 0 and 1.


///////


//////


////// define
`overlay_color`：<samp>object</samp>

- The color to put over the object.


//////

<div class="language-text highlight"><span class="filename"><code>overlay_color</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`r`

- The value of red, between 0 and 1.


///////


/////// define
`g`

- The value of green, between 0 and 1.


///////


/////// define
`b`

- The value of blue, between 0 and 1.


///////


/////// define
`a`

- The value of alpha, between 0 and 1.


///////


//////


////// define
`part_visibility`：<samp>array</samp>

- Determines what part of the object to show or hide.


//////

<div class="language-text highlight"><span class="filename"><code>part_visibility</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- The object that describe different bone visibility.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>


////////


//////// define
`<any object property>`：<samp>boolean</samp>


////////


//////// define
`<any object property>`：<samp>number</samp>


////////



///////


//////


////// define
`rebuild_animation_matrices`：<samp>boolean</samp>

- Whenever or not to rebuild the animation matrices.


//////


////// define
`textures`：<samp>array</samp>

- The texture to apply, multiple texture can be used as to create an overlay effect, a specific material is required though.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- The texture definition to apply.


///////


//////


////// define
`uv_anim`：<samp>object</samp>

- The UV animation to apply to the render texture.


//////

<div class="language-text highlight"><span class="filename"><code>uv_anim</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`offset`：<samp>array</samp>

- The offset to apply the UV, this will cause the texture on the object to shift by said amount, can be molang. The value for how much to offset is usually specified between 0 and 1


///////

<div class="language-text highlight"><span class="filename"><code>offset</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The offset to apply on the texture, can be molang.


////////


///////


/////// define
`scale`：<samp>array</samp>

- The scale to apply to the texture, this will cause texture to seem to grow and shrink if done per frame.


///////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The scale to apply on the texture, can be molang.


////////


///////


//////


/////


////


///

