# Block Server Definition

> 文档版本：1.21.0.24

The minecraft block server definition file, defining a block's behavior.

## 架构

```mcschema
block:
{
  format_version "format_version"
  block "minecraft:block"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas.common.semver.format_version.json}


////

```mcschema
format_version:
number

```

//// html | div.result

////


```mcschema
format_version:
array
{
  integer "<any array element>" : opt
}

```

//// html | div.result
///// define
`<any array element>`：<samp>integer</samp>


/////


////


```mcschema
format_version:
string

```

//// html | div.result

////




//// define
`minecraft:block`：<samp>block</samp> {#assets.schemas.behavior.blocks.subschemas.minecraft_block.json}


////

```mcschema
block:
{
  object "description" : opt
  {
    string "identifier" : opt
    string "category" : opt
    object "menu_category" : opt
    {
      string "category" : opt
      string "group" : opt
      boolean "is_hidden_in_commands" : opt
    }
  }
  object "components" : opt
  {
    netease:tier "netease:tier"
    netease:aabb "netease:aabb"
    netease:face_directional "netease:face_directional"
    netease:fuel "netease:fuel"
    netease:render_layer "netease:render_layer"
    netease:solid "netease:solid"
    netease:pathable "netease:pathable"
    netease:block_entity "netease:block_entity"
    netease:fuel "netease:random_tick"
    netease:redstone_property "netease:redstone_property"
    netease:neighborchanged_sendto_script "netease:neighborchanged_sendto_script"
    netease:redstone "netease:redstone"
    netease:listen_block_remove "netease:listen_block_remove"
    netease:may_place_on "netease:may_place_on"
    netease:fire_resistant "netease:fire_resistant"
    netease:block_properties "netease:block_properties"
    netease:on_stand_on "netease:on_stand_on"
    netease:on_before_fall_on "netease:on_before_fall_on"
    netease:on_after_fall_on "netease:on_after_fall_on"
    netease:on_entity_inside "netease:on_entity_inside"
    netease:on_step_on "netease:on_step_on"
    netease:on_step_off "netease:on_step_off"
    netease:block_random_offset "netease:block_random_offset"
    netease:block_chest "netease:block_chest"
    netease:no_crop_face_block "netease:no_crop_face_block"
    netease:custom_tips "netease:custom_tips"
  }
  object "events" : opt
  {
     "<any object property>" : opt
  }
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The block description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>string</samp>

- The block identifier.


//////


////// define
`category`：<samp>string</samp>


//////


////// define
`menu_category`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>menu_category</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`category`：<samp>string</samp>


///////


/////// define
`group`：<samp>string</samp>


///////


/////// define
`is_hidden_in_commands`：<samp>boolean</samp>


///////


//////


/////


///// define
`components`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`netease:tier`：<samp>netease:tier</samp>

- [`netease:tier`](./components/netease_tier.md)组件。


//////

////// define
`netease:aabb`：<samp>netease:aabb</samp>

- [`netease:aabb`](./components/netease_aabb.md)组件。


//////

////// define
`netease:face_directional`：<samp>netease:face_directional</samp>

- [`netease:face_directional`](./components/netease_face_directional.md)组件。


//////

////// define
`netease:fuel`：<samp>netease:fuel</samp>

- [`netease:fuel`](./components/netease_fuel.md)组件。


//////

////// define
`netease:render_layer`：<samp>netease:render_layer</samp>

- [`netease:render_layer`](./components/netease_render_layer.md)组件。


//////

////// define
`netease:solid`：<samp>netease:solid</samp>

- [`netease:solid`](./components/netease_solid.md)组件。


//////

////// define
`netease:pathable`：<samp>netease:pathable</samp>

- [`netease:pathable`](./components/netease_pathable.md)组件。


//////

////// define
`netease:block_entity`：<samp>netease:block_entity</samp>

- [`netease:block_entity`](./components/netease_block_entity.md)组件。


//////

////// define
`netease:random_tick`：<samp>netease:fuel</samp>

- [`netease:random_tick`](./components/netease_random_tick.md)组件。


//////

////// define
`netease:redstone_property`：<samp>netease:redstone_property</samp>

- [`netease:redstone_property`](./components/netease_redstone_property.md)组件。


//////

////// define
`netease:neighborchanged_sendto_script`：<samp>netease:neighborchanged_sendto_script</samp>

- [`netease:neighborchanged_sendto_script`](./components/netease_neighborchanged_sendto_script.md)组件。


//////

////// define
`netease:redstone`：<samp>netease:redstone</samp>

- [`netease:redstone`](./components/netease_redstone.md)组件。


//////

////// define
`netease:listen_block_remove`：<samp>netease:listen_block_remove</samp>

- [`netease:listen_block_remove`](./components/netease_listen_block_remove.md)组件。


//////

////// define
`netease:may_place_on`：<samp>netease:may_place_on</samp>

- [`netease:may_place_on`](./components/netease_may_place_on.md)组件。


//////

////// define
`netease:fire_resistant`：<samp>netease:fire_resistant</samp>

- [`netease:fire_resistant`](./components/netease_fire_resistant.md)组件。


//////

////// define
`netease:block_properties`：<samp>netease:block_properties</samp>

- [`netease:block_properties`](./components/netease_block_properties.md)组件。


//////

////// define
`netease:on_stand_on`：<samp>netease:on_stand_on</samp>

- [`netease:on_stand_on`](./components/netease_on_stand_on.md)组件。


//////

////// define
`netease:on_before_fall_on`：<samp>netease:on_before_fall_on</samp>

- [`netease:on_before_fall_on`](./components/netease_on_before_fall_on.md)组件。


//////

////// define
`netease:on_after_fall_on`：<samp>netease:on_after_fall_on</samp>

- [`netease:on_after_fall_on`](./components/netease_on_after_fall_on.md)组件。


//////

////// define
`netease:on_entity_inside`：<samp>netease:on_entity_inside</samp>

- [`netease:on_entity_inside`](./components/netease_on_entity_inside.md)组件。


//////

////// define
`netease:on_step_on`：<samp>netease:on_step_on</samp>

- [`netease:on_step_on`](./components/netease_on_step_on.md)组件。


//////

////// define
`netease:on_step_off`：<samp>netease:on_step_off</samp>

- [`netease:on_step_off`](./components/netease_on_step_off.md)组件。


//////

////// define
`netease:block_random_offset`：<samp>netease:block_random_offset</samp>

- [`netease:block_random_offset`](./components/netease_block_random_offset.md)组件。


//////

////// define
`netease:block_chest`：<samp>netease:block_chest</samp>

- [`netease:block_chest`](./components/netease_block_chest.md)组件。


//////

////// define
`netease:no_crop_face_block`：<samp>netease:no_crop_face_block</samp>

- [`netease:no_crop_face_block`](./components/netease_no_crop_face_block.md)组件。


//////

////// define
`netease:custom_tips`：<samp>netease:custom_tips</samp>

- [`netease:custom_tips`](./components/netease_custom_tips.md)组件。


//////

/////


///// define
`events`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>events</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any object property>`


//////


/////


////



///

