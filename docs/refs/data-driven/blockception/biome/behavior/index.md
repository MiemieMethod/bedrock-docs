# 未命名

> 文档版本：1.21.0.24



## 架构

```mcschema
biomes:
{
  object "<any object property>" : opt
  {
    format_version "format_version"
    capped_surface "minecraft:capped_surface"
    climate "minecraft:climate"
    consolidated_features "minecraft:consolidated_features"
    forced_features "minecraft:forced_features"
    frozen_ocean_surface "minecraft:frozen_ocean_surface"
    ignore_automatic_features "minecraft:ignore_automatic_features"
    legacy_world_generation_rules "minecraft:legacy_world_generation_rules"
    mesa_surface "minecraft:mesa_surface"
    mountain_parameters "minecraft:mountain_parameters"
    nether_generation_rules "minecraft:nether_generation_rules"
    nether_surface "minecraft:nether_surface"
    overworld_generation_rules "minecraft:overworld_generation_rules"
    overworld_height "minecraft:overworld_height"
    surface_material_adjustments "minecraft:surface_material_adjustments"
    surface_parameters "minecraft:surface_parameters"
    swamp_surface "minecraft:swamp_surface"
    the_end_surface "minecraft:the_end_surface"
    object "<any object property>" : opt
    {
    }
  }
}

```

/// html | div.result
//// define
`<any object property>`：<samp>object</samp>

- The definition of a biome.


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`format_version`：<samp>format_version</samp> {#assets.schemas-blockception.general.format_version.json}


/////

```mcschema
format_version:
string

```

///// html | div.result

/////



///// define
`minecraft:capped_surface`：<samp>capped_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.capped_surface.json}


/////

```mcschema
capped_surface:
{
  array "ceiling_materials" : opt
  {
    string "<any array element>" : opt
  }
  array "floor_materials" : opt
  {
    string "<any array element>" : opt
  }
  string "sea_material" : opt
  string "foundation_material" : opt
  string "beach_material" : opt
}

```

///// html | div.result
////// define
`ceiling_materials`：<samp>array</samp>

- Materials used for the surface ceiling.


//////

<div class="language-text highlight"><span class="filename"><code>ceiling_materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- A block reference.


///////


//////


////// define
`floor_materials`：<samp>array</samp>

- Materials used for the surface floor.


//////

<div class="language-text highlight"><span class="filename"><code>floor_materials</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- A block reference.


///////


//////


////// define
`sea_material`：<samp>string</samp>

- Material used to replace air blocks below sea level.


//////


////// define
`foundation_material`：<samp>string</samp>

- Material used to repalce solid blocks that are not surface blocks.


//////


////// define
`beach_material`：<samp>string</samp>

- Material used to decorate surface near sea level.


//////


/////



