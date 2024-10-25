# Filters

> 文档版本：1.21.50.25



## 架构

```mcschema
filters:
array
{
  array "<any array element>" : opt
  {
     "<any array element>" : opt
  }
  object "<any array element>" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
  actor_health "<any array element>"
  all_slots_empty "<any array element>"
  any_slots_empty "<any array element>"
  bool_property "<any array element>"
  clock_time "<any array element>"
  distance_to_nearest_player "<any array element>"
  enum_property "<any array element>"
  float_property "<any array element>"
  has_ability "<any array element>"
  has_biome_tag "<any array element>"
  has_component "<any array element>"
  has_container_open "<any array element>"
  has_damage "<any array element>"
  has_equipment "<any array element>"
  has_damaged_equipment "<any array element>"
  has_mob_effect "<any array element>"
  has_nametag "<any array element>"
  has_property "<any array element>"
  has_ranged_weapon "<any array element>"
  has_silk_touch "<any array element>"
  has_tag "<any array element>"
  has_target "<any array element>"
  has_trade_supply "<any array element>"
  hourly_clock_time "<any array element>"
  in_block "<any array element>"
  in_caravan "<any array element>"
  in_clouds "<any array element>"
  in_contact_with_water "<any array element>"
  in_lava "<any array element>"
  in_nether "<any array element>"
  in_overworld "<any array element>"
  in_water_or_rain "<any array element>"
  in_water "<any array element>"
  inactivity_timer "<any array element>"
  int_property "<any array element>"
  is_altitude "<any array element>"
  is_avoiding_mobs "<any array element>"
  is_biome "<any array element>"
  is_block "<any array element>"
  is_brightness "<any array element>"
  is_climbing "<any array element>"
  is_color "<any array element>"
  is_daytime "<any array element>"
  is_difficulty "<any array element>"
  is_family "<any array element>"
  is_game_rule "<any array element>"
  is_humid "<any array element>"
  is_immobile "<any array element>"
  is_in_village "<any array element>"
  is_leashed_to "<any array element>"
  is_leashed "<any array element>"
  is_mark_variant "<any array element>"
  is_missing_health "<any array element>"
  is_moving "<any array element>"
  is_moving "<any array element>"
  is_owner "<any array element>"
  is_persistent "<any array element>"
  is_riding "<any array element>"
  is_skin_id "<any array element>"
  is_sleeping "<any array element>"
  is_sneak_held "<any array element>"
  is_sneaking "<any array element>"
  is_snow_covered "<any array element>"
  is_sitting "<any array element>"
  is_target "<any array element>"
  is_temperature_type "<any array element>"
  is_temperature_value "<any array element>"
  is_underground "<any array element>"
  is_underwater "<any array element>"
  is_variant "<any array element>"
  is_visible "<any array element>"
  is_waterlogged "<any array element>"
  light_level "<any array element>"
  moon_intensity "<any array element>"
  moon_phase "<any array element>"
  on_ground "<any array element>"
  on_ladder "<any array element>"
  random_chance "<any array element>"
  rider_count "<any array element>"
  surface_mob "<any array element>"
  taking_fire_damage "<any array element>"
  target_distance "<any array element>"
  owner_distance "<any array element>"
  trusts "<any array element>"
  weather_at_position "<any array element>"
  weather "<any array element>"
  object "<any array element>" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
}

```

/// html | div.result
//// define
`<any array element>`


////


///


