# Material Instances

> 文档版本：1.21.0.24

The material instances for a block. Maps face or material_instance names in a geometry file to an actual material instance. You can assign a material instance object to any of these faces: "up", "down", "north", "south", "east", "west", or "*". You can also give an instance the name of your choosing such as "my_instance", and then assign it to a face by doing "north":"my_instance".

## 架构

```mcschema
material_instances:
{
  string "<any object property>" : opt
  object "<any object property>" : opt
  {
    boolean "ambient_occlusion" : opt
    boolean "face_dimming" : opt
    string "render_method" : opt
    string "texture" : opt
  }
}

```

/// html | div.result
//// define
`<any object property>`：<samp>string</samp>

- The material instance for a block. Maps face or material_instance names in a geometry file to an actual material instance. You can assign a material instance object to any of these faces: "up", "down", "north", "south", "east", "west", or "*". You can also give an instance the name of your choosing such as "my_instance", and then assign it to a face by doing "north":"my_instance".


////


//// define
`<any object property>`：<samp>object</samp>

- The material instance for a block. Maps face or material_instance names in a geometry file to an actual material instance. You can assign a material instance object to any of these faces: "up", "down", "north", "south", "east", "west", or "*". You can also give an instance the name of your choosing such as "my_instance", and then assign it to a face by doing "north":"my_instance".


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`ambient_occlusion`：<samp>boolean</samp>

- Should this material have ambient occlusion applied when lighting? If true, shadows will be created around and underneath the block.


/////


///// define
`face_dimming`：<samp>boolean</samp>

- Should this material be dimmed by the direction it's facing?


/////


///// define
`render_method`：<samp>string</samp>

- The render method to use. Must be one of these options: opaque - Used for a regular block texture without an alpha layer. Does not allow for transparency or translucency. double_sided - Used for completely disabling backface culling. blend - Used for a block like stained glass. Allows for transparency and translucency (slightly transparent textures). alpha_test - Used for a block like the vanilla (unstained) glass. Does not allow for translucency, only fully opaque or fully transparent textures. Also disables backface culling.


/////


///// define
`texture`：<samp>string</samp>

- Texture name for the material.


/////


////



///

