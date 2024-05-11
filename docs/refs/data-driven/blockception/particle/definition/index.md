# Particle

> 文档版本：1.21.0.24

A particle definition file.

## 架构

```mcschema
particle:
{
  format_version "format_version"
  object "particle_effect" : opt
  {
    object "description" : opt
    {
      identifier "identifier"
      object "basic_render_parameters" : opt
      {
        string "material" : opt
        string "texture" : opt
      }
    }
    object "curves" : opt
    {
      object "^(v|variable)\.[a-zA-z0-9]+$" : opt
      {
        0 "input"
        array "nodes" : opt
        {
          0 "<any array element>"
        }
        object "nodes" : opt
        {
          object "(^[\-0-9]+$|^[\-0-9]+\.[\-0-9]+$)" : opt
          {
          }
        }
        string "type" : opt
        0 "horizontal_range"
      }
    }
    object "components" : opt
    {
      emitter_initialization "minecraft:emitter_initialization"
      emitter_lifetime_events "minecraft:emitter_lifetime_events"
      emitter_rate_manual "minecraft:emitter_lifetime_expression"
      emitter_lifetime_once "minecraft:emitter_lifetime_once"
      emitter_lifetime_looping "minecraft:emitter_lifetime_looping"
      emitter_local_space "minecraft:emitter_local_space"
      emitter_rate_instant "minecraft:emitter_rate_instant"
      emitter_rate_manual "minecraft:emitter_rate_manual"
      emitter_rate_steady "minecraft:emitter_rate_steady"
      emitter_shape_box "minecraft:emitter_shape_box"
      emitter_shape_custom "minecraft:emitter_shape_custom"
      emitter_shape_disc "minecraft:emitter_shape_disc"
      emitter_shape_entity_aabb "minecraft:emitter_shape_entity_aabb"
      emitter_shape_point "minecraft:emitter_shape_point"
      emitter_shape_sphere "minecraft:emitter_shape_sphere"
      particle_appearance_billboard "minecraft:particle_appearance_billboard"
      particle_appearance_tinting "minecraft:particle_appearance_tinting"
      particle_appearance_lighting "minecraft:particle_appearance_lighting"
      particle_expire_if_not_in_blocks "minecraft:particle_expire_if_not_in_blocks"
      particle_expire_if_in_blocks "minecraft:particle_expire_if_in_blocks"
      particle_initialization "minecraft:particle_initialization"
      particle_initial_speed "minecraft:particle_initial_speed"
      particle_initial_spin "minecraft:particle_initial_spin"
      particle_lifetime_expression "minecraft:particle_lifetime_expression"
      particle_lifetime_events "minecraft:particle_lifetime_events"
      particle_kill_plane "minecraft:particle_kill_plane"
      particle_motion_collision "minecraft:particle_motion_collision"
      particle_motion_dynamic "minecraft:particle_motion_dynamic"
      particle_motion_parametric "minecraft:particle_motion_parametric"
    }
    object "events" : opt
    {
      object "<any object property>" : opt
      {
        array "sequence" : opt
        {
           "<any array element>" : opt
        }
        array "randomize" : opt
        {
           "<any array element>" : opt
        }
        object "particle_effect" : opt
        {
          string "effect" : opt
          string "type" : opt
          string "pre_effect_expression" : opt
        }
        object "sound_effect" : opt
        {
          string "event_name" : opt
        }
        string "expression" : opt
        string "log" : opt
        number "weight" : opt
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
`particle_effect`：<samp>object</samp>

- UNDOCUMENTED: particle effect.


////

<div class="language-text highlight"><span class="filename"><code>particle_effect</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- UNDOCUMENTED: description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.particle.identifier.json}

- UNDOCUMENTED: identifier.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`basic_render_parameters`：<samp>object</samp>

- UNDOCUMENTED: basic render parameters.


//////

<div class="language-text highlight"><span class="filename"><code>basic_render_parameters</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`material`：<samp>string</samp>

-  Minecraft material to use for emitter.


///////


/////// define
`texture`：<samp>string</samp>

- Minecraft texture to use for emitter.


///////


//////


/////


///// define
`curves`：<samp>object</samp>

- Curves are interpolation values, with inputs from 0 to 1, and outputs based on the curve. The result of the curve is a Molang variable of the same name that can be referenced in Molang in components. For each rendering frame for each particle, the curves are evaluated and the result is placed in a Molang variable of the name of the curve.


/////

<div class="language-text highlight"><span class="filename"><code>curves</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`^(v|variable)\.[a-zA-z0-9]+$`：<samp>object</samp>

- The curve definitions, conists out of a couple of nodes.


//////

<div class="language-text highlight"><span class="filename"><code>^(v|variable)\.[a-zA-z0-9]+$</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`input`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- What is the input value to use.


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
`nodes`：<samp>array</samp>

- Control nodes for curve.  These are assumed to be equally, used Object for bezier_chain


///////

<div class="language-text highlight"><span class="filename"><code>nodes</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


////////


///////


/////// define
`nodes`：<samp>object</samp>

- Control nodes for curve.  These are assumed to be equally, used Object for bezier_chain


///////

<div class="language-text highlight"><span class="filename"><code>nodes</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`(^[\-0-9]+$|^[\-0-9]+\.[\-0-9]+$)`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>(^[\-0-9]+$|^[\-0-9]+\.[\-0-9]+$)</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////



/////// define
`type`：<samp>string</samp>

- The type of curve.


///////


/////// define
`horizontal_range`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- What is the range the input is mapped onto.


///////


//////


/////


///// define
`components`：<samp>object</samp>

- The particle components.


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:emitter_initialization`：<samp>emitter_initialization</samp>

