# Conditional Bandwidth Optimization

> 文档版本：1.21.0.24

Defines the Conditional Spatial Update Bandwidth Optimizations of this entity.

## 架构

```mcschema
conditional_bandwidth_optimization:
{
  array "conditional_values" : opt
  {
    object "<any array element>" : opt
    {
      integer "max_dropped_ticks" : opt
      number "max_optimized_distance" : opt
      boolean "use_motion_prediction_hints" : opt
      array "conditional_values" : opt
      {
        filters "<any array element>"
      }
    }
  }
  object "default_values" : opt
  {
    integer "max_dropped_ticks" : opt
    number "max_optimized_distance" : opt
    boolean "use_motion_prediction_hints" : opt
  }
}

```

/// html | div.result
//// define
`conditional_values`：<samp>array</samp>

- The object containing the conditional bandwidth optimization values.


////

<div class="language-text highlight"><span class="filename"><code>conditional_values</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>object</samp>

- The object containing the conditional bandwidth optimization values.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`max_dropped_ticks`：<samp>integer</samp>

- In relation to the optimization value, determines the maximum ticks spatial update packets can be not sent.


//////


////// define
`max_optimized_distance`：<samp>number</samp>

- The maximum distance considered during bandwidth optimizations. Any value below the Maximum is interpolated to find optimization, and any value greater than or equal to this Maximum results in Maximum optimization.


//////


////// define
`use_motion_prediction_hints`：<samp>boolean</samp>

- When set to true, smaller motion packets will be sent during drop packet intervals, resulting in the same amount of packets being sent as without optimizations but with much less data being sent. This should be used when actors are travelling very quickly or teleporting to prevent visual oddities.


//////


////// define
`conditional_values`：<samp>array</samp>

- Conditions that must be met for these optimization values to be used.


//////

<div class="language-text highlight"><span class="filename"><code>conditional_values</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>filters</samp>

- 一个[过滤器组](../filter.md)。


///////


//////


/////


////


//// define
`default_values`：<samp>object</samp>

- The object containing the default bandwidth optimization values.


////

<div class="language-text highlight"><span class="filename"><code>default_values</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`max_dropped_ticks`：<samp>integer</samp>

- In relation to the optimization value, determines the maximum ticks spatial update packets can be not sent.


/////


///// define
`max_optimized_distance`：<samp>number</samp>

- The maximum distance considered during bandwidth optimizations. Any value below the Maximum is interpolated to find optimization, and any value greater than or equal to this Maximum results in Maximum optimization.


/////


///// define
`use_motion_prediction_hints`：<samp>boolean</samp>

- When set to true, smaller motion packets will be sent during drop packet intervals, resulting in the same amount of packets being sent as without optimizations but with much less data being sent. This should be used when actors are travelling very quickly or teleporting to prevent visual oddities.


/////


////


///

