# Feature Rules

> 文档版本：1.21.50.25

Each feature rule controls exactly one feature and serves as the root of a chain of feature data.

## 架构

```mcschema
feature_rules:
{
  format_version "format_version"
  feature_rules "minecraft:feature_rules"
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
`minecraft:feature_rules`：<samp>feature_rules</samp> {#assets.schemas-blockception.behavior.feature_rules.format.minecraft.feature_rules.json}


////

```mcschema
feature_rules:
{
  object "description" : opt
  {
    identifier "identifier"
    string "places_feature" : opt
  }
  object "conditions" : opt
  {
    string "placement_pass" : opt
    filters "minecraft:biome_filter"
  }
  object "distribution" : opt
  {
    string "coordinate_eval_order" : opt
    0 "iterations"
    0 "scatter_chance"
    object "scatter_chance" : opt
    {
      number "numerator" : opt
      number "denominator" : opt
    }
    0 "x"
    object "x" : opt
    {
      number "numerator" : opt
      number "denominator" : opt
    }
    object "x" : opt
    {
      string "distribution" : opt
      array "extent" : opt
      {
        number "<any array element>" : opt
      }
    }
     "z" : opt
     "y" : opt
  }
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description of this feature rule.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.feature.identifier.json}

- The name of this feature in the form `namespace_name:feature_name`. `feature_name` must match the filename.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`places_feature`：<samp>string</samp>

- Named reference to the feature controlled by this rule.


//////


/////


///// define
`conditions`：<samp>object</samp>

- Parameters to control where and when the feature will be placed.


/////

<div class="language-text highlight"><span class="filename"><code>conditions</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`placement_pass`：<samp>string</samp>

- When the feature should be placed relative to others. Earlier passes in the list are guaranteed to occur before later passes. Order is not guaranteed within each pass.


//////


////// define
`minecraft:biome_filter`：<samp>filters</samp>

- [`minecraft:biome_filter`](./conditions/filters.md)条件。Parameters to control where and when the feature will be placed.


//////

/////


///// define
`distribution`：<samp>object</samp>

- Parameters controlling the initial scatter of the feature.


/////

<div class="language-text highlight"><span class="filename"><code>distribution</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`coordinate_eval_order`：<samp>string</samp>

- The order in which coordinates will be evaluated. Should be used when a coordinate depends on another. If omitted, defaults to `xzy`.


//////


////// define
`iterations`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Number of scattered positions to generate.


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
`scatter_chance`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Probability (0-100] that this scatter will occur.  Not evaluated each iteration; either no iterations will run, or all will.


//////


////// define
`scatter_chance`：<samp>object</samp>

- Probability numerator / denominator that this scatter will occur.  Not evaluated each iteration; either no iterations will run, or all will.


//////

<div class="language-text highlight"><span class="filename"><code>scatter_chance</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`numerator`：<samp>number</samp>

- UNDOCUMENTED.


///////


/////// define
`denominator`：<samp>number</samp>

- UNDOCUMENTED.


///////


//////



////// define
`x`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Expression for the coordinate (evaluated each iteration).  Mutually exclusive with random distribution object below.


//////


////// define
`x`：<samp>object</samp>

- Distribution for the coordinate (evaluated each iteration).  Mutually exclusive with Molang expression above.


//////

<div class="language-text highlight"><span class="filename"><code>x</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`numerator`：<samp>number</samp>

- UNDOCUMENTED.


///////


/////// define
`denominator`：<samp>number</samp>

- UNDOCUMENTED.


///////


//////


////// define
`x`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>x</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`distribution`：<samp>string</samp>

- Distribution type


///////


/////// define
`extent`：<samp>array</samp>

- Represents the range of values on which that distribution operates, from minimum to maximum.


///////

<div class="language-text highlight"><span class="filename"><code>extent</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>number</samp>


////////


///////


//////



////// define
`z`

- UNDOCUMENTED.


//////


////// define
`y`

- UNDOCUMENTED.


//////


/////


////



///

