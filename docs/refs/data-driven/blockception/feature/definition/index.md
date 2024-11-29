# Features

> 文档版本：1.21.50.25

Features are decorations scattered throughout the world. Things such as trees, plants, flowers, springs, ore, and coral are all features. Basically, if it isn't the terrain or a mob, it's probably a feature!

## 架构

```mcschema
features:
{
  format_version "format_version"
  aggregate_feature "minecraft:aggregate_feature"
  cave_carver_feature "minecraft:cave_carver_feature"
  fossil_feature "minecraft:fossil_feature"
  geode_feature "minecraft:geode_feature"
  growing_plant_feature "minecraft:growing_plant_feature"
  multiface_feature "minecraft:multiface_feature"
  nether_cave_carver_feature "minecraft:nether_cave_carver_feature"
  ore_feature "minecraft:ore_feature"
  partially_exposed_blob_feature "minecraft:partially_exposed_blob_feature"
  scatter_feature "minecraft:scatter_feature"
  search_feature "minecraft:search_feature"
  sequence_feature "minecraft:sequence_feature"
  single_block_feature "minecraft:single_block_feature"
  snap_to_surface_feature "minecraft:snap_to_surface_feature"
  structure_template_feature "minecraft:structure_template_feature"
  surface_relative_threshold_feature "minecraft:surface_relative_threshold_feature"
  tree_feature "minecraft:tree_feature"
  underwater_cave_carver_feature "minecraft:underwater_cave_carver_feature"
  vegetation_patch_feature "minecraft:vegetation_patch_feature"
  weighted_random_feature "minecraft:weighted_random_feature"
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
`minecraft:aggregate_feature`：<samp>aggregate_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.aggregate_feature.json}


////

```mcschema
aggregate_feature:
{
  description "description"
  array "features" : opt
  {
    string "<any array element>" : opt
  }
  string "early_out" : opt
}

```

//// html | div.result
///// define
`description`：<samp>description</samp> {#assets.schemas-blockception.behavior.features.types.description.json}


/////

```mcschema
description:
{
  identifier "identifier"
}