- [`minecraft:emitter_initialization`](./components/emitter_initialization.md)组件。The particle components.


//////

////// define
`minecraft:emitter_lifetime_events`：<samp>emitter_lifetime_events</samp>

- [`minecraft:emitter_lifetime_events`](./components/emitter_lifetime_events.md)组件。The particle components.


//////

////// define
`minecraft:emitter_lifetime_expression`：<samp>emitter_rate_manual</samp>

- [`minecraft:emitter_lifetime_expression`](./components/emitter_lifetime_expression.md)组件。The particle components.


//////

////// define
`minecraft:emitter_lifetime_once`：<samp>emitter_lifetime_once</samp>

- [`minecraft:emitter_lifetime_once`](./components/emitter_lifetime_once.md)组件。The particle components.


//////

////// define
`minecraft:emitter_lifetime_looping`：<samp>emitter_lifetime_looping</samp>

- [`minecraft:emitter_lifetime_looping`](./components/emitter_lifetime_looping.md)组件。The particle components.


//////

////// define
`minecraft:emitter_local_space`：<samp>emitter_local_space</samp>

- [`minecraft:emitter_local_space`](./components/emitter_local_space.md)组件。The particle components.


//////

////// define
`minecraft:emitter_rate_instant`：<samp>emitter_rate_instant</samp>

- [`minecraft:emitter_rate_instant`](./components/emitter_rate_instant.md)组件。The particle components.


//////

////// define
`minecraft:emitter_rate_manual`：<samp>emitter_rate_manual</samp>

- [`minecraft:emitter_rate_manual`](./components/emitter_rate_manual.md)组件。The particle components.


//////

////// define
`minecraft:emitter_rate_steady`：<samp>emitter_rate_steady</samp>

