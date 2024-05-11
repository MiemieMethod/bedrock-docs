# 未命名

> 文档版本：1.21.0.24



## 架构

```mcschema
0:
{
   "format_version" : opt
  object "minecraft:volume" : opt
  {
    object "description" : opt
    {
      volume "identifier"
    }
    object "components" : opt
    {
      object "minecraft:bounds" : opt
      {
        string "dimension" : opt
        array "max" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
          number "2..2" : opt
        }
        array "min" : opt
        {
          number "0..0" : opt
          number "1..1" : opt
          number "2..2" : opt
        }
      }
      object "minecraft:fog" : opt
      {
        string "fog_identifier" : opt
        integer "priority" : opt
      }
      object "minecraft:on_actor_enter" : opt
      {
        array "on_enter" : opt
        {
          object "<any array element>" : opt
          {
            0 "condition"
            string "event" : opt
            string "target" : opt
          }
        }
      }
      object "minecraft:on_actor_leave" : opt
      {
        array "on_enter" : opt
        {
          object "<any array element>" : opt
          {
            0 "condition"
            string "event" : opt
            string "target" : opt
          }
        }
      }
    }
  }
}

```

/// html | div.result
//// define
`format_version`

- Specifies the version of the game this entity was made in. Minimum supported version is 1.17.0. Current supported version is 1.17.0.


////


//// define
`minecraft:volume`：<samp>object</samp>

- UNDOCUMENTED.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:volume</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description contains a single `identifier` string.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>volume</samp> {#assets.schemas-blockception.general.volume.identifier.json}

- The unique identifier for this volume. It must be of the form `namespace:name', where namespace cannot be `minecraft`.


//////

```mcschema
volume:
string

```

////// html | div.result

//////



/////


///// define
`components`：<samp>object</samp>

- UNDOCUMENTED.


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:bounds`：<samp>object</samp>

- Component that defines a minimum and maximum block position for a bounding box and which world dimension the bounding box is in. Every volume must have a bounds component.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:bounds</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`dimension`：<samp>string</samp>

- The name of the dimension the bounding box will exist in: one of `overworld', `nether` or `the end`.


///////


/////// define
`max`：<samp>array</samp>

- The maximum block position of the bounding box.


///////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>


////////


//////// define
`1..1`：<samp>number</samp>


////////


//////// define
`2..2`：<samp>number</samp>


////////


///////


/////// define
`min`：<samp>array</samp>

- The minimum block position of the bounding box.


///////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>


////////


//////// define
`1..1`：<samp>number</samp>


////////


//////// define
`2..2`：<samp>number</samp>


////////


///////


//////


////// define
`minecraft:fog`：<samp>object</samp>

- Displays the given fog whenever a player enters the volume. Each volume can only have one fog attached.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:fog</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`fog_identifier`：<samp>string</samp>

- The identifier of a fog definition. Note that you will not receive any feedback if the definition does not exist.


///////


/////// define
`priority`：<samp>integer</samp>

- The priority for this fog definition setting. Smaller numbers have higher priority. Fogs with equal priority will be combined together.


///////


//////


////// define
`minecraft:on_actor_enter`：<samp>object</samp>

- Component that defines what happens when an actor enters the volume. Can contain multiple json objects.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_actor_enter</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`on_enter`：<samp>array</samp>

- Required array that contains all the triggers.


///////

<div class="language-text highlight"><span class="filename"><code>on_enter</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- Trigger.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`condition`：<samp>0</samp> {#assets.schemas-blockception.molang.string.json}

- Molang expression to test against the actor. The given event will be triggered if the expression evaluates to true.


/////////

```mcschema
0:
string

```

///////// html | div.result

/////////



///////// define
`event`：<samp>string</samp>

- Name of the event to run.


/////////


///////// define
`target`：<samp>string</samp>

- One of `self` or `other`. Self means the event is attached to the volume. Other means the event is attached to the actor.


/////////


////////


///////


//////


////// define
`minecraft:on_actor_leave`：<samp>object</samp>

- Component that defines what happens when an actor leaves the volume.


//////

<div class="language-text highlight"><span class="filename"><code>minecraft:on_actor_leave</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`on_enter`：<samp>array</samp>

- Required array that contains all the triggers.


///////

<div class="language-text highlight"><span class="filename"><code>on_enter</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- Trigger.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`condition`：<samp>[0](#assets.schemas-blockception.molang.string.json)</samp>

- Molang expression to test against the actor. The given event will be triggered if the expression evaluates to true.


/////////


///////// define
`event`：<samp>string</samp>

- Name of the event to run.


/////////


///////// define
`target`：<samp>string</samp>

- One of `self` or `other`. Self means the event is attached to the volume. Other means the event is attached to the actor.


/////////


////////


///////


//////


/////


////


///




```mcschema
volumes:
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


