# <!-- md:samp LevelSettings -->

> 文档版本：r/21_u3<br/>协议版本：729

<!-- md:samp LevelSettings -->类型。该类型用于protocol.type.levelsettings.description

## 结构

```viz
digraph "LevelSettings" {
rankdir = LR
23
23 -> 24
24 -> 25
23 -> 26
26 -> 34
23 -> 35
35 -> 36
23 -> 37
37 -> 38
23 -> 39
39 -> 40
23 -> 41
41 -> 42
23 -> 43
43 -> 51
23 -> 52
52 -> 53
23 -> 54
54 -> 55
23 -> 56
56 -> 57
23 -> 58
58 -> 59
23 -> 60
60 -> 61
23 -> 62
62 -> 63
23 -> 64
64 -> 65
23 -> 66
66 -> 67
23 -> 68
68 -> 69
23 -> 70
70 -> 71
23 -> 72
72 -> 73
23 -> 74
74 -> 75
23 -> 76
76 -> 77
23 -> 78
78 -> 79
23 -> 80
80 -> 81
23 -> 82
82 -> 83
23 -> 84
84 -> 85
23 -> 86
86 -> 87
23 -> 88
88 -> 89
23 -> 90
90 -> 91
23 -> 92
92 -> 93
23 -> 94
94 -> 95
23 -> 96
96 -> 97
23 -> 98
98 -> 99
23 -> 100
100 -> 101
23 -> 102
102 -> 103
23 -> 104
104 -> 105
23 -> 106
106 -> 107
23 -> 108
108 -> 109
23 -> 110
110 -> 111
23 -> 112
112 -> 113
23 -> 114
114 -> 115
23 -> 116
116 -> 117
23 -> 118
118 -> 119
23 -> 120
120 -> 121
23 -> 122
122 -> 123
23 -> 124
124 -> 125
23 -> 126
126 -> 132
23 -> 133
133 -> 134
23 -> 135
135 -> 136
23 -> 137
137 -> 138
23 -> 139
139 -> 140
23 -> 141
141 -> 142
23 -> 143
143 -> 144

23 [label="LevelSettings",comment="name: \"LevelSettings\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="Seed",comment="name: \"Seed\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Spawn Settings",comment="name: \"Spawn Settings\", typeName: \"SpawnSettings\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
34 [label="SpawnSettings",comment="name: \"SpawnSettings\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Generator Type",comment="name: \"Generator Type\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
36 [label="varint",comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Game Type",comment="name: \"Game Type\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
38 [label="varint",comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="is Hardcore Mode enabled?",comment="name: \"is Hardcore Mode enabled?\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
40 [label="bool",comment="name: \"bool\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Game Difficulty",comment="name: \"Game Difficulty\", typeName: \"\", id: 41, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
42 [label="varint",comment="name: \"varint\", typeName: \"\", id: 42, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
43 [label="Default Spawn Block Position",comment="name: \"Default Spawn Block Position\", typeName: \"NetworkBlockPosition\", id: 43, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
51 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
52 [label="Achievements Disabled",comment="name: \"Achievements Disabled\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
53 [label="bool",comment="name: \"bool\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
54 [label="Editor World Type",comment="name: \"Editor World Type\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
55 [label="varint",comment="name: \"varint\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
56 [label="is Created In Editor",comment="name: \"is Created In Editor\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="bool",comment="name: \"bool\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
58 [label="is Exported From Editor",comment="name: \"is Exported From Editor\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
59 [label="bool",comment="name: \"bool\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Day Cycle Stop Time",comment="name: \"Day Cycle Stop Time\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
61 [label="varint",comment="name: \"varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Education Edition Offer",comment="name: \"Education Edition Offer\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
63 [label="varint",comment="name: \"varint\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="Are Education features enabled?",comment="name: \"Are Education features enabled?\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="bool",comment="name: \"bool\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="Education product id",comment="name: \"Education product id\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
67 [label="string",comment="name: \"string\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="Rain Level",comment="name: \"Rain Level\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
69 [label="float",comment="name: \"float\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="Lightning Level",comment="name: \"Lightning Level\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
71 [label="float",comment="name: \"float\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
72 [label="Has confirmed Platform Locked Content",comment="name: \"Has confirmed Platform Locked Content\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
73 [label="bool",comment="name: \"bool\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
74 [label="Was Multiplayer intended to be enabled?",comment="name: \"Was Multiplayer intended to be enabled?\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
75 [label="bool",comment="name: \"bool\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
76 [label="Was LAN broadcasting intended to be enabled?",comment="name: \"Was LAN broadcasting intended to be enabled?\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
77 [label="bool",comment="name: \"bool\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
78 [label="Xbox Live Broadcast Setting",comment="name: \"Xbox Live Broadcast Setting\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
79 [label="varint",comment="name: \"varint\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
80 [label="Platform Broadcast Setting",comment="name: \"Platform Broadcast Setting\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
81 [label="varint",comment="name: \"varint\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
82 [label="Commands Enabled",comment="name: \"Commands Enabled\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="bool",comment="name: \"bool\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="Texture Packs Required",comment="name: \"Texture Packs Required\", typeName: \"\", id: 84, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
85 [label="bool",comment="name: \"bool\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Rule Data",comment="name: \"Rule Data\", typeName: \"GameRulesChangedPacketData\", id: 86, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
87 [label="GameRulesChangedPacketData",comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
88 [label="Experiments",comment="name: \"Experiments\", typeName: \"Experiments\", id: 88, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
89 [label="Experiments",comment="name: \"Experiments\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
90 [label="Has Bonus Chest Enabled?",comment="name: \"Has Bonus Chest Enabled?\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
91 [label="bool",comment="name: \"bool\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
92 [label="Start with Map Enabled?",comment="name: \"Start with Map Enabled?\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
93 [label="bool",comment="name: \"bool\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
94 [label="Player Permissions",comment="name: \"Player Permissions\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
95 [label="varint",comment="name: \"varint\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
96 [label="Server Chunk Tick Range",comment="name: \"Server Chunk Tick Range\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
97 [label="int",comment="name: \"int\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
98 [label="Has locked behavior pack?",comment="name: \"Has locked behavior pack?\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
99 [label="bool",comment="name: \"bool\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
100 [label="Has locked resource pack?",comment="name: \"Has locked resource pack?\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
101 [label="bool",comment="name: \"bool\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
102 [label="Is from locked template?",comment="name: \"Is from locked template?\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
103 [label="bool",comment="name: \"bool\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
104 [label="Use Msa Gamertags Only?",comment="name: \"Use Msa Gamertags Only?\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
105 [label="bool",comment="name: \"bool\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
106 [label="Indicates if this world was created from a template.",comment="name: \"Indicates if this world was created from a template.\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false.\""];
107 [label="bool",comment="name: \"bool\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
108 [label="Indicates if this world is a template with locked settings.",comment="name: \"Indicates if this world is a template with locked settings.\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false.\""];
109 [label="bool",comment="name: \"bool\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
110 [label="Only spawn v1 villagers",comment="name: \"Only spawn v1 villagers\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"This was added for the Village & Pillage update, marking worlds where V1 villagers shouldn't update to V2, and only V1 villagers should be used in the world. This was done for Marketplace content.\""];
111 [label="bool",comment="name: \"bool\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
112 [label="PersonaDisabled?",comment="name: \"PersonaDisabled?\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
113 [label="bool",comment="name: \"bool\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
114 [label="CustomSkinsDisabled?",comment="name: \"CustomSkinsDisabled?\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
115 [label="bool",comment="name: \"bool\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
116 [label="Emote Chat Muted",comment="name: \"Emote Chat Muted\", typeName: \"\", id: 116, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
117 [label="bool",comment="name: \"bool\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
118 [label="Base Game Version",comment="name: \"Base Game Version\", typeName: \"BaseGameVersion\", id: 118, branchId: 0, recurseId: -1, attributes: 256, notes: \"Version of vanilla gameplay that will be used with this world.\""];
119 [label="BaseGameVersion",comment="name: \"BaseGameVersion\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
120 [label="Limited World Width",comment="name: \"Limited World Width\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="int",comment="name: \"int\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="Limited World Depth",comment="name: \"Limited World Depth\", typeName: \"\", id: 122, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
123 [label="int",comment="name: \"int\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
124 [label="Nether type",comment="name: \"Nether type\", typeName: \"\", id: 124, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
125 [label="bool",comment="name: \"bool\", typeName: \"\", id: 125, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
126 [label="Edu Shared Uri Resource",comment="name: \"Edu Shared Uri Resource\", typeName: \"EduSharedUriResource\", id: 126, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
132 [label="EduSharedUriResource",comment="name: \"EduSharedUriResource\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
133 [label="Override force experimental gameplay has value",comment="name: \"Override force experimental gameplay has value\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false\""];
134 [label="bool",comment="name: \"bool\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
135 [label="ChatRestriction Level",comment="name: \"ChatRestriction Level\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
136 [label="byte",comment="name: \"byte\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
137 [label="DisablePlayerInteractions ?",comment="name: \"DisablePlayerInteractions ?\", typeName: \"\", id: 137, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
138 [label="bool",comment="name: \"bool\", typeName: \"\", id: 138, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
139 [label="Server Identifier",comment="name: \"Server Identifier\", typeName: \"\", id: 139, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
140 [label="string",comment="name: \"string\", typeName: \"\", id: 140, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
141 [label="World Identifier from the server.",comment="name: \"World Identifier from the server.\", typeName: \"\", id: 141, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
142 [label="string",comment="name: \"string\", typeName: \"\", id: 142, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
143 [label="Scenario Identifier from the server.",comment="name: \"Scenario Identifier from the server.\", typeName: \"\", id: 143, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
144 [label="string",comment="name: \"string\", typeName: \"\", id: 144, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;25;34;36;38;40;42;51;53;55;57;59;61;63;65;67;69;71;73;75;77;79;81;83;85;87;89;91;93;95;97;99;101;103;105;107;109;111;113;115;117;119;121;123;125;132;134;136;138;140;142;144}

}

```