```

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



/////



///// define
`features`：<samp>array</samp>

- Collection of features to be placed one by one. No guarantee of order. All features use the same input position.


/////

<div class="language-text highlight"><span class="filename"><code>features</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>

- Feature identifer


//////


/////


///// define
`early_out`：<samp>string</samp>

- Do not continue placing features once either the first success or first failure has occurred.


/////


////



//// define
`minecraft:cave_carver_feature`：<samp>cave_carver_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.cave_carver_feature.json}


////

```mcschema
cave_carver_feature:
{
  description "description"
  identifier "fill_with"
  0 "width_modifier"
  integer "skip_carve_chance" : opt
  integer "height_limit" : opt
  array "y_scale" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "horizontal_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "vertical_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "floor_level" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`fill_with`：<samp>identifier</samp> {#assets.schemas-blockception.general.block.identifier.json}

- Reference to the block to fill the cave with.


/////

```mcschema
identifier:
string

```

///// html | div.result

/////



///// define
`width_modifier`：<samp>0</samp> {#assets.schemas-blockception.molang.number.json}

- How many blocks to increase the cave radius by, from the center point of the cave.


/////

```mcschema
0:
string

```

///// html | div.result

/////


```mcschema
0:
number

```

///// html | div.result

/////




///// define
`skip_carve_chance`：<samp>integer</samp>

- The chance to skip doing the carve (1 / value).


/////


///// define
`height_limit`：<samp>integer</samp>

- The height limit where we attempt to carve


/////


///// define
`y_scale`：<samp>array</samp>

- The scaling in y


/////

<div class="language-text highlight"><span class="filename"><code>y_scale</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`horizontal_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>horizontal_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`vertical_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>vertical_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`floor_level`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>floor_level</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


////



//// define
`minecraft:fossil_feature`：<samp>fossil_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.fossil_feature.json}


////

```mcschema
fossil_feature:
{
  description "description"
  identifier "ore_block"
  integer "max_empty_corners" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`ore_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to fill the cave with.


/////


///// define
`max_empty_corners`：<samp>integer</samp>

- UNDOCUMENTED


/////


////



//// define
`minecraft:geode_feature`：<samp>geode_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.geode_feature.json}


////

```mcschema
geode_feature:
{
  description "description"
  identifier "filler"
  identifier "inner_layer"
  identifier "alternate_inner_layer"
  identifier "middle_layer"
  identifier "outer_layer"
  array "inner_placements" : opt
  {
    identifier "<any array element>"
  }
  integer "min_outer_wall_distance" : opt
  integer "max_outer_wall_distance" : opt
  integer "min_distribution_points" : opt
  integer "max_distribution_points" : opt
  integer "min_point_offset" : opt
  integer "max_point_offset" : opt
  integer "max_radius" : opt
  integer "crack_point_offset" : opt
  number "generate_crack_chance" : opt
  number "base_crack_size" : opt
  number "noise_multiplier" : opt
  number "use_potential_placements_chance" : opt
  number "use_alternate_layer0_chance" : opt
  boolean "placements_require_layer0_alternate" : opt
  integer "invalid_blocks_threshold" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`filler`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block to fill the inside of the geode.


/////


///// define
`inner_layer`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block that forms the inside layer of the geode shell.


/////


///// define
`alternate_inner_layer`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block that has a chance of generating instead of inner_layer.


/////


///// define
`middle_layer`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block that forms the middle layer of the geode shell.


/////


///// define
`outer_layer`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block that forms the outer shell of the geode.


/////


///// define
`inner_placements`：<samp>array</samp>

- A list of blocks that may be replaced during placement. Omit this field to allow any block to be replaced.


/////

<div class="language-text highlight"><span class="filename"><code>inner_placements</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- A block that may be replaced during placement.


//////


/////


///// define
`min_outer_wall_distance`：<samp>integer</samp>

- The minimum distance each distribution point must be from the outer wall. [0,10]


/////


///// define
`max_outer_wall_distance`：<samp>integer</samp>

- The maximum distance each distribution point can be from the outer wall. [0,20]


/////


///// define
`min_distribution_points`：<samp>integer</samp>

- The minimum number of points inside the distance field that can get generated. The distance field is the area consisting of all points with a minimum distance to all destribution points. [0,10]


/////


///// define
`max_distribution_points`：<samp>integer</samp>

- The maximum number of points inside the distance field that can get generated. The distance field is the area consisting of all points with a minimum distance to all destribution points. [0,20]


/////


///// define
`min_point_offset`：<samp>integer</samp>

- The lowest possible value of random offset applied to the position of each distribution point. [0,10]


/////


///// define
`max_point_offset`：<samp>integer</samp>

- The highest possible value of random offset applied to the position of each distribution point. [0,10]


/////


///// define
`max_radius`：<samp>integer</samp>

- The maximum possible radius of the geode generated.


/////


///// define
`crack_point_offset`：<samp>integer</samp>

- An offset applied to each distribution point that forms the geode crack opening. [0,10]


/////


///// define
`generate_crack_chance`：<samp>number</samp>

- The likelihood of a geode generating with a crack in its shell. [0,1]


/////


///// define
`base_crack_size`：<samp>number</samp>

- How large the crack opening of the geode should be when generated. [0,5]


/////


///// define
`noise_multiplier`：<samp>number</samp>

- A multiplier applied to the noise that is applied to the distribution points within the geode. Higher = more noisy.


/////


///// define
`use_potential_placements_chance`：<samp>number</samp>

- The likelihood that a special block will be placed on the inside of the geode. [0,1]


/////


///// define
`use_alternate_layer0_chance`：<samp>number</samp>

- The likelihood that a block in the innermost layer of the geode will be replaced with an alternate option. [0,1]


/////


///// define
`placements_require_layer0_alternate`：<samp>boolean</samp>

-  If true, the potential placement block will only be placed on the alternate layer0 blocks that get placed. Potential placement blocks are blocks that depend on the existance of another block to be placed. The latter are the layer0 alternate blocks.


/////


///// define
`invalid_blocks_threshold`：<samp>integer</samp>

- The threshold of invalid blocks for a geode to have a distribution point in before it aborts generation entirely.


/////


////



//// define
`minecraft:growing_plant_feature`：<samp>growing_plant_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.growing_plant_feature.json}


////

```mcschema
growing_plant_feature:
{
  description "description"
  integer "age" : opt
  object "age" : opt
  {
    integer "range_max" : opt
    integer "range_min" : opt
  }
  array "height_distribution" : opt
  {
    array "<any array element>" : opt
    {
       "0..0" : opt
      number "1..1" : opt
    }
  }
  string "growth_direction" : opt
  array "body_blocks" : opt
  {
    array "<any array element>" : opt
    {
      identifier "0..0"
      range_number_type "1..1"
    }
  }
  array "head_blocks" : opt
  boolean "allow_water" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`age`：<samp>integer</samp>

- Age of the head of the plant.


/////


///// define
`age`：<samp>object</samp>

- A range.


/////

<div class="language-text highlight"><span class="filename"><code>age</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`range_max`：<samp>integer</samp>

- The maximum plant height.


//////


////// define
`range_min`：<samp>integer</samp>

- The minimum plant height.


//////


/////



///// define
`height_distribution`：<samp>array</samp>

- Collection of weighted heights that placement will select from.


/////

<div class="language-text highlight"><span class="filename"><code>height_distribution</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>array</samp>

- Collection of weighted heights that placement will select from.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`

- Plant height.


///////


/////// define
`1..1`：<samp>number</samp>

- Weight used in random selection. Value is relative to other weights in the collection.


///////


//////


/////


///// define
`growth_direction`：<samp>string</samp>

- Direction that the plant grows towards. Valid values: UP and DOWN


/////


///// define
`body_blocks`：<samp>array</samp>

- Collection of weighted block descriptor that placement will select from for the body of the plant.


/////

<div class="language-text highlight"><span class="filename"><code>body_blocks</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>array</samp>

- Collection of weighted block descriptor that placement will select from for the plant.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Plant body block.


///////


/////// define
`1..1`：<samp>range_number_type</samp> {#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json}


///////

```mcschema
range_number_type:
number

```

/////// html | div.result

///////


```mcschema
range_number_type:
array
{
  number "0..0" : opt
  number "1..1" : opt
}

```

/////// html | div.result
//////// define
`0..0`：<samp>number</samp>

- The first value of the range.


////////


//////// define
`1..1`：<samp>number</samp>

- The second value of the range.


////////


///////


```mcschema
range_number_type:
{
  number "range_min" : opt
  number "range_max" : opt
}

```

/////// html | div.result
//////// define
`range_min`：<samp>number</samp>

- The minimum value of the range.


////////


//////// define
`range_max`：<samp>number</samp>

- The maximum value of the range.


////////


///////




//////


/////


///// define
`head_blocks`：<samp>array</samp>

- Collection of weighted block descriptor that placement will select from for the body of the plant.


/////

<div class="language-text highlight"><span class="filename"><code>head_blocks</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`allow_water`：<samp>boolean</samp>

- Plant blocks can be placed in water.


/////


////



//// define
`minecraft:multiface_feature`：<samp>multiface_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.multiface_feature.json}


////

```mcschema
multiface_feature:
{
  description "description"
  identifier "places_block"
  integer "search_range" : opt
  boolean "can_place_on_floor" : opt
  boolean "can_place_on_ceiling" : opt
  boolean "can_place_on_wall" : opt
  number "chance_of_spreading" : opt
  array "can_place_on" : opt
  {
    identifier "<any array element>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`places_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to be placed.


/////


///// define
`search_range`：<samp>integer</samp>

- How far, in blocks, this feature can search for a valid position to place.


/////


///// define
`can_place_on_floor`：<samp>boolean</samp>

- Can this feature be placed on the ground (top face of a block)?.


/////


///// define
`can_place_on_ceiling`：<samp>boolean</samp>

- Can this feature be placed on the ceiling (bottom face of a block)?.


/////


///// define
`can_place_on_wall`：<samp>boolean</samp>

- Can this feature be placed on the wall (side faces of a block)?.


/////


///// define
`chance_of_spreading`：<samp>number</samp>

- For each block placed by this feature, how likely will that block spread to another?.


/////


///// define
`can_place_on`：<samp>array</samp>

-  How far, in blocks, this feature can search for a valid position to place.


/////

<div class="language-text highlight"><span class="filename"><code>can_place_on</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

-  A list of blocks that the block in this feature can be placed on. Omit this field to allow any block to be placed on.


//////


/////


////



//// define
`minecraft:nether_cave_carver_feature`：<samp>nether_cave_carver_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.nether_cave_carver_feature.json}


////

```mcschema
nether_cave_carver_feature:
{
  description "description"
  identifier "fill_with"
  0 "width_modifier"
  integer "skip_carve_chance" : opt
  integer "height_limit" : opt
  array "y_scale" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "horizontal_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "vertical_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "floor_level" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`fill_with`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to fill the cave with.


/////


///// define
`width_modifier`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- How many blocks to increase the cave radius by, from the center point of the cave.


/////


///// define
`skip_carve_chance`：<samp>integer</samp>

- The chance to skip doing the carve (1 / value).


/////


///// define
`height_limit`：<samp>integer</samp>

- The height limit where we attempt to carve


/////


///// define
`y_scale`：<samp>array</samp>

- The scaling in y


/////

<div class="language-text highlight"><span class="filename"><code>y_scale</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`horizontal_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>horizontal_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`vertical_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>vertical_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`floor_level`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>floor_level</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


////



//// define
`minecraft:ore_feature`：<samp>ore_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.ore_feature.json}


////

```mcschema
ore_feature:
{
  description "description"
  number "count" : opt
  array "replace_rules" : opt
  {
    object "<any array element>" : opt
    {
      identifier "places_block"
      array "may_replace" : opt
      {
        identifier "<any array element>"
      }
    }
  }
  number "discard_chance_on_air_exposure" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`count`：<samp>number</samp>

- The number of blocks to be placed.


/////


///// define
`replace_rules`：<samp>array</samp>

- Collection of replace rules that will be checked in order of definition. If a rule is resolved, the rest will not be resolved for that block position.


/////

<div class="language-text highlight"><span class="filename"><code>replace_rules</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>

- If a rule is resolved, the rest will not be resolved for that block position.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`places_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to be placed.


///////


/////// define
`may_replace`：<samp>array</samp>

- A list of blocks that may be replaced during placement. Omit this field to allow any block to be replaced.


///////

<div class="language-text highlight"><span class="filename"><code>may_replace</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


///////


//////


/////


///// define
`discard_chance_on_air_exposure`：<samp>number</samp>

- Chance of discarding placement if neighboring block is Air.


/////


////



//// define
`minecraft:partially_exposed_blob_feature`：<samp>partially_exposed_blob_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.partially_exposed_blob_feature.json}


////

```mcschema
partially_exposed_blob_feature:
{
  description "description"
  identifier "places_block"
  number "placement_radius_around_floor" : opt
  number "placement_probability_per_valid_position" : opt
  string "exposed_face" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`places_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to be placed.


/////


///// define
`placement_radius_around_floor`：<samp>number</samp>

- Defines the cubic radius of the blob.


/////


///// define
`placement_probability_per_valid_position`：<samp>number</samp>

- The probability of trying to place a block at each position within the placement bounds.


/////


///// define
`exposed_face`：<samp>string</samp>

- Defines a block face that is allowed to be exposed to air and/or water. Other faces need to be embedded for blocks to be placed by this feature. Defaults to upwards face


/////


////



//// define
`minecraft:scatter_feature`：<samp>scatter_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.scatter_feature.json}


////

```mcschema
scatter_feature:
{
  description "description"
  identifier "places_feature"
  boolean "project_input_to_floor" : opt
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
      string "distribution" : opt
      integer "step_size" : opt
      integer "grid_offset" : opt
      array "extent" : opt
      {
        0 "0..0"
        0 "1..1"
      }
    }
     "z" : opt
     "y" : opt
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`places_feature`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Named reference of feature to be placed.


/////


///// define
`project_input_to_floor`：<samp>boolean</samp>

- If true, snaps the y-value of the scattered position to the terrain heightmap. If false or unset, y-value is unmodified.


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
`iterations`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Number of scattered positions to generate.


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

- Expression for the coordinate (evaluated each iteration). Mutually exclusive with random distribution object below.


//////


////// define
`x`：<samp>object</samp>

- Distribution for the coordinate (evaluated each iteration). Mutually exclusive with Molang expression above.


//////

<div class="language-text highlight"><span class="filename"><code>x</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`distribution`：<samp>string</samp>

- Type of distribution - uniform random, gaussian (centered in the range),  triangle (centered in the range), or grid (either fixed-step or jittered).


///////


/////// define
`step_size`：<samp>integer</samp>

- When the distribution type is grid, defines the distance between steps along this axis.


///////


/////// define
`grid_offset`：<samp>integer</samp>

- When the distribution type is grid, defines the offset along this axis.


///////


/////// define
`extent`：<samp>array</samp>

- The lower and upper bound as an offset from the input position


///////

<div class="language-text highlight"><span class="filename"><code>extent</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`0..0`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Lower bound (inclusive) of the scatter range, as an offset from the input point to scatter around.


////////


//////// define
`1..1`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- Upper bound (inclusive) of the scatter range, as an offset from the input point to scatter around.


////////


///////


//////



////// define
`z`


//////


////// define
`y`


//////


/////


////



//// define
`minecraft:search_feature`：<samp>search_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.search_feature.json}


////

```mcschema
search_feature:
{
  description "description"
  identifier "places_feature"
  object "search_volume" : opt
  {
    array "max" : opt
    {
      integer "0..0" : opt
      integer "1..1" : opt
      integer "2..2" : opt
    }
    array "min" : opt
    {
      integer "0..0" : opt
      integer "1..1" : opt
      integer "2..2" : opt
    }
  }
  string "search_axis" : opt
  integer "required_successes" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`places_feature`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Named reference of feature to be placed.


/////


///// define
`search_volume`：<samp>object</samp>

- Axis-aligned bounding box that will be searched for valid placement positions. Expressed as offsets from the input position.


/////

<div class="language-text highlight"><span class="filename"><code>search_volume</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`max`：<samp>array</samp>

- Maximum extent of the bounding volume expressed as [ x, y, z ].


//////

<div class="language-text highlight"><span class="filename"><code>max</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>integer</samp>


///////


/////// define
`1..1`：<samp>integer</samp>


///////


/////// define
`2..2`：<samp>integer</samp>


///////


//////


////// define
`min`：<samp>array</samp>

- Maxium extent of the bounding volume expressed as [ x, y, z ].


//////

<div class="language-text highlight"><span class="filename"><code>min</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>integer</samp>


///////


/////// define
`1..1`：<samp>integer</samp>


///////


/////// define
`2..2`：<samp>integer</samp>


///////


//////


/////


///// define
`search_axis`：<samp>string</samp>

- Axis that the search will sweep along through the `search_volume`.


/////


///// define
`required_successes`：<samp>integer</samp>

- Number of valid positions the search must find in order to place the referenced feature.


/////


////



//// define
`minecraft:sequence_feature`：<samp>sequence_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.sequence_feature.json}


////

```mcschema
sequence_feature:
{
  description "description"
  array "features" : opt
  {
    identifier "<any array element>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`features`：<samp>array</samp>

- List of features to be placed in sequence. The output position of the previous feature is used as the input position to the next.


/////

<div class="language-text highlight"><span class="filename"><code>features</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- A feature to be placed in sequence. The output position of the previous feature is used as the input position to the next.


//////


/////


////



//// define
`minecraft:single_block_feature`：<samp>single_block_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.single_block_feature.json}


////

```mcschema
single_block_feature:
{
  description "description"
  identifier "places_block"
  array "places_block" : opt
  {
    array "<any array element>" : opt
    {
      identifier "0..0"
      number "1..1" : opt
    }
  }
  boolean "enforce_placement_rules" : opt
  boolean "enforce_survivability_rules" : opt
  boolean "randomize_rotation" : opt
  object "may_attach_to" : opt
  {
     "min_sides_must_attach" : opt
    boolean "auto_rotate" : opt
    identifier "top"
    array "top" : opt
    {
      identifier "<any array element>"
    }
     "bottom" : opt
     "north" : opt
     "south" : opt
     "east" : opt
     "west" : opt
     "all" : opt
     "sides" : opt
     "diagonal" : opt
  }
  object "may_not_attach_to" : opt
  {
     "top" : opt
     "bottom" : opt
     "north" : opt
     "south" : opt
     "east" : opt
     "west" : opt
     "all" : opt
     "sides" : opt
     "diagonal" : opt
  }
  array "may_replace" : opt
  {
    identifier "<any array element>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`places_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to be placed.


/////


///// define
`places_block`：<samp>array</samp>

-  Collection of weighted block references that will be placed.


/////

<div class="language-text highlight"><span class="filename"><code>places_block</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>array</samp>

- Reference to the block to be placed.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to be placed.


///////


/////// define
`1..1`：<samp>number</samp>

- Random weight of this block. A higher number will increase the probability of this block to be picked during placement.


///////


//////


/////



///// define
`enforce_placement_rules`：<samp>boolean</samp>

- If true, enforce the block's canPlace check.


/////


///// define
`enforce_survivability_rules`：<samp>boolean</samp>

- If true, enforce the block's canSurvive check.


/////


///// define
`randomize_rotation`：<samp>boolean</samp>

- If true, randomizes the block's cardinal orientation.


/////


///// define
`may_attach_to`：<samp>object</samp>

- The list of valid block and block faces the given block may attach to when being placed.


/////

<div class="language-text highlight"><span class="filename"><code>may_attach_to</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`min_sides_must_attach`

- Minimum number of sides that must be attached when being placed.


//////


////// define
`auto_rotate`：<samp>boolean</samp>

- Automatically rotate the block to attach sensibly.


//////


////// define
`top`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block it may attach to.


//////


////// define
`top`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>top</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block it may attach to.


///////


//////



////// define
`bottom`

- UNDOCUMENTED.


//////


////// define
`north`

- UNDOCUMENTED.


//////


////// define
`south`

- UNDOCUMENTED.


//////


////// define
`east`

- UNDOCUMENTED.


//////


////// define
`west`

- UNDOCUMENTED.


//////


////// define
`all`

- UNDOCUMENTED.


//////


////// define
`sides`

- UNDOCUMENTED.


//////


////// define
`diagonal`

- UNDOCUMENTED.


//////


/////


///// define
`may_not_attach_to`：<samp>object</samp>

- Denylist which specifies where the block can't be placed.


/////

<div class="language-text highlight"><span class="filename"><code>may_not_attach_to</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`top`

- UNDOCUMENTED.


//////


////// define
`bottom`

- UNDOCUMENTED.


//////


////// define
`north`

- UNDOCUMENTED.


//////


////// define
`south`

- UNDOCUMENTED.


//////


////// define
`east`

- UNDOCUMENTED.


//////


////// define
`west`

- UNDOCUMENTED.


//////


////// define
`all`

- UNDOCUMENTED.


//////


////// define
`sides`

- UNDOCUMENTED.


//////


////// define
`diagonal`

- UNDOCUMENTED.


//////


/////


///// define
`may_replace`：<samp>array</samp>

- A list of blocks that may be replaced during placement. Omit this field to allow any block to be replaced.


/////

<div class="language-text highlight"><span class="filename"><code>may_replace</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- A block that may be replaced during placement. Omit this field to allow any block to be replaced.


//////


/////


////



//// define
`minecraft:snap_to_surface_feature`：<samp>snap_to_surface_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.snap_to_surface_feature.json}


////

```mcschema
snap_to_surface_feature:
{
  description "description"
  identifier "feature_to_snap"
  number "vertical_search_range" : opt
  string "surface" : opt
  boolean "allow_air_placement" : opt
  boolean "allow_underwater_placement" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`feature_to_snap`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Named reference of feature to be snapped.


/////


///// define
`vertical_search_range`：<samp>number</samp>

- Range to search for a floor or ceiling for snaping the feature.


/////


///// define
`surface`：<samp>string</samp>

- Defines the surface that the y-value of the placement position will be snapped to. Valid values: `ceiling` and `floor'


/////


///// define
`allow_air_placement`：<samp>boolean</samp>

- Determines whether the feature can snap through air blocks


/////


///// define
`allow_underwater_placement`：<samp>boolean</samp>

- Determines whether the feature can snap through water blocks


/////


////



//// define
`minecraft:structure_template_feature`：<samp>structure_template_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.structure_template_feature.json}


////

```mcschema
structure_template_feature:
{
  description "description"
  string "structure_name" : opt
  integer "adjustment_radius" : opt
  string "facing_direction" : opt
  object "constraints" : opt
  {
    object "grounded" : opt
    {
    }
    object "unburied" : opt
    {
    }
    object "block_intersection" : opt
    {
      array "block_allowlist" : opt
      {
        identifier "<any array element>"
      }
      array "block_whitelist" : opt
      {
        identifier "<any array element>"
      }
    }
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`structure_name`：<samp>string</samp>

- Reference to the structure to be placed.


/////


///// define
`adjustment_radius`：<samp>integer</samp>

- How far the structure is allowed to move when searching for a valid placement position. Search is radial, stopping when the nearest valid position is found. Defaults to 0 if omitted.


/////


///// define
`facing_direction`：<samp>string</samp>

- Direction the structure will face when placed in the world. Defaults to `random` if omitted.


/////


///// define
`constraints`：<samp>object</samp>

- Specific constraints that must be satisfied when placing this structure.


/////

<div class="language-text highlight"><span class="filename"><code>constraints</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`grounded`：<samp>object</samp>

- When specified, ensures the structure is on the ground.


//////

<div class="language-text highlight"><span class="filename"><code>grounded</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`unburied`：<samp>object</samp>

- When specified, ensures the structure has air above it.


//////

<div class="language-text highlight"><span class="filename"><code>unburied</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`block_intersection`：<samp>object</samp>

- When specified, ensures the structure has air above it.


//////

<div class="language-text highlight"><span class="filename"><code>block_intersection</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`block_allowlist`：<samp>array</samp>

- List of blocks the owning structure is allowed to intersect with.


///////

<div class="language-text highlight"><span class="filename"><code>block_allowlist</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


///////


/////// define
`block_whitelist`：<samp>array</samp>

- List of blocks the owning structure is allowed to intersect with.


///////

<div class="language-text highlight"><span class="filename"><code>block_whitelist</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


///////


//////


/////


////



//// define
`minecraft:surface_relative_threshold_feature`：<samp>surface_relative_threshold_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.surface_relative_threshold_feature.json}


////

```mcschema
surface_relative_threshold_feature:
{
  description "description"
  identifier "feature_to_place"
  integer "minimum_distance_below_surface" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`feature_to_place`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Named reference of feature to be placed.


/////


///// define
`minimum_distance_below_surface`：<samp>integer</samp>

- The minimum number of blocks required to be between the estimated surface level and a valid place for this feature.


/////


////



//// define
`minecraft:tree_feature`：<samp>tree_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.tree_feature.json}


////

```mcschema
tree_feature:
{
  description "description"
  identifier "base_block"
  array "base_block" : opt
  {
    identifier "<any array element>"
  }
  object "base_cluster" : opt
  {
    array "may_replace" : opt
    {
      identifier "<any array element>"
    }
    integer "num_clusters" : opt
    integer "cluster_radius" : opt
  }
  array "may_grow_on" : opt
  {
    identifier "<any array element>"
  }
  array "may_replace" : opt
  {
    identifier "<any array element>"
  }
  array "may_grow_through" : opt
  {
    identifier "<any array element>"
  }
  object "acacia_trunk" : opt
  {
    integer "trunk_width" : opt
    object "trunk_height" : opt
    {
      integer "base" : opt
      array "intervals" : opt
      {
        integer "<any array element>" : opt
      }
      integer "min_height_for_canopy" : opt
    }
    object "trunk_lean" : opt
    {
      boolean "allow_diagonal_growth" : opt
      range_number_type "lean_height"
      range_number_type "lean_steps"
      range_number_type "lean_length"
    }
    string "trunk_block" : opt
    object "branches" : opt
    {
      range_number_type "branch_length"
      range_number_type "branch_position"
      chance_information "branch_chance"
      object "branch_canopy" : opt
      {
        object "acacia_canopy" : opt
        {
          integer "canopy_size" : opt
          string "leaf_block" : opt
          boolean "simplify_canopy" : opt
        }
        object "canopy" : opt
        {
          object "canopy_offset" : opt
          {
            integer "min" : opt
            integer "max" : opt
          }
          integer "min_width" : opt
          object "canopy_slope" : opt
          {
            integer "rise" : opt
            integer "run" : opt
          }
          chance_information "variation_chance"
          array "variation_chance" : opt
          {
            chance_information "<any array element>"
          }
          string "leaf_block" : opt
          object "canopy_decoration" : opt
          {
            chance_information "decoration_chance"
            identifier "decoration_block"
            integer "num_steps" : opt
            string "step_direction" : opt
          }
        }
        object "cherry_canopy" : opt
        {
          string "leaf_block" : opt
          integer "height" : opt
          integer "radius" : opt
          integer "trunk_width" : opt
          chance_information "wide_bottom_layer_hole_chance"
          chance_information "corner_hole_chance"
          chance_information "hanging_leaves_chance"
          chance_information "hanging_leaves_extension_chance"
        }
        object "fancy_canopy" : opt
        {
          integer "height" : opt
          integer "radius" : opt
          string "leaf_block" : opt
        }
        object "mangrove_canopy" : opt
        {
          integer "canopy_height" : opt
          integer "canopy_radius" : opt
          integer "leaf_placement_attempts" : opt
          array "leaf_blocks" : opt
          {
            string "0..0" : opt
            number "1..1" : opt
          }
          object "canopy_decoration" : opt
          {
            chance_information "decoration_chance"
            identifier "decoration_block"
            integer "num_steps" : opt
            string "step_direction" : opt
          }
          identifier "hanging_block"
          chance_information "hanging_block_placement_chance"
        }
        object "mega_canopy" : opt
        {
          integer "canopy_height" : opt
          integer "base_radius" : opt
          number "core_width" : opt
          boolean "simplify_canopy" : opt
          string "leaf_block" : opt
        }
        object "mega_pine_canopy" : opt
        {
          integer "canopy_height" : opt
          integer "base_radius" : opt
          number "radius_step_modifier" : opt
          number "core_width" : opt
          string "leaf_block" : opt
        }
        object "pine_canopy" : opt
        {
          integer "height" : opt
          integer "radius" : opt
          string "leaf_block" : opt
        }
        object "roofed_canopy" : opt
        {
          integer "canopy_height" : opt
          integer "core_width" : opt
          integer "outer_radius" : opt
          integer "inner_radius" : opt
          string "leaf_block" : opt
        }
        object "spruce_canopy" : opt
        {
          integer "lower_offset" : opt
          integer "upper_offset" : opt
          integer "max_radius" : opt
          string "leaf_block" : opt
        }
      }
      object "trunk_decoration" : opt
      {
      }
    }
  }
  object "cherry_trunk" : opt
  {
    string "trunk_block" : opt
    object "trunk_height" : opt
    {
      integer "base" : opt
      array "intervals" : opt
      {
        integer "<any array element>" : opt
      }
    }
    object "branches" : opt
    {
      object "tree_type_weights" : opt
      {
        integer "one_branch" : opt
        integer "two_branches" : opt
        integer "two_branches_and_trunk" : opt
      }
      range_number_type "branch_horizontal_length"
      range_number_type "branch_start_offset_from_top"
      range_number_type "branch_end_offset_from_top"
      chance_information "branch_chance"
      object "branch_canopy" : opt
      {
      }
    }
  }
  object "fallen_trunk" : opt
  {
    integer "log_length" : opt
    integer "stump_height" : opt
    integer "height_modifier" : opt
    string "trunk_block" : opt
    identifier "log_decoration_feature"
    object "trunk_decoration" : opt
    {
    }
  }
  object "fancy_trunk" : opt
  {
    object "trunk_height" : opt
    {
      integer "base" : opt
      integer "variance" : opt
      number "scale" : opt
    }
    integer "trunk_width" : opt
    object "branches" : opt
    {
      number "slope" : opt
      number "density" : opt
      number "min_altitude_factor" : opt
    }
    string "trunk_block" : opt
    number "width_scale" : opt
    number "foliage_altitude_factor" : opt
  }
  object "mangrove_trunk" : opt
  {
    integer "trunk_width" : opt
    object "trunk_height" : opt
    {
      integer "base" : opt
      integer "height_rand_a" : opt
      integer "height_rand_b" : opt
    }
    string "trunk_block" : opt
    object "branches" : opt
    {
      range_number_type "branch_length"
      range_number_type "branch_steps"
      chance_information "branch_chance"
    }
    object "trunk_decoration" : opt
    {
    }
  }
  object "mega_trunk" : opt
  {
    integer "trunk_width" : opt
    object "trunk_height" : opt
    {
      integer "base" : opt
      array "intervals" : opt
      {
        integer "<any array element>" : opt
      }
      integer "min_height_for_canopy" : opt
    }
    string "trunk_block" : opt
    object "trunk_decoration" : opt
    {
    }
    object "branches" : opt
    {
      integer "branch_length" : opt
      number "branch_slope" : opt
      range_number_type "branch_interval"
      object "branch_altitude_factor" : opt
      {
        number "min" : opt
        number "max" : opt
      }
      object "branch_canopy" : opt
      {
      }
    }
  }
  object "trunk" : opt
  {
    range_number_type "trunk_height"
    range_number_type "height_modifier"
    object "can_be_submerged" : opt
    {
      integer "max_depth" : opt
    }
    boolean "can_be_submerged" : opt
    string "trunk_block" : opt
    object "trunk_decoration" : opt
    {
    }
  }
  object "acacia_canopy" : opt
  {
    integer "canopy_size" : opt
    string "leaf_block" : opt
    boolean "simplify_canopy" : opt
  }
  object "canopy" : opt
  {
    object "canopy_offset" : opt
    {
      integer "min" : opt
      integer "max" : opt
    }
    integer "min_width" : opt
    object "canopy_slope" : opt
    {
      integer "rise" : opt
      integer "run" : opt
    }
    chance_information "variation_chance"
    array "variation_chance" : opt
    {
      chance_information "<any array element>"
    }
    string "leaf_block" : opt
    object "canopy_decoration" : opt
    {
      chance_information "decoration_chance"
      identifier "decoration_block"
      integer "num_steps" : opt
      string "step_direction" : opt
    }
  }
  object "cherry_canopy" : opt
  {
    string "leaf_block" : opt
    integer "height" : opt
    integer "radius" : opt
    integer "trunk_width" : opt
    chance_information "wide_bottom_layer_hole_chance"
    chance_information "corner_hole_chance"
    chance_information "hanging_leaves_chance"
    chance_information "hanging_leaves_extension_chance"
  }
  object "fancy_canopy" : opt
  {
    integer "height" : opt
    integer "radius" : opt
    string "leaf_block" : opt
  }
  object "mangrove_canopy" : opt
  {
    integer "canopy_height" : opt
    integer "canopy_radius" : opt
    integer "leaf_placement_attempts" : opt
    array "leaf_blocks" : opt
    {
      string "0..0" : opt
      number "1..1" : opt
    }
    object "canopy_decoration" : opt
    {
    }
    identifier "hanging_block"
    chance_information "hanging_block_placement_chance"
  }
  object "mega_canopy" : opt
  {
    integer "canopy_height" : opt
    integer "base_radius" : opt
    number "core_width" : opt
    boolean "simplify_canopy" : opt
    string "leaf_block" : opt
  }
  object "mega_pine_canopy" : opt
  {
    integer "canopy_height" : opt
    integer "base_radius" : opt
    number "radius_step_modifier" : opt
    number "core_width" : opt
    string "leaf_block" : opt
  }
  object "pine_canopy" : opt
  {
    integer "height" : opt
    integer "radius" : opt
    string "leaf_block" : opt
  }
  object "roofed_canopy" : opt
  {
    integer "canopy_height" : opt
    integer "core_width" : opt
    integer "outer_radius" : opt
    integer "inner_radius" : opt
    string "leaf_block" : opt
  }
  object "spruce_canopy" : opt
  {
    integer "lower_offset" : opt
    integer "upper_offset" : opt
    integer "max_radius" : opt
    string "leaf_block" : opt
  }
  object "random_spread_canopy" : opt
  {
    integer "canopy_height" : opt
    integer "canopy_radius" : opt
    integer "leaf_placement_attempts" : opt
    array "leaf_blocks" : opt
    {
      string "0..0" : opt
      number "1..1" : opt
    }
  }
  object "mangrove_roots" : opt
  {
    integer "max_root_width" : opt
    integer "max_root_length" : opt
    identifier "root_block"
    object "above_root" : opt
    {
      chance_information "above_root_chance"
      identifier "above_root_block"
      identifier "muddy_root_block"
      identifier "mud_block"
      range_number_type "y_offset"
      array "roots_may_grow_through" : opt
      {
        identifier "<any array element>"
      }
      object "root_decoration" : opt
      {
      }
    }
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`base_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


/////


///// define
`base_block`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>base_block</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


/////



///// define
`base_cluster`：<samp>object</samp>

- Allows you to define a number of clusters for the base of the tree. Used to generate mega tree variants.


/////

<div class="language-text highlight"><span class="filename"><code>base_cluster</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`may_replace`：<samp>array</samp>

- List of blocks that the base cluster of a tree can replace.


//////

<div class="language-text highlight"><span class="filename"><code>may_replace</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


///////


//////


////// define
`num_clusters`：<samp>integer</samp>

- Number of clusters that can be generated.


//////


////// define
`cluster_radius`：<samp>integer</samp>

- Radius where the clusters that can be generated.


//////


/////


///// define
`may_grow_on`：<samp>array</samp>

- List of blocks where a tree can grow on.


/////

<div class="language-text highlight"><span class="filename"><code>may_grow_on</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


/////


///// define
`may_replace`：<samp>array</samp>

- List of blocks that a tree can replace.


/////

<div class="language-text highlight"><span class="filename"><code>may_replace</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


/////


///// define
`may_grow_through`：<samp>array</samp>

- List of blocks that a tree can grow through.


/////

<div class="language-text highlight"><span class="filename"><code>may_grow_through</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


/////


///// define
`acacia_trunk`：<samp>object</samp>

- Configutarion for the acacia trunk.


/////

<div class="language-text highlight"><span class="filename"><code>acacia_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


//////


////// define
`trunk_height`：<samp>object</samp>

- Configuration object for the trunk height.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_height</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base`：<samp>integer</samp>

- Min height for the trunk.


///////


/////// define
`intervals`：<samp>array</samp>

- Intervals used to randomize the trunk height, the value of each interval will create a random number where (0 <= rand < interval)), and will be added to the height.


///////

<div class="language-text highlight"><span class="filename"><code>intervals</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>integer</samp>


////////


///////


/////// define
`min_height_for_canopy`：<samp>integer</samp>

- Min height where the canopy can be placed.


///////


//////


////// define
`trunk_lean`：<samp>object</samp>

- Configuration object for diagonal branches.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_lean</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`allow_diagonal_growth`：<samp>boolean</samp>

- If true, diagonal branches will be created.


///////


/////// define
`lean_height`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Number of blocks below the tree height at which diagonal branches can be created.


///////


/////// define
`lean_steps`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Number of steps taken in X/Z direction while creating a diagonal branch.


///////


/////// define
`lean_length`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Length for the diagonal branch in the Y axis.


///////


//////


////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`branches`：<samp>object</samp>

- Configuration object for branches.


//////

<div class="language-text highlight"><span class="filename"><code>branches</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`branch_length`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Length for the branch in the Y axis.


///////


/////// define
`branch_position`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Starting Y position for the branch.


///////


/////// define
`branch_chance`：<samp>chance_information</samp> {#assets.schemas-blockception.behavior.features.types.chance_information.json}

- Probability of creating a branch.


///////

```mcschema
chance_information:
{
  number "numerator" : opt
  number "denominator" : opt
}

```

/////// html | div.result
//////// define
`numerator`：<samp>number</samp>

- UNDOCUMENTED.


////////


//////// define
`denominator`：<samp>number</samp>

- UNDOCUMENTED.


////////


///////


```mcschema
chance_information:
number

```

/////// html | div.result

///////




/////// define
`branch_canopy`：<samp>object</samp>

- Configuration object for the canopy.


///////

<div class="language-text highlight"><span class="filename"><code>branch_canopy</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`acacia_canopy`：<samp>object</samp>

- Configuration object for the acacia canopy.


////////

<div class="language-text highlight"><span class="filename"><code>acacia_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_size`：<samp>integer</samp>

- The size of the canopy.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


///////// define
`simplify_canopy`：<samp>boolean</samp>

- If true the canopy uses a simple pattern.


/////////


////////


//////// define
`canopy`：<samp>object</samp>

- Configuration object for the normal canopy.


////////

<div class="language-text highlight"><span class="filename"><code>canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_offset`：<samp>object</samp>

- Canopy position offset relative to the block above the trunk.


/////////

<div class="language-text highlight"><span class="filename"><code>canopy_offset</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`min`：<samp>integer</samp>

- Min canopy position offset.


//////////


////////// define
`max`：<samp>integer</samp>

- Max canopy position offset.


//////////


/////////


///////// define
`min_width`：<samp>integer</samp>

- Min width for the canopy.


/////////


///////// define
`canopy_slope`：<samp>object</samp>

- Configuration object for the canopy slope.


/////////

<div class="language-text highlight"><span class="filename"><code>canopy_slope</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`rise`：<samp>integer</samp>

- The numerator for the slope fraction.


//////////


////////// define
`run`：<samp>integer</samp>

- The denominator for the slope fraction.


//////////


/////////


///////// define
`variation_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Determines the chance of creating leaf blocks for every layer of the canopy. Larger numbers create a denser tree.


/////////


///////// define
`variation_chance`：<samp>array</samp>

- Determines the chance of creating leaf blocks for every layer of the canopy. Larger numbers create a denser tree.


/////////

<div class="language-text highlight"><span class="filename"><code>variation_chance</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`<any array element>`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>


//////////


/////////



///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


///////// define
`canopy_decoration`：<samp>object</samp>

- Configuration object for the canopy decoration.


/////////

<div class="language-text highlight"><span class="filename"><code>canopy_decoration</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`decoration_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of decorating the trunk.


//////////


////////// define
`decoration_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block used for decorating the trunk.


//////////


////////// define
`num_steps`：<samp>integer</samp>

- Number of decoration blocks to place.


//////////


////////// define
`step_direction`：<samp>string</samp>

- Directions to spread decoration blocks.


//////////


/////////


////////


//////// define
`cherry_canopy`：<samp>object</samp>

- Configuration object for the cherry canopy.


////////

<div class="language-text highlight"><span class="filename"><code>cherry_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


///////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


/////////


///////// define
`wide_bottom_layer_hole_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having a hole in the bottom layer.


/////////


///////// define
`corner_hole_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having a hole in the corner.


/////////


///////// define
`hanging_leaves_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having hanging leaves


/////////


///////// define
`hanging_leaves_extension_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of hanging leaves extending further down


/////////


////////


//////// define
`fancy_canopy`：<samp>object</samp>

- Configuration object for the fancy canopy.


////////

<div class="language-text highlight"><span class="filename"><code>fancy_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


//////// define
`mangrove_canopy`：<samp>object</samp>

- Configuration object for the mangrove canopy.


////////

<div class="language-text highlight"><span class="filename"><code>mangrove_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`canopy_radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`leaf_placement_attempts`：<samp>integer</samp>

- Max number of attempts to create leaf blocks.


/////////


///////// define
`leaf_blocks`：<samp>array</samp>

- The blocks that form the canopy of the tree


/////////

<div class="language-text highlight"><span class="filename"><code>leaf_blocks</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`0..0`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////////


////////// define
`1..1`：<samp>number</samp>

- Weight used in random selection. Value is relative to other weights in the collection.


//////////


/////////


///////// define
`canopy_decoration`：<samp>object</samp>

- Configuration object for the decoration.


/////////

<div class="language-text highlight"><span class="filename"><code>canopy_decoration</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result
////////// define
`decoration_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of decorating the trunk.


//////////


////////// define
`decoration_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block used for decorating the trunk.


//////////


////////// define
`num_steps`：<samp>integer</samp>

- Number of decoration blocks to place.


//////////


////////// define
`step_direction`：<samp>string</samp>

- Directions to spread decoration blocks.


//////////


/////////


///////// define
`hanging_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block to be used as a hanging block.


/////////


///////// define
`hanging_block_placement_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of creating a hanging leaf block.


/////////


////////


//////// define
`mega_canopy`：<samp>object</samp>

- Configuration object for the mega canopy.


////////

<div class="language-text highlight"><span class="filename"><code>mega_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`base_radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`core_width`：<samp>number</samp>

- Width of the tree trunk.


/////////


///////// define
`simplify_canopy`：<samp>boolean</samp>

- If true the canopy uses a simple pattern.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


//////// define
`mega_pine_canopy`：<samp>object</samp>

- Configuration object for the mega pine canopy.


////////

<div class="language-text highlight"><span class="filename"><code>mega_pine_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`base_radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`radius_step_modifier`：<samp>number</samp>

- Modifier for the base radius of the canopy.


/////////


///////// define
`core_width`：<samp>number</samp>

- Width of the tree trunk.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


//////// define
`pine_canopy`：<samp>object</samp>

- Configuration object for the pine canopy.


////////

<div class="language-text highlight"><span class="filename"><code>pine_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


/////////


///////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


//////// define
`roofed_canopy`：<samp>object</samp>

- Configuration object for the roofed canopy.


////////

<div class="language-text highlight"><span class="filename"><code>roofed_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`canopy_height`：<samp>integer</samp>

- Roofed canopies feature a base and a top layer, and an extra cap layer on some occasions, this value controls the number of layers in the middle.


/////////


///////// define
`core_width`：<samp>integer</samp>

- Width of the tree trunk.


/////////


///////// define
`outer_radius`：<samp>integer</samp>

- Radius used for the base and top layers.


/////////


///////// define
`inner_radius`：<samp>integer</samp>

- Radius used for the middle layers.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


//////// define
`spruce_canopy`：<samp>object</samp>

- Configuration object for the spruce canopy.


////////

<div class="language-text highlight"><span class="filename"><code>spruce_canopy</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`lower_offset`：<samp>integer</samp>

- Min canopy position offset.


/////////


///////// define
`upper_offset`：<samp>integer</samp>

- Max canopy position offset.


/////////


///////// define
`max_radius`：<samp>integer</samp>

- Max radius of the canopy.


/////////


///////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


/////////


////////


///////


/////// define
`trunk_decoration`：<samp>object</samp>

- Configuration object for the decoration.


///////

<div class="language-text highlight"><span class="filename"><code>trunk_decoration</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


///// define
`cherry_trunk`：<samp>object</samp>

- Configutarion for the cherry trunk.


/////

<div class="language-text highlight"><span class="filename"><code>cherry_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`trunk_height`：<samp>object</samp>

- Configuration object for the trunk height.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_height</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base`：<samp>integer</samp>

- Min height for the trunk.


///////


/////// define
`intervals`：<samp>array</samp>

- Intervals used to randomize the trunk height, the value of each interval will create a random number where (0 <= rand < interval)), and will be added to the height.


///////

<div class="language-text highlight"><span class="filename"><code>intervals</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>integer</samp>


////////


///////


//////


////// define
`branches`：<samp>object</samp>

- Configuration object for branches.


//////

<div class="language-text highlight"><span class="filename"><code>branches</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`tree_type_weights`：<samp>object</samp>

- Configuration object to pick a tree variant based on a weighted random number


///////

<div class="language-text highlight"><span class="filename"><code>tree_type_weights</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`one_branch`：<samp>integer</samp>

- Tree variant with one branch.


////////


//////// define
`two_branches`：<samp>integer</samp>

- Tree variant with two branches.


////////


//////// define
`two_branches_and_trunk`：<samp>integer</samp>

- Tree variant with three branch.


////////


///////


/////// define
`branch_horizontal_length`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Branch length in X/Z axis.


///////


/////// define
`branch_start_offset_from_top`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Branch starting position relative to the top of the tree


///////


/////// define
`branch_end_offset_from_top`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Branch end position relative to the top of the tree


///////


/////// define
`branch_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of creating a branch.


///////


/////// define
`branch_canopy`：<samp>object</samp>

- Configuration object for the canopy.


///////

<div class="language-text highlight"><span class="filename"><code>branch_canopy</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


///// define
`fallen_trunk`：<samp>object</samp>

- Configutarion for the fallen trunk.


/////

<div class="language-text highlight"><span class="filename"><code>fallen_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`log_length`：<samp>integer</samp>

- Length of the fallen log.


//////


////// define
`stump_height`：<samp>integer</samp>

- height of the stump.


//////


////// define
`height_modifier`：<samp>integer</samp>

- Modifier for the length of the fallen log.


//////


////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`log_decoration_feature`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Feature that can be used to decorate the fallen log.


//////


////// define
`trunk_decoration`：<samp>object</samp>

- Configuration object for the decoration.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`fancy_trunk`：<samp>object</samp>

- Configutarion for the fancy trunk.


/////

<div class="language-text highlight"><span class="filename"><code>fancy_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_height`：<samp>object</samp>

- Configuration object for the trunk height.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_height</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base`：<samp>integer</samp>

- Min height for the trunk.


///////


/////// define
`variance`：<samp>integer</samp>

- Modifier for the trunk height.


///////


/////// define
`scale`：<samp>number</samp>

- Final tree height is multiplied by this scale.


///////


//////


////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


//////


////// define
`branches`：<samp>object</samp>

- Configuration object for branches.


//////

<div class="language-text highlight"><span class="filename"><code>branches</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`slope`：<samp>number</samp>

- Slope for the branch, where 0 is horizontal and 1 is vertical.


///////


/////// define
`density`：<samp>number</samp>

- Density of foliage.


///////


/////// define
`min_altitude_factor`：<samp>number</samp>

- Min height for branches. Represented by a percentage of the tree height.


///////


//////


////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`width_scale`：<samp>number</samp>

- Scale modifier for the tree radius.


//////


////// define
`foliage_altitude_factor`：<samp>number</samp>

- Min height for foliage. Represented by a percentage of the tree height.


//////


/////


///// define
`mangrove_trunk`：<samp>object</samp>

- Configutarion for the mangrove trunk.


/////

<div class="language-text highlight"><span class="filename"><code>mangrove_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


//////


////// define
`trunk_height`：<samp>object</samp>

- Configuration object for the trunk height.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_height</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base`：<samp>integer</samp>

- Min height for the trunk.


///////


/////// define
`height_rand_a`：<samp>integer</samp>

- Tree height modifier A.


///////


/////// define
`height_rand_b`：<samp>integer</samp>

- Tree height modifier B.


///////


//////


////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`branches`：<samp>object</samp>

- Configuration object for branches.


//////

<div class="language-text highlight"><span class="filename"><code>branches</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`branch_length`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Length for the branch in the Y axis.


///////


/////// define
`branch_steps`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Number of branches to place.


///////


/////// define
`branch_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of creating a branch.


///////


//////


////// define
`trunk_decoration`：<samp>object</samp>

- Configuration object for the decoration.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`mega_trunk`：<samp>object</samp>

- Configutarion for the mega trunk.


/////

<div class="language-text highlight"><span class="filename"><code>mega_trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


//////


////// define
`trunk_height`：<samp>object</samp>

- Configuration object for the trunk height.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_height</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`base`：<samp>integer</samp>

- Min height for the trunk.


///////


/////// define
`intervals`：<samp>array</samp>

- Intervals used to randomize the trunk height, the value of each interval will create a random number where (0 <= rand < interval)), and will be added to the height.


///////

<div class="language-text highlight"><span class="filename"><code>intervals</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>integer</samp>


////////


///////


/////// define
`min_height_for_canopy`：<samp>integer</samp>

- Min height where the canopy can be placed.


///////


//////


////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`trunk_decoration`：<samp>object</samp>

- Configuration object for the decoration.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`branches`：<samp>object</samp>

- Configuration object for branches.


//////

<div class="language-text highlight"><span class="filename"><code>branches</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`branch_length`：<samp>integer</samp>

- Length for the branch.


///////


/////// define
`branch_slope`：<samp>number</samp>

- Slope for the branch, where 0 is horizontal and 1 is vertical.


///////


/////// define
`branch_interval`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Randomized distance between branches.


///////


/////// define
`branch_altitude_factor`：<samp>object</samp>

- Altitude at which branches can spawn, relative to the tree height.


///////

<div class="language-text highlight"><span class="filename"><code>branch_altitude_factor</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`min`：<samp>number</samp>

- Min altitude where branches can spawn.


////////


//////// define
`max`：<samp>number</samp>

- Max altitude where branches can spawn.


////////


///////


/////// define
`branch_canopy`：<samp>object</samp>

- Configuration object for the canopy.


///////

<div class="language-text highlight"><span class="filename"><code>branch_canopy</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


///// define
`trunk`：<samp>object</samp>

- Configutarion for the normal trunk.


/////

<div class="language-text highlight"><span class="filename"><code>trunk</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`trunk_height`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Defines the height of the trunk.


//////


////// define
`height_modifier`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Modifier for the height of the trunk.


//////


////// define
`can_be_submerged`：<samp>object</samp>

- Specifies if the trunk can be submerged.


//////

<div class="language-text highlight"><span class="filename"><code>can_be_submerged</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`max_depth`：<samp>integer</samp>

- Defines the max depth at which the trunk can be submerged.


///////


//////


////// define
`can_be_submerged`：<samp>boolean</samp>

- Specifies if the trunk can be submerged.


//////



////// define
`trunk_block`：<samp>string</samp>

- The block that forms the tree trunk.


//////


////// define
`trunk_decoration`：<samp>object</samp>

- Configuration object for the decoration.


//////

<div class="language-text highlight"><span class="filename"><code>trunk_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`acacia_canopy`：<samp>object</samp>

- Configuration object for the acacia canopy.


/////

<div class="language-text highlight"><span class="filename"><code>acacia_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_size`：<samp>integer</samp>

- The size of the canopy.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


////// define
`simplify_canopy`：<samp>boolean</samp>

- If true the canopy uses a simple pattern.


//////


/////


///// define
`canopy`：<samp>object</samp>

- Configuration object for the normal canopy.


/////

<div class="language-text highlight"><span class="filename"><code>canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_offset`：<samp>object</samp>

- Canopy position offset relative to the block above the trunk.


//////

<div class="language-text highlight"><span class="filename"><code>canopy_offset</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`min`：<samp>integer</samp>

- Min canopy position offset.


///////


/////// define
`max`：<samp>integer</samp>

- Max canopy position offset.


///////


//////


////// define
`min_width`：<samp>integer</samp>

- Min width for the canopy.


//////


////// define
`canopy_slope`：<samp>object</samp>

- Configuration object for the canopy slope.


//////

<div class="language-text highlight"><span class="filename"><code>canopy_slope</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`rise`：<samp>integer</samp>

- The numerator for the slope fraction.


///////


/////// define
`run`：<samp>integer</samp>

- The denominator for the slope fraction.


///////


//////


////// define
`variation_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Determines the chance of creating leaf blocks for every layer of the canopy. Larger numbers create a denser tree.


//////


////// define
`variation_chance`：<samp>array</samp>

- Determines the chance of creating leaf blocks for every layer of the canopy. Larger numbers create a denser tree.


//////

<div class="language-text highlight"><span class="filename"><code>variation_chance</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>


///////


//////



////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


////// define
`canopy_decoration`：<samp>object</samp>

- Configuration object for the canopy decoration.


//////

<div class="language-text highlight"><span class="filename"><code>canopy_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`decoration_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of decorating the trunk.


///////


/////// define
`decoration_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block used for decorating the trunk.


///////


/////// define
`num_steps`：<samp>integer</samp>

- Number of decoration blocks to place.


///////


/////// define
`step_direction`：<samp>string</samp>

- Directions to spread decoration blocks.


///////


//////


/////


///// define
`cherry_canopy`：<samp>object</samp>

- Configuration object for the cherry canopy.


/////

<div class="language-text highlight"><span class="filename"><code>cherry_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`trunk_width`：<samp>integer</samp>

- The width of the tree trunk.


//////


////// define
`wide_bottom_layer_hole_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having a hole in the bottom layer.


//////


////// define
`corner_hole_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having a hole in the corner.


//////


////// define
`hanging_leaves_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of the canopy having hanging leaves


//////


////// define
`hanging_leaves_extension_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of hanging leaves extending further down


//////


/////


///// define
`fancy_canopy`：<samp>object</samp>

- Configuration object for the fancy canopy.


/////

<div class="language-text highlight"><span class="filename"><code>fancy_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`mangrove_canopy`：<samp>object</samp>

- Configuration object for the mangrove canopy.


/////

<div class="language-text highlight"><span class="filename"><code>mangrove_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`canopy_radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`leaf_placement_attempts`：<samp>integer</samp>

- Max number of attempts to create leaf blocks.


//////


////// define
`leaf_blocks`：<samp>array</samp>

- The blocks that form the canopy of the tree


//////

<div class="language-text highlight"><span class="filename"><code>leaf_blocks</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>string</samp>

- The block thata forms the canopy of the tree.


///////


/////// define
`1..1`：<samp>number</samp>

- Weight used in random selection. Value is relative to other weights in the collection.


///////


//////


////// define
`canopy_decoration`：<samp>object</samp>

- Configuration object for the decoration.


//////

<div class="language-text highlight"><span class="filename"><code>canopy_decoration</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`hanging_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block to be used as a hanging block.


//////


////// define
`hanging_block_placement_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of creating a hanging leaf block.


//////


/////


///// define
`mega_canopy`：<samp>object</samp>

- Configuration object for the mega canopy.


/////

<div class="language-text highlight"><span class="filename"><code>mega_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`base_radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`core_width`：<samp>number</samp>

- Width of the tree trunk.


//////


////// define
`simplify_canopy`：<samp>boolean</samp>

- If true the canopy uses a simple pattern.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`mega_pine_canopy`：<samp>object</samp>

- Configuration object for the mega pine canopy.


/////

<div class="language-text highlight"><span class="filename"><code>mega_pine_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`base_radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`radius_step_modifier`：<samp>number</samp>

- Modifier for the base radius of the canopy.


//////


////// define
`core_width`：<samp>number</samp>

- Width of the tree trunk.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`pine_canopy`：<samp>object</samp>

- Configuration object for the pine canopy.


/////

<div class="language-text highlight"><span class="filename"><code>pine_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`roofed_canopy`：<samp>object</samp>

- Configuration object for the roofed canopy.


/////

<div class="language-text highlight"><span class="filename"><code>roofed_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_height`：<samp>integer</samp>

- Roofed canopies feature a base and a top layer, and an extra cap layer on some occasions, this value controls the number of layers in the middle.


//////


////// define
`core_width`：<samp>integer</samp>

- Width of the tree trunk.


//////


////// define
`outer_radius`：<samp>integer</samp>

- Radius used for the base and top layers.


//////


////// define
`inner_radius`：<samp>integer</samp>

- Radius used for the middle layers.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`spruce_canopy`：<samp>object</samp>

- Configuration object for the spruce canopy.


/////

<div class="language-text highlight"><span class="filename"><code>spruce_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`lower_offset`：<samp>integer</samp>

- Min canopy position offset.


//////


////// define
`upper_offset`：<samp>integer</samp>

- Max canopy position offset.


//////


////// define
`max_radius`：<samp>integer</samp>

- Max radius of the canopy.


//////


////// define
`leaf_block`：<samp>string</samp>

- The block thata forms the canopy of the tree.


//////


/////


///// define
`random_spread_canopy`：<samp>object</samp>

- Configuration object for the random spread canopy.


/////

<div class="language-text highlight"><span class="filename"><code>random_spread_canopy</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`canopy_height`：<samp>integer</samp>

- Number of layers for the canopy.


//////


////// define
`canopy_radius`：<samp>integer</samp>

- The radius of the canopy.


//////


////// define
`leaf_placement_attempts`：<samp>integer</samp>

- Max number of attempts to create leaf blocks.


//////


////// define
`leaf_blocks`：<samp>array</samp>

- The blocks that form the canopy of the tree


//////

<div class="language-text highlight"><span class="filename"><code>leaf_blocks</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>string</samp>

- The block thata forms the canopy of the tree.


///////


/////// define
`1..1`：<samp>number</samp>

- Weight used in random selection. Value is relative to other weights in the collection.


///////


//////


/////


///// define
`mangrove_roots`：<samp>object</samp>

- Configuration for mangrove roots


/////

<div class="language-text highlight"><span class="filename"><code>mangrove_roots</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`max_root_width`：<samp>integer</samp>

- Max width that the roots can occupy. The width increases up to the max width while moving downwards. When a max width is reached, roots will grow vertically


//////


////// define
`max_root_length`：<samp>integer</samp>

- Max length that the roots can occupy.


//////


////// define
`root_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Block used for roots.


//////


////// define
`above_root`：<samp>object</samp>

- Configuration object for blocks decorating the top of the roots


//////

<div class="language-text highlight"><span class="filename"><code>above_root</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`above_root_chance`：<samp>[chance_information](#assets.schemas-blockception.behavior.features.types.chance_information.json)</samp>

- Probability of creating a block above the root


///////


/////// define
`above_root_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block placed on the top of the roots.


///////


/////// define
`muddy_root_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block used for muddy roots.


///////


/////// define
`mud_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- The block used to determine if a muddy root should be placed.


///////


/////// define
`y_offset`：<samp>[range_number_type](#assets.schemas-blockception.behavior.entities.format.types.range_number_type.json)</samp>

- Root offset from the trunk


///////


/////// define
`roots_may_grow_through`：<samp>array</samp>

- List of blocks that a root can grow through.


///////

<div class="language-text highlight"><span class="filename"><code>roots_may_grow_through</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


////////


///////


/////// define
`root_decoration`：<samp>object</samp>

- Configuration object for the decoration.


///////

<div class="language-text highlight"><span class="filename"><code>root_decoration</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


////



//// define
`minecraft:underwater_cave_carver_feature`：<samp>underwater_cave_carver_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.underwater_cave_carver_feature.json}


////

```mcschema
underwater_cave_carver_feature:
{
  description "description"
  identifier "fill_with"
  0 "width_modifier"
  integer "skip_carve_chance" : opt
  integer "height_limit" : opt
  array "y_scale" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "horizontal_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "vertical_radius_multiplier" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  array "floor_level" : opt
  {
    number "0..0" : opt
    number "1..1" : opt
  }
  identifier "replace_air_with"
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`fill_with`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to fill the cave with.


/////


///// define
`width_modifier`：<samp>[0](#assets.schemas-blockception.molang.number.json)</samp>

- How many blocks to increase the cave radius by, from the center point of the cave.


/////


///// define
`skip_carve_chance`：<samp>integer</samp>

- The chance to skip doing the carve (1 / value).


/////


///// define
`height_limit`：<samp>integer</samp>

- The height limit where we attempt to carve


/////


///// define
`y_scale`：<samp>array</samp>

- The scaling in y


/////

<div class="language-text highlight"><span class="filename"><code>y_scale</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`horizontal_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>horizontal_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`vertical_radius_multiplier`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>vertical_radius_multiplier</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`floor_level`：<samp>array</samp>


/////

<div class="language-text highlight"><span class="filename"><code>floor_level</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`0..0`：<samp>number</samp>


//////


////// define
`1..1`：<samp>number</samp>


//////


/////


///// define
`replace_air_with`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Reference to the block to replace air blocks with.


/////


////



//// define
`minecraft:vegetation_patch_feature`：<samp>vegetation_patch_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.vegetation_patch_feature.json}


////

```mcschema
vegetation_patch_feature:
{
  description "description"
  array "replaceable_blocks" : opt
  {
    identifier "<any array element>"
  }
  identifier "ground_block"
  identifier "vegetation_feature"
  string "surface" : opt
  integer "depth" : opt
  number "extra_deep_block_chance" : opt
  integer "vertical_range" : opt
  number "vegetation_chance" : opt
  integer "horizontal_radius" : opt
  number "extra_edge_column_chance" : opt
  boolean "waterlogged" : opt
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`replaceable_blocks`：<samp>array</samp>

- Blocks that can be replaced by the ground blocks on the patch.


/////

<div class="language-text highlight"><span class="filename"><code>replaceable_blocks</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>


//////


/////


///// define
`ground_block`：<samp>[identifier](#assets.schemas-blockception.general.block.identifier.json)</samp>

- Block used to create a base for the vegetation patch.


/////


///// define
`vegetation_feature`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Feature that will be placed by the patch.


/////


///// define
`surface`：<samp>string</samp>

- Determines if a vegetation patch will grow from the ceiling or the floor.


/////


///// define
`depth`：<samp>integer</samp>

- Depth of the base covered by the ground blocks.


/////


///// define
`extra_deep_block_chance`：<samp>number</samp>

- Probability of putting the ground blocks one block deeper. Adds some randomness to the bottom of the patch.


/////


///// define
`vertical_range`：<samp>integer</samp>

- Vertical range used to determine a suitable surface position for the patch.


/////


///// define
`vegetation_chance`：<samp>number</samp>

- Probability of spawning vegetation on the patch. Larger numbers create a denser vegetation patch.


/////


///// define
`horizontal_radius`：<samp>integer</samp>

- Horizontal area that the vegetation patch will cover.


/////


///// define
`extra_edge_column_chance`：<samp>number</samp>

- Probability of spawning vegetation on the edge of the patch radius.


/////


///// define
`waterlogged`：<samp>boolean</samp>

- If true, waterlogs the positions occupied by the ground blocks.


/////


////



//// define
`minecraft:weighted_random_feature`：<samp>weighted_random_feature</samp> {#assets.schemas-blockception.behavior.features.features.minecraft.weighted_random_feature.json}


////

```mcschema
weighted_random_feature:
{
  description "description"
  array "features" : opt
  {
    array "<any array element>" : opt
    {
      identifier "0..0"
      number "1..1" : opt
    }
  }
}

```

//// html | div.result
///// define
`description`：<samp>[description](#assets.schemas-blockception.behavior.features.types.description.json)</samp>


/////


///// define
`features`：<samp>array</samp>

-  Collection of weighted features that placement will select from.


/////

<div class="language-text highlight"><span class="filename"><code>features</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>array</samp>

- Named reference to a feature.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`0..0`：<samp>[identifier](#assets.schemas-blockception.general.feature.identifier.json)</samp>

- Named reference to a feature.


///////


/////// define
`1..1`：<samp>number</samp>

- Weight used in random selection. Value is relative to other weights in the collection.


///////


//////


/////


////



///