```mcschema
filters:
{
  array "all_of" : opt
  {
     "<any array element>" : opt
  }
  object "all_of" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
  actor_health "all_of"
  all_slots_empty "all_of"
  any_slots_empty "all_of"
  bool_property "all_of"
  clock_time "all_of"
  distance_to_nearest_player "all_of"
  enum_property "all_of"
  float_property "all_of"
  has_ability "all_of"
  has_biome_tag "all_of"
  has_component "all_of"
  has_container_open "all_of"
  has_damage "all_of"
  has_equipment "all_of"
  has_damaged_equipment "all_of"
  has_mob_effect "all_of"
  has_nametag "all_of"
  has_property "all_of"
  has_ranged_weapon "all_of"
  has_silk_touch "all_of"
  has_tag "all_of"
  has_target "all_of"
  has_trade_supply "all_of"
  hourly_clock_time "all_of"
  in_block "all_of"
  in_caravan "all_of"
  in_clouds "all_of"
  in_contact_with_water "all_of"
  in_lava "all_of"
  in_nether "all_of"
  in_overworld "all_of"
  in_water_or_rain "all_of"
  in_water "all_of"
  inactivity_timer "all_of"
  int_property "all_of"
  is_altitude "all_of"
  is_avoiding_mobs "all_of"
  is_biome "all_of"
  is_block "all_of"
  is_brightness "all_of"
  is_climbing "all_of"
  is_color "all_of"
  is_daytime "all_of"
  is_difficulty "all_of"
  is_family "all_of"
  is_game_rule "all_of"
  is_humid "all_of"
  is_immobile "all_of"
  is_in_village "all_of"
  is_leashed_to "all_of"
  is_leashed "all_of"
  is_mark_variant "all_of"
  is_missing_health "all_of"
  is_moving "all_of"
  is_moving "all_of"
  is_owner "all_of"
  is_persistent "all_of"
  is_riding "all_of"
  is_skin_id "all_of"
  is_sleeping "all_of"
  is_sneak_held "all_of"
  is_sneaking "all_of"
  is_snow_covered "all_of"
  is_sitting "all_of"
  is_target "all_of"
  is_temperature_type "all_of"
  is_temperature_value "all_of"
  is_underground "all_of"
  is_underwater "all_of"
  is_variant "all_of"
  is_visible "all_of"
  is_waterlogged "all_of"
  light_level "all_of"
  moon_intensity "all_of"
  moon_phase "all_of"
  on_ground "all_of"
  on_ladder "all_of"
  random_chance "all_of"
  rider_count "all_of"
  surface_mob "all_of"
  taking_fire_damage "all_of"
  target_distance "all_of"
  owner_distance "all_of"
  trusts "all_of"
  weather_at_position "all_of"
  weather "all_of"
  object "all_of" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
   "any_of" : opt
   "none_of" : opt
}

```

/// html | div.result
//// define
`all_of`

- All tests in an `all_of` group must pass in order for the group to pass.


////


//// define
`any_of`

- One or more tests in an `any_of` group must pass in order for the group to pass.


////


//// define
`none_of`

- All tests in a `none_of` group must fail in order for the group to pass.


////


///


```mcschema
actor_health:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests the health of the subject.


////


//// define
`operator`：<samp>operator</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json}

- (Optional) The comparison to apply with `value`.


////

```mcschema
operator:
string

```

//// html | div.result

////



//// define
`subject`：<samp>subject</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json}

- (Optional) The subject of this filter test.


////

```mcschema
subject:
string

```

//// html | div.result

////



//// define
`value`：<samp>integer</samp>

- (Required) A integer value.


////


///




```mcschema
all_slots_empty:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  equipment_location "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the designated equipment location for the subject entity is completely empty.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>equipment_location</samp> {#assets.schemas-blockception.behavior.entities.filters.filters.types.equipment_location.json}

- The equipment location to test.


////

```mcschema
equipment_location:
string

```

//// html | div.result

////



///




```mcschema
any_slots_empty:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  equipment_location "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the designated equipment location for the subject entity has any empty slot.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>[equipment_location](#assets.schemas-blockception.behavior.entities.filters.filters.types.equipment_location.json)</samp>

- The equipment location to test.


////


///




```mcschema
bool_property:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the bool actor property matches the value provided.


////


//// define
`domain`：<samp>string</samp>

- (Required) The property name to look for


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>boolean</samp>

- true or false.


////


///




```mcschema
clock_time:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Compares the current time with a float value in the range (0.0, 1.0).
0.0= Noon
0.25= Sunset
0.5= Midnight
0.75= Sunrise


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>number</samp>

- (Required) A floating point value.


////


///




```mcschema
distance_to_nearest_player:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Compares the distance to the nearest Player with a float value.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- (Required) A floating point value.


////


///




```mcschema
enum_property:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the enum actor property matches the value provided.


////


//// define
`domain`：<samp>string</samp>

- (Required) The property name to look for


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>string</samp>

- (Required) A string value.


////


///




```mcschema
float_property:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the float actor property matches the value provided.


////


//// define
`domain`：<samp>string</samp>

- (Required) The property name to look for


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>number</samp>

- (Required) A floating point value.


////


///




```mcschema
has_ability:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity has the named ability.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- (Required) The Ability type to test.


////


///




```mcschema
has_biome_tag:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  biome_tag "value"
  biome "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests whether the biome the subject is in has the specified tag.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>biome_tag</samp> {#assets.schemas-blockception.general.vanilla.biome_tag.json}

- The tag to look for.


////

```mcschema
biome_tag:
string

```

//// html | div.result

////