## 字段

```title='LevelSettings'
[seed][spawn_settings][generator_type][game_type][is_hardcore_mode_enabled][game_difficulty][default_spawn_block_position][achievements_disabled][editor_world_type][is_created_in_editor][is_exported_from_editor][day_cycle_stop_time][education_edition_offer][are_education_features_enabled][education_product_id][rain_level][lightning_level][has_confirmed_platform_locked_content][was_multiplayer_intended_to_be_enabled][was_lan_broadcasting_intended_to_be_enabled][xbox_live_broadcast_setting][platform_broadcast_setting][commands_enabled][texture_packs_required][rule_data][experiments][has_bonus_chest_enabled][start_with_map_enabled][player_permissions][server_chunk_tick_range][has_locked_behavior_pack][has_locked_resource_pack][is_from_locked_template][use_msa_gamertags_only][indicates_if_this_world_was_created_from_a_template.][indicates_if_this_world_is_a_template_with_locked_settings.][only_spawn_v1_villagers][personadisabled][customskinsdisabled][emote_chat_muted][base_game_version][limited_world_width][limited_world_depth][nether_type][edu_shared_uri_resource][override_force_experimental_gameplay_has_value][chatrestriction_level][disableplayerinteractions][server_identifier][world_identifier_from_the_server.][scenario_identifier_from_the_server.]
```