- [`minecraft:emitter_rate_steady`](./components/emitter_rate_steady.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_box`：<samp>emitter_shape_box</samp>

- [`minecraft:emitter_shape_box`](./components/emitter_shape_box.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_custom`：<samp>emitter_shape_custom</samp>

- [`minecraft:emitter_shape_custom`](./components/emitter_shape_custom.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_disc`：<samp>emitter_shape_disc</samp>

- [`minecraft:emitter_shape_disc`](./components/emitter_shape_disc.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_entity_aabb`：<samp>emitter_shape_entity_aabb</samp>

- [`minecraft:emitter_shape_entity_aabb`](./components/emitter_shape_entity_aabb.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_point`：<samp>emitter_shape_point</samp>

- [`minecraft:emitter_shape_point`](./components/emitter_shape_point.md)组件。The particle components.


//////

////// define
`minecraft:emitter_shape_sphere`：<samp>emitter_shape_sphere</samp>

- [`minecraft:emitter_shape_sphere`](./components/emitter_shape_sphere.md)组件。The particle components.


//////

////// define
`minecraft:particle_appearance_billboard`：<samp>particle_appearance_billboard</samp>

- [`minecraft:particle_appearance_billboard`](./components/particle_appearance_billboard.md)组件。The particle components.


//////

////// define
`minecraft:particle_appearance_tinting`：<samp>particle_appearance_tinting</samp>

- [`minecraft:particle_appearance_tinting`](./components/particle_appearance_tinting.md)组件。The particle components.


//////

////// define
`minecraft:particle_appearance_lighting`：<samp>particle_appearance_lighting</samp>

- [`minecraft:particle_appearance_lighting`](./components/particle_appearance_lighting.md)组件。The particle components.


//////

////// define
`minecraft:particle_expire_if_not_in_blocks`：<samp>particle_expire_if_not_in_blocks</samp>

- [`minecraft:particle_expire_if_not_in_blocks`](./components/particle_expire_if_not_in_blocks.md)组件。The particle components.


//////

////// define
`minecraft:particle_expire_if_in_blocks`：<samp>particle_expire_if_in_blocks</samp>

- [`minecraft:particle_expire_if_in_blocks`](./components/particle_expire_if_in_blocks.md)组件。The particle components.


//////

////// define
`minecraft:particle_initialization`：<samp>particle_initialization</samp>

- [`minecraft:particle_initialization`](./components/particle_initialization.md)组件。The particle components.


//////

////// define
`minecraft:particle_initial_speed`：<samp>particle_initial_speed</samp>

- [`minecraft:particle_initial_speed`](./components/particle_initial_speed.md)组件。The particle components.


//////

////// define
`minecraft:particle_initial_spin`：<samp>particle_initial_spin</samp>

- [`minecraft:particle_initial_spin`](./components/particle_initial_spin.md)组件。The particle components.


//////

////// define
`minecraft:particle_lifetime_expression`：<samp>particle_lifetime_expression</samp>

- [`minecraft:particle_lifetime_expression`](./components/particle_lifetime_expression.md)组件。The particle components.


//////

////// define
`minecraft:particle_lifetime_events`：<samp>particle_lifetime_events</samp>

- [`minecraft:particle_lifetime_events`](./components/particle_lifetime_events.md)组件。The particle components.


//////

////// define
`minecraft:particle_kill_plane`：<samp>particle_kill_plane</samp>

- [`minecraft:particle_kill_plane`](./components/particle_kill_plane.md)组件。The particle components.


//////

////// define
`minecraft:particle_motion_collision`：<samp>particle_motion_collision</samp>

- [`minecraft:particle_motion_collision`](./components/particle_motion_collision.md)组件。The particle components.


//////

////// define
`minecraft:particle_motion_dynamic`：<samp>particle_motion_dynamic</samp>

- [`minecraft:particle_motion_dynamic`](./components/particle_motion_dynamic.md)组件。The particle components.


//////

////// define
`minecraft:particle_motion_parametric`：<samp>particle_motion_parametric</samp>

- [`minecraft:particle_motion_parametric`](./components/particle_motion_parametric.md)组件。The particle components.


//////

/////


///// define
`events`：<samp>object</samp>

- UNDOCUMENTED: events.


/////

<div class="language-text highlight"><span class="filename"><code>events</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any object property>`：<samp>object</samp>

- The particle event.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`sequence`：<samp>array</samp>

- A sequence of elements to execute.


///////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`

- The particle event.


////////


///////


/////// define
`randomize`：<samp>array</samp>

- A list of elements to execute one of.


///////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`

- The particle event.


////////


///////


/////// define
`particle_effect`：<samp>object</samp>

- Particle effect action.


///////

<div class="language-text highlight"><span class="filename"><code>particle_effect</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`effect`：<samp>string</samp>

- Identifier of the effect.


////////


//////// define
`type`：<samp>string</samp>

- UNDOCUMENTED: type.


////////


//////// define
`pre_effect_expression`：<samp>string</samp>

- Molang expression to run on the new emitter.


////////


///////


/////// define
`sound_effect`：<samp>object</samp>

- Sound effect action.


///////

<div class="language-text highlight"><span class="filename"><code>sound_effect</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`event_name`：<samp>string</samp>

- Name of the level sound event.


////////


///////


/////// define
`expression`：<samp>string</samp>

- Molang expression to run on the event-firing emitter.


///////


/////// define
`log`：<samp>string</samp>

- Message to log, along with the firing effect's name and event position.


///////


/////// define
`weight`：<samp>number</samp>

- The weight of the element.


///////


//////


/////


////


///

