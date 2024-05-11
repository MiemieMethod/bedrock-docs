# Actor Animation

> 文档版本：1.21.0.24

The RP animation that changes an actors models, or molang data.

## 架构

```mcschema
actor_animation:
{
  format_version "format_version"
  object "animations" : opt
  {
    object "^animation\.[a-z\.]+" : opt
    {
      0 "anim_time_update"
      number "animation_length" : opt
      0 "blend_weight"
      object "bones" : opt
      {
        object "<any object property>" : opt
        {
          array "position" : opt
          {
            0 "0..0"
            0 "1..1"
            0 "2..2"
          }
          object "position" : opt
          {
            0 "^(\d+\.\d+|\d+)$"
            array "^(\d+\.\d+|\d+)$" : opt
            object "^(\d+\.\d+|\d+)$" : opt
            {
              string "lerp_mode" : opt
              array "pre" : opt
              array "post" : opt
            }
          }
          array "rotation" : opt
          {
            0 "0..0"
            0 "1..1"
            0 "2..2"
          }
          object "rotation" : opt
          {
            0 "^(\d+\.\d+|\d+)$"
            array "^(\d+\.\d+|\d+)$" : opt
            object "^(\d+\.\d+|\d+)$" : opt
            {
              string "lerp_mode" : opt
              array "pre" : opt
              array "post" : opt
            }
          }
          object "relative_to" : opt
          {
            string "rotation" : opt
          }
          0 "scale"
          array "scale" : opt
          {
            0 "0..0"
            0 "1..1"
            0 "2..2"
          }
          object "scale" : opt
          {
            0 "^(\d+\.\d+|\d+)$"
            array "^(\d+\.\d+|\d+)$" : opt
            object "^(\d+\.\d+|\d+)$" : opt
            {
              string "lerp_mode" : opt
              array "pre" : opt
              array "post" : opt
            }
          }
        }
      }
      boolean "loop" : opt
      string "loop" : opt
      0 "loop_delay"
      boolean "override_previous_animation" : opt
      object "particle_effects" : opt
      {
        object "^(\d+\.\d+|\d+)$" : opt
        {
          string "effect" : opt
          string "locator" : opt
          0 "pre_effect_script"
          boolean "bind_to_actor" : opt
        }
        array "^(\d+\.\d+|\d+)$" : opt
        {
          object "<any array element>" : opt
          {
          }
        }
      }
      0 "start_delay"
      object "sound_effects" : opt
      {
        object "^(\d+\.\d+|\d+)$" : opt
        {
          string "effect" : opt
        }
        array "^(\d+\.\d+|\d+)$" : opt
        {
          object "<any array element>" : opt
          {
          }
        }
      }
      object "timeline" : opt
      {
        string "^(\d+\.\d+|\d+)$" : opt
        array "^(\d+\.\d+|\d+)$" : opt
        {
          string "<any array element>" : opt
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
`animations`：<samp>object</samp>

- The animation specification.


////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^animation\.[a-z\.]+`：<samp>object</samp>

- The animation specification.


/////

<div class="language-text highlight"><span class="filename"><code>^animation\.[a-z\.]+</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`anim_time_update`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- How does time pass when playing the animation. Defaults to `query.anim_time + query.delta_time` which means advance in seconds.


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
`animation_length`：<samp>number</samp>

- Override calculated value (set as the last keyframe time) and set animation length in seconds.


//////


////// define
`blend_weight`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The weight of the animation when blending with other animations. Defaults to 1.


//////


////// define
`bones`：<samp>object</samp>

- Defines how the bones in an animation move or transform.


//////

<div class="language-text highlight"><span class="filename"><code>bones</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>object</samp>

- The bone definition that declare how it transforms during animation.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`position`：<samp>array</samp>

- An array of 3 items that describe the bones position.


////////

<div class="language-text highlight"><span class="filename"><code>position</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The position over the X-axis or forwards/backwards.
Can be molang or a float


/////////


///////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The position over the Y-axis, or up/down.
Can be molang or a float


/////////


///////// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The position over the Z-axis, or left/right.
Can be molang or a float


/////////


////////


//////// define
`position`：<samp>object</samp>

- The Position transformation during this animation.


////////

<div class="language-text highlight"><span class="filename"><code>position</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`^(\d+\.\d+|\d+)$`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Uniform position.


/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>

- An array of 3 items that describe the bones position.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>object</samp>

- A single point in time.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`lerp_mode`：<samp>string</samp>

- UNDOCUMENTED.


//////////


////////// define
`pre`：<samp>array</samp>

- An array of 3 items that describe the bones position.


//////////

<div class="language-text highlight"><span class="filename"><code>pre</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


////////// define
`post`：<samp>array</samp>

- An array of 3 items that describe the bones position.


//////////

