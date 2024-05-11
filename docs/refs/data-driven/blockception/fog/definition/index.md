# Fog

> 文档版本：1.21.0.24

UNDOCUMENTED.

## 架构

```mcschema
fog:
{
  format_version "format_version"
  object "minecraft:fog_settings" : opt
  {
    object "description" : opt
    {
      identifier "identifier"
    }
    object "distance" : opt
    {
      object "air" : opt
      {
        number "fog_start" : opt
        number "fog_end" : opt
        string "fog_color" : opt
        string "render_distance_type" : opt
        object "transition_fog" : opt
        {
          object "init_fog" : opt
          {
            string "fog_color" : opt
            number "fog_start" : opt
            number "fog_end" : opt
            string "render_distance_type" : opt
          }
          number "min_percent" : opt
          number "mid_seconds" : opt
          number "mid_percent" : opt
          number "max_seconds" : opt
        }
      }
      object "weather" : opt
      {
      }
      object "water" : opt
      {
      }
      object "lava" : opt
      {
      }
      object "lava_resistance" : opt
      {
      }
      object "powder_snow" : opt
      {
      }
    }
    object "volumetric" : opt
    {
      object "density" : opt
      {
        object "air" : opt
        {
          number "max_density" : opt
          number "max_density_height" : opt
          number "zero_density_height" : opt
          boolean "uniform" : opt
        }
        object "water" : opt
        {
        }
        object "lava" : opt
        {
        }
        object "lava_resistance" : opt
        {
        }
      }
      object "media_coefficients" : opt
      {
        object "air" : opt
        {
          array "absorption" : opt
          {
            number "0..0" : opt
            number "1..1" : opt
            number "2..2" : opt
          }
          string "absorption" : opt
           "scattering" : opt
        }
        object "water" : opt
        {
        }
        object "cloud" : opt
        {
        }
      }
    }
  }
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
`minecraft:fog_settings`：<samp>object</samp>

- The definition of a single fog.


////

<div class="language-text highlight"><span class="filename"><code>minecraft:fog_settings</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`description`：<samp>object</samp>

- The identifying description of this fog settings.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.fog.identifier.json}

- The identifier for these fog settings. The identifier must include a namespace.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



/////


///// define
`distance`：<samp>object</samp>

- The distance fog settings for different camera locations.


/////

<div class="language-text highlight"><span class="filename"><code>distance</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`air`：<samp>object</samp>

- The fog settings when the camera is in the air.


//////

<div class="language-text highlight"><span class="filename"><code>air</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`fog_start`：<samp>number</samp>

- The distance from the player that the fog will begin to appear. 'fog_start' must be less than or equal to 'fog_end'.


///////


/////// define
`fog_end`：<samp>number</samp>

- The distance from the player that the fog will become fully opaque. 'fog_end' must be greater than or equal to 'fog_start'.


///////


/////// define
`fog_color`：<samp>string</samp>

- The color that the fog will take on.


///////


/////// define
`render_distance_type`：<samp>string</samp>

- Determines how distance value is used. Fixed distance is measured in blocks. Dynamic distance is multiplied by the current render distance.


///////


/////// define
`transition_fog`：<samp>object</samp>

- Additional fog data which will slowly transition to the distance fog of current biome.


///////

<div class="language-text highlight"><span class="filename"><code>transition_fog</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`init_fog`：<samp>object</samp>

- Initial fog that will slowly transition into water distance fog of the biome when player goes into water.


////////

<div class="language-text highlight"><span class="filename"><code>init_fog</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`fog_color`：<samp>string</samp>

- The color that the fog will take on.


/////////


///////// define
`fog_start`：<samp>number</samp>

- The distance from the player that the fog will begin to appear. 'fog_start' must be less than or equal to 'fog_end'.


/////////


///////// define
`fog_end`：<samp>number</samp>

- The distance from the player that the fog will become fully opaque. 'fog_end' must be greater than or equal to 'fog_start'.


/////////


///////// define
`render_distance_type`：<samp>string</samp>

- Determines how distance value is used. Fixed distance is measured in blocks. Dynamic distance is multiplied by the current render distance.


/////////


////////


//////// define
`min_percent`：<samp>number</samp>

- The minimum progress of fog transition.


////////


//////// define
`mid_seconds`：<samp>number</samp>

- The time takes to reach certain progress('mid_percent') of fog transition.


////////


//////// define
`mid_percent`：<samp>number</samp>

- The progress of fog transition after 'mid_seconds' seconds.


////////


//////// define
`max_seconds`：<samp>number</samp>

- Total amount of time takes to complete fog transition.


////////


///////


//////


////// define
`weather`：<samp>object</samp>

-  The fog settings for when the camera is in the air with active weather (rain, snow, etc..).


//////

<div class="language-text highlight"><span class="filename"><code>weather</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`water`：<samp>object</samp>

- The fog settings when the camera is in water.


//////

<div class="language-text highlight"><span class="filename"><code>water</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`lava`：<samp>object</samp>

- The fog settings when the camera is in lava.


//////

<div class="language-text highlight"><span class="filename"><code>lava</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`lava_resistance`：<samp>object</samp>

- The fog settings when the camera is in lava and the player has the lava resistance effect active.


//////

<div class="language-text highlight"><span class="filename"><code>lava_resistance</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`powder_snow`：<samp>object</samp>

- The fog settings when the camera is inside a Powder Snow block.


//////

<div class="language-text highlight"><span class="filename"><code>powder_snow</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`volumetric`：<samp>object</samp>

- The volumetric fog settings.


/////

<div class="language-text highlight"><span class="filename"><code>volumetric</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`density`：<samp>object</samp>

- The density settings for different camera locations.


//////

<div class="language-text highlight"><span class="filename"><code>density</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`air`：<samp>object</samp>

- Fog density values as light passes through air blocks.


///////

<div class="language-text highlight"><span class="filename"><code>air</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`max_density`：<samp>number</samp>

- The maximum amount of opaqueness that the ground fog will take on. A value from [0.0, 1.0].


////////


//////// define
`max_density_height`：<samp>number</samp>

- The height in blocks that the ground fog will become it's maximum density.


////////


//////// define
`zero_density_height`：<samp>number</samp>

- The height in blocks that the ground fog will be completely transparent and begin to appear. This value needs to be at least 1 higher than `max_density_height`.


////////


//////// define
`uniform`：<samp>boolean</samp>

- When set to true, the density will be uniform across all heights.


////////


///////


/////// define
`water`：<samp>object</samp>

- Fog density values as light passes through water blocks.


///////

<div class="language-text highlight"><span class="filename"><code>water</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


/////// define
`lava`：<samp>object</samp>

- Fog density values as light passes through lava blocks.


///////

<div class="language-text highlight"><span class="filename"><code>lava</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


/////// define
`lava_resistance`：<samp>object</samp>

- Fog density values as light passes through lava blocks while the player has lava resistance.


///////

<div class="language-text highlight"><span class="filename"><code>lava_resistance</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


////// define
`media_coefficients`：<samp>object</samp>

- The coefficient settings for the volumetric fog in different blocks.


//////

<div class="language-text highlight"><span class="filename"><code>media_coefficients</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`air`：<samp>object</samp>

- Fog coefficient values while light passes through air.


///////

<div class="language-text highlight"><span class="filename"><code>air</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`absorption`：<samp>array</samp>

- Proportion of light that is absorbed (lost) per block.


////////

<div class="language-text highlight"><span class="filename"><code>absorption</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`0..0`：<samp>number</samp>


/////////


///////// define
`1..1`：<samp>number</samp>


/////////


///////// define
`2..2`：<samp>number</samp>


/////////


////////


//////// define
`absorption`：<samp>string</samp>

- Proportion of light that is absorbed (lost) per block.


////////



//////// define
`scattering`

- Proportion of light that is scattered per block.


////////


///////


/////// define
`water`：<samp>object</samp>

- Fog coefficient values while light passes through water.


///////

<div class="language-text highlight"><span class="filename"><code>water</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


/////// define
`cloud`：<samp>object</samp>

- Fog coefficient values while light passes through clouds.


///////

<div class="language-text highlight"><span class="filename"><code>cloud</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


////


///

