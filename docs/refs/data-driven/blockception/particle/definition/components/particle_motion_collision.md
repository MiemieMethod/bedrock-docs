# Particle Motion Collision Component For 1.10.0

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
particle_motion_collision:
{
  number "collision_drag" : opt
  number "coefficient_of_restitution" : opt
  number "collision_radius" : opt
  0 "enabled"
  boolean "expire_on_contact" : opt
  array "events" : opt
  {
    object "<any array element>" : opt
    {
      string "event" : opt
      number "min_speed" : opt
    }
  }
}

```

/// html | div.result
//// define
`collision_drag`：<samp>number</samp>

- UNDOCUMENTED: collision drag.


////


//// define
`coefficient_of_restitution`：<samp>number</samp>

- UNDOCUMENTED: coefficient of restitution.


////


//// define
`collision_radius`：<samp>number</samp>

- UNDOCUMENTED: collision radius.


////


//// define
`enabled`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- UNDOCUMENTED: enabled.


////

```mcschema
0:
string

```

//// html | div.result

////


```mcschema
0:
number

```

//// html | div.result

////




//// define
`expire_on_contact`：<samp>boolean</samp>

- UNDOCUMENTED: expire on contact.


////


//// define
`events`：<samp>array</samp>

- UNDOCUMENTED: events.


////

<div class="language-text highlight"><span class="filename"><code>events</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED: events.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`event`：<samp>string</samp>

- UNDOCUMENTED: event.


//////


////// define
`min_speed`：<samp>number</samp>

- UNDOCUMENTED: Minimum speed.


//////


/////


////


///

