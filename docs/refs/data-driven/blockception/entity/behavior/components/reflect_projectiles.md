# Reflect Projectiles

> 文档版本：1.21.50.25

[EXPERIMENTAL] Allows an entity to reflect projectiles.

## 架构

```mcschema
reflect_projectiles:
{
  string "azimuth_angle" : opt
  number "azimuth_angle" : opt
  string "elevation_angle" : opt
  number "elevation_angle" : opt
  array "reflected_projectiles" : opt
  {
    string "<any array element>" : opt
  }
  string "reflection_scale" : opt
  number "reflection_scale" : opt
  string "reflection_sound" : opt
}

```

/// html | div.result
//// define
`azimuth_angle`：<samp>string</samp>

- A Molang expression defining the angle in degrees to add to the projectile's y axis rotation.


////


//// define
`azimuth_angle`：<samp>number</samp>

- A Molang expression defining the angle in degrees to add to the projectile's y axis rotation.


////



//// define
`elevation_angle`：<samp>string</samp>

- A Molang expression defining the angle in degrees to add to the projectile's x axis rotation.


////


//// define
`elevation_angle`：<samp>number</samp>

- A Molang expression defining the angle in degrees to add to the projectile's x axis rotation.


////



//// define
`reflected_projectiles`：<samp>array</samp>

- An array of strings defining the types of projectiles that are reflected when they hit the entity.


////

<div class="language-text highlight"><span class="filename"><code>reflected_projectiles</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`<any array element>`：<samp>string</samp>


/////


////


//// define
`reflection_scale`：<samp>string</samp>

- A Molang expression defining the velocity scaling of the reflected projectile. Values below 1 decrease the projectile's velocity, and values above 1 increase it.


////


//// define
`reflection_scale`：<samp>number</samp>

- A Molang expression defining the velocity scaling of the reflected projectile. Values below 1 decrease the projectile's velocity, and values above 1 increase it.


////



//// define
`reflection_sound`：<samp>string</samp>

- A string defining the name of the sound event to be played when a projectile is reflected. "reflect" unless specified.


////


///

