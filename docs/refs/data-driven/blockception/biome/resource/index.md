# Biomes Client

> 文档版本：1.21.50.25

The minecraft biomes definition file.

## 架构

```mcschema
json:
{
  object "biomes" : opt
  {
    object "bamboo_jungle_hills" : opt
    {
       "fog_color" : opt
      identifier "fog_identifier"
      array "fog_ids_to_merge" : opt
      {
        identifier "<any array element>"
      }
      boolean "inherit_from_prior_fog" : opt
      boolean "remove_all_prior_fog" : opt
       "water_fog_color" : opt
      integer "water_fog_distance" : opt
       "water_surface_color" : opt
      number "water_surface_transparency" : opt
    }
    object "bamboo_jungle" : opt
    {
    }
    object "basalt_deltas" : opt
    {
    }
    object "beach" : opt
    {
    }
    object "birch_forest_hills" : opt
    {
    }
    object "birch_forest" : opt
    {
    }
    object "cherry_grove" : opt
    {
    }
    object "cold_beach" : opt
    {
    }
    object "cold_ocean" : opt
    {
    }
    object "cold_taiga_hills" : opt
    {
    }
    object "cold_taiga_mutated" : opt
    {
    }
    object "cold_taiga" : opt
    {
    }
    object "crimson_forest" : opt
    {
    }
    object "deep_cold_ocean" : opt
    {
    }
    object "deep_frozen_ocean" : opt
    {
    }
    object "deep_lukewarm_ocean" : opt
    {
    }
    object "deep_ocean" : opt
    {
    }
    object "deep_warm_ocean" : opt
    {
    }
    object "default" : opt
    {
    }
    object "desert_hills" : opt
    {
    }
    object "desert" : opt
    {
    }
    object "extreme_hills_edge" : opt
    {
    }
    object "extreme_hills_mutated" : opt
    {
    }
    object "extreme_hills_plus_trees_mutated" : opt
    {
    }
    object "extreme_hills_plus_trees" : opt
    {
    }
    object "extreme_hills" : opt
    {
    }
    object "flower_forest" : opt
    {
    }
    object "forest_hills" : opt
    {
    }
    object "forest" : opt
    {
    }
    object "frozen_ocean" : opt
    {
    }
    object "frozen_river" : opt
    {
    }
    object "hell" : opt
    {
    }
    object "ice_mountains" : opt
    {
    }
    object "ice_plains_spikes" : opt
    {
    }
    object "ice_plains" : opt
    {
    }
    object "jungle_edge" : opt
    {
    }
    object "jungle_hills" : opt
    {
    }
    object "jungle_mutated" : opt
    {
    }
    object "jungle" : opt
    {
    }
    object "lukewarm_ocean" : opt
    {
    }
    object "mangrove_swamp" : opt
    {
    }
    object "mega_spruce_taiga_mutated" : opt
    {
    }
    object "mega_spruce_taiga" : opt
    {
    }
    object "mega_taiga_hills" : opt
    {
    }
    object "mega_taiga_mutated" : opt
    {
    }
    object "mega_taiga" : opt
    {
    }
    object "mesa_bryce" : opt
    {
    }
    object "mesa_mutated" : opt
    {
    }
    object "mesa_plateau_stone" : opt
    {
    }
    object "mesa_plateau" : opt
    {
    }
    object "mesa" : opt
    {
    }
    object "mushroom_island_shore" : opt
    {
    }
    object "mushroom_island" : opt
    {
    }
    object "ocean" : opt
    {
    }
    object "plains" : opt
    {
    }
    object "river" : opt
    {
    }
    object "roofed_forest" : opt
    {
    }
    object "savanna_mutated" : opt
    {
    }
    object "savanna_plateau" : opt
    {
    }
    object "savanna" : opt
    {
    }
    object "soulsand_valley" : opt
    {
    }
    object "stone_beach" : opt
    {
    }
    object "sunflower_plains" : opt
    {
    }
    object "swampland_mutated" : opt
    {
    }
    object "swampland" : opt
    {
    }
    object "taiga_hills" : opt
    {
    }
    object "taiga_mutated" : opt
    {
    }
    object "taiga" : opt
    {
    }
    object "the_end" : opt
    {
    }
    object "warm_ocean" : opt
    {
    }
    object "warped_forest" : opt
    {
    }
  }
}

```