/// html | div.result
//// define
Seed：<!-- md:samp unsigned int64 -->

- 基本类型。protocol.type.levelsettings.seed.description


////
//// define
Spawn Settings：[<!-- md:samp SpawnSettings -->](../types/spawnsettings.md)

- 特殊类型。protocol.type.levelsettings.spawn_settings.description


////
//// define
Generator Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.generator_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Legacy`|`0`|protocol.enum.legacy|
  |`Overworld`|`1`|protocol.enum.overworld|
  |`Flat`|`2`|protocol.enum.flat|
  |`Nether`|`3`|protocol.enum.nether|
  |`TheEnd`|`4`|protocol.enum.theend|
  |`Void`|`5`|protocol.enum.void|
  |`Undefined`|`6`|protocol.enum.undefined|



////
//// define
Game Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.game_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`|protocol.enum.undefined|
  |`Survival`|`0`|protocol.enum.survival|
  |`Creative`|`1`|protocol.enum.creative|
  |`Adventure`|`2`|protocol.enum.adventure|
  |`Default`|`5`|protocol.enum.default|
  |`Spectator`|`6`|protocol.enum.spectator|
  |`WorldDefault`|`Survival`|protocol.enum.worlddefault|



////
//// define
is Hardcore Mode enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.is_hardcore_mode_enabled.description


