# Ambient Sound Interval

> 文档版本：1.21.0.24

Sets the entity's delay between playing its ambient sound.

## 架构

```mcschema
ambient_sound_interval:
{
  string "event_name" : opt
  array "event_names" : opt
  {
    object "<any array element>" : opt
    {
      string "condition" : opt
      sound_event "event_name"
    }
  }
  number "range" : opt
  number "value" : opt
}

```

/// html | div.result
//// define
`event_name`：<samp>string</samp>

- Level sound event to be played as the ambient sound.


////


//// define
`event_names`：<samp>array</samp>

- List of dynamic level sound events, with conditions for choosing between them. Evaluated in order, first one wins. If none evaluate to true, 'event_name' will take precedence.


////

<div class="language-text highlight"><span class="filename"><code>event_names</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`condition`：<samp>string</samp>

- The condition that must be satisfied to select the given ambient sound.


//////


////// define
`event_name`：<samp>sound_event</samp> {#assets.schemas-blockception.general.sound_event.json}

- Level sound event to be played as the ambient sound.


//////

```mcschema
sound_event:
string

```

////// html | div.result

//////



/////


////


//// define
`range`：<samp>number</samp>

- Maximum time in seconds to randomly add to the ambient sound delay time.


////


//// define
`value`：<samp>number</samp>

- Minimum time in seconds before the entity plays its ambient sound again.


////


///

