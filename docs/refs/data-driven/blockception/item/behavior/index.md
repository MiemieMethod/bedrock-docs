# Item

> 文档版本：1.21.0.24

Minecraft items

## 架构

```mcschema
items:
{
  format_version "format_version"
  items "minecraft:item"
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
`minecraft:item`：<samp>items</samp> {#assets.schemas-blockception.behavior.items.format.minecraft.item.json}


////

```mcschema
items:
{
  object "description" : opt
  {
    identifier "identifier"
    boolean "is_experimental" : opt
    object "menu_category" : opt
    {
      item_group "group"
      creative_category "category"
      boolean "is_hidden_in_commands" : opt
    }
  }
  object "components" : opt
  {
    minecraft:allow_off_hand "minecraft:allow_off_hand"
    minecraft:block_placer "minecraft:block_placer"
    minecraft:can_destroy_in_creative "minecraft:can_destroy_in_creative"
    minecraft:cooldown "minecraft:cooldown"
    minecraft:damage "minecraft:damage"
    minecraft:digger "minecraft:digger"
    minecraft:display_name "minecraft:display_name"
    minecraft:durability "minecraft:durability"
    minecraft:enchantable "minecraft:enchantable"
    minecraft:entity_placer "minecraft:entity_placer"
    minecraft:food "minecraft:food"
    minecraft:fuel "minecraft:fuel"
    minecraft:foil "minecraft:glint"
    minecraft:hand_equipped "minecraft:hand_equipped"
    minecraft:icon "minecraft:icon"
    minecraft:liquid_clipped "minecraft:liquid_clipped"
    minecraft:max_stack_size "minecraft:max_stack_size"
    minecraft:projectile "minecraft:projectile"
    minecraft:record "minecraft:record"
    minecraft:repairable "minecraft:repairable"
    minecraft:shooter "minecraft:shooter"
    minecraft:should_despawn "minecraft:should_despawn"
    minecraft:stacked_by_data "minecraft:stacked_by_data"
    minecraft:tags "minecraft:tags"
    minecraft: "minecraft:throwable"
    minecraft:use_animation "minecraft:use_animation"
    minecraft:use_modifiers "minecraft:use_modifiers"
    minecraft:wearable "minecraft:wearable"
    object "<any object property>" : opt
    {
    }
  }
  events "events"
}

```

//// html | div.result
///// define
`description`：<samp>object</samp>

- The description for this item


/////

<div class="language-text highlight"><span class="filename"><code>description</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`identifier`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- The identifier for this item. The name must include a namespace and must not use the Minecraft namespace unless overriding a Vanilla item.


//////

```mcschema
identifier:
string

```

////// html | div.result

//////



////// define
`is_experimental`：<samp>boolean</samp>

- If this item is experimental, it will only be registered if the world is marked as experimental.


//////


////// define
`menu_category`：<samp>object</samp>

- The Creative Category that includes the specified item.


//////

<div class="language-text highlight"><span class="filename"><code>menu_category</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`group`：<samp>item_group</samp> {#assets.schemas-blockception.general.vanilla.item_group.json}


///////

```mcschema
item_group:
string

```

/////// html | div.result

///////



/////// define
`category`：<samp>creative_category</samp> {#assets.schemas-blockception.general.vanilla.creative_category.json}


///////

```mcschema
creative_category:
string