//// define
`value`：<samp>biome</samp> {#assets.schemas-blockception.general.vanilla.biome.json}

- The tag to look for.


////

```mcschema
biome:
string

```

//// html | div.result

////




///




```mcschema
has_component:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity contains the named component.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- (Required) The component name to look for.


////


///




```mcschema
has_container_open:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- (Optional) true or false.


////


///




```mcschema
has_damage:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity receives the named damage type.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Damage type to test.


////


///




```mcschema
has_equipment:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  identifier "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests for the presence of a named item in the designated slot of the subject entity.


////


//// define
`domain`：<samp>string</samp>

- The equipment location to test.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>identifier</samp> {#assets.schemas-blockception.general.item.identifier.json}

- The item name to look for.


////

```mcschema
identifier:
string

```

//// html | div.result

////



///




```mcschema
has_damaged_equipment:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  identifier "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests for the presence of a damaged named item in the designated slot of the subject entity.


////


//// define
`domain`：<samp>string</samp>

- The equipment location to test.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>[identifier](#assets.schemas-blockception.general.item.identifier.json)</samp>

- The item name to look for.


////


///




```mcschema
has_mob_effect:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  effect "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests whether the Subject has the specified mob effect.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>effect</samp> {#assets.schemas-blockception.general.vanilla.effect.json}

- The specified mob effect.


////

```mcschema
effect:
string

```

//// html | div.result

////



///




```mcschema
has_nametag:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests for the presence of a named item in the designated slot of the subject entity.


////


//// define
`domain`：<samp>string</samp>

- The equipment location to test.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- The namtag to look for


////


///




```mcschema
has_property:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests for the presence of a property of the subject entity.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optionall) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>string</samp>

- (Required) The property name to look for.


////


///




```mcschema
has_ranged_weapon:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
has_silk_touch:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
has_tag:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity has the tag provided.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The tag as a string.


////


///




```mcschema
has_target:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
has_trade_supply:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests whether the target has any trade supply left. Will return false if the target cannot be traded with.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
hourly_clock_time:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Compares the current 24 hour time with an int value in the range[0, 24000].


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- (Required) An integer value set between 0 and 24000.


////


///




```mcschema
in_block:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is inside a specified Block type.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>string</samp>

- (Optional) A string value.


////


///




```mcschema
in_caravan:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity is in a caravan.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_clouds:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is in the clouds.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_contact_with_water:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity in contact with any water: water, rain, splash water bottle.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- (Optional) true or false.


////


///




```mcschema
in_lava:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is in lava.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_nether:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_overworld:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_water_or_rain:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is in water or rain.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
in_water:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is in water.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
inactivity_timer:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- The Family name to look for.


////


///




```mcschema
int_property:
{
  string "test" : opt
  string "domain" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the integer actor property matches the value provided.


////


//// define
`domain`：<samp>string</samp>

- (Required) The property name to look for


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>

- (Optional) The comparison to apply with `value`.


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>

- (Optional) The subject of this filter test.


////


//// define
`value`：<samp>integer</samp>

- (Required) A integer value.


////


///




```mcschema
is_altitude:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests the current altitude against a provided value. 0= bedrock elevation.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- The altitude value to compare with.


////


///




```mcschema
is_avoiding_mobs:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity is fleeing from other mobs.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_biome:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  biome "value"
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests whether the Subject is currently in the named biome.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>[biome](#assets.schemas-blockception.general.vanilla.biome.json)</samp>

- The biome type to test.


////


///




```mcschema
is_block:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Family name to look for.


////


///




```mcschema
is_brightness:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests the current brightness against a provided value in the range (0.0f, 1.0f).


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- The brightness value to compare with.


////


///




```mcschema
is_climbing:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity is climbing.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_color:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity is the named color.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Palette Color to test.


////


///




```mcschema
is_daytime:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true during the daylight hours.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_difficulty:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests the current difficulty level of the game.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The game's difficulty level to test.


////


///




```mcschema
is_family:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true when the subject entity is a member of the named family.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Family name to look for.


////


///




```mcschema
is_game_rule:
{
   "domain" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`domain`

- The Game Rule to test.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- Tests whether a named game rule is active.


////


///




```mcschema
is_humid:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests whether the Subject is in an area with humidity.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_immobile:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_in_village:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_leashed_to:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_leashed:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_mark_variant:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- The altitude value to compare with.


////


///




```mcschema
is_missing_health:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_moving:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///







```mcschema
is_owner:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_persistent:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_riding:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_skin_id:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- The altitude value to compare with.


////


///




```mcschema
is_sleeping:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_sneak_held:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_sneaking:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_snow_covered:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_sitting:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Returns true if the subject entity is sitting.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_target:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_temperature_type:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Biome temperature catagory to test.


////


///




```mcschema
is_temperature_value:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- The Biome temperature value to compare with.


////


///




```mcschema
is_underground:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_underwater:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_variant:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- The altitude value to compare with.


////


///




```mcschema
is_visible:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
is_waterlogged:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- true or false.


////


///




```mcschema
light_level:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- An integer value.


////


///




```mcschema
moon_intensity:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- A floating point value.


////


///




```mcschema
moon_phase:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- An integer value.


////


///




```mcschema
on_ground:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
on_ladder:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
random_chance:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- An integer value.


////


///




```mcschema
rider_count:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  integer "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>integer</samp>

- An integer value.


////


///




```mcschema
surface_mob:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
taking_fire_damage:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- Tests if the subject is taking fire damage. Requires the damage_sensor component


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
target_distance:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- (Required) A floating point value.


////


///




```mcschema
owner_distance:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  number "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>number</samp>

- (Required) A floating point value.


////


///




```mcschema
trusts:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  boolean "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>boolean</samp>

- True or false.


////


///




```mcschema
weather_at_position:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Family name to look for.


////


///




```mcschema
weather:
{
  string "test" : opt
  operator "operator"
  subject "subject"
  string "value" : opt
}

```

/// html | div.result
//// define
`test`：<samp>string</samp>

- The test property.


////


//// define
`operator`：<samp>[operator](#assets.schemas-blockception.behavior.entities.filters.filters.types.operator.json)</samp>


////


//// define
`subject`：<samp>[subject](#assets.schemas-blockception.behavior.entities.filters.filters.types.subject.json)</samp>


////


//// define
`value`：<samp>string</samp>

- The Family name to look for.


////


///




```mcschema
filters:
{
  array "all_of" : opt
  {
     "<any array element>" : opt
  }
  object "all_of" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
  actor_health "all_of"
  all_slots_empty "all_of"
  any_slots_empty "all_of"
  bool_property "all_of"
  clock_time "all_of"
  distance_to_nearest_player "all_of"
  enum_property "all_of"
  float_property "all_of"
  has_ability "all_of"
  has_biome_tag "all_of"
  has_component "all_of"
  has_container_open "all_of"
  has_damage "all_of"
  has_equipment "all_of"
  has_damaged_equipment "all_of"
  has_mob_effect "all_of"
  has_nametag "all_of"
  has_property "all_of"
  has_ranged_weapon "all_of"
  has_silk_touch "all_of"
  has_tag "all_of"
  has_target "all_of"
  has_trade_supply "all_of"
  hourly_clock_time "all_of"
  in_block "all_of"
  in_caravan "all_of"
  in_clouds "all_of"
  in_contact_with_water "all_of"
  in_lava "all_of"
  in_nether "all_of"
  in_overworld "all_of"
  in_water_or_rain "all_of"
  in_water "all_of"
  inactivity_timer "all_of"
  int_property "all_of"
  is_altitude "all_of"
  is_avoiding_mobs "all_of"
  is_biome "all_of"
  is_block "all_of"
  is_brightness "all_of"
  is_climbing "all_of"
  is_color "all_of"
  is_daytime "all_of"
  is_difficulty "all_of"
  is_family "all_of"
  is_game_rule "all_of"
  is_humid "all_of"
  is_immobile "all_of"
  is_in_village "all_of"
  is_leashed_to "all_of"
  is_leashed "all_of"
  is_mark_variant "all_of"
  is_missing_health "all_of"
  is_moving "all_of"
  is_moving "all_of"
  is_owner "all_of"
  is_persistent "all_of"
  is_riding "all_of"
  is_skin_id "all_of"
  is_sleeping "all_of"
  is_sneak_held "all_of"
  is_sneaking "all_of"
  is_snow_covered "all_of"
  is_sitting "all_of"
  is_target "all_of"
  is_temperature_type "all_of"
  is_temperature_value "all_of"
  is_underground "all_of"
  is_underwater "all_of"
  is_variant "all_of"
  is_visible "all_of"
  is_waterlogged "all_of"
  light_level "all_of"
  moon_intensity "all_of"
  moon_phase "all_of"
  on_ground "all_of"
  on_ladder "all_of"
  random_chance "all_of"
  rider_count "all_of"
  surface_mob "all_of"
  taking_fire_damage "all_of"
  target_distance "all_of"
  owner_distance "all_of"
  trusts "all_of"
  weather_at_position "all_of"
  weather "all_of"
  object "all_of" : opt
  {
     "all_of" : opt
     "any_of" : opt
     "none_of" : opt
  }
   "any_of" : opt
   "none_of" : opt
}

```

/// html | div.result
//// define
`all_of`

- All tests in an `all_of` group must pass in order for the group to pass.


////


//// define
`any_of`

- One or more tests in an `any_of` group must pass in order for the group to pass.


////


//// define
`none_of`

- All tests in a `none_of` group must fail in order for the group to pass.


////


///




