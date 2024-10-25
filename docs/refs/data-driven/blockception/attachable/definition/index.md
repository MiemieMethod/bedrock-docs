# 未命名

> 文档版本：1.21.50.25



## 架构

```mcschema
attachables:
{
  string "format_version" : opt
  object "minecraft:attachable" : opt
  {
    object "description" : opt
    {
      object "animations" : opt
      {
        string "<any object property>" : opt
      }
      array "animation_controllers" : opt
      {
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
        }
      }
      boolean "enable_attachables" : opt
      object "geometry" : opt
      {
        string "<any object property>" : opt
      }
      identifier "identifier"
      object "item" : opt
      {
        string "<any object property>" : opt
      }
      object "materials" : opt
      {
        material "<any object property>"
      }
      string "min_engine_version" : opt
      object "particle_effects" : opt
      {
        string "<any object property>" : opt
      }
      object "particle_emitters" : opt
      {
        string "<any object property>" : opt
      }
      array "render_controllers" : opt
      {
        string "<any array element>" : opt
      }
      array "sound_effects" : opt
      {
        string "<any array element>" : opt
      }
      object "spawn_egg" : opt
      {
        string "base_colour" : opt
        string "overlay_color" : opt
        string "texture" : opt
        integer "texture_index" : opt
      }
      object "scripts" : opt
      {
        array "pre_animation" : opt
        {
          0 "<any array element>"
        }
        string "scale" : opt
        array "animate" : opt
        {
          string "<any array element>" : opt
          object "<any array element>" : opt
          {
            string "<any object property>" : opt
          }
        }
        0 "parent_setup"
      }
      object "textures" : opt
      {
        string "<any object property>" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`minecraft:attachable`：<samp>object</samp>

- The attachables definition for 1.8.0


////

<div class="language-text highlight"><span class="filename"><code>minecraft:attachable</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- UNDOCUMENTED: description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animations`：<samp>object</samp>

- The connecting of animations in animations controllers with the actuall animations, names should corosponds.


//////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


////// define
`animation_controllers`：<samp>array</samp>

- UNDOCUMENTED: animation controllers.


//////

<div class="language-text highlight"><span class="filename"><code>animation_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED: animation controllers.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


////////


///////


//////


////// define
`enable_attachables`：<samp>boolean</samp>

- UNDOCUMENTED: enable attachables.


//////


////// define
`geometry`：<samp>object</samp>

- UNDOCUMENTED: geometry.


//////

<div class="language-text highlight"><span class="filename"><code>geometry</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- UNDOCUMENTED: identifier.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`item`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED.


///////


//////