////
//// define
Game Difficulty：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.game_difficulty.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Peaceful`|`0`|protocol.enum.peaceful|
  |`Easy`|`1`|protocol.enum.easy|
  |`Normal`|`2`|protocol.enum.normal|
  |`Hard`|`3`|protocol.enum.hard|
  |`Count`|`4`|protocol.enum.count|
  |`Unknown`|`5`|protocol.enum.unknown|



////
//// define
Default Spawn Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。protocol.type.levelsettings.default_spawn_block_position.description


////
//// define
Achievements Disabled：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.achievements_disabled.description


////
//// define
Editor World Type：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.editor_world_type.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NonEditor`|`0`|protocol.enum.noneditor|
  |`EditorProject`|`1`|protocol.enum.editorproject|
  |`EditorTestLevel`|`2`|protocol.enum.editortestlevel|



////
//// define
is Created In Editor：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.is_created_in_editor.description


////
//// define
is Exported From Editor：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.is_exported_from_editor.description


////
//// define
Day Cycle Stop Time：<!-- md:samp varint -->

- 基本类型。protocol.type.levelsettings.day_cycle_stop_time.description


////
//// define
Education Edition Offer：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.education_edition_offer.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`RestOfWorld`|`1`|protocol.enum.restofworld|
  |`China_Deprecated`|`2`|protocol.enum.china_deprecated|



////
//// define
Are Education features enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.are_education_features_enabled.description


////
//// define
Education product id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.levelsettings.education_product_id.description


////
//// define
Rain Level：<!-- md:samp float -->

- 基本类型。protocol.type.levelsettings.rain_level.description


////
//// define
Lightning Level：<!-- md:samp float -->

- 基本类型。protocol.type.levelsettings.lightning_level.description


////
//// define
Has confirmed Platform Locked Content：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.has_confirmed_platform_locked_content.description


////
//// define
Was Multiplayer intended to be enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.was_multiplayer_intended_to_be_enabled.description


////
//// define
Was LAN broadcasting intended to be enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.was_lan_broadcasting_intended_to_be_enabled.description


////
//// define
Xbox Live Broadcast Setting：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.xbox_live_broadcast_setting.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoMultiPlay`|`0`|protocol.enum.nomultiplay|
  |`InviteOnly`|`1`|protocol.enum.inviteonly|
  |`FriendsOnly`|`2`|protocol.enum.friendsonly|
  |`FriendsOfFriends`|`3`|protocol.enum.friendsoffriends|
  |`Public`|`4`|protocol.enum.public|



////
//// define
Platform Broadcast Setting：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.platform_broadcast_setting.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoMultiPlay`|`0`|protocol.enum.nomultiplay|
  |`InviteOnly`|`1`|protocol.enum.inviteonly|
  |`FriendsOnly`|`2`|protocol.enum.friendsonly|
  |`FriendsOfFriends`|`3`|protocol.enum.friendsoffriends|
  |`Public`|`4`|protocol.enum.public|



