# Block Sensor

> 文档版本：1.21.50.25

Fires off a specified event when a block in the block list is broken within the sensor range.

## 架构

```mcschema
block_sensor:
{
  integer "sensor_radius" : opt
  array "on_break" : opt
  {
    object "<any array element>" : opt
    {
      array "block_list" : opt
      {
        identifier "<any array element>"
      }
      string "on_block_broken" : opt
    }
  }
  array "sources" : opt
  {
    filters "<any array element>"
  }
}

```

/// html | div.result
//// define
`sensor_radius`：<samp>integer</samp>

- The maximum radial distance in which a specified block can be detected. The biggest radius is 32.0.


////


//// define
`on_break`：<samp>array</samp>

- Blocks that will trigger the component when broken and what event will trigger.


////

<div class="language-text highlight"><span class="filename"><code>on_break</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- Event to run when a block breaks.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`block_list`：<samp>array</samp>

- List of blocks that will trigger the sensor.


//////

<div class="language-text highlight"><span class="filename"><code>block_list</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>identifier</samp> {#assets.schemas-blockception.general.block.identifier.json}


///////

```mcschema
identifier:
string

```

/////// html | div.result

///////



//////


////// define
`on_block_broken`：<samp>string</samp>

- Event to run when a block breaks.


//////


/////


////


//// define
`sources`：<samp>array</samp>

- List of sources that break the block to listen for. If none are specified, all block breaks will be detected.


////

<div class="language-text highlight"><span class="filename"><code>sources</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


/////


////


///