/// html | div.result
//// define
`biomes`：<samp>object</samp>

- A collection of predefined biomes.


////

<div class="language-text highlight"><span class="filename"><code>biomes</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`bamboo_jungle_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>bamboo_jungle_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`fog_color`

- The colouration of this object.


//////


////// define
`fog_identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.fog.identifier.json}

- The fog to be associated to this biome.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`fog_ids_to_merge`：<samp>array</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>fog_ids_to_merge</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>[identifier](#assets.schemas-blockception.general.fog.identifier.json)</samp>


///////


//////


////// define
`inherit_from_prior_fog`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


////// define
`remove_all_prior_fog`：<samp>boolean</samp>

- UNDOCUMENTED.


//////


////// define
`water_fog_color`

- The colouration of this object.


//////


////// define
`water_fog_distance`：<samp>integer</samp>

- The distance the water fog start at.


//////


////// define
`water_surface_color`

- The colouration of this object.


//////


////// define
`water_surface_transparency`：<samp>number</samp>

- The amount of transpareny the surface of the water has.


//////


/////


///// define
`bamboo_jungle`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>bamboo_jungle</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`basalt_deltas`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>basalt_deltas</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`beach`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>beach</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`birch_forest_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>birch_forest_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`birch_forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>birch_forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cherry_grove`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cherry_grove</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cold_beach`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cold_beach</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cold_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cold_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cold_taiga_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cold_taiga_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cold_taiga_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cold_taiga_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`cold_taiga`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>cold_taiga</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`crimson_forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>crimson_forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`deep_cold_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>deep_cold_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`deep_frozen_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>deep_frozen_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`deep_lukewarm_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>deep_lukewarm_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`deep_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>deep_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`deep_warm_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>deep_warm_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`default`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>default</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`desert_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>desert_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`desert`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>desert</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`extreme_hills_edge`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>extreme_hills_edge</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`extreme_hills_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>extreme_hills_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`extreme_hills_plus_trees_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>extreme_hills_plus_trees_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`extreme_hills_plus_trees`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>extreme_hills_plus_trees</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`extreme_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>extreme_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`flower_forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>flower_forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`forest_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>forest_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`frozen_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>frozen_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`frozen_river`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>frozen_river</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`hell`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>hell</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`ice_mountains`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>ice_mountains</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`ice_plains_spikes`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>ice_plains_spikes</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`ice_plains`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>ice_plains</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`jungle_edge`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>jungle_edge</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`jungle_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>jungle_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`jungle_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>jungle_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`jungle`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>jungle</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`lukewarm_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>lukewarm_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mangrove_swamp`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mangrove_swamp</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mega_spruce_taiga_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mega_spruce_taiga_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mega_spruce_taiga`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mega_spruce_taiga</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mega_taiga_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mega_taiga_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mega_taiga_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mega_taiga_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mega_taiga`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mega_taiga</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mesa_bryce`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mesa_bryce</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mesa_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mesa_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mesa_plateau_stone`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mesa_plateau_stone</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mesa_plateau`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mesa_plateau</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mesa`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mesa</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mushroom_island_shore`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mushroom_island_shore</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`mushroom_island`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>mushroom_island</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`plains`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>plains</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`river`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>river</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`roofed_forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>roofed_forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`savanna_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>savanna_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`savanna_plateau`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>savanna_plateau</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`savanna`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>savanna</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`soulsand_valley`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>soulsand_valley</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`stone_beach`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>stone_beach</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`sunflower_plains`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>sunflower_plains</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`swampland_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>swampland_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`swampland`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>swampland</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`taiga_hills`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>taiga_hills</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`taiga_mutated`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>taiga_mutated</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`taiga`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>taiga</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`the_end`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>the_end</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`warm_ocean`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>warm_ocean</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


///// define
`warped_forest`：<samp>object</samp>

- The specification of colors in a given biome.


/////

<div class="language-text highlight"><span class="filename"><code>warped_forest</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result

/////


////


///

