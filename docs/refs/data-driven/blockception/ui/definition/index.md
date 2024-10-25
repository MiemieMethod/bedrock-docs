# Minecraft JSON UI

> 文档版本：1.21.50.25



## 架构

```mcschema
minecraft_json_ui:
{
  string "namespace" : opt
  object "<any object property>" : opt
  {
    array "controls" : opt
    {
      object "<any array element>" : opt
      {
        object "<any object property>" : opt
        {
        }
      }
    }
    controls "controls"
    array "modifications" : opt
    {
      object "<any array element>" : opt
      {
        string "control_name" : opt
        string "array_name" : opt
        string "operation" : opt
        bindings "where"
        bindings "target"
        string "target_control" : opt
        bindings "value"
        array "value" : opt
        {
          object "<any array element>" : opt
          {
            object "<any object property>" : opt
            {
            }
          }
        }
        value "value"
      }
    }
    allow_clipping "allow_clipping"
    allow_debug_missing_texture "allow_debug_missing_texture"
    allow_scroll_even_when_content_fits "allow_scroll_even_when_content_fits"
    alpha "alpha"
    always_handle_pointer "always_handle_pointer"
    always_handle_scrolling "always_handle_scrolling"
    always_listen_to_input "always_listen_to_input"
    always_rotate "always_rotate"
    anchor_from "anchor_from"
    anchor_to "anchor_to"
    animations "anims"
    background_control "background_control"
    background_hover_control "background_hover_control"
    backup_font_type "backup_font_type"
    bilinear "bilinear"
    bindings "bindings"
    button_mappings "button_mappings"
    cache_screen "cache_screen"
    checked_control "checked_control"
    checked_hover_control "checked_hover_control"
    checked_locked_control "checked_locked_control"
    checked_locked_hover_control "checked_locked_hover_control"
    clip_direction "clip_direction"
    clip_pixel_perfect "clip_pixelperfect"
    clips_children "clips_children"
    close_on_player_hurt "close_on_player_hurt"
    collection_index "collection_index"
    collection_name "collection_name"
    color "color"
    consume_hover_events "consume_hover_events"
    contained "contained"
    control_name "control_name"
    default_control "default_control"
    default_focus_precedence "default_focus_precedence"
    disable_anim_fast_forward "disable_anim_fast_forward"
    draggable "draggable"
    dropdown_area "dropdown_area"
    dropdown_content_control "dropdown_content_control"
    dropdown_name "dropdown_name"
    enable_directional_toggling "enable_directional_toggling"
    enable_profanity_filter "enable_profanity_filter"
    enabled_newline "enabled_newline"
    enabled "enabled"
    factory "factory"
    fill "fill"
    focus_change_down "focus_change_down"
    focus_change_left "focus_change_left"
    focus_change_right "focus_change_right"
    focus_change_up "focus_change_up"
    focus_container "focus_container"
    focus_enabled "focus_enabled"
    focus_identifier "focus_identifier"
    focus_magnet_enabled "focus_magnet_enabled"
    focus_navigation_mode_down "focus_navigation_mode_down"
    focus_navigation_mode_left "focus_navigation_mode_left"
    focus_navigation_mode_right "focus_navigation_mode_right"
    focus_navigation_mode_up "focus_navigation_mode_up"
    focus_wrap_enabled "focus_wrap_enabled"
    font_scale_factor "font_scale_factor"
    font_size "font_size"
    font_type "font_type"
    force_render_below "force_render_below"
    force_texture_reload "force_texture_reload"
    grid_dimension_binding "grid_dimension_binding"
    grid_dimensions "grid_dimensions"
    grid_item_template "grid_item_template"
    grid_position "grid_position"
    grid_rescaling_type "grid_rescaling_type"
    handle_deselect "handle_deselect"
    handle_select "handle_select"
    hide_hyphen "hide_hyphen"
    alpha "hover_alpha"
    color "hover_color"
    hover_control "hover_control"
    hover_enabled "hover_enabled"
    ignored "ignored"
    images "images"
    indent_control "indent_control"
    inherit_max_sibling_height "inherit_max_sibling_height"
    inherit_max_sibling_width "inherit_max_sibling_width"
    is_modal "is_modal"
    is_showing_menu "is_showing_menu"
    jump_to_bottom_on_update "jump_to_bottom_on_update"
    keep_ratio "keep_ratio"
    layer "layer"
    localize "localize"
    alpha "locked_alpha"
    color "locked_color"
    locked_control "locked_control"
    low_frequency_rendering "low_frequency_rendering"
    max_length "max_length"
    max_size "max_size"
    maximum_grid_items "maximum_grid_items"
    min_size "min_size"
    modal "modal"
    offset "offset"
    orientation "orientation"
    place_holder_control "place_holder_control"
    alpha "pressed_alpha"
    color "pressed_color"
    pressed_control "pressed_control"
    prevent_touch_input "prevent_touch_input"
    color "primary_color"
    progress_control "progress_control"
    progress_hover_control "progress_hover_control"
    propagate_alpha "propagate_alpha"
    property_bag "property_bag"
    radio_toggle_group "radio_toggle_group"
    render_game_behind "render_game_behind"
    render_only_when_topmost "render_only_when_topmost"
    renderer "renderer"
    reset_event "reset_event"
    reset_on_focus_lost "reset_on_focus_lost"
    rotate_speed "rotate_speed"
    screen_draws_last "screen_draws_last"
    screen_not_flushable "screen_not_flushable"
    scroll_box_and_track_panel "scroll_box_and_track_panel"
    scroll_content "scroll_content"
    scroll_speed "scroll_speed"
    scroll_view_port "scroll_view_port"
    scrollbar_box "scrollbar_box"
    scrollbar_touch_button "scrollbar_touch_button"
    scrollbar_track_button "scrollbar_track_button"
    scrollbar_track "scrollbar_track"
    send_telemetry "send_telemetry"
    shadow "shadow"
    should_steal_mouse "should_steal_mouse"
    size "size"
    slider_box_control "slider_box_control"
    slider_collection_name "slider_collection_name"
    slider_deselected_button "slider_deselected_button"
    slider_direction "slider_direction"
    slider_name "slider_name"
    slider_select_on_hover "slider_select_on_hover"
    slider_selected_button "slider_selected_button"
    slider_small_decrease_button "slider_small_decrease_button"
    slider_small_increase_button "slider_small_increase_button"
    slider_steps "slider_steps"
    slider_track_button "slider_track_button"
    sound_name "sound_name"
    sound_pitch "sound_pitch"
    sound_volume "sound_volume"
    text_alignment "text_alignment"
    text_box_name "text_box_name"
    text_control "text_control"
    text_edit_box_grid_collection_name "text_edit_box_grid_collection_name"
    text_labels "text_labels"
    text_type "text_type"
    text "text"
    texture_file_system "texture_file_system"
    texture "texture"
    tiled "tiled"
    toggle_default_state "toggle_default_state"
    toggle_grid_collection_name "toggle_grid_collection_name"
    toggle_group_default_selected "toggle_group_default_selected"
    toggle_group_forced_index "toggle_group_forced_index"
    toggle_name "toggle_name"
    toggle_off_button "toggle_off_button"
    toggle_on_button "toggle_on_button"
    touch_mode "touch_mode"
    tts_control_header "tts_control_header"
    tts_control_type_order_priority "tts_control_type_order_priority"
    tts_ignore_count "tts_ignore_count"
    tts_ignore_subsections "tts_ignore_subsections"
    tts_index_priority "tts_index_priority"
    tts_inherit_siblings "tts_inherit_siblings"
    tts_name "tts_name"
    tts_override_control_value "tts_override_control_value"
    tts_section_header "tts_section_header"
    tts_toggle_off "tts_toggle_off"
    tts_toggle_on "tts_toggle_on"
    tts_value_changed "tts_value_changed"
    tts_value_order_priority "tts_value_order_priority"
    tts_section_container "ttsSectionContainer"
    type "type"
    unchecked_control "unchecked_control"
    unchecked_hover_control "unchecked_hover_control"
    unchecked_locked_control "unchecked_locked_control"
    unchecked_locked_hover_control "unchecked_locked_hover_control"
    use_anchored_offset "use_anchored_offset"
    use_child_anchors "use_child_anchors"
    use_last_focus "use_last_focus"
    uv_size "uv_size"
    uv "uv"
    variables "variables"
    virtual_keyboard_buffer_control "virtual_keyboard_buffer_control"
    visible "visible"
    zip_folder "zip_folder"
    variable_definition "^\$.*"
  }
  object "<any object property>" : opt
  {
    animation_type "anim_type"
    animation_reset_name "animation_reset_name"
    destroy_at_end "destroy_at_end"
    disable_anim_fast_forward "disable_anim_fast_forward"
    duration "duration"
    easing "easing"
    end_event "end_event"
    fps "fps"
    frame_count "frame_count"
    frame_step "frame_step"
    from "from"
    initial_uv "initial_uv"
    next "next"
    play_event "play_event"
    propagate_alpha "propagate_alpha"
    reversible "reversible"
    scale_from_starting_alpha "scale_from_starting_alpha"
    to "to"
    uv "uv"
    uv_size "uv_size"
    variable_definition "^\$.*"
  }
  object "<any object property>" : opt
  {
    string "type" : opt
    control_ids "control_ids"
    control_name "control_name"
    variable_definition "^\$.*"
  }
}

```

