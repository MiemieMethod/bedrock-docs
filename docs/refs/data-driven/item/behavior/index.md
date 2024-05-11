# Item Server Definition

> 文档版本：1.21.0.24

The minecraft item server definition file, defining a item's behavior.

## 架构

```mcschema
item:
{
  format_version "format_version"
  minecraft:item "minecraft:item"
}

```

/// html | div.result
//// define
`format_version`：<samp>format_version</samp> {#assets.schemas.common.semver.format_version_no_number.json}


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
`minecraft:item`：<samp>minecraft:item</samp> {#assets.schemas.behavior.items.subschemas.minecraft_item.json}


////

```mcschema
minecraft:item:
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
    string "custom_item_type" : opt
    boolean "register_to_create_menu" : opt
  }
  object "components" : opt
  {
    minecraft:max_damage "minecraft:max_damage"
    minecraft:seed "minecraft:seed"
    minecraft:camera "minecraft:camera"
    minecraft:block "minecraft:block"
    minecraft:can_destroy_in_creative "minecraft:can_destroy_in_creative"
    minecraft:max_stack_size "minecraft:max_stack_size"
    minecraft:hover_text_color "minecraft:hover_text_color"
    minecraft:stacked_by_data "minecraft:stacked_by_data"
    minecraft:hand_equipped "minecraft:hand_equipped"
    minecraft:liquid_clipped "minecraft:liquid_clipped"
    minecraft:allow_off_hand "minecraft:allow_off_hand"
    minecraft:damage "minecraft:damage"
    minecraft:should_despawn "minecraft:should_despawn"
    minecraft:use_animation "minecraft:use_animation"
    minecraft:use_duration "minecraft:use_duration"
    minecraft:use_modifiers "minecraft:use_modifiers"
    minecraft:foil "minecraft:foil"
    minecraft:mining_speed "minecraft:mining_speed"
    minecraft:enchantable "minecraft:enchantable"
    minecraft:frame_count "minecraft:frame_count"
    minecraft:creative_category "minecraft:creative_category"
    minecraft:render_offsets "minecraft:render_offsets"
    minecraft:glint "minecraft:glint"
    minecraft:interact_button "minecraft:interact_button"
    minecraft:icon "minecraft:icon"
    minecraft:armor "minecraft:armor"
    minecraft:item_storage "minecraft:item_storage"
    minecraft:chargeable "minecraft:chargeable"
    minecraft:cooldown "minecraft:cooldown"
    minecraft:durability "minecraft:durability"
    minecraft:digger "minecraft:digger"
    minecraft:display_name "minecraft:display_name"
    minecraft:entity_placer "minecraft:entity_placer"
    minecraft:food "minecraft:food"
    minecraft:fuel "minecraft:fuel"
    minecraft:on_use "minecraft:on_use"
    minecraft:on_use_on "minecraft:on_use_on"
    minecraft:block_placer "minecraft:block_placer"
    minecraft:projectile "minecraft:projectile"
    minecraft:repairable "minecraft:repairable"
    minecraft:shooter "minecraft:shooter"
    minecraft:throwable "minecraft:throwable"
    minecraft:weapon "minecraft:weapon"
    minecraft:wearable "minecraft:wearable"
    minecraft:record "minecraft:record"
    minecraft:custom_components "minecraft:custom_components"
    minecraft:tags "minecraft:tags"
    netease:show_in_hand "netease:show_in_hand"
    netease:fire_resistant "netease:fire_resistant"
    netease:allow_offhand "netease:allow_offhand"
    netease:enchant_material "netease:enchant_material"
    netease:fuel "netease:fuel"
    netease:cooldown "netease:cooldown"
    netease:customtips "netease:customtips"
    object "^tag:[a-zA-Z0-9_.:-]+$" : opt
    {
    }
    object "^[a-zA-Z0-9_.:-]+$" : opt
    {
    }
  }
  object "events" : opt
  {
     "on_fertilized" : opt
    definition_event "on_tool_used"
    definition_event "<any object property>"
  }
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The item description.


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>string</samp>

- The item identifier.


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


////// define
`custom_item_type`：<samp>string</samp>

- 我的世界中国版自定义物品类别，请勿在国际版上使用。


//////


////// define
`register_to_create_menu`：<samp>boolean</samp>

- 是否注册到创造栏。我的世界中国版自定义物品注册属性，请勿在国际版上使用。


//////


/////


///// define
`components`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:max_damage`：<samp>minecraft:max_damage</samp>

- [`minecraft:max_damage`](./components/minecraft_max_damage.md)组件。


//////

////// define
`minecraft:seed`：<samp>minecraft:seed</samp>

- [`minecraft:seed`](./components/minecraft_seed.md)组件。


//////

////// define
`minecraft:camera`：<samp>minecraft:camera</samp>

- [`minecraft:camera`](./components/minecraft_camera.md)组件。


//////

////// define
`minecraft:block`：<samp>minecraft:block</samp>

- [`minecraft:block`](./components/minecraft_block.md)组件。


//////

////// define
`minecraft:can_destroy_in_creative`：<samp>minecraft:can_destroy_in_creative</samp>

- [`minecraft:can_destroy_in_creative`](./components/minecraft_can_destroy_in_creative.md)组件。


//////

////// define
`minecraft:max_stack_size`：<samp>minecraft:max_stack_size</samp>

- [`minecraft:max_stack_size`](./components/minecraft_max_stack_size.md)组件。


//////

////// define
`minecraft:hover_text_color`：<samp>minecraft:hover_text_color</samp>

- [`minecraft:hover_text_color`](./components/minecraft_hover_text_color.md)组件。


//////

////// define
`minecraft:stacked_by_data`：<samp>minecraft:stacked_by_data</samp>

- [`minecraft:stacked_by_data`](./components/minecraft_stacked_by_data.md)组件。


//////

////// define
`minecraft:hand_equipped`：<samp>minecraft:hand_equipped</samp>

- [`minecraft:hand_equipped`](./components/minecraft_hand_equipped.md)组件。


//////

////// define
`minecraft:liquid_clipped`：<samp>minecraft:liquid_clipped</samp>

- [`minecraft:liquid_clipped`](./components/minecraft_liquid_clipped.md)组件。


//////

////// define
`minecraft:allow_off_hand`：<samp>minecraft:allow_off_hand</samp>

- [`minecraft:allow_off_hand`](./components/minecraft_allow_off_hand.md)组件。


//////

////// define
`minecraft:damage`：<samp>minecraft:damage</samp>

- [`minecraft:damage`](./components/minecraft_damage.md)组件。


//////

////// define
`minecraft:should_despawn`：<samp>minecraft:should_despawn</samp>

- [`minecraft:should_despawn`](./components/minecraft_should_despawn.md)组件。


//////

////// define
`minecraft:use_animation`：<samp>minecraft:use_animation</samp>

- [`minecraft:use_animation`](./components/minecraft_use_animation.md)组件。


//////

////// define
`minecraft:use_duration`：<samp>minecraft:use_duration</samp>

- [`minecraft:use_duration`](./components/minecraft_use_duration.md)组件。


//////

////// define
`minecraft:use_modifiers`：<samp>minecraft:use_modifiers</samp>

- [`minecraft:use_modifiers`](./components/minecraft_use_modifiers.md)组件。


//////

////// define
`minecraft:foil`：<samp>minecraft:foil</samp>

- [`minecraft:foil`](./components/minecraft_foil.md)组件。


//////

////// define
`minecraft:mining_speed`：<samp>minecraft:mining_speed</samp>

- [`minecraft:mining_speed`](./components/minecraft_mining_speed.md)组件。


//////

////// define
`minecraft:enchantable`：<samp>minecraft:enchantable</samp>

- [`minecraft:enchantable`](./components/minecraft_enchantable.md)组件。


//////

////// define
`minecraft:frame_count`：<samp>minecraft:frame_count</samp>

- [`minecraft:frame_count`](./components/minecraft_frame_count.md)组件。


//////

////// define
`minecraft:creative_category`：<samp>minecraft:creative_category</samp>

- [`minecraft:creative_category`](./components/minecraft_creative_category.md)组件。


//////

////// define
`minecraft:render_offsets`：<samp>minecraft:render_offsets</samp>

- [`minecraft:render_offsets`](./components/minecraft_render_offsets.md)组件。


//////

////// define
`minecraft:glint`：<samp>minecraft:glint</samp>

- [`minecraft:glint`](./components/minecraft_glint.md)组件。


//////

////// define
`minecraft:interact_button`：<samp>minecraft:interact_button</samp>

- [`minecraft:interact_button`](./components/minecraft_interact_button.md)组件。


//////

////// define
`minecraft:icon`：<samp>minecraft:icon</samp>

- [`minecraft:icon`](./components/minecraft_icon.md)组件。


//////

////// define
`minecraft:armor`：<samp>minecraft:armor</samp>

- [`minecraft:armor`](./components/minecraft_armor.md)组件。


//////

////// define
`minecraft:item_storage`：<samp>minecraft:item_storage</samp>

- [`minecraft:item_storage`](./components/minecraft_item_storage.md)组件。


//////

////// define
`minecraft:chargeable`：<samp>minecraft:chargeable</samp>

- [`minecraft:chargeable`](./components/minecraft_chargeable.md)组件。


//////

////// define
`minecraft:cooldown`：<samp>minecraft:cooldown</samp>

- [`minecraft:cooldown`](./components/minecraft_cooldown.md)组件。


//////

////// define
`minecraft:durability`：<samp>minecraft:durability</samp>

- [`minecraft:durability`](./components/minecraft_durability.md)组件。


//////

////// define
`minecraft:digger`：<samp>minecraft:digger</samp>

- [`minecraft:digger`](./components/minecraft_digger.md)组件。


//////

////// define
`minecraft:display_name`：<samp>minecraft:display_name</samp>

- [`minecraft:display_name`](./components/minecraft_display_name.md)组件。


//////

////// define
`minecraft:entity_placer`：<samp>minecraft:entity_placer</samp>

- [`minecraft:entity_placer`](./components/minecraft_entity_placer.md)组件。


//////

////// define
`minecraft:food`：<samp>minecraft:food</samp>

- [`minecraft:food`](./components/minecraft_food.md)组件。


//////

////// define
`minecraft:fuel`：<samp>minecraft:fuel</samp>

- [`minecraft:fuel`](./components/minecraft_fuel.md)组件。


//////

////// define
`minecraft:on_use`：<samp>minecraft:on_use</samp>

- [`minecraft:on_use`](./components/minecraft_on_use.md)组件。


//////

////// define
`minecraft:on_use_on`：<samp>minecraft:on_use_on</samp>

- [`minecraft:on_use_on`](./components/minecraft_on_use_on.md)组件。


//////

////// define
`minecraft:block_placer`：<samp>minecraft:block_placer</samp>

- [`minecraft:block_placer`](./components/minecraft_block_placer.md)组件。


//////

////// define
`minecraft:projectile`：<samp>minecraft:projectile</samp>

- [`minecraft:projectile`](./components/minecraft_projectile.md)组件。


//////

////// define
`minecraft:repairable`：<samp>minecraft:repairable</samp>

- [`minecraft:repairable`](./components/minecraft_repairable.md)组件。


//////

////// define
`minecraft:shooter`：<samp>minecraft:shooter</samp>

- [`minecraft:shooter`](./components/minecraft_shooter.md)组件。


//////

////// define
`minecraft:throwable`：<samp>minecraft:throwable</samp>

- [`minecraft:throwable`](./components/minecraft_throwable.md)组件。


//////

////// define
`minecraft:weapon`：<samp>minecraft:weapon</samp>

- [`minecraft:weapon`](./components/minecraft_weapon.md)组件。


//////

////// define
`minecraft:wearable`：<samp>minecraft:wearable</samp>

- [`minecraft:wearable`](./components/minecraft_wearable.md)组件。


//////

////// define
`minecraft:record`：<samp>minecraft:record</samp>

- [`minecraft:record`](./components/minecraft_record.md)组件。


//////

////// define
`minecraft:custom_components`：<samp>minecraft:custom_components</samp>

- [`minecraft:custom_components`](./components/minecraft_custom_components.md)组件。


//////

////// define
`minecraft:tags`：<samp>minecraft:tags</samp>

- [`minecraft:tags`](./components/minecraft_tags.md)组件。


//////

////// define
`netease:show_in_hand`：<samp>netease:show_in_hand</samp>

- [`netease:show_in_hand`](./components/netease_show_in_hand.md)组件。


//////

////// define
`netease:fire_resistant`：<samp>netease:fire_resistant</samp>

- [`netease:fire_resistant`](./components/netease_fire_resistant.md)组件。


//////

////// define
`netease:allow_offhand`：<samp>netease:allow_offhand</samp>

- [`netease:allow_offhand`](./components/netease_allow_offhand.md)组件。


//////

////// define
`netease:enchant_material`：<samp>netease:enchant_material</samp>

- [`netease:enchant_material`](./components/netease_enchant_material.md)组件。


//////

////// define
`netease:fuel`：<samp>netease:fuel</samp>

- [`netease:fuel`](./components/netease_fuel.md)组件。


//////

////// define
`netease:cooldown`：<samp>netease:cooldown</samp>

- [`netease:cooldown`](./components/netease_cooldown.md)组件。


//////

////// define
`netease:customtips`：<samp>netease:customtips</samp>

- [`netease:customtips`](./components/netease_customtips.md)组件。


//////

////// define
`^tag:[a-zA-Z0-9_.:-]+$`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>^tag:[a-zA-Z0-9_.:-]+$</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


////// define
`^[a-zA-Z0-9_.:-]+$`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>^[a-zA-Z0-9_.:-]+$</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`events`：<samp>object</samp>


/////

<div class="language-text highlight"><span class="filename"><code>events</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`on_fertilized`


//////


////// define
`on_tool_used`：<samp>definition_event</samp> {#assets.schemas.common.definition.definition_event.json}


//////

```mcschema
definition_event:
{
  number "weight" : opt
  expression_node_no_version "condition"
  array "randomize" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  array "sequence" : opt
  {
    object "<any array element>" : opt
    {
    }
  }
  definition_trigger_no_condition "trigger"
}

```

////// html | div.result
/////// define
`weight`：<samp>number</samp>


///////


/////// define
`condition`：<samp>expression_node_no_version</samp> {#assets.schemas.common.molang.expression_node_no_version.json}


///////

```mcschema
expression_node_no_version:
string

```

/////// html | div.result

///////


```mcschema
expression_node_no_version:
boolean

```

/////// html | div.result

///////


```mcschema
expression_node_no_version:
number

```

/////// html | div.result

///////




/////// define
`randomize`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`sequence`：<samp>array</samp>


///////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`trigger`：<samp>definition_trigger_no_condition</samp> {#assets.schemas.common.definition.definition_trigger_no_condition.json}


///////

```mcschema
definition_trigger_no_condition:
string

```

/////// html | div.result

///////


```mcschema
definition_trigger_no_condition:
{
  string "event" : opt
  string "target" : opt
}

```

/////// html | div.result
//////// define
`event`：<samp>string</samp>


////////


//////// define
`target`：<samp>string</samp>


////////


///////




//////



////// define
`<any object property>`：<samp>[definition_event](#assets.schemas.common.definition.definition_event.json)</samp>


//////


/////


////



///

