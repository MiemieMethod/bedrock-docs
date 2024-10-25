# 未命名

> 文档版本：1.21.0.24

The material instances for a block. Maps face or material_instance names in a geometry file to an actual material instance. You can assign a material instance object to any of these faces: "up", "down", "north", "south", "east", "west", or "*". You can also give an instance the name of your choosing such as "my_instance", and then assign it to a face by doing "north":"my_instance".

## 架构

```mcschema
minecraft:material_instances:
{
  object "^(?:\*[a-zA-Z0-9_]*|[a-zA-Z0-9_]*\*|\*|[a-zA-Z0-9_]+)$" : opt
  {
    string "textures" : opt
    boolean "ambient_occlusion" : opt
    boolean "face_dimming" : opt
    string "render_method" : opt
  }
  string "^(?:\*[a-zA-Z0-9_]*|[a-zA-Z0-9_]*\*|\*|[a-zA-Z0-9_]+)$" : opt
}

```

/// html | div.result
//// define
`^(?:\*[a-zA-Z0-9_]*|[a-zA-Z0-9_]*\*|\*|[a-zA-Z0-9_]+)$`：<samp>object</samp>


////

<div class="language-text highlight"><span class="filename"><code>^(?:\*[a-zA-Z0-9_]*|[a-zA-Z0-9_]*\*|\*|[a-zA-Z0-9_]+)$</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`textures`：<samp>string</samp>

- Texture name for the material.


/////


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


////


//// define
`^(?:\*[a-zA-Z0-9_]*|[a-zA-Z0-9_]*\*|\*|[a-zA-Z0-9_]+)$`：<samp>string</samp>


////



///