////// define
`materials`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>material</samp> {#assets.schemas-blockception.general.vanilla.material.json}

- Material Reference.


///////

```mcschema
material:
string

```

/////// html | div.result

///////



//////


////// define
`min_engine_version`：<samp>string</samp>

- UNDOCUMENTED: Minimum engine version.


//////


////// define
`particle_effects`：<samp>object</samp>

- UNDOCUMENTED: particle effects.


//////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


////// define
`particle_emitters`：<samp>object</samp>

- UNDOCUMENTED: particle emitters.


//////

<div class="language-text highlight"><span class="filename"><code>particle_emitters</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


////// define
`render_controllers`：<samp>array</samp>

- UNDOCUMENTED: render controllers.


//////

<div class="language-text highlight"><span class="filename"><code>render_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: render controllers.


///////


//////


////// define
`sound_effects`：<samp>array</samp>

- UNDOCUMENTED: sound effects.


//////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: sound effects.


///////


//////


////// define
`spawn_egg`：<samp>object</samp>

- UNDOCUMENTED: spawn egg.


//////

<div class="language-text highlight"><span class="filename"><code>spawn_egg</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base_colour`：<samp>string</samp>

- UNDOCUMENTED: base colour.


///////


/////// define
`overlay_color`：<samp>string</samp>

- UNDOCUMENTED: overlay color.


///////


/////// define
`texture`：<samp>string</samp>

- UNDOCUMENTED: texture.


///////


/////// define
`texture_index`：<samp>integer</samp>

- UNDOCUMENTED: texture index.


///////


//////


////// define
`scripts`：<samp>object</samp>

- UNDOCUMENTED: scripts.


//////

<div class="language-text highlight"><span class="filename"><code>scripts</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`pre_animation`：<samp>array</samp>

- UNDOCUMENTED: pre aninamtion.


///////

<div class="language-text highlight"><span class="filename"><code>pre_animation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- UNDOCUMENTED: pre aninamtion.


////////

```mcschema
0:
string

```

//////// html | div.result

////////


```mcschema
0:
number

```

//////// html | div.result

////////




///////


/////// define
`scale`：<samp>string</samp>

- UNDOCUMENTED: scale.


///////


/////// define
`animate`：<samp>array</samp>

- UNDOCUMENTED: animate.


///////

<div class="language-text highlight"><span class="filename"><code>animate</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: oneOf[0].


////////


//////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED: oneOf[1].


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


/////////


////////



///////


/////// define
`parent_setup`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


//////


////// define
`textures`：<samp>object</samp>

- UNDOCUMENTED: textures.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


/////


////


///




```mcschema
attachables:
{
  string "format_version" : opt
  object "minecraft:attachable" : opt
  {
    object "description" : opt
    {
      object "animations" : opt
      {
        string "<any object property>" : opt
      }
      array "animation_controllers" : opt
      boolean "enable_attachables" : opt
      object "geometry" : opt
      {
        string "[a-zA-Z0-9_\.\-]+" : opt
      }
      identifier "identifier"
      object "item" : opt
      {
        string "<any object property>" : opt
      }
      object "materials" : opt
      {
        material "<any object property>"
      }
      string "min_engine_version" : opt
      object "particle_effects" : opt
      {
        string "<any object property>" : opt
      }
      object "particle_emitters" : opt
      {
        string "<any object property>" : opt
      }
      array "render_controllers" : opt
      {
        string "<any array element>" : opt
      }
      object "scripts" : opt
      {
        array "animate" : opt
        {
          string "<any array element>" : opt
          object "<any array element>" : opt
          {
            string "<any object property>" : opt
          }
        }
        array "initialize" : opt
        {
          0 "<any array element>"
        }
        array "pre_animation" : opt
        {
          0 "<any array element>"
        }
        0 "parent_setup"
        0 "scale"
      }
      array "sound_effects" : opt
      {
        string "<any array element>" : opt
      }
      object "spawn_egg" : opt
      {
        string "base_colour" : opt
        string "overlay_color" : opt
        string "texture" : opt
        integer "texture_index" : opt
      }
      object "textures" : opt
      {
        string "<any object property>" : opt
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>

- A version that tells minecraft what type of data format can be expected when reading this file.


////


//// define
`minecraft:attachable`：<samp>object</samp>

- The attachables definition.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:attachable</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- UNDOCUMENTED: description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animations`：<samp>object</samp>

- The collection of animations references.


//////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A single animation reference.


///////


//////


////// define
`animation_controllers`：<samp>array</samp>

- The specification of animation controllers.


//////

<div class="language-text highlight"><span class="filename"><code>animation_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`enable_attachables`：<samp>boolean</samp>

- UNDOCUMENTED: enable attachables.


//////


////// define
`geometry`：<samp>object</samp>

- The geometry specification.


//////

<div class="language-text highlight"><span class="filename"><code>geometry</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`[a-zA-Z0-9_\.\-]+`：<samp>string</samp>

- A single geometry reference.


///////


//////


////// define
`identifier`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>

- UNDOCUMENTED: identifier.


//////


////// define
`item`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>item</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED.


///////


//////


////// define
`materials`：<samp>object</samp>

- A collection of material references.


//////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>[material](#assets.schemas-blockception.general.vanilla.material.json)</samp>

- A single material reference.


///////


//////


////// define
`min_engine_version`：<samp>string</samp>

- The minimum engine needed to use this.


//////


////// define
`particle_effects`：<samp>object</samp>

- A collection of particle effect references.


//////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A single particle effect reference.


///////


//////


////// define
`particle_emitters`：<samp>object</samp>

- UNDOCUMENTED: particle emitters.


//////

<div class="language-text highlight"><span class="filename"><code>particle_emitters</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


////// define
`render_controllers`：<samp>array</samp>

- UNDOCUMENTED: render controllers.


//////

<div class="language-text highlight"><span class="filename"><code>render_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: render controllers.


///////


//////


////// define
`scripts`：<samp>object</samp>

- UNDOCUMENTED: scripts.


//////

<div class="language-text highlight"><span class="filename"><code>scripts</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`animate`：<samp>array</samp>

- UNDOCUMENTED: animate.


///////

<div class="language-text highlight"><span class="filename"><code>animate</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: oneOf[0].


////////


//////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED: oneOf[1].


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


/////////


////////



///////


/////// define
`initialize`：<samp>array</samp>

- UNDOCUMENTED: initialize.


///////

<div class="language-text highlight"><span class="filename"><code>initialize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: initialize.


////////


///////


/////// define
`pre_animation`：<samp>array</samp>

- UNDOCUMENTED: pre aninamtion.


///////

<div class="language-text highlight"><span class="filename"><code>pre_animation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: pre aninamtion.


////////


///////


/////// define
`parent_setup`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: parent setup.


///////


/////// define
`scale`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: scale.


///////


//////


////// define
`sound_effects`：<samp>array</samp>

- UNDOCUMENTED: sound effects.


//////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED: sound effects.


///////


//////


////// define
`spawn_egg`：<samp>object</samp>

- UNDOCUMENTED: spawn egg.


//////

<div class="language-text highlight"><span class="filename"><code>spawn_egg</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base_colour`：<samp>string</samp>

- UNDOCUMENTED: base colour.


///////


/////// define
`overlay_color`：<samp>string</samp>

- UNDOCUMENTED: overlay color.


///////


/////// define
`texture`：<samp>string</samp>

- UNDOCUMENTED: texture.


///////


/////// define
`texture_index`：<samp>integer</samp>

- UNDOCUMENTED: texture index.


///////


//////


////// define
`textures`：<samp>object</samp>

- UNDOCUMENTED: textures.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- UNDOCUMENTED: additionalProperties.


///////


//////


/////


////


///







```mcschema
attachables:
{
  format_version "format_version"
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



///