/// html | div.result
//// define
`namespace`：<samp>string</samp>


////


//// define
`<any object property>`：<samp>object</samp>

- An element is a control that can be added to a screen. It can be a button, a label, an image, etc.


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`controls`：<samp>array</samp>

- The controls that are contained within this element.


/////

<div class="language-text highlight"><span class="filename"><code>controls</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>object</samp>


///////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result

///////


//////


/////


///// define
`controls`：<samp>item_ref</samp> {#assets.schemas-blockception.resource.ui.general.item_ref.json}

- The controls that are contained within this element.


/////

```mcschema
element_reference:
string

```

///// html | div.result

/////


```mcschema
element_reference:
string

```

///// html | div.result

/////


```mcschema
variable_reference:
string

```

///// html | div.result

/////


```mcschema
variable_reference:
string

```

///// html | div.result

/////


```mcschema
variable_reference:
string

```

///// html | div.result

/////






///// define
`modifications`：<samp>array</samp>

- Modifications to the element.


/////

<div class="language-text highlight"><span class="filename"><code>modifications</code></span><pre id="__code_1"><span></span></pre></div>

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`control_name`：<samp>string</samp>


///////


/////// define
`array_name`：<samp>string</samp>


///////


/////// define
`operation`：<samp>string</samp>


///////


/////// define
`where`：<samp>bindings</samp> {#assets.schemas-blockception.resource.ui.elements.properties.bindings.json}


///////



```mcschema
bindings:
array
{
  object "<any array element>" : opt
  {
    string "binding_collection_name"
    string "binding_collection_prefix"
    string "binding_condition" : opt
    binding_condition "binding_condition"
    string "binding_name"
    string "binding_name_override"
    string "binding_type" : opt
    variable "binding_type"
    boolean "ignored"
    boolean "resolve_sibling_scope"
    string "source_control_name"
    string "source_property_name"
    string "target_property_name"
  }
}

```

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`binding_collection_name`：<samp>string</samp> {#assets.schemas-blockception.resource.ui.general.string.json}

- The name of the collection that the binding is in.


/////////

```mcschema
string:
string

```

///////// html | div.result

/////////






///////// define
`binding_collection_prefix`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The prefix of the collection that the binding is in.


/////////


///////// define
`binding_condition`：<samp>string</samp>

- The condition that must be met for the binding to be applied.


/////////


///////// define
`binding_condition`：<samp>[item_ref](#assets.schemas-blockception.resource.ui.general.item_ref.json)</samp>

- The condition that must be met for the binding to be applied.


/////////



///////// define
`binding_name`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the binding. This is used to reference the binding in the element's properties.


/////////


///////// define
`binding_name_override`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the binding. This is used to reference the binding in the element's properties.


/////////


///////// define
`binding_type`：<samp>string</samp>

- The type of the binding.


/////////


///////// define
`binding_type`：<samp>variable</samp> {#assets.schemas-blockception.resource.ui.general.variable.json}

- The type of the binding.


/////////

```mcschema
variable:
string

```

///////// html | div.result

/////////


```mcschema
variable:
string

```

///////// html | div.result

/////////


```mcschema
variable:
string

```

///////// html | div.result

/////////





///////// define
`ignored`：<samp>boolean</samp> {#assets.schemas-blockception.resource.ui.general.boolean.json}

- If true, the binding will be ignored.


/////////

```mcschema
boolean:
boolean

```

///////// html | div.result

/////////






///////// define
`resolve_sibling_scope`：<samp>[boolean](#assets.schemas-blockception.resource.ui.general.boolean.json)</samp>

- If true, the binding will resolve sibling scope.


/////////


///////// define
`source_control_name`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the control that the binding is in.


/////////


///////// define
`source_property_name`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the property that the binding is in.


/////////


///////// define
`target_property_name`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the property that the binding is in.


/////////


////////


///////




/////// define
`target`：<samp>[bindings](#assets.schemas-blockception.resource.ui.elements.properties.bindings.json)</samp>


///////


/////// define
`target_control`：<samp>string</samp>


///////


/////// define
`value`：<samp>[bindings](#assets.schemas-blockception.resource.ui.elements.properties.bindings.json)</samp>


///////


/////// define
`value`：<samp>array</samp>

- The controls to add.


///////

<div class="language-text highlight"><span class="filename"><code>value</code></span><pre id="__code_1"><span></span></pre></div>

/////// html | div.result
//////// define
`<any array element>`：<samp>object</samp>


////////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//////// html | div.result
///////// define
`<any object property>`：<samp>object</samp>


/////////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

///////// html | div.result

/////////


////////


///////


/////// define
`value`：<samp>[item_ref](#assets.schemas-blockception.resource.ui.general.item_ref.json)</samp>

- The controls to add.


///////




//////


/////


///// define
`allow_clipping`：<samp>allow_clipping</samp> {#assets.schemas-blockception.resource.ui.elements.properties.allow_clipping.json}


/////




///// define
`allow_debug_missing_texture`：<samp>allow_debug_missing_texture</samp> {#assets.schemas-blockception.resource.ui.elements.properties.allow_debug_missing_texture.json}


/////




///// define
`allow_scroll_even_when_content_fits`：<samp>allow_scroll_even_when_content_fits</samp> {#assets.schemas-blockception.resource.ui.elements.properties.allow_scroll_even_when_content_fits.json}


/////




///// define
`alpha`：<samp>alpha</samp> {#assets.schemas-blockception.resource.ui.elements.properties.alpha.json}


/////



```mcschema
alpha:
number

```

///// html | div.result

/////




///// define
`always_handle_pointer`：<samp>always_handle_pointer</samp> {#assets.schemas-blockception.resource.ui.elements.properties.always_handle_pointer.json}


/////




///// define
`always_handle_scrolling`：<samp>always_handle_scrolling</samp> {#assets.schemas-blockception.resource.ui.elements.properties.always_handle_scrolling.json}


/////




///// define
`always_listen_to_input`：<samp>always_listen_to_input</samp> {#assets.schemas-blockception.resource.ui.elements.properties.always_listen_to_input.json}


/////




///// define
`always_rotate`：<samp>always_rotate</samp> {#assets.schemas-blockception.resource.ui.elements.properties.always_rotate.json}


/////




///// define
`anchor_from`：<samp>anchor_from</samp> {#assets.schemas-blockception.resource.ui.elements.properties.anchor_from.json}


/////

```mcschema
anchor:
string

```

///// html | div.result

/////







///// define
`anchor_to`：<samp>anchor_to</samp> {#assets.schemas-blockception.resource.ui.elements.properties.anchor_to.json}


/////







///// define
`anims`：<samp>animations</samp> {#assets.schemas-blockception.resource.ui.elements.properties.anims.json}


/////



```mcschema
animations:
array
{
  <any array element> "<any array element>"
}

```

///// html | div.result
////// define
`<any array element>`：<samp>[item_ref](#assets.schemas-blockception.resource.ui.general.item_ref.json)</samp>


//////


/////




///// define
`background_control`：<samp>background_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.background_control.json}


/////




///// define
`background_hover_control`：<samp>background_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.background_hover_control.json}


/////




///// define
`backup_font_type`：<samp>backup_font_type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.backup_font_type.json}


/////

```mcschema
backup_font_type:
string

```

///// html | div.result

/////






///// define
`bilinear`：<samp>bilinear</samp> {#assets.schemas-blockception.resource.ui.elements.properties.bilinear.json}


/////




///// define
`bindings`：<samp>[bindings](#assets.schemas-blockception.resource.ui.elements.properties.bindings.json)</samp>


/////


///// define
`button_mappings`：<samp>button_mappings</samp> {#assets.schemas-blockception.resource.ui.elements.properties.button_mappings.json}


/////



```mcschema
button_mappings:
array
{
  object "<any array element>" : opt
  {
    ['string', 'boolean'] "<any object property>" : opt
  }
}

```

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`：<samp>['string', 'boolean']</samp>


///////


//////


/////




///// define
`cache_screen`：<samp>cache_screen</samp> {#assets.schemas-blockception.resource.ui.elements.properties.cache_screen.json}


/////




///// define
`checked_control`：<samp>checked_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.checked_control.json}


/////

```mcschema
checked_control:
string

```

///// html | div.result

/////






///// define
`checked_hover_control`：<samp>checked_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.checked_hover_control.json}


/////

```mcschema
checked_hover_control:
string

```

///// html | div.result

/////






///// define
`checked_locked_control`：<samp>checked_locked_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.checked_locked_control.json}


/////

```mcschema
checked_locked_control:
string

```

///// html | div.result

/////






///// define
`checked_locked_hover_control`：<samp>checked_locked_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.checked_locked_hover_control.json}


/////

```mcschema
checked_locked_hover_control:
string

```

///// html | div.result

/////






///// define
`clip_direction`：<samp>clip_direction</samp> {#assets.schemas-blockception.resource.ui.elements.properties.clip_direction.json}


/////

```mcschema
clip_direction:
string

```

///// html | div.result

/////






///// define
`clip_pixelperfect`：<samp>clip_pixel_perfect</samp> {#assets.schemas-blockception.resource.ui.elements.properties.clip_pixelperfect.json}


/////




///// define
`clips_children`：<samp>clips_children</samp> {#assets.schemas-blockception.resource.ui.elements.properties.clips_children.json}


/////




///// define
`close_on_player_hurt`：<samp>close_on_player_hurt</samp> {#assets.schemas-blockception.resource.ui.elements.properties.close_on_player_hurt.json}


/////




///// define
`collection_index`：<samp>collection_index</samp> {#assets.schemas-blockception.resource.ui.elements.properties.collection_index.json}


/////

```mcschema
integer:
integer

```

///// html | div.result

/////







///// define
`collection_name`：<samp>collection_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.collection_name.json}


/////




///// define
`color`：<samp>color</samp> {#assets.schemas-blockception.resource.ui.elements.properties.color.json}


/////



```mcschema
color:
array
{
  number "0..0" : opt
  number "1..1" : opt
  number "2..2" : opt
}

```

///// html | div.result
////// define
`0..0`：<samp>number</samp>

- A variable


//////


////// define
`1..1`：<samp>number</samp>

- A variable


//////


////// define
`2..2`：<samp>number</samp>

- A variable


//////


/////





///// define
`consume_hover_events`：<samp>consume_hover_events</samp> {#assets.schemas-blockception.resource.ui.elements.properties.consume_hover_events.json}


/////




///// define
`contained`：<samp>contained</samp> {#assets.schemas-blockception.resource.ui.elements.properties.contained.json}


/////




///// define
`control_name`：<samp>control_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.control_name.json}


/////




///// define
`default_control`：<samp>default_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.default_control.json}


/////




///// define
`default_focus_precedence`：<samp>default_focus_precedence</samp> {#assets.schemas-blockception.resource.ui.elements.properties.default_focus_precedence.json}


/////




///// define
`disable_anim_fast_forward`：<samp>disable_anim_fast_forward</samp> {#assets.schemas-blockception.resource.ui.elements.properties.disable_anim_fast_forward.json}


/////




///// define
`draggable`：<samp>draggable</samp> {#assets.schemas-blockception.resource.ui.elements.properties.draggable.json}


/////




///// define
`dropdown_area`：<samp>dropdown_area</samp> {#assets.schemas-blockception.resource.ui.elements.properties.dropdown_area.json}


/////



```mcschema
vec4:
array
{
  string "0..0" : opt
  string "0..0" : opt
  integer "0..0" : opt
   "1..1" : opt
   "2..2" : opt
   "3..3" : opt
}

```

///// html | div.result
////// define
`0..0`：<samp>string</samp>

- A variable


//////


////// define
`0..0`：<samp>string</samp>

- A variable


//////


////// define
`0..0`：<samp>integer</samp>

- A variable


//////



////// define
`1..1`

- A variable


//////


////// define
`2..2`

- A variable


//////


////// define
`3..3`

- A variable


//////


/////





///// define
`dropdown_content_control`：<samp>dropdown_content_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.dropdown_content_control.json}


/////




///// define
`dropdown_name`：<samp>dropdown_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.dropdown_name.json}


/////




///// define
`enable_directional_toggling`：<samp>enable_directional_toggling</samp> {#assets.schemas-blockception.resource.ui.elements.properties.enable_directional_toggling.json}


/////




///// define
`enable_profanity_filter`：<samp>enable_profanity_filter</samp> {#assets.schemas-blockception.resource.ui.elements.properties.enable_profanity_filter.json}


/////




///// define
`enabled_newline`：<samp>enabled_newline</samp> {#assets.schemas-blockception.resource.ui.elements.properties.enabled_newline.json}


/////




///// define
`enabled`：<samp>enabled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.enabled.json}


/////




///// define
`factory`：<samp>factory</samp> {#assets.schemas-blockception.resource.ui.elements.properties.factory.json}


/////

```mcschema
factory:
{
  control_ids "control_ids"
  string "control_name"
  array "factory_variables" : opt
  {
    string "<any array element>" : opt
  }
  string "factory_variables" : opt
  string "name" : opt
  variable_definition "^\$.*"
}

```

///// html | div.result
////// define
`control_ids`：<samp>control_ids</samp> {#assets.schemas-blockception.resource.ui.elements.properties.control_ids.json}


//////

```mcschema
control_ids:
string

```

////// html | div.result

//////


```mcschema
control_ids:
{
  string "<any object property>" : opt
}

```

////// html | div.result
/////// define
`<any object property>`：<samp>string</samp>


///////


//////




////// define
`control_name`：<samp>[string](#assets.schemas-blockception.resource.ui.general.string.json)</samp>

- The name of the control that will be created by the factory.


//////


////// define
`factory_variables`：<samp>array</samp>

- The variables that will be used by the factory.


//////

<div class="language-text highlight"><span class="filename"><code>factory_variables</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any array element>`：<samp>string</samp>


///////


//////


////// define
`factory_variables`：<samp>string</samp>

- The variables that will be used by the factory.


//////



////// define
`name`：<samp>string</samp>

- The name of the factory.


//////


////// define
`^\$.*`：<samp>variable_definition</samp> {#assets.schemas-blockception.resource.ui.general.variables.json}


//////

////// define
`variables`

- A variable is a reference to a value that can be used in the UI.


//////



/////






///// define
`fill`：<samp>fill</samp> {#assets.schemas-blockception.resource.ui.elements.properties.fill.json}


/////




///// define
`focus_change_down`：<samp>focus_change_down</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_change_down.json}


/////

```mcschema
focus_change_down:
string

```

///// html | div.result

/////






///// define
`focus_change_left`：<samp>focus_change_left</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_change_left.json}


/////

```mcschema
focus_change_left:
string

```

///// html | div.result

/////






///// define
`focus_change_right`：<samp>focus_change_right</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_change_right.json}


/////

```mcschema
focus_change_right:
string

```

///// html | div.result

/////






///// define
`focus_change_up`：<samp>focus_change_up</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_change_up.json}


/////

```mcschema
focus_change_up:
string

```

///// html | div.result

/////






///// define
`focus_container`：<samp>focus_container</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_container.json}


/////




///// define
`focus_enabled`：<samp>focus_enabled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_enabled.json}


/////




///// define
`focus_identifier`：<samp>focus_identifier</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_identifier.json}


/////




///// define
`focus_magnet_enabled`：<samp>focus_magnet_enabled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_magnet_enabled.json}


/////




///// define
`focus_navigation_mode_down`：<samp>focus_navigation_mode_down</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_navigation_mode_down.json}


/////

```mcschema
navigation_mode:
string

```

///// html | div.result

/////







///// define
`focus_navigation_mode_left`：<samp>focus_navigation_mode_left</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_navigation_mode_left.json}


/////







///// define
`focus_navigation_mode_right`：<samp>focus_navigation_mode_right</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_navigation_mode_right.json}


/////







///// define
`focus_navigation_mode_up`：<samp>focus_navigation_mode_up</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_navigation_mode_up.json}


/////







///// define
`focus_wrap_enabled`：<samp>focus_wrap_enabled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.focus_wrap_enabled.json}


/////




///// define
`font_scale_factor`：<samp>font_scale_factor</samp> {#assets.schemas-blockception.resource.ui.elements.properties.font_scale_factor.json}


/////

```mcschema
number:
number

```

///// html | div.result

/////







///// define
`font_size`：<samp>font_size</samp> {#assets.schemas-blockception.resource.ui.elements.properties.font_size.json}


/////

```mcschema
font_size:
string

```

///// html | div.result

/////






///// define
`font_type`：<samp>font_type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.font_type.json}


/////

```mcschema
font_type:
string

```

///// html | div.result

/////






///// define
`force_render_below`：<samp>force_render_below</samp> {#assets.schemas-blockception.resource.ui.elements.properties.force_render_below.json}


/////




///// define
`force_texture_reload`：<samp>force_texture_reload</samp> {#assets.schemas-blockception.resource.ui.elements.properties.force_texture_reload.json}


/////




///// define
`grid_dimension_binding`：<samp>grid_dimension_binding</samp> {#assets.schemas-blockception.resource.ui.elements.properties.grid_dimension_binding.json}


/////




///// define
`grid_dimensions`：<samp>grid_dimensions</samp> {#assets.schemas-blockception.resource.ui.elements.properties.grid_dimensions.json}


/////



```mcschema
vec2:
array
{
  string "0..0" : opt
  string "0..0" : opt
  integer "0..0" : opt
  string "1..1" : opt
}

```

///// html | div.result
////// define
`0..0`：<samp>string</samp>

- A variable


//////


////// define
`1..1`：<samp>string</samp>

- A variable


//////


/////





///// define
`grid_item_template`：<samp>grid_item_template</samp> {#assets.schemas-blockception.resource.ui.elements.properties.grid_item_template.json}


/////




///// define
`grid_position`：<samp>grid_position</samp> {#assets.schemas-blockception.resource.ui.elements.properties.grid_position.json}


/////




///// define
`grid_rescaling_type`：<samp>grid_rescaling_type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.grid_rescaling_type.json}


/////

```mcschema
grid_rescaling_type:
string

```

///// html | div.result

/////






///// define
`handle_deselect`：<samp>handle_deselect</samp> {#assets.schemas-blockception.resource.ui.elements.properties.handle_deselect.json}


/////




///// define
`handle_select`：<samp>handle_select</samp> {#assets.schemas-blockception.resource.ui.elements.properties.handle_select.json}


/////




///// define
`hide_hyphen`：<samp>hide_hyphen</samp> {#assets.schemas-blockception.resource.ui.elements.properties.hide_hyphen.json}


/////




///// define
`hover_alpha`：<samp>[alpha](#assets.schemas-blockception.resource.ui.elements.properties.alpha.json)</samp>


/////


///// define
`hover_color`：<samp>[color](#assets.schemas-blockception.resource.ui.elements.properties.color.json)</samp>


/////


///// define
`hover_control`：<samp>hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.hover_control.json}


/////

```mcschema
hover_control:
string

```

///// html | div.result

/////






///// define
`hover_enabled`：<samp>hover_enabled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.hover_enabled.json}


/////




///// define
`ignored`：<samp>ignored</samp> {#assets.schemas-blockception.resource.ui.elements.properties.ignored.json}


/////




///// define
`images`：<samp>images</samp> {#assets.schemas-blockception.resource.ui.elements.properties.images.json}


/////



```mcschema
images:
array
{
  <any array element> "<any array element>"
}

```

///// html | div.result
////// define
`<any array element>`：<samp>[item_ref](#assets.schemas-blockception.resource.ui.general.item_ref.json)</samp>


//////


/////




///// define
`indent_control`：<samp>indent_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.indent_control.json}


/////

```mcschema
indent_control:
string

```

///// html | div.result

/////






///// define
`inherit_max_sibling_height`：<samp>inherit_max_sibling_height</samp> {#assets.schemas-blockception.resource.ui.elements.properties.inherit_max_sibling_height.json}


/////




///// define
`inherit_max_sibling_width`：<samp>inherit_max_sibling_width</samp> {#assets.schemas-blockception.resource.ui.elements.properties.inherit_max_sibling_width.json}


/////




///// define
`is_modal`：<samp>is_modal</samp> {#assets.schemas-blockception.resource.ui.elements.properties.is_modal.json}


/////




///// define
`is_showing_menu`：<samp>is_showing_menu</samp> {#assets.schemas-blockception.resource.ui.elements.properties.is_showing_menu.json}


/////




///// define
`jump_to_bottom_on_update`：<samp>jump_to_bottom_on_update</samp> {#assets.schemas-blockception.resource.ui.elements.properties.jump_to_bottom_on_update.json}


/////




///// define
`keep_ratio`：<samp>keep_ratio</samp> {#assets.schemas-blockception.resource.ui.elements.properties.keep_ratio.json}


/////




///// define
`layer`：<samp>layer</samp> {#assets.schemas-blockception.resource.ui.elements.properties.layer.json}


/////




///// define
`localize`：<samp>localize</samp> {#assets.schemas-blockception.resource.ui.elements.properties.localize.json}


/////




///// define
`locked_alpha`：<samp>[alpha](#assets.schemas-blockception.resource.ui.elements.properties.alpha.json)</samp>


/////


///// define
`locked_color`：<samp>[color](#assets.schemas-blockception.resource.ui.elements.properties.color.json)</samp>


/////


///// define
`locked_control`：<samp>locked_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.locked_control.json}


/////

```mcschema
locked_control:
string

```

///// html | div.result

/////






///// define
`low_frequency_rendering`：<samp>low_frequency_rendering</samp> {#assets.schemas-blockception.resource.ui.elements.properties.low_frequency_rendering.json}


/////




///// define
`max_length`：<samp>max_length</samp> {#assets.schemas-blockception.resource.ui.elements.properties.max_length.json}


/////




///// define
`max_size`：<samp>max_size</samp> {#assets.schemas-blockception.resource.ui.elements.properties.max_size.json}


/////



```mcschema
size:
array
{
  string "0..0" : opt
  string "0..0" : opt
  integer "0..0" : opt
  string "1..1" : opt
}

```

///// html | div.result
////// define
`0..0`：<samp>string</samp>

- A size coordinate.


//////


////// define
`1..1`：<samp>string</samp>

- A size coordinate.


//////


/////





///// define
`maximum_grid_items`：<samp>maximum_grid_items</samp> {#assets.schemas-blockception.resource.ui.elements.properties.maximum_grid_items.json}


/////




///// define
`min_size`：<samp>min_size</samp> {#assets.schemas-blockception.resource.ui.elements.properties.min_size.json}


/////




///// define
`modal`：<samp>modal</samp> {#assets.schemas-blockception.resource.ui.elements.properties.modal.json}


/////




///// define
`offset`：<samp>offset</samp> {#assets.schemas-blockception.resource.ui.elements.properties.offset.json}


/////




///// define
`orientation`：<samp>orientation</samp> {#assets.schemas-blockception.resource.ui.elements.properties.orientation.json}


/////

```mcschema
orientation:
string

```

///// html | div.result

/////






///// define
`place_holder_control`：<samp>place_holder_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.place_holder_control.json}


/////




///// define
`pressed_alpha`：<samp>[alpha](#assets.schemas-blockception.resource.ui.elements.properties.alpha.json)</samp>


/////


///// define
`pressed_color`：<samp>[color](#assets.schemas-blockception.resource.ui.elements.properties.color.json)</samp>


/////


///// define
`pressed_control`：<samp>pressed_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.pressed_control.json}


/////

```mcschema
pressed_control:
string

```

///// html | div.result

/////






///// define
`prevent_touch_input`：<samp>prevent_touch_input</samp> {#assets.schemas-blockception.resource.ui.elements.properties.prevent_touch_input.json}


/////




///// define
`primary_color`：<samp>[color](#assets.schemas-blockception.resource.ui.elements.properties.color.json)</samp>


/////


///// define
`progress_control`：<samp>progress_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.progress_control.json}


/////




///// define
`progress_hover_control`：<samp>progress_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.progress_hover_control.json}


/////




///// define
`propagate_alpha`：<samp>propagate_alpha</samp> {#assets.schemas-blockception.resource.ui.elements.properties.propagate_alpha.json}


/////




///// define
`property_bag`：<samp>property_bag</samp> {#assets.schemas-blockception.resource.ui.elements.properties.property_bag.json}


/////

```mcschema
property_bag:
{
  any "<any object property>"
}

```

///// html | div.result
////// define
`<any object property>`：<samp>any</samp> {#assets.schemas-blockception.resource.ui.general.any.json}


//////

```mcschema
any:
['array', 'boolean', 'integer', 'number', 'object', 'string']

```

////// html | div.result

//////



/////






///// define
`radio_toggle_group`：<samp>radio_toggle_group</samp> {#assets.schemas-blockception.resource.ui.elements.properties.radio_toggle_group.json}


/////




///// define
`render_game_behind`：<samp>render_game_behind</samp> {#assets.schemas-blockception.resource.ui.elements.properties.render_game_behind.json}


/////




///// define
`render_only_when_topmost`：<samp>render_only_when_topmost</samp> {#assets.schemas-blockception.resource.ui.elements.properties.render_only_when_topmost.json}


/////




///// define
`renderer`：<samp>renderer</samp> {#assets.schemas-blockception.resource.ui.elements.properties.renderer.json}


/////

```mcschema
renderer:
string

```

///// html | div.result

/////






///// define
`reset_event`：<samp>reset_event</samp> {#assets.schemas-blockception.resource.ui.elements.properties.reset_event.json}


/////




///// define
`reset_on_focus_lost`：<samp>reset_on_focus_lost</samp> {#assets.schemas-blockception.resource.ui.elements.properties.reset_on_focus_lost.json}


/////




///// define
`rotate_speed`：<samp>rotate_speed</samp> {#assets.schemas-blockception.resource.ui.elements.properties.rotate_speed.json}


/////




///// define
`screen_draws_last`：<samp>screen_draws_last</samp> {#assets.schemas-blockception.resource.ui.elements.properties.screen_draws_last.json}


/////




///// define
`screen_not_flushable`：<samp>screen_not_flushable</samp> {#assets.schemas-blockception.resource.ui.elements.properties.screen_not_flushable.json}


/////




///// define
`scroll_box_and_track_panel`：<samp>scroll_box_and_track_panel</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scroll_box_and_track_panel.json}


/////




///// define
`scroll_content`：<samp>scroll_content</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scroll_content.json}


/////




///// define
`scroll_speed`：<samp>scroll_speed</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scroll_speed.json}


/////




///// define
`scroll_view_port`：<samp>scroll_view_port</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scroll_view_port.json}


/////




///// define
`scrollbar_box`：<samp>scrollbar_box</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scrollbar_box.json}


/////

```mcschema
scrollbar_box:
string

```

///// html | div.result

/////






///// define
`scrollbar_touch_button`：<samp>scrollbar_touch_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scrollbar_touch_button.json}


/////




///// define
`scrollbar_track_button`：<samp>scrollbar_track_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scrollbar_track_button.json}


/////




///// define
`scrollbar_track`：<samp>scrollbar_track</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scrollbar_track.json}


/////

```mcschema
scrollbar_track:
string

```

///// html | div.result

/////






///// define
`send_telemetry`：<samp>send_telemetry</samp> {#assets.schemas-blockception.resource.ui.elements.properties.send_telemetry.json}


/////




///// define
`shadow`：<samp>shadow</samp> {#assets.schemas-blockception.resource.ui.elements.properties.shadow.json}


/////




///// define
`should_steal_mouse`：<samp>should_steal_mouse</samp> {#assets.schemas-blockception.resource.ui.elements.properties.should_steal_mouse.json}


/////




///// define
`size`：<samp>size</samp> {#assets.schemas-blockception.resource.ui.elements.properties.size.json}


/////




///// define
`slider_box_control`：<samp>slider_box_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_box_control.json}


/////

```mcschema
slider_box_control:
string

```

///// html | div.result

/////






///// define
`slider_collection_name`：<samp>slider_collection_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_collection_name.json}


/////




///// define
`slider_deselected_button`：<samp>slider_deselected_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_deselected_button.json}


/////




///// define
`slider_direction`：<samp>slider_direction</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_direction.json}


/////




///// define
`slider_name`：<samp>slider_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_name.json}


/////




///// define
`slider_select_on_hover`：<samp>slider_select_on_hover</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_select_on_hover.json}


/////




///// define
`slider_selected_button`：<samp>slider_selected_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_selected_button.json}


/////




///// define
`slider_small_decrease_button`：<samp>slider_small_decrease_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_small_decrease_button.json}


/////




///// define
`slider_small_increase_button`：<samp>slider_small_increase_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_small_increase_button.json}


/////




///// define
`slider_steps`：<samp>slider_steps</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_steps.json}


/////




///// define
`slider_track_button`：<samp>slider_track_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.slider_track_button.json}


/////




///// define
`sound_name`：<samp>sound_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.sound_name.json}


/////




///// define
`sound_pitch`：<samp>sound_pitch</samp> {#assets.schemas-blockception.resource.ui.elements.properties.sound_pitch.json}


/////




///// define
`sound_volume`：<samp>sound_volume</samp> {#assets.schemas-blockception.resource.ui.elements.properties.sound_volume.json}


/////

```mcschema
sound_volume:
number

```

///// html | div.result

/////






///// define
`text_alignment`：<samp>text_alignment</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_alignment.json}


/////




///// define
`text_box_name`：<samp>text_box_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_box_name.json}


/////




///// define
`text_control`：<samp>text_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_control.json}


/////




///// define
`text_edit_box_grid_collection_name`：<samp>text_edit_box_grid_collection_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_edit_box_grid_collection_name.json}


/////




///// define
`text_labels`：<samp>text_labels</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_labels.json}


/////

```mcschema
text_labels:
array
{
  string "<any array element>" : opt
}

```

///// html | div.result
////// define
`<any array element>`：<samp>string</samp>


//////


/////






///// define
`text_type`：<samp>text_type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text_type.json}


/////

```mcschema
text_type:
string

```

///// html | div.result

/////






///// define
`text`：<samp>text</samp> {#assets.schemas-blockception.resource.ui.elements.properties.text.json}


/////




///// define
`texture_file_system`：<samp>texture_file_system</samp> {#assets.schemas-blockception.resource.ui.elements.properties.texture_file_system.json}


/////

```mcschema
texture_file_system:
string

```

///// html | div.result

/////






///// define
`texture`：<samp>texture</samp> {#assets.schemas-blockception.resource.ui.elements.properties.texture.json}


/////

```mcschema
texture:
string

```

///// html | div.result

/////




```mcschema
texture:
string

```

///// html | div.result

/////




///// define
`tiled`：<samp>tiled</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tiled.json}


/////

```mcschema
tiled:
boolean

```

///// html | div.result

/////


```mcschema
tiled:
string

```

///// html | div.result

/////






///// define
`toggle_default_state`：<samp>toggle_default_state</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_default_state.json}


/////

```mcschema
toggle_default_state:
string

```

///// html | div.result

/////






///// define
`toggle_grid_collection_name`：<samp>toggle_grid_collection_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_grid_collection_name.json}


/////




///// define
`toggle_group_default_selected`：<samp>toggle_group_default_selected</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_group_default_selected.json}


/////




///// define
`toggle_group_forced_index`：<samp>toggle_group_forced_index</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_group_forced_index.json}


/////




///// define
`toggle_name`：<samp>toggle_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_name.json}


/////




///// define
`toggle_off_button`：<samp>toggle_off_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_off_button.json}


/////




///// define
`toggle_on_button`：<samp>toggle_on_button</samp> {#assets.schemas-blockception.resource.ui.elements.properties.toggle_on_button.json}


/////




///// define
`touch_mode`：<samp>touch_mode</samp> {#assets.schemas-blockception.resource.ui.elements.properties.touch_mode.json}


/////

```mcschema
touch_mode:
string

```

///// html | div.result

/////






///// define
`tts_control_header`：<samp>tts_control_header</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.control_header.json}


/////




///// define
`tts_control_type_order_priority`：<samp>tts_control_type_order_priority</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.control_type_order_priority.json}


/////




///// define
`tts_ignore_count`：<samp>tts_ignore_count</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.ignore_count.json}


/////




///// define
`tts_ignore_subsections`：<samp>tts_ignore_subsections</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.ignore_subsections.json}


/////




///// define
`tts_index_priority`：<samp>tts_index_priority</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.index_priority.json}


/////




///// define
`tts_inherit_siblings`：<samp>tts_inherit_siblings</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.inherit_siblings.json}


/////




///// define
`tts_name`：<samp>tts_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.name.json}


/////




///// define
`tts_override_control_value`：<samp>tts_override_control_value</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.override_control_value.json}


/////




///// define
`tts_section_header`：<samp>tts_section_header</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.section_header.json}


/////




///// define
`tts_toggle_off`：<samp>tts_toggle_off</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.toggle_off.json}


/////




///// define
`tts_toggle_on`：<samp>tts_toggle_on</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.toggle_on.json}


/////




///// define
`tts_value_changed`：<samp>tts_value_changed</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.value_changed.json}


/////




///// define
`tts_value_order_priority`：<samp>tts_value_order_priority</samp> {#assets.schemas-blockception.resource.ui.elements.properties.tts.value_order_priority.json}


/////




///// define
`ttsSectionContainer`：<samp>tts_section_container</samp> {#assets.schemas-blockception.resource.ui.elements.properties.ttsSectionContainer.json}


/////




///// define
`type`：<samp>type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.type.json}


/////

```mcschema
type:
string

```

///// html | div.result

/////



///// define
`unchecked_control`：<samp>unchecked_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.unchecked_control.json}


/////

```mcschema
unchecked_control:
string

```

///// html | div.result

/////






///// define
`unchecked_hover_control`：<samp>unchecked_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.unchecked_hover_control.json}


/////

```mcschema
unchecked_hover_control:
string

```

///// html | div.result

/////






///// define
`unchecked_locked_control`：<samp>unchecked_locked_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.unchecked_locked_control.json}


/////

```mcschema
unchecked_locked_control:
string

```

///// html | div.result

/////






///// define
`unchecked_locked_hover_control`：<samp>unchecked_locked_hover_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.unchecked_locked_hover_control.json}


/////

```mcschema
unchecked_locked_hover_control:
string

```

///// html | div.result

/////






///// define
`use_anchored_offset`：<samp>use_anchored_offset</samp> {#assets.schemas-blockception.resource.ui.elements.properties.use_anchored_offset.json}


/////




///// define
`use_child_anchors`：<samp>use_child_anchors</samp> {#assets.schemas-blockception.resource.ui.elements.properties.use_child_anchors.json}


/////




///// define
`use_last_focus`：<samp>use_last_focus</samp> {#assets.schemas-blockception.resource.ui.elements.properties.use_last_focus.json}


/////




///// define
`uv_size`：<samp>uv_size</samp> {#assets.schemas-blockception.resource.ui.elements.properties.uv_size.json}


/////




///// define
`uv`：<samp>uv</samp> {#assets.schemas-blockception.resource.ui.elements.properties.uv.json}


/////




///// define
`variables`：<samp>variables</samp> {#assets.schemas-blockception.resource.ui.elements.properties.variables.json}


/////



```mcschema
variables:
array
{
  object "<any array element>" : opt
  {
     "<any object property>" : opt
  }
}

```

///// html | div.result
////// define
`<any array element>`：<samp>object</samp>


//////

<div class="language-text highlight"><span class="filename"><code>&lt;any array element&gt;</code></span><pre id="__code_1"><span></span></pre></div>

////// html | div.result
/////// define
`<any object property>`

- A variable is a reference to a value that can be used in the UI.


///////


//////


/////


```mcschema
variables:
{
   "<any object property>" : opt
}

```

///// html | div.result
////// define
`<any object property>`

- A variable is a reference to a value that can be used in the UI.


//////


/////




///// define
`virtual_keyboard_buffer_control`：<samp>virtual_keyboard_buffer_control</samp> {#assets.schemas-blockception.resource.ui.elements.properties.virtual_keyboard_buffer_control.json}


/////




///// define
`visible`：<samp>visible</samp> {#assets.schemas-blockception.resource.ui.elements.properties.visible.json}


/////




///// define
`zip_folder`：<samp>zip_folder</samp> {#assets.schemas-blockception.resource.ui.elements.properties.zip_folder.json}


/////




///// define
`^\$.*`：<samp>[variable_definition](#assets.schemas-blockception.resource.ui.general.variables.json)</samp>


/////


////


//// define
`<any object property>`：<samp>object</samp>

- An animation is a set of keyframes that can be applied to an element.


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`anim_type`：<samp>animation_type</samp> {#assets.schemas-blockception.resource.ui.elements.properties.anim_type.json}


/////

```mcschema
animation_type:
string

```

///// html | div.result

/////






///// define
`animation_reset_name`：<samp>animation_reset_name</samp> {#assets.schemas-blockception.resource.ui.elements.properties.animation_reset_name.json}


/////




///// define
`destroy_at_end`：<samp>destroy_at_end</samp> {#assets.schemas-blockception.resource.ui.elements.properties.destroy_at_end.json}


/////

```mcschema
destroy_at_end:
string

```

///// html | div.result

/////






///// define
`disable_anim_fast_forward`：<samp>[disable_anim_fast_forward](#assets.schemas-blockception.resource.ui.elements.properties.disable_anim_fast_forward.json)</samp>


/////


///// define
`duration`：<samp>duration</samp> {#assets.schemas-blockception.resource.ui.elements.properties.duration.json}


/////




///// define
`easing`：<samp>easing</samp> {#assets.schemas-blockception.resource.ui.elements.properties.easing.json}


/////

```mcschema
easing:
string

```

///// html | div.result

/////






///// define
`end_event`：<samp>end_event</samp> {#assets.schemas-blockception.resource.ui.elements.properties.end_event.json}


/////




///// define
`fps`：<samp>fps</samp> {#assets.schemas-blockception.resource.ui.elements.properties.fps.json}


/////




///// define
`frame_count`：<samp>frame_count</samp> {#assets.schemas-blockception.resource.ui.elements.properties.frame_count.json}


/////




///// define
`frame_step`：<samp>frame_step</samp> {#assets.schemas-blockception.resource.ui.elements.properties.frame_step.json}


/////




///// define
`from`：<samp>from</samp> {#assets.schemas-blockception.resource.ui.elements.properties.from.json}


/////

```mcschema
from:
number

```

///// html | div.result

/////






///// define
`initial_uv`：<samp>initial_uv</samp> {#assets.schemas-blockception.resource.ui.elements.properties.initial_uv.json}


/////




///// define
`next`：<samp>next</samp> {#assets.schemas-blockception.resource.ui.elements.properties.next.json}


/////




///// define
`play_event`：<samp>play_event</samp> {#assets.schemas-blockception.resource.ui.elements.properties.play_event.json}


/////




///// define
`propagate_alpha`：<samp>[propagate_alpha](#assets.schemas-blockception.resource.ui.elements.properties.propagate_alpha.json)</samp>


/////


///// define
`reversible`：<samp>reversible</samp> {#assets.schemas-blockception.resource.ui.elements.properties.reversible.json}


/////




///// define
`scale_from_starting_alpha`：<samp>scale_from_starting_alpha</samp> {#assets.schemas-blockception.resource.ui.elements.properties.scale_from_starting_alpha.json}


/////




///// define
`to`：<samp>to</samp> {#assets.schemas-blockception.resource.ui.elements.properties.to.json}


/////

```mcschema
to:
number

```

///// html | div.result

/////






///// define
`uv`：<samp>[uv](#assets.schemas-blockception.resource.ui.elements.properties.uv.json)</samp>


/////


///// define
`uv_size`：<samp>[uv_size](#assets.schemas-blockception.resource.ui.elements.properties.uv_size.json)</samp>


/////


///// define
`^\$.*`：<samp>[variable_definition](#assets.schemas-blockception.resource.ui.general.variables.json)</samp>


/////


////


//// define
`<any object property>`：<samp>object</samp>


////

<div class="language-text highlight"><span class="filename"><code>&lt;any object property&gt;</code></span><pre id="__code_1"><span></span></pre></div>

//// html | div.result
///// define
`type`：<samp>string</samp>

- The type of the element


/////


///// define
`control_ids`：<samp>[control_ids](#assets.schemas-blockception.resource.ui.elements.properties.control_ids.json)</samp>


/////


///// define
`control_name`：<samp>[control_name](#assets.schemas-blockception.resource.ui.elements.properties.control_name.json)</samp>


/////


///// define
`^\$.*`：<samp>[variable_definition](#assets.schemas-blockception.resource.ui.general.variables.json)</samp>


/////


////



///