////
//// define
Commands Enabled：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.commands_enabled.description


////
//// define
Texture Packs Required：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.texture_packs_required.description


////
//// define
Rule Data：[<!-- md:samp GameRulesChangedPacketData -->](../types/gameruleschangedpacketdata.md)

- 特殊类型。protocol.type.levelsettings.rule_data.description


////
//// define
Experiments：[<!-- md:samp Experiments -->](../types/experiments.md)

- 特殊类型。protocol.type.levelsettings.experiments.description


////
//// define
Has Bonus Chest Enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.has_bonus_chest_enabled.description


////
//// define
Start with Map Enabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.start_with_map_enabled.description


////
//// define
Player Permissions：<!-- md:samp varint -->

- 基本类型枚举。protocol.type.levelsettings.player_permissions.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Visitor`|`0`|protocol.enum.visitor|
  |`Member`|`1`|protocol.enum.member|
  |`Operator`|`2`|protocol.enum.operator|
  |`Custom`|`3`|protocol.enum.custom|



////
//// define
Server Chunk Tick Range：<!-- md:samp int -->

- 基本类型。protocol.type.levelsettings.server_chunk_tick_range.description


////
//// define
Has locked behavior pack?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.has_locked_behavior_pack.description


////
//// define
Has locked resource pack?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.has_locked_resource_pack.description


////
//// define
Is from locked template?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.is_from_locked_template.description


////
//// define
Use Msa Gamertags Only?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.use_msa_gamertags_only.description


////
//// define
Indicates if this world was created from a template.：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.indicates_if_this_world_was_created_from_a_template..descriptionFor servers this should always be false.


////
//// define
Indicates if this world is a template with locked settings.：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.indicates_if_this_world_is_a_template_with_locked_settings..descriptionFor servers this should always be false.


////
//// define
Only spawn v1 villagers：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.only_spawn_v1_villagers.descriptionThis was added for the Village & Pillage update, marking worlds where V1 villagers shouldn't update to V2, and only V1 villagers should be used in the world. This was done for Marketplace content.


////
//// define
PersonaDisabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.personadisabled.description


////
//// define
CustomSkinsDisabled?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.customskinsdisabled.description


////
//// define
Emote Chat Muted：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.emote_chat_muted.description


////
//// define
Base Game Version：[<!-- md:samp BaseGameVersion -->](../types/basegameversion.md)

- 特殊类型。protocol.type.levelsettings.base_game_version.descriptionVersion of vanilla gameplay that will be used with this world.


////
//// define
Limited World Width：<!-- md:samp int -->

- 基本类型。protocol.type.levelsettings.limited_world_width.description


////
//// define
Limited World Depth：<!-- md:samp int -->

- 基本类型。protocol.type.levelsettings.limited_world_depth.description


////
//// define
Nether type：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.nether_type.description


////
//// define
Edu Shared Uri Resource：[<!-- md:samp EduSharedUriResource -->](../types/edushareduriresource.md)

- 特殊类型。protocol.type.levelsettings.edu_shared_uri_resource.description


////
//// define
Override force experimental gameplay has value：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.override_force_experimental_gameplay_has_value.descriptionFor servers this should always be false


////
//// define
ChatRestriction Level：<!-- md:samp byte -->

- 基本类型枚举。protocol.type.levelsettings.chatrestriction_level.description枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`|无|
  |`Dropped`|`1`|protocol.enum.dropped|
  |`Disabled`|`2`|protocol.enum.disabled|



////
//// define
DisablePlayerInteractions ?：<!-- md:samp bool -->

- 基本类型。protocol.type.levelsettings.disableplayerinteractions.description


////
//// define
Server Identifier：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.levelsettings.server_identifier.description


////
//// define
World Identifier from the server.：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.levelsettings.world_identifier_from_the_server..description


////
//// define
Scenario Identifier from the server.：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。protocol.type.levelsettings.scenario_identifier_from_the_server..description


////

///

