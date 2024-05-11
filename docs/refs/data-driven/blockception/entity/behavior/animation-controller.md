# Animation Controller

> 文档版本：1.21.0.24

Animation controller for behaviors.

## 架构

```mcschema
animation_controller:
{
  format_version "format_version"
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
            }
          }
          array "on_entry" : opt
          {
            string "<any array element>" : opt
            string "<any array element>" : opt
            string "<any array element>" : opt
          }
          array "on_exit" : opt
          {
            string "<any array element>" : opt
          }
          array "transitions" : opt
          {
            object "<any array element>" : opt
            {
              0 "<any object property>"
            }
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
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


////

```mcschema
format_version:
string

```

//// html | div.result

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

- A object specification on when to animate.


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



/////////



////////


//////// define
`on_entry`：<samp>array</samp>

- Events, commands or transitions to preform on entry of this state.


////////

<div class="language-text highlight"><span class="filename"><code>on_entry</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- The event or commands to execute.


/////////


///////// define
`<any array element>`：<samp>string</samp>

- The event or commands to execute.


/////////


///////// define
`<any array element>`：<samp>string</samp>

- The event or commands to execute.


/////////



////////


//////// define
`on_exit`：<samp>array</samp>

- Events, commands or transitions to preform on exit of this state.


////////

<div class="language-text highlight"><span class="filename"><code>on_exit</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- The event or commands to execute.


/////////


////////


//////// define
`transitions`：<samp>array</samp>

- The transition definition for.


////////

<div class="language-text highlight"><span class="filename"><code>transitions</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>object</samp>

- A transition to another state.


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any object property>`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>


//////////


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