```

/////// html | div.result

///////



/////// define
`is_hidden_in_commands`：<samp>boolean</samp>

- Determines whether or not this item can be used with commands. Commands can use items by default


///////


//////


/////


///// define
`components`：<samp>object</samp>

- The components of this item.


/////

<div class="language-text highlight"><span class="filename"><code>components</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`minecraft:allow_off_hand`：<samp>minecraft:allow_off_hand</samp>

- [`minecraft:allow_off_hand`](./components/allow_off_hand.md)组件。The components of this item.


//////

////// define
`minecraft:block_placer`：<samp>minecraft:block_placer</samp>

- [`minecraft:block_placer`](./components/block_placer.md)组件。The components of this item.


//////

////// define
`minecraft:can_destroy_in_creative`：<samp>minecraft:can_destroy_in_creative</samp>

- [`minecraft:can_destroy_in_creative`](./components/can_destroy_in_creative.md)组件。The components of this item.


//////

////// define
`minecraft:cooldown`：<samp>minecraft:cooldown</samp>

- [`minecraft:cooldown`](./components/cooldown.md)组件。The components of this item.


//////

////// define
`minecraft:damage`：<samp>minecraft:damage</samp>

- [`minecraft:damage`](./components/damage.md)组件。The components of this item.


//////

////// define
`minecraft:digger`：<samp>minecraft:digger</samp>

- [`minecraft:digger`](./components/digger.md)组件。The components of this item.


//////

////// define
`minecraft:display_name`：<samp>minecraft:display_name</samp>

- [`minecraft:display_name`](./components/display_name.md)组件。The components of this item.


//////

////// define
`minecraft:durability`：<samp>minecraft:durability</samp>

- [`minecraft:durability`](./components/durability.md)组件。The components of this item.


//////

////// define
`minecraft:enchantable`：<samp>minecraft:enchantable</samp>

- [`minecraft:enchantable`](./components/enchantable.md)组件。The components of this item.


//////

////// define
`minecraft:entity_placer`：<samp>minecraft:entity_placer</samp>

- [`minecraft:entity_placer`](./components/entity_placer.md)组件。The components of this item.


//////

////// define
`minecraft:food`：<samp>minecraft:food</samp>

- [`minecraft:food`](./components/food.md)组件。The components of this item.


//////

////// define
`minecraft:fuel`：<samp>minecraft:fuel</samp>

- [`minecraft:fuel`](./components/fuel.md)组件。The components of this item.


//////

////// define
`minecraft:glint`：<samp>minecraft:foil</samp>

- [`minecraft:glint`](./components/glint.md)组件。The components of this item.


//////

////// define
`minecraft:hand_equipped`：<samp>minecraft:hand_equipped</samp>

- [`minecraft:hand_equipped`](./components/hand_equipped.md)组件。The components of this item.


//////

////// define
`minecraft:icon`：<samp>minecraft:icon</samp>

- [`minecraft:icon`](./components/icon.md)组件。The components of this item.


//////

////// define
`minecraft:liquid_clipped`：<samp>minecraft:liquid_clipped</samp>

- [`minecraft:liquid_clipped`](./components/liquid_clipped.md)组件。The components of this item.


//////

////// define
`minecraft:max_stack_size`：<samp>minecraft:max_stack_size</samp>

- [`minecraft:max_stack_size`](./components/max_stack_size.md)组件。The components of this item.


//////

////// define
`minecraft:projectile`：<samp>minecraft:projectile</samp>

- [`minecraft:projectile`](./components/projectile.md)组件。The components of this item.


//////

////// define
`minecraft:record`：<samp>minecraft:record</samp>

- [`minecraft:record`](./components/record.md)组件。The components of this item.


//////

////// define
`minecraft:repairable`：<samp>minecraft:repairable</samp>

- [`minecraft:repairable`](./components/repairable.md)组件。The components of this item.


//////

////// define
`minecraft:shooter`：<samp>minecraft:shooter</samp>

- [`minecraft:shooter`](./components/shooter.md)组件。The components of this item.


//////

////// define
`minecraft:should_despawn`：<samp>minecraft:should_despawn</samp>

- [`minecraft:should_despawn`](./components/should_despawn.md)组件。The components of this item.


//////

////// define
`minecraft:stacked_by_data`：<samp>minecraft:stacked_by_data</samp>

- [`minecraft:stacked_by_data`](./components/stacked_by_data.md)组件。The components of this item.


//////

////// define
`minecraft:tags`：<samp>minecraft:tags</samp>

- [`minecraft:tags`](./components/tags.md)组件。The components of this item.


//////

////// define
`minecraft:throwable`：<samp>minecraft:</samp>

- [`minecraft:throwable`](./components/throwable.md)组件。The components of this item.


//////

////// define
`minecraft:use_animation`：<samp>minecraft:use_animation</samp>

- [`minecraft:use_animation`](./components/use_animation.md)组件。The components of this item.


//////

////// define
`minecraft:use_modifiers`：<samp>minecraft:use_modifiers</samp>

- [`minecraft:use_modifiers`](./components/use_modifiers.md)组件。The components of this item.


//////

////// define
`minecraft:wearable`：<samp>minecraft:wearable</samp>

- [`minecraft:wearable`](./components/wearable.md)组件。The components of this item.


//////

////// define
`<any object property>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////


///// define
`events`：<samp>events</samp> {#assets.schemas-blockception.behavior.items.format.events.json}


/////

```mcschema
events:
{
  object "on_consume" : opt
  {
    array "sequence" : opt
    {
      object "<any array element>" : opt
      {
      }
    }
    array "randomize" : opt
    {
      object "<any array element>" : opt
      {
      }
    }
    object "run_command" : opt
    {
      array "command" : opt
      {
        string "<any array element>" : opt
      }
      string "target" : opt
    }
  }
  object "<any object property>" : opt
  {
  }
}

```

///// html | div.result
////// define
`on_consume`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>on_consume</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`sequence`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>sequence</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`randomize`：<samp>array</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>randomize</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result

////////


///////


/////// define
`run_command`：<samp>object</samp>

- UNDOCUMENTED.


///////

<div class="language-text highlight"><span class="filename"><code>run_command</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`command`：<samp>array</samp>

- UNDOCUMENTED.


////////

<div class="language-text highlight"><span class="filename"><code>command</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any array element>`：<samp>string</samp>

- UNDOCUMENTED.


/////////


////////


//////// define
`target`：<samp>string</samp>

- UNDOCUMENTED.


////////


///////


//////


////// define
`<any object property>`：<samp>object</samp>

- UNDOCUMENTED.


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result

//////


/////



////



///

