# 未命名

> 文档版本：1.21.50.25



## 架构

```mcschema
entity:
{
  string "format_version" : opt
  object "minecraft:client_entity" : opt
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
        string "[a-zA-Z0-9_\.\-]+" : opt
      }
      boolean "hide_armor" : opt
      boolean "held_item_ignores_lighting" : opt
      identifier "identifier"
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
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
        }
      }
      object "scripts" : opt
      {
        array "pre_animation" : opt
        {
          0 "<any array element>"
        }
        0 "parent_setup"
        0 "scale"
        0 "scalex"
        0 "scaley"
        0 "scalez"
      }
      object "sound_effects" : opt
      {
        string "<any object property>" : opt
      }
      object "spawn_egg" : opt
      {
        string "base_color" : opt
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
`minecraft:client_entity`：<samp>object</samp>

- The entity description for clientside rendering, animations and models.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:client_entity</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The entity description for clientside rendering, animations and models.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animations`：<samp>object</samp>

- These names are used by the animation controller JSON. Players can reference animations from the vanilla Minecraft Resource Pack or create their own. Custom animations should be in the animation folder at the root of the Resource Pack.


//////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- These names are used by the animation controller JSON. Players can reference animations from the vanilla Minecraft Resource Pack or create their own. Custom animations should be in the animation folder at the root of the Resource Pack.


///////


//////


////// define
`animation_controllers`：<samp>array</samp>

- A reference to an animation controller.


//////

<div class="language-text highlight"><span class="filename"><code>animation_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- A collection of animation controllers.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- A reference to an animation.


////////


///////


//////


////// define
`enable_attachables`：<samp>boolean</samp>

- UNDOCUMENTED: enable attachables.


//////


////// define
`geometry`：<samp>object</samp>

- The reference to defined geometries in `<resource pack>/models/'.


//////

<div class="language-text highlight"><span class="filename"><code>geometry</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`[a-zA-Z0-9_\.\-]+`：<samp>string</samp>

- The reference to the geometry.


///////


//////


////// define
`hide_armor`：<samp>boolean</samp>

- Hides or shows the possible armor.


//////


////// define
`held_item_ignores_lighting`：<samp>boolean</samp>

- This determines if the item held by an entity should render fully lit up (if true), or depending on surrounding lighting.


//////


////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.entity.identifier.json}

- The entity indentifier.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`materials`：<samp>object</samp>

- A collection of material definitions.


//////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>material</samp> {#assets.schemas-blockception.general.vanilla.material.json}

- Material reference.


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

- The minimum engine version to be used.


//////


////// define
`particle_effects`：<samp>object</samp>

- Keys are required and need to be unique from all other keys in the animation controllers. Players can reference particles from the vanilla Minecraft Resource Pack or create their own. Custom particles should be in the particle folder at the root of the Resource Pack.


//////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- Particle reference.


///////


//////


////// define
`particle_emitters`：<samp>object</samp>

- A collection of particle emitters definitions.


//////

<div class="language-text highlight"><span class="filename"><code>particle_emitters</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- Particle emitter reference.


///////


//////


////// define
`render_controllers`：<samp>array</samp>

- Players can reference Render Controllers from the vanilla Minecraft Resource Pack or create their own. Custom Render Controllers should be in the textures folder at the root of the Resource Pack.


//////

<div class="language-text highlight"><span class="filename"><code>render_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- A single render controller definition.


///////


/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- A render controller activate on conditional.


////////


///////



//////


////// define
`scripts`：<samp>object</samp>

- The place where variables, and animations / controller to be run is specified.


//////

<div class="language-text highlight"><span class="filename"><code>scripts</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`pre_animation`：<samp>array</samp>

- Client side scripts that are evaluated immediately before animations are processed.


///////

<div class="language-text highlight"><span class="filename"><code>pre_animation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- Clientside molang variables that are to be evaluated during the animation.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



///////


/////// define
`parent_setup`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- UNDOCUMENTED: parent setup.


///////

```mcschema
0:
string

```

/////// html | div.result

///////


```mcschema
0:
number

