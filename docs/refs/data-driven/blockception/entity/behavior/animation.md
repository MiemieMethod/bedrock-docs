# Animation

> 文档版本：1.21.0.24

Animation for behavior for.

## 架构

```mcschema
animations:
{
  format_version "format_version"
  object "animations" : opt
  {
    object "^animation\.[a-z\.]+" : opt
    {
      number "animation_length" : opt
      boolean "loop" : opt
      object "timeline" : opt
      {
        string "^(\d+\.\d+|\d+)$" : opt
        string "^(\d+\.\d+|\d+)$" : opt
        string "^(\d+\.\d+|\d+)$" : opt
        string "^(\d+\.\d+|\d+)$" : opt
        array "^(\d+\.\d+|\d+)$" : opt
        {
          string "<any array element>" : opt
        }
      }
      0 "anim_time_update"
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

- A single animation definition for.


/////

<div class="language-text highlight"><span class="filename"><code>^animation\.[a-z\.]+</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`animation_length`：<samp>number</samp>

- The time in seconds this animation will last.


//////


////// define
`loop`：<samp>boolean</samp>

- Whenever this animation should loop once it reaches the end, will only happen if the animation is still active.


//////


////// define
`timeline`：<samp>object</samp>

- A timeline specification, property names are timestamps.


//////

<div class="language-text highlight"><span class="filename"><code>timeline</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`^(\d+\.\d+|\d+)$`：<samp>string</samp>

- Sets the value to a molang variable.


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>string</samp>

- Executes a minecraft command.


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>string</samp>

- The event or commands to execute.


///////


/////// define
`^(\d+\.\d+|\d+)$`：<samp>string</samp>

- An event to be called upon within the executing entity.


///////



/////// define
`^(\d+\.\d+|\d+)$`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>^(\d+\.\d+|\d+)$</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>string</samp>

- The event or commands to execute.


////////


///////



//////


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




/////


////


///

