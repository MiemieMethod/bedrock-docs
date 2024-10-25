# Animation Controller

> 文档版本：1.21.50.25

UNDOCUMENTED.

## 架构

```mcschema
animation_controller:
{
  string "format_version" : opt
  object "animation_controllers" : opt
  {
    object "^controller\.animation\.[a-z\.]+" : opt
    {
      object "states" : opt
      {
        object "[a-z\.]+" : opt
        {
          array "animations" : opt
          {
            string "<any array element>" : opt
            object "<any array element>" : opt
            {
              0 "<any object property>"
              number "<any object property>" : opt
            }
          }
          number "blend_transition" : opt
          object "blend_transition" : opt
          {
            number "<any object property>" : opt
          }
          boolean "blend_via_shortest_path" : opt
          array "particle_effects" : opt
          {
            object "<any array element>" : opt
            {
              boolean "bind_to_actor" : opt
              string "effect" : opt
              string "locator" : opt
              string "pre_effect_script" : opt
            }
          }
          array "sound_effects" : opt
          {
            object "<any array element>" : opt
            {
              string "effect" : opt
            }
          }
          array "transitions" : opt
          {
             "<any array element>" : opt
          }
          object "variables" : opt
          {
            object "<any object property>" : opt
            {
              0 "input"
              object "remap_curve" : opt
              {
                number "<any object property>" : opt
              }
            }
          }
          array "on_entry" : opt
          {
            string "<any array element>" : opt
          }
          array "on_exit" : opt
          {
            string "<any array element>" : opt
          }
        }
      }
      string "initial_state" : opt
    }
  }
}

```

/// html | div.result
//// define
`format_version`：<samp>string</samp>


////


//// define
`animation_controllers`：<samp>object</samp>

- The animation controllers schema for.


////

<div class="language-text highlight"><span class="filename"><code>animation_controllers</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`^controller\.animation\.[a-z\.]+`：<samp>object</samp>

- A single animation controller.


/////

<div class="language-text highlight"><span class="filename"><code>^controller\.animation\.[a-z\.]+</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`states`：<samp>object</samp>

- The states of this animation controller.


//////

<div class="language-text highlight"><span class="filename"><code>states</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`[a-z\.]+`：<samp>object</samp>

- Animation state.


///////

<div class="language-text highlight"><span class="filename"><code>[a-z\.]+</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`animations`：<samp>array</samp>

- The animations definition for.


////////

<div class="language-text highlight"><span class="filename"><code>animations</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- A single string that specifies which animation there are.


/////////


///////// define
`<any array element>`：<samp>object</samp>

- A object specification on how to transition.


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any object property>`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}


//////////

```mcschema
0:
string

```

////////// html | div.result

//////////



////////// define
`<any object property>`：<samp>number</samp>

- A blend weight.


//////////



/////////



////////


//////// define
`blend_transition`：<samp>number</samp>

- A short-hand version of blend_out that simply sets the amount of time to fade out if the animation is interrupted.


////////


//////// define
`blend_transition`：<samp>object</samp>

- Specifies the cross-fade time in seconds when transitioning to another state.


////////

<div class="language-text highlight"><span class="filename"><code>blend_transition</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>number</samp>

- Mapping of time since the animation was canceled, to the blend value at that time. A default key of time=0 to a blend value of 1.0 is provided if any other key is set and a blend value at time=0 hasn't already been set.


/////////


////////



//////// define
`blend_via_shortest_path`：<samp>boolean</samp>

- When blending a transition to another state, animate each euler axis through the shortest rotation, instead of by value.


////////


//////// define
`particle_effects`：<samp>array</samp>

- The effects to be emitted.


////////

<div class="language-text highlight"><span class="filename"><code>particle_effects</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED: particle effects.


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`bind_to_actor`：<samp>boolean</samp>

- Set to false to have the effect spawned in the world without being bound to an actor (by default an effect is bound to the actor).


//////////


////////// define
`effect`：<samp>string</samp>

- The name of a particle effect that should be played.


//////////


////////// define
`locator`：<samp>string</samp>

- The name of a locator on the actor where the effect should be located.


//////////


////////// define
`pre_effect_script`：<samp>string</samp>

- A molang script that will be run when the particle emitter is initialized.


//////////


/////////


////////


//////// define
`sound_effects`：<samp>array</samp>

- Collection of sounds to trigger on entry to this animation state.


////////

<div class="language-text highlight"><span class="filename"><code>sound_effects</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`effect`：<samp>string</samp>

- Valid sound effect names should be listed in the entity's resource_definition json file.


//////////


/////////


////////


//////// define
`transitions`：<samp>array</samp>

- The transition definition for.


////////

<div class="language-text highlight"><span class="filename"><code>transitions</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`

- The specification on when to transition to a new state.


/////////


////////


//////// define
`variables`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>variables</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`input`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}


//////////

```mcschema
0:
string

```

////////// html | div.result

//////////


```mcschema
0:
number

```

////////// html | div.result

//////////




////////// define
`remap_curve`：<samp>object</samp>


//////////

<div class="language-text highlight"><span class="filename"><code>remap_curve</code></span><pre id="__code_1"><span></span></pre></div>

////////// html | div.result
/////////// define
`<any object property>`：<samp>number</samp>


///////////


//////////


/////////


////////


//////// define
`on_entry`：<samp>array</samp>

- Sets molang on data on entry.


////////

<div class="language-text highlight"><span class="filename"><code>on_entry</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


/////////


////////


//////// define
`on_exit`：<samp>array</samp>

- Sets molang on data on exit.


////////

<div class="language-text highlight"><span class="filename"><code>on_exit</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


/////////


////////


///////


//////


////// define
`initial_state`：<samp>string</samp>

- The state to start with, if not specified state at position 0 in the array is used.


//////


/////


////


///