///// define
`minecraft:climate`：<samp>climate</samp> {#assets.schemas-blockception.behavior.biomes.components.climate.json}


/////

```mcschema
climate:
{
  number "temperature" : opt
  number "downfall" : opt
  number "red_spores" : opt
  number "blue_spores" : opt
  number "ash" : opt
  number "white_ash" : opt
  array "snow_accumulation" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
}

```

///// html | div.result
////// define
`temperature`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`downfall`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`red_spores`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`blue_spores`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`ash`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`white_ash`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`snow_accumulation`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>snow_accumulation</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>number</samp>


///////


/////// define
`1..1`：<samp>number</samp>


///////


//////


/////



///// define
`minecraft:consolidated_features`：<samp>consolidated_features</samp> {#assets.schemas-blockception.behavior.biomes.components.consolidated_features.json}


/////

```mcschema
consolidated_features:
{
}

```

///// html | div.result

/////



///// define
`minecraft:forced_features`：<samp>forced_features</samp> {#assets.schemas-blockception.behavior.biomes.components.forced_features.json}


/////

```mcschema
forced_features:
{
  array "after_sky_pass" : opt
  {
    object "<any array element>" : opt
    {
      string "coordinate_eval_order" : opt
      string "identifier" : opt
      0 "iterations"
      string "places_feature" : opt
      object "scatter_chance" : opt
      {
        integer "denominator" : opt
        integer "numerator" : opt
      }
      0 "scatter_chance"
      number "scatter_chance" : opt
      0 "x"
      number "x" : opt
      object "x" : opt
      {
        string "distribution" : opt
        array "extent" : opt
        {
          0 "0..0"
          0 "1..1"
        }
        integer "grid_offset" : opt
        integer "step_size" : opt
      }
       "y" : opt
       "z" : opt
    }
  }
  array "after_surface_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "after_underground_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "before_sky_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "before_surface_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "before_underground_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "final_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "first_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "surface_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "sky_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "underground_pass" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
}

```

///// html | div.result
////// define
`after_sky_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>after_sky_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`coordinate_eval_order`：<samp>string</samp>

- The order in which coordinates will be evaluated. Should be used when a coordinate depends on another. If omitted, defaults to `xzy`.


////////


//////// define
`identifier`：<samp>string</samp>

- UNDOCUMENTED.


////////


//////// define
`iterations`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- Number of scattered positions to generate.


////////

```mcschema
0:
string

```

//////// html | div.result

////////


```mcschema
0:
number

```

//////// html | div.result

////////




//////// define
`places_feature`：<samp>string</samp>

- UNDOCUMENTED.


////////


//////// define
`scatter_chance`：<samp>object</samp>

- Probability numerator / denominator that this scatter will occur.  Not evaluated each iteration; either no iterations will run, or all will.


////////

<div class="language-text highlight"><span class="filename"><code>scatter_chance</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`denominator`：<samp>integer</samp>

- UNDOCUMENTED.


/////////


///////// define
`numerator`：<samp>integer</samp>

- UNDOCUMENTED.


/////////


////////


//////// define
`scatter_chance`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Probability (0-100) that this scatter will occur.  Not evaluated each iteration; either no iterations will run, or all will.


////////


//////// define
`scatter_chance`：<samp>number</samp>

- Probability (0-100) that this scatter will occur.  Not evaluated each iteration; either no iterations will run, or all will.


////////



//////// define
`x`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Expression for the coordinate (evaluated each iteration).  Mutually exclusive with random distribution object below.


////////


//////// define
`x`：<samp>number</samp>

- Expression for the coordinate (evaluated each iteration).  Mutually exclusive with random distribution object below.


////////


//////// define
`x`：<samp>object</samp>

- Distribution for the coordinate (evaluated each iteration). Mutually exclusive with Molang expression above.


////////

<div class="language-text highlight"><span class="filename"><code>x</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`distribution`：<samp>string</samp>

- Type of distribution - uniform random, gaussian (centered in the range), or grid (either fixed-step or jittered).


/////////


///////// define
`extent`：<samp>array</samp>

- UNDOCUMENTED.


/////////

<div class="language-text highlight"><span class="filename"><code>extent</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Lower bound (inclusive) of the scatter range, as an offset from the input point to scatter around.


//////////


////////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Upper bound (inclusive) of the scatter range, as an offset from the input point to scatter around.


//////////


/////////


///////// define
`grid_offset`：<samp>integer</samp>

- When the distribution type is grid, defines the offset along this axis.


/////////


///////// define
`step_size`：<samp>integer</samp>

- When the distribution type is grid, defines the distance between steps along this axis.


/////////


////////



//////// define
`y`


////////


//////// define
`z`


////////


///////


//////


////// define
`after_surface_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>after_surface_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`after_underground_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>after_underground_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`before_sky_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>before_sky_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`before_surface_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>before_surface_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`before_underground_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>before_underground_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`final_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>final_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`first_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>first_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`surface_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>surface_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`sky_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>sky_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`underground_pass`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>underground_pass</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////



///// define
`minecraft:frozen_ocean_surface`：<samp>frozen_ocean_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.frozen_ocean_surface.json}


/////

```mcschema
frozen_ocean_surface:
{
   "top_material" : opt
   "mid_material" : opt
   "sea_floor_material" : opt
   "foundation_material" : opt
   "sea_material" : opt
  integer "sea_floor_depth" : opt
}

```

///// html | div.result
////// define
`top_material`

- Controls the block type used for the surface of this biome.


//////


////// define
`mid_material`

- Controls the block type used in a layer below the surface of this biome.


//////


////// define
`sea_floor_material`

- Controls the block type used as a floor for bodies of water in this biome.


//////


////// define
`foundation_material`

- Controls the block type used deep underground in this biome.


//////


////// define
`sea_material`

- Controls the block type used for the bodies of water in this biome.


//////


////// define
`sea_floor_depth`：<samp>integer</samp>

- Controls how deep below the world water level the floor should occur.


//////


/////



///// define
`minecraft:ignore_automatic_features`：<samp>ignore_automatic_features</samp> {#assets.schemas-blockception.behavior.biomes.components.ignore_automatic_features.json}


/////

```mcschema
ignore_automatic_features:
{
}

```

///// html | div.result

/////



///// define
`minecraft:legacy_world_generation_rules`：<samp>legacy_world_generation_rules</samp> {#assets.schemas-blockception.behavior.biomes.components.legacy_world_generation_rules.json}


/////

```mcschema
legacy_world_generation_rules:
{
}

```

///// html | div.result

/////



///// define
`minecraft:mesa_surface`：<samp>mesa_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.mesa_surface.json}


/////

```mcschema
mesa_surface:
{
   "top_material" : opt
   "mid_material" : opt
   "sea_floor_material" : opt
   "foundation_material" : opt
   "sea_material" : opt
  integer "sea_floor_depth" : opt
  string "clay_material" : opt
  string "hard_clay_material" : opt
  boolean "bryce_pillars" : opt
  boolean "has_forest" : opt
}

```

///// html | div.result
////// define
`top_material`

- Controls the block type used for the surface of this biome.


//////


////// define
`mid_material`

- Controls the block type used in a layer below the surface of this biome.


//////


////// define
`sea_floor_material`

- Controls the block type used as a floor for bodies of water in this biome.


//////


////// define
`foundation_material`

- Controls the block type used deep underground in this biome.


//////


////// define
`sea_material`

- Controls the block type used for the bodies of water in this biome.


//////


////// define
`sea_floor_depth`：<samp>integer</samp>

- Controls how deep below the world water level the floor should occur.


//////


////// define
`clay_material`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`hard_clay_material`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`bryce_pillars`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


////// define
`has_forest`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


/////



///// define
`minecraft:mountain_parameters`：<samp>mountain_parameters</samp> {#assets.schemas-blockception.behavior.biomes.components.mountain_parameters.json}


/////

```mcschema
mountain_parameters:
{
  number "peaks_factor" : opt
  object "steep_material_adjustment" : opt
  {
    string "material" : opt
    boolean "north_slopes" : opt
    boolean "south_slopes" : opt
    boolean "west_slopes" : opt
    boolean "east_slopes" : opt
  }
  object "top_slide" : opt
  {
     "enabled" : opt
  }
}

```

///// html | div.result
////// define
`peaks_factor`：<samp>number</samp>

- UNDOCUMENTED.


//////


////// define
`steep_material_adjustment`：<samp>object</samp>

- Defines surface material for steep slopes.


//////

<div class="language-text highlight"><span class="filename"><code>steep_material_adjustment</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`material`：<samp>string</samp>

- Block type use as steep material.


///////


/////// define
`north_slopes`：<samp>boolean</samp>

- Enable for north facing slopes.


///////


/////// define
`south_slopes`：<samp>boolean</samp>

- Enable for south facing slopes.


///////


/////// define
`west_slopes`：<samp>boolean</samp>

- Enable for west facing slopes.


///////


/////// define
`east_slopes`：<samp>boolean</samp>

- Enable for east facing slopes.


///////


//////


////// define
`top_slide`：<samp>object</samp>

- Controls the density tapering that happens at the top of the world to prevent terrain from reaching too high.


//////

<div class="language-text highlight"><span class="filename"><code>top_slide</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`enabled`

- If false, top slide will be disabled. If true, other parameters will be taken into account


///////


//////


/////



///// define
`minecraft:nether_generation_rules`：<samp>nether_generation_rules</samp> {#assets.schemas-blockception.behavior.biomes.components.nether_generation_rules.json}


/////

```mcschema
nether_generation_rules:
{
  number "target_temperature" : opt
  number "target_humidity" : opt
  number "target_altitude" : opt
  number "target_weirdness" : opt
  number "weight" : opt
}

```

///// html | div.result
////// define
`target_temperature`：<samp>number</samp>

- Temperature with which this biome should selected, relative to other biomes.


//////


////// define
`target_humidity`：<samp>number</samp>

- Humidity with which this biome should selected, relative to other biomes.


//////


////// define
`target_altitude`：<samp>number</samp>

- Altitude with which this biome should selected, relative to other biomes.


//////


////// define
`target_weirdness`：<samp>number</samp>

- Weirdness with which this biome should selected, relative to other biomes.


//////


////// define
`weight`：<samp>number</samp>

- Weight with which this biome should selected, relative to other biomes.


//////


/////



///// define
`minecraft:nether_surface`：<samp>nether_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.nether_surface.json}


/////

```mcschema
nether_surface:
{
}

```

///// html | div.result

/////



///// define
`minecraft:overworld_generation_rules`：<samp>overworld_generation_rules</samp> {#assets.schemas-blockception.behavior.biomes.components.overworld_generation_rules.json}


/////

```mcschema
overworld_generation_rules:
{
  string "hills_transformation" : opt
  array "hills_transformation" : opt
  {
    string "<any array element>" : opt
    array "<any array element>" : opt
    {
      string "0..0" : opt
      integer "1..1" : opt
    }
  }
   "mutate_transformation" : opt
   "river_transformation" : opt
   "shore_transformation" : opt
  array "generate_for_climates" : opt
  {
    array "<any array element>" : opt
    {
      string "0..0" : opt
      integer "1..1" : opt
    }
  }
}

```

///// html | div.result
////// define
`hills_transformation`：<samp>string</samp>

- UNDOCUMENTED.


//////


////// define
`hills_transformation`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>hills_transformation</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


///////


/////// define
`<any array element>`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>string</samp>

- UNDOCUMENTED.


////////


//////// define
`1..1`：<samp>integer</samp>

- UNDOCUMENTED.


////////


///////



//////



////// define
`mutate_transformation`

- UNDOCUMENTED.


//////


////// define
`river_transformation`

- UNDOCUMENTED.


//////


////// define
`shore_transformation`

- UNDOCUMENTED.


//////


////// define
`generate_for_climates`：<samp>array</samp>

- Controls the world generation climate categories that this biome can spawn for.  A single biome can be associated with multiple categories with different weightings.


//////

<div class="language-text highlight"><span class="filename"><code>generate_for_climates</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>string</samp>

- Name of a climate category.


////////


//////// define
`1..1`：<samp>integer</samp>

- Weight with which this biome should be selected, relative to other biomes in the same category.


////////


///////


//////


/////



///// define
`minecraft:overworld_height`：<samp>overworld_height</samp> {#assets.schemas-blockception.behavior.biomes.components.overworld_height.json}


/////

```mcschema
overworld_height:
{
  array "noise_params" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  string "noise_type" : opt
}

```

///// html | div.result
////// define
`noise_params`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>noise_params</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>number</samp>


///////


/////// define
`1..1`：<samp>number</samp>


///////


//////


////// define
`noise_type`：<samp>string</samp>

- UNDOCUMENTED.


//////


/////



///// define
`minecraft:surface_material_adjustments`：<samp>surface_material_adjustments</samp> {#assets.schemas-blockception.behavior.biomes.components.surface_material_adjustments.json}


/////

```mcschema
surface_material_adjustments:
{
  array "adjustments" : opt
  {
    object "<any array element>" : opt
    {
      array "height_range" : opt
      {
        0 "0..0"
        0 "1..1"
      }
      object "materials" : opt
      {
        string "top_material" : opt
        string "mid_material" : opt
        string "sea_floor_material" : opt
        string "foundation_material" : opt
        string "sea_material" : opt
      }
      array "noise_range" : opt
      {
         "0..0" : opt
         "1..1" : opt
      }
    }
  }
}

```

///// html | div.result
////// define
`adjustments`：<samp>array</samp>

- All adjustments that match the column's noise values will be applied in the order listed.


//////

<div class="language-text highlight"><span class="filename"><code>adjustments</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`height_range`：<samp>array</samp>

- Defines a range of noise values [min, max] for which this adjustment should be applied.


////////

<div class="language-text highlight"><span class="filename"><code>height_range</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


/////////


///////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>


/////////


////////


//////// define
`materials`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>materials</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`top_material`：<samp>string</samp>

- Controls the block type used for the surface of this biome when this adjustment is active.


/////////


///////// define
`mid_material`：<samp>string</samp>

- Controls the block type used in a layer below the surface of this biome when this adjustment is active.


/////////


///////// define
`sea_floor_material`：<samp>string</samp>

- Controls the block type used as a floor for bodies of water in this biome when this adjustment is active.


/////////


///////// define
`foundation_material`：<samp>string</samp>

- Controls the block type used deep underground in this biome when this adjustment is active.


/////////


///////// define
`sea_material`：<samp>string</samp>

- Controls the block type used in the bodies of water in this biome when this adjustment is active.


/////////


////////


//////// define
`noise_range`：<samp>array</samp>

- Defines a range of noise values [min, max] for which this adjustment should be applied.


////////

<div class="language-text highlight"><span class="filename"><code>noise_range</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`


/////////


///////// define
`1..1`


/////////


////////


///////


//////


/////



///// define
`minecraft:surface_parameters`：<samp>surface_parameters</samp> {#assets.schemas-blockception.behavior.biomes.components.surface_parameters.json}


/////

```mcschema
surface_parameters:
{
   "top_material" : opt
   "mid_material" : opt
   "sea_floor_material" : opt
   "foundation_material" : opt
   "sea_material" : opt
  integer "sea_floor_depth" : opt
}

```

///// html | div.result
////// define
`top_material`

- Controls the block type used for the surface of this biome.


//////


////// define
`mid_material`

- Controls the block type used in a layer below the surface of this biome.


//////


////// define
`sea_floor_material`

- Controls the block type used as a floor for bodies of water in this biome.


//////


////// define
`foundation_material`

- Controls the block type used deep underground in this biome.


//////


////// define
`sea_material`

- Controls the block type used for the bodies of water in this biome.


//////


////// define
`sea_floor_depth`：<samp>integer</samp>

- Controls how deep below the world water level the floor should occur.


//////


/////



///// define
`minecraft:swamp_surface`：<samp>swamp_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.swamp_surface.json}


/////

```mcschema
swamp_surface:
{
   "top_material" : opt
   "mid_material" : opt
   "sea_floor_material" : opt
   "foundation_material" : opt
   "sea_material" : opt
  integer "sea_floor_depth" : opt
}

```

///// html | div.result
////// define
`top_material`

- Controls the block type used for the surface of this biome.


//////


////// define
`mid_material`

- Controls the block type used in a layer below the surface of this biome.


//////


////// define
`sea_floor_material`

- Controls the block type used as a floor for bodies of water in this biome.


//////


////// define
`foundation_material`

- Controls the block type used deep underground in this biome.


//////


////// define
`sea_material`

- Controls the block type used for the bodies of water in this biome.


//////


////// define
`sea_floor_depth`：<samp>integer</samp>

- Controls how deep below the world water level the floor should occur.


//////


/////



///// define
`minecraft:the_end_surface`：<samp>the_end_surface</samp> {#assets.schemas-blockception.behavior.biomes.components.the_end_surface.json}


/////

```mcschema
the_end_surface:
{
}

```

///// html | div.result

/////



///// define
`<any object property>`：<samp>object</samp>

- Components with no namespace are treated as `tags': any name consisting of alphanumeric characters, `.` and `_` is permitted; the tag is attached to the biome so that either code or data may check for its existence; tag components may not have member fields.


/////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////


///