<div class="language-text highlight"><span class="filename"><code>post</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


/////////



////////



//////// define
`rotation`：<samp>array</samp>

- An array of 3 items that describe the bones rotation.


////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The rotation over the X-axis, or up or down.
Can be molang or a float


/////////


///////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The rotation over the Y-axis, or yaw.
Can be molang or a float


/////////


///////// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The rotation over the Z-axis, or roll.
Can be molang or a float


/////////


////////


//////// define
`rotation`：<samp>object</samp>

- The rotation transformation during this animation.


////////

<div class="language-text highlight"><span class="filename"><code>rotation</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`^(\d+\.\d+|\d+)$`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Uniform rotation.


/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>

- An array of 3 items that describe the bones rotation.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>object</samp>

- A single point in time.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`lerp_mode`：<samp>string</samp>

- UNDOCUMENTED.


//////////


////////// define
`pre`：<samp>array</samp>

- An array of 3 items that describe the bones rotation.


//////////

<div class="language-text highlight"><span class="filename"><code>pre</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


////////// define
`post`：<samp>array</samp>

- An array of 3 items that describe the bones rotation.


//////////

<div class="language-text highlight"><span class="filename"><code>post</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


/////////



////////



//////// define
`relative_to`：<samp>object</samp>

- If set, makes the bone rotation relative to the entity instead of the bone's parent.


////////

<div class="language-text highlight"><span class="filename"><code>relative_to</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`rotation`：<samp>string</samp>

- If set, makes the bone rotation relative to the entity instead of the bone's parent.


/////////


////////


//////// define
`scale`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Uniform scale.


////////


//////// define
`scale`：<samp>array</samp>

- An array of 3 items that describe the bones scale.


////////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The scale over the X-axis or forwards/backwards.
Can be molang or a float


/////////


///////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The scale over the Y-axis, or up/down.
Can be molang or a float


/////////


///////// define
`2..2`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- The scale over the Z-axis, or left/right.
Can be molang or a float


/////////


////////


//////// define
`scale`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>scale</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`^(\d+\.\d+|\d+)$`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Uniform rotation.


/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>

- An array of 3 items that describe the bones scale.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


///////// define
`^(\d+\.\d+|\d+)$`：<samp>object</samp>

- A single point in time.


/////////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`lerp_mode`：<samp>string</samp>

- UNDOCUMENTED.


//////////


////////// define
`pre`：<samp>array</samp>

- An array of 3 items that describe the bones scale.


//////////

<div class="language-text highlight"><span class="filename"><code>pre</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


////////// define
`post`：<samp>array</samp>

- An array of 3 items that describe the bones scale.


//////////

<div class="language-text highlight"><span class="filename"><code>post</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result

//////////


/////////



////////



///////


//////


////// define
`loop`：<samp>boolean</samp>

- Should this animation stop, loop, or stay on the last frame when finished (true, false, hold_on_last_frame).


//////


////// define
`loop`：<samp>string</samp>

- Should this animation stop, loop, or stay on the last frame when finished (true, false, hold_on_last_frame).


//////



////// define
`loop_delay`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- How long to wait in seconds before looping this animation. Note that this expression is evaluated after each loop and on looping animation only.


//////


////// define
`override_previous_animation`：<samp>boolean</samp>

- Reset bones in this animation to the default pose before applying this animation.


//////


////// define
`particle_effects`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`^(\d+\.\d+|\d+)$`：<samp>object</samp>

- A single point in time.


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`effect`：<samp>string</samp>

- The name of a particle effect that should be played.


////////


//////// define
`locator`：<samp>string</samp>

- The name of a locator on the actor where the effect should be located.


////////


//////// define
`pre_effect_script`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- A molang script that will be run when the particle emitter is initialized.


////////

```mcschema
0:
string

```

//////// html | div.result

////////



//////// define
`bind_to_actor`：<samp>boolean</samp>

- Set to false to have the effect spawned in the world without being bound to an actor (by default an effect is bound to the actor).


////////


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>

- A single point in time.


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////



//////


////// define
`start_delay`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- How long to wait in seconds before playing this animation. Note that this expression is evaluated once before playing, and only re-evaluated if asked to play from the beginning again. A looping animation should use `loop_delay` if it wants a delay between loops.


//////


////// define
`sound_effects`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`^(\d+\.\d+|\d+)$`：<samp>object</samp>

- A single point in time.


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`effect`：<samp>string</samp>

- Valid sound effect names should be listed in the entity's resource_definition json file.


////////


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>

- A single point in time.


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////



//////


////// define
`timeline`：<samp>object</samp>

- The time line.


//////

<div class="language-text highlight"><span class="filename"><code>timeline</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`^(\d+\.\d+|\d+)$`：<samp>string</samp>

- Variable definition.


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- Variable definition.


////////


///////



//////


/////


////


///

