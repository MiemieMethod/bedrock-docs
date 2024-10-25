# Ravager Blocked

> 文档版本：1.21.50.25

Defines the ravager's response to their melee attack being blocked.

## 架构

```mcschema
ravager_blocked:
{
  number "knockback_strength" : opt
  array "reaction_choices" : opt
  {
    object "<any array element>" : opt
    {
      integer "weight" : opt
      event "value"
    }
  }
}

```

/// html | div.result
//// define
`knockback_strength`：<samp>number</samp>

- The strength with which blocking entities should be knocked back.


////


//// define
`reaction_choices`：<samp>array</samp>

- A list of weighted responses to the melee attack being blocked.


////

<div class="language-text highlight"><span class="filename"><code>reaction_choices</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`weight`：<samp>integer</samp>

- The chance of this reaction being picked.


//////


////// define
`value`：<samp>event</samp> {#assets.schemas-blockception.behavior.entities.format.types.event.json}

- An event that runs when this reaction is picked.


//////

```mcschema
event:
string

```

////// html | div.result

//////


```mcschema
event:
{
  string "event" : opt
  string "target" : opt
}

```

////// html | div.result
/////// define
`event`：<samp>string</samp>

- The event to fire.


///////


/////// define
`target`：<samp>string</samp>

- The target of the event.


///////


//////




/////


////


///