```

/////// html | div.result

///////




/////// define
`scale`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Scale sets the scale of the mob's geometry.


///////


/////// define
`scalex`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


/////// define
`scaley`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


/////// define
`scalez`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


//////


////// define
`sound_effects`：<samp>object</samp>

- A collection of sound effect definition.


//////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A sound effect definition.


///////


//////


////// define
`spawn_egg`：<samp>object</samp>

- The definition of how the spawn_egg icon looks like.


//////

<div class="language-text highlight"><span class="filename"><code>spawn_egg</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base_color`：<samp>string</samp>

- The basic color of the egg.


///////


/////// define
`overlay_color`：<samp>string</samp>

- The colors of the dots on the egg.


///////


/////// define
`texture`：<samp>string</samp>

- The texture reference in item_texture.json


///////


/////// define
`texture_index`：<samp>integer</samp>

- The index of the texture.


///////


//////


////// define
`textures`：<samp>object</samp>

- A collection of references to textures in the resourcepack.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A reference to a texture in the resourcepack.


///////


//////


/////


////


///



```mcschema
entity:
{
  format_version "format_version"
  object "minecraft:client_entity" : opt
  {
    object "description" : opt
    {
      object "animations" : opt
      {
        string "<any object property>" : opt
      }
      boolean "enable_attachables" : opt
      object "geometry" : opt
      {
        string "[a-zA-Z0-9_\.\-]+" : opt
      }
      string "queryable_geometry" : opt
      boolean "hide_armor" : opt
      boolean "held_item_ignores_lighting" : opt
      identifier "identifier"
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
        object "<any array element>" : opt
        {
          string "<any object property>" : opt
        }
      }
      object "scripts" : opt
      {
        array "animate" : opt
        {
          string "<any array element>" : opt
          object "<any array element>" : opt
          {
            string "<any object property>" : opt
            number "<any object property>" : opt
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
        0 "scalex"
        0 "scaley"
        0 "scalez"
        boolean "should_update_bones_and_effects_offscreen" : opt
        0 "should_update_bones_and_effects_offscreen"
        boolean "should_update_effects_offscreen" : opt
        0 "should_update_effects_offscreen"
        object "variables" : opt
        {
          string "variable.[a-zA-Z_][a-zA-Z0-9_]*" : opt
        }
      }
      object "sound_effects" : opt
      {
        string "<any object property>" : opt
      }
      object "spawn_egg" : opt
      {
        string "base_color" : opt
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
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

////



//// define
`minecraft:client_entity`：<samp>object</samp>

- The entity description for clientside rendering, animations and models.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:client_entity</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The entity description for clientside rendering, animations and models.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animations`：<samp>object</samp>

- These names are used by the animation controller JSON. Players can reference animations from the vanilla Minecraft Resource Pack or create their own. Custom animations should be in the animation folder at the root of the Resource Pack.


//////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- These names are used by the animation controller JSON. Players can reference animations from the vanilla Minecraft Resource Pack or create their own. Custom animations should be in the animation folder at the root of the Resource Pack.


///////


//////


////// define
`enable_attachables`：<samp>boolean</samp>

- Whether or not attachables are enaboled.


//////


////// define
`geometry`：<samp>object</samp>

