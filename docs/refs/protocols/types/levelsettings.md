# <!-- md:samp LevelSettings -->

> 文档版本：r/20_u7<br/>协议版本：662

<!-- md:samp LevelSettings -->类型。

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
41 -> 49
23 -> 50
50 -> 51
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
124 -> 130
23 -> 131
131 -> 132
23 -> 133
133 -> 134
23 -> 135
135 -> 136

23 [label="LevelSettings",comment="name: \"LevelSettings\", typeName: \"\", id: 23, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
24 [label="Seed",comment="name: \"Seed\", typeName: \"\", id: 24, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
25 [label="unsigned int64",comment="name: \"unsigned int64\", typeName: \"\", id: 25, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
26 [label="Spawn Settings",comment="name: \"Spawn Settings\", typeName: \"SpawnSettings\", id: 26, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
34 [label="SpawnSettings",comment="name: \"SpawnSettings\", typeName: \"\", id: 34, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
35 [label="Generator Type",comment="name: \"Generator Type\", typeName: \"\", id: 35, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GeneratorType\""];
36 [label="varint",comment="name: \"varint\", typeName: \"\", id: 36, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
37 [label="Game Type",comment="name: \"Game Type\", typeName: \"\", id: 37, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: GameType\""];
38 [label="varint",comment="name: \"varint\", typeName: \"\", id: 38, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
39 [label="Game Difficulty",comment="name: \"Game Difficulty\", typeName: \"\", id: 39, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Difficulty\""];
40 [label="varint",comment="name: \"varint\", typeName: \"\", id: 40, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
41 [label="Default Spawn Block Position",comment="name: \"Default Spawn Block Position\", typeName: \"NetworkBlockPosition\", id: 41, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
49 [label="NetworkBlockPosition",comment="name: \"NetworkBlockPosition\", typeName: \"\", id: 49, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
50 [label="Achievements Disabled",comment="name: \"Achievements Disabled\", typeName: \"\", id: 50, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
51 [label="bool",comment="name: \"bool\", typeName: \"\", id: 51, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
52 [label="Editor World Type",comment="name: \"Editor World Type\", typeName: \"\", id: 52, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Editor::WorldType\""];
53 [label="varint",comment="name: \"varint\", typeName: \"\", id: 53, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
54 [label="is Created In Editor",comment="name: \"is Created In Editor\", typeName: \"\", id: 54, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
55 [label="bool",comment="name: \"bool\", typeName: \"\", id: 55, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
56 [label="is Exported From Editor",comment="name: \"is Exported From Editor\", typeName: \"\", id: 56, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
57 [label="bool",comment="name: \"bool\", typeName: \"\", id: 57, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
58 [label="Day Cycle Stop Time",comment="name: \"Day Cycle Stop Time\", typeName: \"\", id: 58, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
59 [label="varint",comment="name: \"varint\", typeName: \"\", id: 59, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
60 [label="Education Edition Offer",comment="name: \"Education Edition Offer\", typeName: \"\", id: 60, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: EducationEditionOffer\""];
61 [label="varint",comment="name: \"varint\", typeName: \"\", id: 61, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
62 [label="Are Education features enabled?",comment="name: \"Are Education features enabled?\", typeName: \"\", id: 62, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
63 [label="bool",comment="name: \"bool\", typeName: \"\", id: 63, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
64 [label="Education product id",comment="name: \"Education product id\", typeName: \"\", id: 64, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
65 [label="string",comment="name: \"string\", typeName: \"\", id: 65, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
66 [label="Rain Level",comment="name: \"Rain Level\", typeName: \"\", id: 66, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
67 [label="float",comment="name: \"float\", typeName: \"\", id: 67, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
68 [label="Lightning Level",comment="name: \"Lightning Level\", typeName: \"\", id: 68, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
69 [label="float",comment="name: \"float\", typeName: \"\", id: 69, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
70 [label="Has confirmed Platform Locked Content",comment="name: \"Has confirmed Platform Locked Content\", typeName: \"\", id: 70, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
71 [label="bool",comment="name: \"bool\", typeName: \"\", id: 71, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
72 [label="Was Multiplayer intended to be enabled?",comment="name: \"Was Multiplayer intended to be enabled?\", typeName: \"\", id: 72, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
73 [label="bool",comment="name: \"bool\", typeName: \"\", id: 73, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
74 [label="Was LAN broadcasting intended to be enabled?",comment="name: \"Was LAN broadcasting intended to be enabled?\", typeName: \"\", id: 74, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
75 [label="bool",comment="name: \"bool\", typeName: \"\", id: 75, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
76 [label="Xbox Live Broadcast Setting",comment="name: \"Xbox Live Broadcast Setting\", typeName: \"\", id: 76, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Social::GamePublishSetting\""];
77 [label="varint",comment="name: \"varint\", typeName: \"\", id: 77, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
78 [label="Platform Broadcast Setting",comment="name: \"Platform Broadcast Setting\", typeName: \"\", id: 78, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: Social::GamePublishSetting\""];
79 [label="varint",comment="name: \"varint\", typeName: \"\", id: 79, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
80 [label="Commands Enabled",comment="name: \"Commands Enabled\", typeName: \"\", id: 80, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
81 [label="bool",comment="name: \"bool\", typeName: \"\", id: 81, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
82 [label="Texture Packs Required",comment="name: \"Texture Packs Required\", typeName: \"\", id: 82, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
83 [label="bool",comment="name: \"bool\", typeName: \"\", id: 83, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
84 [label="Rule Data",comment="name: \"Rule Data\", typeName: \"GameRulesChangedPacketData\", id: 84, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
85 [label="GameRulesChangedPacketData",comment="name: \"GameRulesChangedPacketData\", typeName: \"\", id: 85, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
86 [label="Experiments",comment="name: \"Experiments\", typeName: \"Experiments\", id: 86, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
87 [label="Experiments",comment="name: \"Experiments\", typeName: \"\", id: 87, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
88 [label="Has Bonus Chest Enabled?",comment="name: \"Has Bonus Chest Enabled?\", typeName: \"\", id: 88, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
89 [label="bool",comment="name: \"bool\", typeName: \"\", id: 89, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
90 [label="Start with Map Enabled?",comment="name: \"Start with Map Enabled?\", typeName: \"\", id: 90, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
91 [label="bool",comment="name: \"bool\", typeName: \"\", id: 91, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
92 [label="Player Permissions",comment="name: \"Player Permissions\", typeName: \"\", id: 92, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: PlayerPermissionLevel\""];
93 [label="byte",comment="name: \"byte\", typeName: \"\", id: 93, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
94 [label="Server Chunk Tick Range",comment="name: \"Server Chunk Tick Range\", typeName: \"\", id: 94, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
95 [label="int",comment="name: \"int\", typeName: \"\", id: 95, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
96 [label="Has locked behavior pack?",comment="name: \"Has locked behavior pack?\", typeName: \"\", id: 96, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
97 [label="bool",comment="name: \"bool\", typeName: \"\", id: 97, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
98 [label="Has locked resource pack?",comment="name: \"Has locked resource pack?\", typeName: \"\", id: 98, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
99 [label="bool",comment="name: \"bool\", typeName: \"\", id: 99, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
100 [label="Is from locked template?",comment="name: \"Is from locked template?\", typeName: \"\", id: 100, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
101 [label="bool",comment="name: \"bool\", typeName: \"\", id: 101, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
102 [label="Use Msa Gamertags Only?",comment="name: \"Use Msa Gamertags Only?\", typeName: \"\", id: 102, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
103 [label="bool",comment="name: \"bool\", typeName: \"\", id: 103, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
104 [label="Indicates if this world was created from a template.",comment="name: \"Indicates if this world was created from a template.\", typeName: \"\", id: 104, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false.\""];
105 [label="bool",comment="name: \"bool\", typeName: \"\", id: 105, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
106 [label="Indicates if this world is a template with locked settings.",comment="name: \"Indicates if this world is a template with locked settings.\", typeName: \"\", id: 106, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false.\""];
107 [label="bool",comment="name: \"bool\", typeName: \"\", id: 107, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
108 [label="Only spawn v1 villagers",comment="name: \"Only spawn v1 villagers\", typeName: \"\", id: 108, branchId: 0, recurseId: -1, attributes: 0, notes: \"This was added for the Village & Pillage update, marking worlds where V1 villagers shouldn't update to V2, and only V1 villagers should be used in the world. This was done for Marketplace content.\""];
109 [label="bool",comment="name: \"bool\", typeName: \"\", id: 109, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
110 [label="PersonaDisabled?",comment="name: \"PersonaDisabled?\", typeName: \"\", id: 110, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
111 [label="bool",comment="name: \"bool\", typeName: \"\", id: 111, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
112 [label="CustomSkinsDisabled?",comment="name: \"CustomSkinsDisabled?\", typeName: \"\", id: 112, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
113 [label="bool",comment="name: \"bool\", typeName: \"\", id: 113, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
114 [label="Emote Chat Muted",comment="name: \"Emote Chat Muted\", typeName: \"\", id: 114, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
115 [label="bool",comment="name: \"bool\", typeName: \"\", id: 115, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
116 [label="Base Game Version",comment="name: \"Base Game Version\", typeName: \"BaseGameVersion\", id: 116, branchId: 0, recurseId: -1, attributes: 256, notes: \"Version of vanilla gameplay that will be used with this world.\""];
117 [label="BaseGameVersion",comment="name: \"BaseGameVersion\", typeName: \"\", id: 117, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
118 [label="Limited World Width",comment="name: \"Limited World Width\", typeName: \"\", id: 118, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
119 [label="int",comment="name: \"int\", typeName: \"\", id: 119, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
120 [label="Limited World Depth",comment="name: \"Limited World Depth\", typeName: \"\", id: 120, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
121 [label="int",comment="name: \"int\", typeName: \"\", id: 121, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
122 [label="Nether type",comment="name: \"Nether type\", typeName: \"\", id: 122, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
123 [label="bool",comment="name: \"bool\", typeName: \"\", id: 123, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
124 [label="Edu Shared Uri Resource",comment="name: \"Edu Shared Uri Resource\", typeName: \"EduSharedUriResource\", id: 124, branchId: 0, recurseId: -1, attributes: 256, notes: \"\""];
130 [label="EduSharedUriResource",comment="name: \"EduSharedUriResource\", typeName: \"\", id: 130, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
131 [label="Override force experimental gameplay has value",comment="name: \"Override force experimental gameplay has value\", typeName: \"\", id: 131, branchId: 0, recurseId: -1, attributes: 0, notes: \"For servers this should always be false\""];
132 [label="bool",comment="name: \"bool\", typeName: \"\", id: 132, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
133 [label="ChatRestriction Level",comment="name: \"ChatRestriction Level\", typeName: \"\", id: 133, branchId: 0, recurseId: -1, attributes: 0, notes: \"enumeration: ChatRestrictionLevel\""];
134 [label="byte",comment="name: \"byte\", typeName: \"\", id: 134, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
135 [label="DisablePlayerInteractions ?",comment="name: \"DisablePlayerInteractions ?\", typeName: \"\", id: 135, branchId: 0, recurseId: -1, attributes: 0, notes: \"\""];
136 [label="bool",comment="name: \"bool\", typeName: \"\", id: 136, branchId: 0, recurseId: -1, attributes: 512, notes: \"\""];
{ rank = max;25;34;36;38;40;49;51;53;55;57;59;61;63;65;67;69;71;73;75;77;79;81;83;85;87;89;91;93;95;97;99;101;103;105;107;109;111;113;115;117;119;121;123;130;132;134;136}

}

```

## 字段

```title='LevelSettings'
[seed][spawn_settings][generator_type][game_type][game_difficulty][default_spawn_block_position][achievements_disabled][editor_world_type][is_created_in_editor][is_exported_from_editor][day_cycle_stop_time][education_edition_offer][are_education_features_enabled?][education_product_id][rain_level][lightning_level][has_confirmed_platform_locked_content][was_multiplayer_intended_to_be_enabled?][was_lan_broadcasting_intended_to_be_enabled?][xbox_live_broadcast_setting][platform_broadcast_setting][commands_enabled][texture_packs_required][rule_data][experiments][has_bonus_chest_enabled?][start_with_map_enabled?][player_permissions][server_chunk_tick_range][has_locked_behavior_pack?][has_locked_resource_pack?][is_from_locked_template?][use_msa_gamertags_only?][indicates_if_this_world_was_created_from_a_template.][indicates_if_this_world_is_a_template_with_locked_settings.][only_spawn_v1_villagers][personadisabled?][customskinsdisabled?][emote_chat_muted][base_game_version][limited_world_width][limited_world_depth][nether_type][edu_shared_uri_resource][override_force_experimental_gameplay_has_value][chatrestriction_level][disableplayerinteractions_?]
```

/// html | div.result
//// define
Seed：<!-- md:samp unsigned int64 -->

- 基本类型。


////
//// define
Spawn Settings：[<!-- md:samp SpawnSettings -->](../types/spawnsettings.md)

- 特殊类型。


////
//// define
Generator Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Legacy`|`0`||
  |`Overworld`|`1`||
  |`Flat`|`2`||
  |`Nether`|`3`||
  |`TheEnd`|`4`||
  |`Void`|`5`||
  |`Undefined`|`6`||



////
//// define
Game Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Undefined`|`-1`||
  |`Survival`|`0`||
  |`Creative`|`1`||
  |`Adventure`|`2`||
  |`Default`|`5`||
  |`Spectator`|`6`||
  |`WorldDefault`|`Survival`||



////
//// define
Game Difficulty：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Peaceful`|`0`||
  |`Easy`|`1`||
  |`Normal`|`2`||
  |`Hard`|`3`||
  |`Count`|`4`||
  |`Unknown`|`5`||



////
//// define
Default Spawn Block Position：[<!-- md:samp NetworkBlockPosition -->](../types/networkblockposition.md)

- 特殊类型。


////
//// define
Achievements Disabled：<!-- md:samp bool -->

- 基本类型。


////
//// define
Editor World Type：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NonEditor`|`0`||
  |`EditorProject`|`1`||
  |`EditorTestLevel`|`2`||



////
//// define
is Created In Editor：<!-- md:samp bool -->

- 基本类型。


////
//// define
is Exported From Editor：<!-- md:samp bool -->

- 基本类型。


////
//// define
Day Cycle Stop Time：<!-- md:samp varint -->

- 基本类型。


////
//// define
Education Edition Offer：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`RestOfWorld`|`1`||
  |`China_Deprecated`|`2`||



////
//// define
Are Education features enabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Education product id：[<!-- md:samp string -->](../types/string.md)

- 特殊类型。


////
//// define
Rain Level：<!-- md:samp float -->

- 基本类型。


////
//// define
Lightning Level：<!-- md:samp float -->

- 基本类型。


////
//// define
Has confirmed Platform Locked Content：<!-- md:samp bool -->

- 基本类型。


////
//// define
Was Multiplayer intended to be enabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Was LAN broadcasting intended to be enabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Xbox Live Broadcast Setting：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoMultiPlay`|`0`||
  |`InviteOnly`|`1`||
  |`FriendsOnly`|`2`||
  |`FriendsOfFriends`|`3`||
  |`Public`|`4`||



////
//// define
Platform Broadcast Setting：<!-- md:samp varint -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`NoMultiPlay`|`0`||
  |`InviteOnly`|`1`||
  |`FriendsOnly`|`2`||
  |`FriendsOfFriends`|`3`||
  |`Public`|`4`||



////
//// define
Commands Enabled：<!-- md:samp bool -->

- 基本类型。


////
//// define
Texture Packs Required：<!-- md:samp bool -->

- 基本类型。


////
//// define
Rule Data：[<!-- md:samp GameRulesChangedPacketData -->](../types/gameruleschangedpacketdata.md)

- 特殊类型。


////
//// define
Experiments：[<!-- md:samp Experiments -->](../types/experiments.md)

- 特殊类型。


////
//// define
Has Bonus Chest Enabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Start with Map Enabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Player Permissions：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`Visitor`|`0`||
  |`Member`|`1`||
  |`Operator`|`2`||
  |`Custom`|`3`||



////
//// define
Server Chunk Tick Range：<!-- md:samp int -->

- 基本类型。


////
//// define
Has locked behavior pack?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Has locked resource pack?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Is from locked template?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Use Msa Gamertags Only?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Indicates if this world was created from a template.：<!-- md:samp bool -->

- 基本类型。For servers this should always be false.


////
//// define
Indicates if this world is a template with locked settings.：<!-- md:samp bool -->

- 基本类型。For servers this should always be false.


////
//// define
Only spawn v1 villagers：<!-- md:samp bool -->

- 基本类型。This was added for the Village & Pillage update, marking worlds where V1 villagers shouldn't update to V2, and only V1 villagers should be used in the world. This was done for Marketplace content.


////
//// define
PersonaDisabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
CustomSkinsDisabled?：<!-- md:samp bool -->

- 基本类型。


////
//// define
Emote Chat Muted：<!-- md:samp bool -->

- 基本类型。


////
//// define
Base Game Version：[<!-- md:samp BaseGameVersion -->](../types/basegameversion.md)

- 特殊类型。Version of vanilla gameplay that will be used with this world.


////
//// define
Limited World Width：<!-- md:samp int -->

- 基本类型。


////
//// define
Limited World Depth：<!-- md:samp int -->

- 基本类型。


////
//// define
Nether type：<!-- md:samp bool -->

- 基本类型。


////
//// define
Edu Shared Uri Resource：[<!-- md:samp EduSharedUriResource -->](../types/edushareduriresource.md)

- 特殊类型。


////
//// define
Override force experimental gameplay has value：<!-- md:samp bool -->

- 基本类型。For servers this should always be false


////
//// define
ChatRestriction Level：<!-- md:samp byte -->

- 基本类型枚举。枚举值如下：

  |键|值|描述|
  |---|---|---|
  |`None`|`0`||
  |`Dropped`|`1`||
  |`Disabled`|`2`||



////
//// define
DisablePlayerInteractions ?：<!-- md:samp bool -->

- 基本类型。


////

///