- The reference to defined geometries in `<resource pack>/models/'.


//////

<div class="language-text highlight"><span class="filename"><code>geometry</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`[a-zA-Z0-9_\.\-]+`：<samp>string</samp>

- The reference to the geometry.


///////


//////


////// define
`queryable_geometry`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`hide_armor`：<samp>boolean</samp>

- Hides or shows the possible armor.


//////


////// define
`held_item_ignores_lighting`：<samp>boolean</samp>

- This determines if the item held by an entity should render fully lit up (if true), or depending on surrounding lighting.


//////


////// define
`identifier`：<samp>[identifier](#assets.schemas-blockception.general.entity.identifier.json)</samp>

- The entity indentifier.


//////


////// define
`materials`：<samp>object</samp>

- A collection of material definitions.


//////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>[material](#assets.schemas-blockception.general.vanilla.material.json)</samp>

- Material reference.


///////


//////


////// define
`min_engine_version`：<samp>string</samp>

- The minimum engine version to be used.


//////


////// define
`particle_effects`：<samp>object</samp>

- A collection of particle definitions.


//////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- Particle reference.


///////


//////


////// define
`particle_emitters`：<samp>object</samp>

- A collection of particle emitters definitions.


//////

<div class="language-text highlight"><span class="filename"><code>particle_emitters</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- Particle emitter reference.


///////


//////


////// define
`render_controllers`：<samp>array</samp>

- A collection of Render controller definitions.


//////

<div class="language-text highlight"><span class="filename"><code>render_controllers</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- A single render controller definition.


///////


/////// define
`<any array element>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any object property>`：<samp>string</samp>

- A render controller activate on conditional.


////////


///////



//////


////// define
`scripts`：<samp>object</samp>

- The place where variables, and animations / controller to be run is specified.


//////

<div class="language-text highlight"><span class="filename"><code>scripts</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`animate`：<samp>array</samp>

- The array of items to animate.


///////

<div class="language-text highlight"><span class="filename"><code>animate</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- A single animation or animation controller to run.


////////


//////// define
`<any array element>`：<samp>object</samp>

- A single animation or animation controller to run on condition.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>string</samp>

- A molang condition.


/////////


///////// define
`<any object property>`：<samp>number</samp>

- Blend weight.


/////////



////////



///////


/////// define
`initialize`：<samp>array</samp>

- Clientside molang variables that are to be evaluated during the creation of the entity.


///////

<div class="language-text highlight"><span class="filename"><code>initialize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- Clientside molang variables that are to be evaluated during the creation of the entity.


////////


///////


/////// define
`pre_animation`：<samp>array</samp>

- Clientside molang variables that are to be evaluated during the animation.


///////

<div class="language-text highlight"><span class="filename"><code>pre_animation</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- Clientside molang variables that are to be evaluated during the animation.


////////


///////


/////// define
`parent_setup`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- UNDOCUMENTED: parent setup.


///////


/////// define
`scale`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Scale sets the scale of the mob's geometry.


///////


/////// define
`scalex`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


/////// define
`scaley`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


/////// define
`scalez`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


///////


/////// define
`should_update_bones_and_effects_offscreen`：<samp>boolean</samp>

- Bones and effects will still be updated if the entity is off screen if this expression returns anything other than 0.0.


///////


/////// define
`should_update_bones_and_effects_offscreen`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- Bones and effects will still be updated if the entity is off screen if this expression returns anything other than 0.0.


///////



/////// define
`should_update_effects_offscreen`：<samp>boolean</samp>

- Effects will still be updated if the entity is off screen if this expression or `should_update_bones_and_effects_offscreen` returns anything other than 0.0.


///////


/////// define
`should_update_effects_offscreen`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- Effects will still be updated if the entity is off screen if this expression or `should_update_bones_and_effects_offscreen` returns anything other than 0.0.


///////



/////// define
`variables`：<samp>object</samp>

-  A list of variables that need certain settings applied to them. Currently, for the client, only `public` is supported.


///////

<div class="language-text highlight"><span class="filename"><code>variables</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`variable.[a-zA-Z_][a-zA-Z0-9_]*`：<samp>string</samp>

-  If a variable is public, it can be read by other mobs. See the molang `->` operator for details.


////////


///////


//////


////// define
`sound_effects`：<samp>object</samp>

- A collection of sound effect definition.


//////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A sound effect definition.


///////


//////


////// define
`spawn_egg`：<samp>object</samp>

- The definition of how the spawn_egg icon looks like.


//////

<div class="language-text highlight"><span class="filename"><code>spawn_egg</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base_color`：<samp>string</samp>

- The basic color of the egg.


///////


/////// define
`overlay_color`：<samp>string</samp>

- The colors of the dots on the egg.


///////


/////// define
`texture`：<samp>string</samp>

- The texture reference in item_texture.json


///////


/////// define
`texture_index`：<samp>integer</samp>

- The index of the texture.


///////


//////


////// define
`textures`：<samp>object</samp>

- A collection of references to textures in the resourcepack.


//////

<div class="language-text highlight"><span class="filename"><code>textures</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>

- A reference to a texture in the resourcepack.


///////


//////


/////


////


///



