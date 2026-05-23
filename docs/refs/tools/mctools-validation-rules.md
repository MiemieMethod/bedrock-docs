# 创作者工具内容校验规则

本文整理Minecraft Creator Tools官方“内容校验规则参考”中的全部规则组，用于在开发附加包、皮肤包与世界模板时快速定位规则ID、严重性和自动修复能力。

数据来源：`Microsoft Learn/creator/Reference/Content/MCToolsValReference`。

## 严重性标记

| 标记 | 含义 |
| --- | --- |
| 🔴Error | 必须修复的问题，通常会导致内容无法正确加载或发布。 |
| 🟡Warning | 建议修复的问题，可能导致兼容性或稳定性风险。 |
| 🔵Recommendation | 建议遵循的最佳实践项。 |
| ℹ️Info | 信息项，用于输出统计或状态摘要。 |

## 规则组总览

| 规则组 | 源文件 | 规则数 | 官方说明 |
| --- | --- | ---: | --- |
| Base Game Version | `basegamever.md` | 9 | Validates base_game_version in world template manifests and checks that it... |
| Blocks Catalog | `blockscat.md` | 4 | Validates blocks.json catalog files in resource packs. Checks for unused block... |
| Coop Item Naming | `caddonireq.md` | 17 | Validates individual content items against Cooperative Add-On naming... |
| Coop Add-On Requirements | `caddonreq.md` | 17 | A set of requirements for cooperative Add-On projects. See... |
| Beta Features | `cbfg.md` | 3 | Validates that add-on content does not use beta features flags. The... |
| Deprecated Features | `checkfeaturedeprecation.md` | 4 | Checks for deprecated features, blocks, and textures that may be removed in... |
| Manifest Validation | `chkmanif.md` | 35 | Comprehensive validation of pack manifest.json files. Validates format version,... |
| Community JSON Schema Validation | `comjson.md` | 1 | Validates JSON files against their corresponding schemas based on item type.... |
| Pack Icon | `cpackicon.md` | 4 | Validates behavior and resource pack icons (pack_icon.png) for correct format,... |
| Particle Identifiers | `cparti.md` | 3 | Validates particle effect identifiers for proper namespace formatting. Particle... |
| Skin Pack | `cspj.md` | 18 | Validates skin pack content including skins.json structure, skin textures,... |
| World Icon | `cwi.md` | 4 | Validates world template icons (world_icon.jpeg) for correct format, size, and... |
| Entity Type | `entitytype.md` | 12 | Validates entity type definitions in behavior packs. Checks format_version... |
| Experimental Flags | `expflag.md` | 3 | Validates experimental flags in world templates. Experiments that were enabled... |
| Forbidden Files | `forbfile.md` | 4 | Validates that packs only contain files with allowed extensions and do not... |
| Format Version | `formatver.md` | 45 | Validates format_version fields across various Minecraft JSON definition files... |
| Geometry Format | `geofmt.md` | 2 | Validates model geometry files for format compatibility and restricted... |
| Model Geometry | `geometry.md` | 4 | Validates and analyzes model geometry files (.geo.json) for blocks, entities,... |
| Content Counts | `items.md` | 2 | Provides counts of various content types found in the project including packs,... |
| Item Types | `itemtype.md` | 12 | Validates behavior pack item type definitions including format versions,... |
| JSON Schema Validation | `json.md` | 1 | Validates JSON files against official JSON schemas located at public/schemas.... |
| JSON Form Structure Validation | `jsonf.md` | 17 | Validates JSON files against Minecraft documentation-derived form schemas.... |
| Content Tags | `jsontags.md` | 11 | Tracks content types and component usage across JSON files in the project. Used... |
| Language Files | `langfiles.md` | 5 | Validates that localization files (.lang) and the languages.json catalog are... |
| File Size/Lines | `linesize.md` | 0 | Aggregates file size and line count statistics for all project items, broken... |
| MC Functions | `mcfunction.md` | 2 | Validates .mcfunction files for correct command syntax and formatting.... |
| Min Engine Version | `minenginever.md` | 18 | Validates and updates the min_engine_version field in pack manifests. This... |
| BOM Validation | `nobom.md` | 1 | Validates that JSON files do not contain byte order marks (BOM). BOMs can cause... |
| Pack Manifest Info | `pack.md` | 18 | Extracts and validates information from behavior pack and resource pack... |
| Pack Metadata Info | `packmetadata.md` | 23 | Extracts and validates a project summary. |
| Pack Size | `packsize.md` | 9 | Analyzes pack file sizes and counts to ensure content fits within platform... |
| Path Length | `pathlength.md` | 3 | Validates file paths for length and format compatibility across platforms. Long... |
| Project Integrity | `prjint.md` | 2 | Validates the structural integrity of the project, checking for orphaned files... |
| Animation Analysis | `resourceanimation.md` | 2 | Analyzes resource pack animation files to count animations and bone references.... |
| Resource Pack Deps | `rpdepends.md` | 3 | Validates that resource pack dependencies declared in behavior pack manifests... |
| Script Analysis | `script.md` | 1 | Analyzes JavaScript/TypeScript script files to identify Minecraft Script API... |
| Script Modules | `scriptmodule.md` | 6 | Validates script module dependencies in behavior pack manifests and... |
| Sharing Validation | `sharing.md` | 2 | Validates content for sharing and marketplace requirements. Identifies custom... |
| Sounds Definition | `sndsdef.md` | 4 | Validates sound_definitions.json files that define custom sounds for the... |
| Platform Validation | `strict.md` | 3 | Validates content against strict platform requirements. Identifies cases where... |
| Project Summary | `summary.md` | 2 | Provides high-level summary information about the project's manifests and pack... |
| Texture Validation | `texture.md` | 2 | Validates texture references across entities, blocks, items, particles, and UI... |
| Texture Images | `textureimage.md` | 20 | Analyzes texture image files (PNG, JPG, TGA) for dimensions, memory usage, and... |
| Texture References | `textureref.md` | 1 | Collects and aggregates all texture references from across the project... |
| Content Types | `types.md` | 1 | Aggregates information about all content types defined in the project including... |
| Unknown Files | `unkfile.md` | 1 | Identifies files with unrecognized extensions that are not standard Minecraft... |
| Unknown JSON | `unkjson.md` | 1 | Identifies JSON files that don't match any known Minecraft content schema.... |
| Unlinked Items | `unlink.md` | 2 | Identifies content items that are defined but not referenced anywhere in the... |
| File Validation | `valfile.md` | 3 | Validates that content files are properly formatted and parseable. Catches JSON... |
| Vanilla Duplicates | `vandupes.md` | 2 | Detects content that duplicates vanilla Minecraft files. Unnecessary copies... |
| VS Code Files | `vscodefile.md` | 2 | Validates VS Code configuration files (tasks.json, launch.json) in projects.... |
| World Validation | `world.md` | 6 | Validates world-level settings including experiments, version requirements, and... |
| World Data | `worlddata.md` | 18 | Analyzes world data including LevelDB chunks, command blocks, level.dat... |
| World Pack Refs | `wpackrefs.md` | 7 | Validates pack references in world templates. Ensures that behavior_packs.json... |

## 规则组明细

### Base Game Version

- 源文件：`basegamever.md`
- 官方标题：`Base Game Version Validation Rules`
- 官方范围说明：Validates base_game_version in world template manifests and checks that it matches the current Minecraft version. Can suggest updates to bring base_game_version in line with the latest version.
- 规则数量：9

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `BASEGAMEVER100` | Base Version Undefined | 🔴 Error<br/>错误 | 无 |
| `BASEGAMEVER110` | Major Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `BASEGAMEVER111` | Major Version High | 🔴 Error<br/>错误 | ✅ |
| `BASEGAMEVER120` | Minor Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `BASEGAMEVER121` | Minor Version High | 🔴 Error<br/>错误 | ✅ |
| `BASEGAMEVER130` | Patch Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `BASEGAMEVER131` | Patch Version High | 🔴 Error<br/>错误 | ✅ |
| `BASEGAMEVER500` | Version Retrieval Failed | 🔴 Error<br/>错误 | 无 |
| `BASEGAMEVER501` | Version Parse Failed | 🔴 Error<br/>错误 | 无 |

### Blocks Catalog

- 源文件：`blockscat.md`
- 官方标题：`Blocks Catalog Validation Rules`
- 官方范围说明：Validates blocks.json catalog files in resource packs. Checks for unused block resource identifiers and vanilla overrides. Can remove unused block resource identifiers.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `BLOCKSCAT53` | Block Resource Identifier | ℹ️ Info<br/>信息 | 无 |
| `BLOCKSCAT100` | Unused Block Resource | 🔵 Recommendation<br/>建议 | ✅ |
| `BLOCKSCAT101` | Block Catalog Found | ℹ️ Info<br/>信息 | 无 |
| `BLOCKSCAT102` | Vanilla Override Block | 🔵 Recommendation<br/>建议 | 无 |

### Coop Item Naming

- 源文件：`caddonireq.md`
- 官方标题：`Coop Item Naming Validation Rules`
- 官方范围说明：Validates individual content items against Cooperative Add-On naming conventions and structure requirements. Ensures items use properly namespaced identifiers to avoid conflicts with other add-ons.
- 规则数量：17

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CADDONIREQ100` | BAC ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ101` | BAC Name Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ110` | BA ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ111` | BA Name Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ112` | JSON ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ120` | RAC ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ121` | RAC Name Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ130` | RA ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ131` | RA Name Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ140` | RC ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ141` | RC Name Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ150` | Geometry ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ151` | Geometry Name | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ160` | Material ID Format | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ161` | Material Namespace | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ170` | Missing Pack Scope | 🔴 Error<br/>错误 | 无 |
| `CADDONIREQ191` | Dimension Found | 🔴 Error<br/>错误 | 无 |

### Coop Add-On Requirements

- 源文件：`caddonreq.md`
- 官方标题：`Coop Add-On Requirements Validation Rules`
- 官方范围说明：A set of requirements for cooperative Add-On projects. See https://learn.microsoft.com/minecraft/creator/documents/practices/guidelinesforbuildingcooperativeaddons for more info.
- 规则数量：17

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CADDONREQ101` | No Loose Files | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ102` | No Common Folder Names | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ104` | Loose Creator File | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ108` | Multiple Creator Folders | 🟡 Warning<br/>警告 | 无 |
| `CADDONREQ109` | Unsupported Folder Name | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ110` | Multiple Type Folders | 🟡 Warning<br/>警告 | 无 |
| `CADDONREQ111` | Loose Type Files | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ131` | No Dimension Elements | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ133` | No UI Elements | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ160` | BP Manifest Missing | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ161` | RP Manifest Missing | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ163` | RP Manifest Count | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ164` | BP Manifest Invalid | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ165` | BP-RP Dependency Missing | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ166` | BP-RP Dependency Invalid | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ168` | RP-BP Dependency Missing | 🔴 Error<br/>错误 | 无 |
| `CADDONREQ169` | RP-BP Dependency Invalid | 🔴 Error<br/>错误 | 无 |

### Beta Features

- 源文件：`cbfg.md`
- 官方标题：`Beta Features Validation Rules`
- 官方范围说明：Validates that add-on content does not use beta features flags. The 'use_beta_features' property is not allowed in entity, block, or item behavior definitions for published content. This validator scans manifest files and custom definition JSON files to detect usage of beta feature flags.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CBFG101` | File Read Error | 🔴 Error<br/>错误 | 无 |
| `CBFG102` | JSON Parse Error (Beta Features) | 🔴 Error<br/>错误 | 无 |
| `CBFG103` | Beta Features Flag | 🔴 Error<br/>错误 | 无 |

### Deprecated Features

- 源文件：`checkfeaturedeprecation.md`
- 官方标题：`Deprecated Features Validation Rules`
- 官方范围说明：Checks for deprecated features, blocks, and textures that may be removed in future Minecraft versions. Update deprecated content to ensure long-term compatibility.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CHECKFEATUREDEPRECATION101` | Deprecated Block | 🟡 Warning<br/>警告 | 无 |
| `CHECKFEATUREDEPRECATION102` | Deprecated Terrain | 🟡 Warning<br/>警告 | 无 |
| `CHECKFEATUREDEPRECATION103` | Deprecated Texture | 🟡 Warning<br/>警告 | 无 |
| `CHECKFEATUREDEPRECATION104` | JSON Syntax Error (Deprecation Check) | 🔴 Error<br/>错误 | 无 |

### Manifest Validation

- 源文件：`chkmanif.md`
- 官方标题：`Manifest Validation Validation Rules`
- 官方范围说明：Comprehensive validation of pack manifest.json files. Validates format version, UUIDs, header properties, modules, dependencies, subpacks, capabilities, and settings. Ensures manifests comply with Minecraft Bedrock Edition requirements.
- 规则数量：35

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CHKMANIF101` | Invalid Format | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF102` | Schema Error | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF103` | Manifest Count | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF104` | Missing Property | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF105` | Required Property | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF106` | Version Mismatch | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF107` | Invalid Scope | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF108` | Multiple Templates | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF109` | Invalid Module | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF110` | Duplicate UUID | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF111` | Invalid UUID | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF112` | Missing Dep ID | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF113` | Duplicate Dep ID | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF114` | Invalid Module Name | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF115` | Version Parse Error | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF116` | Version Too Low | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF117` | Invalid Capability | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF118` | Duplicate Folder | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF119` | Duplicate Subpack | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF120` | Invalid Subpack | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF121` | Invalid Tier | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF122` | Settings Missing | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF123` | Invalid Setting | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF124` | Invalid Min/Max | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF125` | Slider Default | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF126` | Dropdown Default | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF127` | Invalid Step | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF128` | Duplicate Setting | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF129` | Missing Namespace | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF130` | Few Options | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF131` | Duplicate Option | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF132` | Base Version Error | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF133` | Wildcard Version | 🟡 Warning<br/>警告 | 无 |
| `CHKMANIF134` | PBR Engine Version | 🔴 Error<br/>错误 | 无 |
| `CHKMANIF135` | Missing PBR Cap | 🟡 Warning<br/>警告 | 无 |

### Community JSON Schema Validation

- 源文件：`comjson.md`
- 官方标题：`Community JSON Schema Validation Validation Rules`
- 官方范围说明：Validates JSON files against their corresponding schemas based on item type. Reports schema validation errors and warns when files are not at a current format version. Topic IDs 100+ are computed as JsonSchemaErrorBase (100) + ProjectItemType. Topic IDs 1100+ are computed as NotCurrentFormatVersionBase (1100) + ProjectItemType.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `COMJSON1` | JSON Parse Error (Community Schema) | 🔴 Error<br/>错误 | 无 |

### Pack Icon

- 源文件：`cpackicon.md`
- 官方标题：`Pack Icon Validation Rules`
- 官方范围说明：Validates behavior and resource pack icons (pack_icon.png) for correct format, size, and placement. The icon is shown in the pack selection screens.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CPACKICON101` | Missing Icon | 🟡 Warning<br/>警告 | 无 |
| `CPACKICON102` | Multiple Icons | 🟡 Warning<br/>警告 | 无 |
| `CPACKICON103` | Invalid Format | 🔴 Error<br/>错误 | 无 |
| `CPACKICON104` | Invalid Size | 🟡 Warning<br/>警告 | 无 |

### Particle Identifiers

- 源文件：`cparti.md`
- 官方标题：`Particle Identifiers Validation Rules`
- 官方范围说明：Validates particle effect identifiers for proper namespace formatting. Particle identifiers should follow the creator:name convention.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CPARTI101` | File Read Error | 🔴 Error<br/>错误 | 无 |
| `CPARTI102` | Version Read Error | 🔴 Error<br/>错误 | 无 |
| `CPARTI103` | Invalid Identifier | 🔴 Error<br/>错误 | 无 |

### Skin Pack

- 源文件：`cspj.md`
- 官方标题：`Skin Pack Validation Rules`
- 官方范围说明：Validates skin pack content including skins.json structure, skin textures, capes, localization keys, and model configurations.
- 规则数量：18

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CSPJ101` | Missing skins.json | 🔴 Error<br/>错误 | 无 |
| `CSPJ102` | Invalid JSON | 🔴 Error<br/>错误 | 无 |
| `CSPJ103` | Name Mismatch | 🔴 Error<br/>错误 | 无 |
| `CSPJ105` | Duplicate Texture | 🟡 Warning<br/>警告 | 无 |
| `CSPJ106` | Cape Size Error | 🔴 Error<br/>错误 | 无 |
| `CSPJ107` | Texture Size Error | 🔴 Error<br/>错误 | 无 |
| `CSPJ108` | Creator Only | 🔴 Error<br/>错误 | 无 |
| `CSPJ109` | Read Failed | 🔴 Error<br/>错误 | 无 |
| `CSPJ110` | Orphan Texture | 🟡 Warning<br/>警告 | 无 |
| `CSPJ111` | Missing Loc Key | 🔴 Error<br/>错误 | 无 |
| `CSPJ112` | Unused Loc Key | 🟡 Warning<br/>警告 | 无 |
| `CSPJ113` | Key Whitespace | 🔴 Error<br/>错误 | 无 |
| `CSPJ115` | Invalid Model | 🔴 Error<br/>错误 | 无 |
| `CSPJ116` | Too Many Skins | 🔴 Error<br/>错误 | 无 |
| `CSPJ117` | Blank Outer | 🟡 Warning<br/>警告 | 无 |
| `CSPJ118` | Invisible Angles | 🟡 Warning<br/>警告 | 无 |
| `CSPJ119` | Partial Invisible | 🟡 Warning<br/>警告 | 无 |
| `CSPJ120` | Pack Not Found | 🔴 Error<br/>错误 | 无 |

### World Icon

- 源文件：`cwi.md`
- 官方标题：`World Icon Validation Rules`
- 官方范围说明：Validates world template icons (world_icon.jpeg) for correct format, size, and placement. The icon is shown in the world selection screen.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `CWI101` | Missing Icon | 🟡 Warning<br/>警告 | 无 |
| `CWI102` | Multiple Icons | 🟡 Warning<br/>警告 | 无 |
| `CWI103` | Invalid Format | 🔴 Error<br/>错误 | 无 |
| `CWI104` | Invalid Size | 🟡 Warning<br/>警告 | 无 |

### Entity Type

- 源文件：`entitytype.md`
- 官方标题：`Entity Type Validation Rules`
- 官方范围说明：Validates entity type definitions in behavior packs. Checks format_version against the current Minecraft version and can update format versions to the latest.
- 规则数量：12

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `ENTITYTYPE52` | Runtime Identifier | ℹ️ Info<br/>信息 | 无 |
| `ENTITYTYPE53` | Entity Identifier | ℹ️ Info<br/>信息 | 无 |
| `ENTITYTYPE54` | Entity Metadata | ℹ️ Info<br/>信息 | 无 |
| `ENTITYTYPE100` | Format Version Undefined | 🔴 Error<br/>错误 | 无 |
| `ENTITYTYPE110` | Major Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `ENTITYTYPE111` | Major Version High | 🔴 Error<br/>错误 | ✅ |
| `ENTITYTYPE120` | Minor Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `ENTITYTYPE121` | Minor Version High | 🔴 Error<br/>错误 | ✅ |
| `ENTITYTYPE130` | Patch Version Low | 🔵 Recommendation<br/>建议 | ✅ |
| `ENTITYTYPE131` | Patch Version High | 🔴 Error<br/>错误 | ✅ |
| `ENTITYTYPE500` | Version Retrieval Failed | 🔴 Error<br/>错误 | 无 |
| `ENTITYTYPE501` | Version Parse Failed | 🔴 Error<br/>错误 | 无 |

### Experimental Flags

- 源文件：`expflag.md`
- 官方标题：`Experimental Flags Validation Rules`
- 官方范围说明：Validates experimental flags in world templates. Experiments that were enabled can affect world behavior even after being disabled.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `EXPFLAG101` | Experiment Active | 🟡 Warning<br/>警告 | 无 |
| `EXPFLAG102` | Missing Level.dat | 🔴 Error<br/>错误 | 无 |
| `EXPFLAG103` | World Not Found | 🔴 Error<br/>错误 | 无 |

### Forbidden Files

- 源文件：`forbfile.md`
- 官方标题：`Forbidden Files Validation Rules`
- 官方范围说明：Validates that packs only contain files with allowed extensions and do not include blocked file names or invalid characters. Different pack types (behavior pack, resource pack, world template) have different allowed file type lists.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `FORBFILE101` | File Read Error | 🔴 Error<br/>错误 | 无 |
| `FORBFILE102` | Invalid Extension | 🔴 Error<br/>错误 | 无 |
| `FORBFILE103` | Blocked Filename | 🔴 Error<br/>错误 | 无 |
| `FORBFILE104` | Invalid Character | 🔴 Error<br/>错误 | 无 |

### Format Version

- 源文件：`formatver.md`
- 官方标题：`Format Version Validation Rules`
- 官方范围说明：Validates format_version fields across various Minecraft JSON definition files including block types, item types, recipes, animations, and animation controllers. Compares versions against the current Minecraft version and can update them to the latest.
- 规则数量：45

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `FORMATVER100` | Format Undefined | 🔴 Error<br/>错误 | 无 |
| `FORMATVER110` | Block Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER112` | Block Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER114` | Block Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER116` | Block Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER118` | Block Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER120` | Block Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER130` | Item Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER132` | Item Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER134` | Item Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER136` | Item Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER138` | Item Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER140` | Item Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER150` | Recipe Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER152` | Recipe Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER154` | Recipe Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER156` | Recipe Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER158` | Recipe Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER160` | Recipe Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER170` | BP Anim Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER172` | BP Anim Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER174` | BP Anim Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER176` | BP Anim Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER178` | BP Anim Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER180` | BP Anim Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER190` | BP AnimCtrl Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER192` | BP AnimCtrl Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER194` | BP AnimCtrl Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER196` | BP AnimCtrl Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER198` | BP AnimCtrl Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER200` | BP AnimCtrl Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER210` | RP Anim Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER212` | RP Anim Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER214` | RP Anim Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER216` | RP Anim Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER218` | RP Anim Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER220` | RP Anim Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER230` | RP AnimCtrl Major Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER232` | RP AnimCtrl Major High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER234` | RP AnimCtrl Minor Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER236` | RP AnimCtrl Minor High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER238` | RP AnimCtrl Patch Low | 🔵 Recommendation<br/>建议 | ✅ |
| `FORMATVER240` | RP AnimCtrl Patch High | 🔴 Error<br/>错误 | ✅ |
| `FORMATVER500` | Version Retrieval Failed | 🔴 Error<br/>错误 | 无 |
| `FORMATVER501` | Version Parse Failed | 🔴 Error<br/>错误 | 无 |

### Geometry Format

- 源文件：`geofmt.md`
- 官方标题：`Geometry Format Validation Rules`
- 官方范围说明：Validates model geometry files for format compatibility and restricted features. Identifies geometry features that may not work on all platforms.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `GEOFMT101` | Restricted Poly Mesh | 🔴 Error<br/>错误 | 无 |
| `GEOFMT102` | JSON Syntax Error (Geometry) | 🔴 Error<br/>错误 | 无 |

### Model Geometry

- 源文件：`geometry.md`
- 官方标题：`Model Geometry Validation Rules`
- 官方范围说明：Validates and analyzes model geometry files (.geo.json) for blocks, entities, and items. Tracks cube counts and complexity to identify potential performance issues.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `GEOMETRY101` | Block Geometry | ℹ️ Info<br/>信息 | 无 |
| `GEOMETRY102` | Entity Geometry | ℹ️ Info<br/>信息 | 无 |
| `GEOMETRY103` | Item Geometry | ℹ️ Info<br/>信息 | 无 |
| `GEOMETRY501` | Complex Block | 🟡 Warning<br/>警告 | 无 |

### Content Counts

- 源文件：`items.md`
- 官方标题：`Content Counts Validation Rules`
- 官方范围说明：Provides counts of various content types found in the project including packs, entities, blocks, items, and other definitions.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `ITEMS102` | Behavior Pack | ℹ️ Info<br/>信息 | 无 |
| `ITEMS103` | Resource Pack | ℹ️ Info<br/>信息 | 无 |

### Item Types

- 源文件：`itemtype.md`
- 官方标题：`Item Types Validation Rules`
- 官方范围说明：Validates behavior pack item type definitions including format versions, identifiers, and metadata. Can automatically update format versions to the latest.
- 规则数量：12

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `ITEMTYPE53` | Identifier | ℹ️ Info<br/>信息 | 无 |
| `ITEMTYPE54` | Metadata | ℹ️ Info<br/>信息 | 无 |
| `ITEMTYPE55` | Category | ℹ️ Info<br/>信息 | 无 |
| `ITEMTYPE100` | Version Defined | ℹ️ Info<br/>信息 | 无 |
| `ITEMTYPE110` | Major Version Low | 🟡 Warning<br/>警告 | ✅ |
| `ITEMTYPE111` | Major Version High | 🔴 Error<br/>错误 | ✅ |
| `ITEMTYPE120` | Minor Version Low | 🟡 Warning<br/>警告 | ✅ |
| `ITEMTYPE121` | Minor Version High | 🔴 Error<br/>错误 | ✅ |
| `ITEMTYPE130` | Patch Version Low | ℹ️ Info<br/>信息 | ✅ |
| `ITEMTYPE131` | Patch Version High | 🟡 Warning<br/>警告 | ✅ |
| `ITEMTYPE500` | Version Fetch Error | 🔴 Error<br/>错误 | 无 |
| `ITEMTYPE501` | Version Parse Error | 🔴 Error<br/>错误 | 无 |

### JSON Schema Validation

- 源文件：`json.md`
- 官方标题：`JSON Schema Validation Validation Rules`
- 官方范围说明：Validates JSON files against official JSON schemas located at public/schemas. Reports schema validation errors and warns when files are not at a current format version. Topic IDs 100+ are computed as JsonSchemaErrorBase (100) + ProjectItemType. Topic IDs 1100+ are computed as NotCurrentFormatVersionBase (1100) + ProjectItemType.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `JSON1` | JSON Parse Error (Schema Validation) | 🔴 Error<br/>错误 | 无 |

### JSON Form Structure Validation

- 源文件：`jsonf.md`
- 官方标题：`JSON Form Structure Validation Validation Rules`
- 官方范围说明：Validates JSON files against Minecraft documentation-derived form schemas. These schemas define the expected structure, types, and constraints for Minecraft content files like entity definitions, block definitions, spawn rules, etc. The validator checks type compatibility, value ranges, string lengths, required fields, enum values, and more based on metadata in form.json files.
- 规则数量：17

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `JSONF101` | Unexpected String Where Object Expected | 🔴 Error<br/>错误 | 无 |
| `JSONF102` | Unexpected Boolean Where Object Expected | 🔴 Error<br/>错误 | 无 |
| `JSONF103` | Unexpected Number Where Object Expected | 🔴 Error<br/>错误 | 无 |
| `JSONF110` | Data Type Mismatch | 🟡 Warning<br/>警告 | 无 |
| `JSONF111` | Value Below Minimum | 🟡 Warning<br/>警告 | 无 |
| `JSONF112` | Value Above Maximum | 🟡 Warning<br/>警告 | 无 |
| `JSONF113` | String Too Short | 🟡 Warning<br/>警告 | 无 |
| `JSONF114` | String Too Long | 🟡 Warning<br/>警告 | 无 |
| `JSONF115` | Value Not in Choices | 🟡 Warning<br/>警告 | 无 |
| `JSONF116` | Pattern Mismatch | 🟡 Warning<br/>警告 | 无 |
| `JSONF117` | Array Length Mismatch | 🟡 Warning<br/>警告 | 无 |
| `JSONF118` | Point/Range Size Mismatch | 🟡 Warning<br/>警告 | 无 |
| `JSONF119` | Key Not Allowed | 🟡 Warning<br/>警告 | 无 |
| `JSONF120` | Unexpected Property | 🟡 Warning<br/>警告 | 无 |
| `JSONF121` | Missing Required Field | 🟡 Warning<br/>警告 | 无 |
| `JSONF401` | JSON Parse Error (Form Validation) | 🔴 Error<br/>错误 | 无 |
| `JSONF402` | Form Not Found | ℹ️ Info<br/>信息 | 无 |

### Content Tags

- 源文件：`jsontags.md`
- 官方标题：`Content Tags Validation Rules`
- 官方范围说明：Tracks content types and component usage across JSON files in the project. Used to build content indexes for cross-referencing.
- 规则数量：11

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `JSONTAGS101` | Entity Type | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS102` | Block Type | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS103` | Item Type | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS104` | Terrain Texture | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS105` | Item Texture | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS106` | Sound Definition | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS107` | Music Definition | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS108` | Sound File | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS109` | Biome Behavior Type | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS110` | Biome Client Type | ℹ️ Info<br/>信息 | 无 |
| `JSONTAGS111` | Particle Type | ℹ️ Info<br/>信息 | 无 |

### Language Files

- 源文件：`langfiles.md`
- 官方标题：`Language Files Validation Rules`
- 官方范围说明：Validates that localization files (.lang) and the languages.json catalog are properly synchronized within each pack. For each language listed in languages.json, there must be a corresponding .lang file, and vice versa. English (en_US) is always required.
- 规则数量：5

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `LANGFILES101` | Missing Catalog | 🟡 Warning<br/>警告 | 无 |
| `LANGFILES102` | Missing English | 🔴 Error<br/>错误 | 无 |
| `LANGFILES103` | Invalid JSON | 🔴 Error<br/>错误 | 无 |
| `LANGFILES104` | Missing Lang File | 🔴 Error<br/>错误 | 无 |
| `LANGFILES105` | Orphaned Lang File | 🟡 Warning<br/>警告 | 无 |

### File Size/Lines

- 源文件：`linesize.md`
- 官方标题：`MCTools Validation Rules Documentation - minecraft:linesize`
- 官方范围说明：Aggregates file size and line count statistics for all project items, broken down by item type. For binary files, reports file size; for text files, reports number of significant lines. Topic IDs are computed dynamically as TopicTestIdBase (100) + ProjectItemType value. All topics produce featureAggregate (info) type messages.
- 规则数量：0

该规则组仅输出统计信息，不定义独立规则ID。

### MC Functions

- 源文件：`mcfunction.md`
- 官方标题：`MC Functions Validation Rules`
- 官方范围说明：Validates .mcfunction files for correct command syntax and formatting. MCFunction files contain Minecraft commands that execute in behavior packs.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `MCFUNCTION102` | Invalid Syntax | 🔴 Error<br/>错误 | 无 |
| `MCFUNCTION103` | Leading Slash | 🟡 Warning<br/>警告 | 无 |

### Min Engine Version

- 源文件：`minenginever.md`
- 官方标题：`Min Engine Version Validation Rules`
- 官方范围说明：Validates and updates the min_engine_version field in pack manifests. This version specifies the minimum Minecraft version required to use the pack.
- 规则数量：18

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `MINENGINEVER100` | BP Version Defined | ℹ️ Info<br/>信息 | 无 |
| `MINENGINEVER110` | BP Major Low | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER111` | BP Major High | 🔴 Error<br/>错误 | ✅ |
| `MINENGINEVER120` | BP Minor Low | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER121` | BP Minor High | 🔴 Error<br/>错误 | ✅ |
| `MINENGINEVER130` | BP Patch Low | ℹ️ Info<br/>信息 | ✅ |
| `MINENGINEVER131` | BP Patch High | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER180` | No Manifest | 🔴 Error<br/>错误 | 无 |
| `MINENGINEVER181` | Version Errors | 🔴 Error<br/>错误 | 无 |
| `MINENGINEVER200` | RP Version Defined | ℹ️ Info<br/>信息 | 无 |
| `MINENGINEVER210` | RP Major Low | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER211` | RP Major High | 🔴 Error<br/>错误 | ✅ |
| `MINENGINEVER220` | RP Minor Low | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER221` | RP Minor High | 🔴 Error<br/>错误 | ✅ |
| `MINENGINEVER230` | RP Patch Low | ℹ️ Info<br/>信息 | ✅ |
| `MINENGINEVER231` | RP Patch High | 🟡 Warning<br/>警告 | ✅ |
| `MINENGINEVER500` | Version Retrieved | ℹ️ Info<br/>信息 | 无 |
| `MINENGINEVER501` | Version Parsed | ℹ️ Info<br/>信息 | 无 |

### BOM Validation

- 源文件：`nobom.md`
- 官方标题：`BOM Validation Validation Rules`
- 官方范围说明：Validates that JSON files do not contain byte order marks (BOM). BOMs can cause parsing failures in Minecraft.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `NOBOM101` | BOM Detected | 🔴 Error<br/>错误 | 无 |

### Pack Manifest Info

- 源文件：`pack.md`
- 官方标题：`Pack Manifest Info Validation Rules`
- 官方范围说明：Extracts and validates information from behavior pack and resource pack manifest.json files including names, descriptions, UUIDs, versions, and icons.
- 规则数量：18

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `PACK104` | BP Name | ℹ️ Info<br/>信息 | 无 |
| `PACK105` | BP Description | ℹ️ Info<br/>信息 | 无 |
| `PACK106` | BP Custom ID | ℹ️ Info<br/>信息 | 无 |
| `PACK107` | BP Min Version | ℹ️ Info<br/>信息 | 无 |
| `PACK108` | BP UUID | ℹ️ Info<br/>信息 | 无 |
| `PACK109` | BP Manifest | ℹ️ Info<br/>信息 | 无 |
| `PACK111` | RP Min Version | ℹ️ Info<br/>信息 | 无 |
| `PACK112` | RP UUID | ℹ️ Info<br/>信息 | 无 |
| `PACK113` | RP Manifest | ℹ️ Info<br/>信息 | 无 |
| `PACK114` | RP Name | ℹ️ Info<br/>信息 | 无 |
| `PACK115` | RP Description | ℹ️ Info<br/>信息 | 无 |
| `PACK116` | RP Custom ID | ℹ️ Info<br/>信息 | 无 |
| `PACK117` | RP Format Version | ℹ️ Info<br/>信息 | 无 |
| `PACK118` | Sub Packs | ℹ️ Info<br/>信息 | 无 |
| `PACK121` | RP Icon | ℹ️ Info<br/>信息 | 无 |
| `PACK122` | BP Icon | ℹ️ Info<br/>信息 | 无 |
| `PACK123` | Skin Pack Icon | ℹ️ Info<br/>信息 | 无 |
| `PACK245` | Subpack Tiers | ℹ️ Info<br/>信息 | 无 |

### Pack Metadata Info

- 源文件：`packmetadata.md`
- 官方标题：`Pack Metadata Info Validation Rules`
- 官方范围说明：Extracts and validates a project summary.
- 规则数量：23

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `PACKMETADATA101` | Metadata Pack Id | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA102` | Metadata Offer Id | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA141` | Card Title | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA142` | Catalog Description | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA143` | Content Approved | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA144` | Creator Name | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA146` | Is Update | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA147` | Last Updated | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA148` | Product Genre | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA149` | Product Price | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA150` | Product Subgenre | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA151` | Product Title | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA152` | Original Release Date | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA153` | Pack Type | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA154` | Player Count | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA155` | Acquirable | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA156` | Readable Offer Id | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA157` | Release Date | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA158` | Product Id | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA159` | Submission Date | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA160` | Submission Version | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA161` | World Type | ℹ️ Info<br/>信息 | 无 |
| `PACKMETADATA162` | Offer Type | ℹ️ Info<br/>信息 | 无 |

### Pack Size

- 源文件：`packsize.md`
- 官方标题：`Pack Size Validation Rules`
- 官方范围说明：Analyzes pack file sizes and counts to ensure content fits within platform limits. Large packs can cause download issues and slow loading times on mobile devices.
- 规则数量：9

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `PACKSIZE101` | Total Size | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE102` | File Count | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE103` | Folder Count | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE104` | Content Size | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE105` | Content Files | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE106` | Content Folders | ℹ️ Info<br/>信息 | 无 |
| `PACKSIZE401` | Addon Size Warning | 🟡 Warning<br/>警告 | 无 |
| `PACKSIZE402` | Package Size Warning | 🟡 Warning<br/>警告 | 无 |
| `PACKSIZE410` | Zip Processing Error | 🔴 Error<br/>错误 | 无 |

### Path Length

- 源文件：`pathlength.md`
- 官方标题：`Path Length Validation Rules`
- 官方范围说明：Validates file paths for length and format compatibility across platforms. Long paths can cause issues on some operating systems and storage systems.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `PATHLENGTH102` | Deep Nesting | 🟡 Warning<br/>警告 | 无 |
| `PATHLENGTH103` | Path Too Long | 🔴 Error<br/>错误 | 无 |
| `PATHLENGTH104` | Mixed Case Path | 🔵 Recommendation<br/>建议 | 无 |

### Project Integrity

- 源文件：`prjint.md`
- 官方标题：`Project Integrity Validation Rules`
- 官方范围说明：Validates the structural integrity of the project, checking for orphaned files that don't belong to any pack and detecting nested manifest structures that indicate improperly organized packs.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `PRJINT101` | Extraneous Content | 🟡 Warning<br/>警告 | 无 |
| `PRJINT102` | Nested Pack Structure | 🔴 Error<br/>错误 | 无 |

### Animation Analysis

- 源文件：`resourceanimation.md`
- 官方标题：`Animation Analysis Validation Rules`
- 官方范围说明：Analyzes resource pack animation files to count animations and bone references. Used to assess animation complexity.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `RESOURCEANIMATION101` | Animation Count | ℹ️ Info<br/>信息 | 无 |
| `RESOURCEANIMATION102` | Bone Count | ℹ️ Info<br/>信息 | 无 |

### Resource Pack Deps

- 源文件：`rpdepends.md`
- 官方标题：`Resource Pack Deps Validation Rules`
- 官方范围说明：Validates that resource pack dependencies declared in behavior pack manifests are properly resolved and available.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `RPDEPENDS101` | Invalid Manifest JSON | 🔴 Error<br/>错误 | 无 |
| `RPDEPENDS102` | Missing Resource Pack | 🔴 Error<br/>错误 | 无 |
| `RPDEPENDS103` | Processing Error | 🔴 Error<br/>错误 | 无 |

### Script Analysis

- 源文件：`script.md`
- 官方标题：`Script Analysis Validation Rules`
- 官方范围说明：Analyzes JavaScript/TypeScript script files to identify Minecraft Script API usage. Parses code to extract API references and usage patterns.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `SCRIPT101` | APIs Used | ℹ️ Info<br/>信息 | 无 |

### Script Modules

- 源文件：`scriptmodule.md`
- 官方标题：`Script Modules Validation Rules`
- 官方范围说明：Validates script module dependencies in behavior pack manifests and package.json files. Checks for version compatibility and can update module versions to the latest supported versions.
- 规则数量：6

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `SCRIPTMODULE100` | BP Module Dependency | ℹ️ Info<br/>信息 | 无 |
| `SCRIPTMODULE101` | Package Dependency | ℹ️ Info<br/>信息 | 无 |
| `SCRIPTMODULE102` | Package Dev Dependency | ℹ️ Info<br/>信息 | 无 |
| `SCRIPTMODULE110` | Missing Package Registration | 🔴 Error<br/>错误 | 无 |
| `SCRIPTMODULE111` | Missing NPM Registration | 🔴 Error<br/>错误 | 无 |
| `SCRIPTMODULE114` | Beta Version Outdated | 🔴 Error<br/>错误 | 无 |

### Sharing Validation

- 源文件：`sharing.md`
- 官方标题：`Sharing Validation Validation Rules`
- 官方范围说明：Validates content for sharing and marketplace requirements. Identifies custom capabilities and potentially problematic content that may affect distribution.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `SHARING100` | Custom Capabilities | ℹ️ Info<br/>信息 | 无 |
| `SHARING101` | Strong Language | 🟡 Warning<br/>警告 | 无 |

### Sounds Definition

- 源文件：`sndsdef.md`
- 官方标题：`Sounds Definition Validation Rules`
- 官方范围说明：Validates sound_definitions.json files that define custom sounds for the resource pack. Ensures proper structure and references to audio files.
- 规则数量：4

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `SNDSDEF101` | Multiple Definitions | 🟡 Warning<br/>警告 | 无 |
| `SNDSDEF102` | Invalid Structure | 🔴 Error<br/>错误 | 无 |
| `SNDSDEF103` | Invalid JSON | 🔴 Error<br/>错误 | 无 |
| `SNDSDEF104` | Loose Definition | 🟡 Warning<br/>警告 | 无 |

### Platform Validation

- 源文件：`strict.md`
- 官方标题：`Platform Validation Validation Rules`
- 官方范围说明：Validates content against strict platform requirements. Identifies cases where custom content overrides vanilla Minecraft identifiers, which may cause compatibility issues or unexpected behavior.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `STRICT100` | Entity Override | 🟡 Warning<br/>警告 | 无 |
| `STRICT101` | Runtime ID Override | 🟡 Warning<br/>警告 | 无 |
| `STRICT104` | Item Override | 🟡 Warning<br/>警告 | 无 |

### Project Summary

- 源文件：`summary.md`
- 官方标题：`Project Summary Validation Rules`
- 官方范围说明：Provides high-level summary information about the project's manifests and pack configuration.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `SUMMARY101` | Resource Manifest | ℹ️ Info<br/>信息 | 无 |
| `SUMMARY102` | Behavior Manifest | ℹ️ Info<br/>信息 | 无 |

### Texture Validation

- 源文件：`texture.md`
- 官方标题：`Texture Validation Validation Rules`
- 官方范围说明：Validates texture references across entities, blocks, items, particles, and UI elements. Tracks texture handle usage to prevent exceeding platform limits.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `TEXTURE100` | Handle Limit Exceeded | 🔴 Error<br/>错误 | 无 |
| `TEXTURE101` | Textures | ℹ️ Info<br/>信息 | 无 |

### Texture Images

- 源文件：`textureimage.md`
- 官方标题：`Texture Images Validation Rules`
- 官方范围说明：Analyzes texture image files (PNG, JPG, TGA) for dimensions, memory usage, and tiering compatibility. Ensures textures fit within platform memory budgets for different device tiers.
- 规则数量：20

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `TEXTUREIMAGE101` | Texture Images | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE200` | Texture Images Tier0 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE201` | Texture Images Tier1 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE202` | Texture Images Tier2 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE203` | Texture Images Tier3 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE204` | Texture Images Tier4 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE205` | Texture Images Tier5 | ℹ️ Info<br/>信息 | 无 |
| `TEXTUREIMAGE401` | PNG/JPG Error | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE402` | Texture Over Budget | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE403` | Total Over Budget | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE404` | TGA Error | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE405` | Atlas Over Budget | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE406` | Atlas Budget Warning | 🟡 Warning<br/>警告 | 无 |
| `TEXTUREIMAGE407` | Atlas Budget Error | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE408` | Empty Image | 🟡 Warning<br/>警告 | 无 |
| `TEXTUREIMAGE409` | Invalid Tiering | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE410` | Vibrant Visuals Error | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE460` | Missing Texture | 🟡 Warning<br/>警告 | 无 |
| `TEXTUREIMAGE461` | Incomplete Override | 🔴 Error<br/>错误 | 无 |
| `TEXTUREIMAGE462` | Mashup Incomplete | 🔴 Error<br/>错误 | 无 |

### Texture References

- 源文件：`textureref.md`
- 官方标题：`Texture References Validation Rules`
- 官方范围说明：Collects and aggregates all texture references from across the project including entity textures, block textures, particle effects, and UI elements.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `TEXTUREREF101` | Reference List | ℹ️ Info<br/>信息 | 无 |

### Content Types

- 源文件：`types.md`
- 官方标题：`Content Types Validation Rules`
- 官方范围说明：Aggregates information about all content types defined in the project including entities, blocks, items, and other custom definitions.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `TYPES101` | Type Summary | ℹ️ Info<br/>信息 | 无 |

### Unknown Files

- 源文件：`unkfile.md`
- 官方标题：`Unknown Files Validation Rules`
- 官方范围说明：Identifies files with unrecognized extensions that are not standard Minecraft content types. Unknown files may indicate misplaced assets or incompatible content.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `UNKFILE102` | Unknown File Type | 🔴 Error<br/>错误 | 无 |

### Unknown JSON

- 源文件：`unkjson.md`
- 官方标题：`Unknown JSON Validation Rules`
- 官方范围说明：Identifies JSON files that don't match any known Minecraft content schema. Unknown JSON files may indicate misplaced content or unsupported custom formats.
- 规则数量：1

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `UNKJSON101` | Unknown JSON Type | 🟡 Warning<br/>警告 | 无 |

### Unlinked Items

- 源文件：`unlink.md`
- 官方标题：`Unlinked Items Validation Rules`
- 官方范围说明：Identifies content items that are defined but not referenced anywhere in the project. Also detects dependencies on vanilla Minecraft content that may change.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `UNLINK191` | Unused Item | 🟡 Warning<br/>警告 | 无 |
| `UNLINK205` | Vanilla Reference | 🔵 Recommendation<br/>建议 | 无 |

### File Validation

- 源文件：`valfile.md`
- 官方标题：`File Validation Validation Rules`
- 官方范围说明：Validates that content files are properly formatted and parseable. Catches JSON syntax errors and encoding issues that would prevent content from loading.
- 规则数量：3

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `VALFILE102` | Invalid JSON | 🔴 Error<br/>错误 | 无 |
| `VALFILE103` | Empty File | 🟡 Warning<br/>警告 | 无 |
| `VALFILE104` | Binary Content | 🔴 Error<br/>错误 | 无 |

### Vanilla Duplicates

- 源文件：`vandupes.md`
- 官方标题：`Vanilla Duplicates Validation Rules`
- 官方范围说明：Detects content that duplicates vanilla Minecraft files. Unnecessary copies increase pack size and may cause conflicts with game updates.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `VANDUPES101` | Exact Duplicate | 🔴 Error<br/>错误 | 无 |
| `VANDUPES102` | Partial Duplicate | 🟡 Warning<br/>警告 | 无 |

### VS Code Files

- 源文件：`vscodefile.md`
- 官方标题：`VS Code Files Validation Rules`
- 官方范围说明：Validates VS Code configuration files (tasks.json, launch.json) in projects. Checks for proper Minecraft-related task and debug configurations.
- 规则数量：2

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `VSCODEFILE100` | No Deploy Tasks | 🔵 Recommendation<br/>建议 | 无 |
| `VSCODEFILE101` | No Debug Config | 🔵 Recommendation<br/>建议 | 无 |

### World Validation

- 源文件：`world.md`
- 官方标题：`World Validation Validation Rules`
- 官方范围说明：Validates world-level settings including experiments, version requirements, and metadata. These settings affect how the world loads and what features are available.
- 规则数量：6

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `WORLD101` | Beta APIs | ℹ️ Info<br/>信息 | 无 |
| `WORLD102` | Data Driven Items | ℹ️ Info<br/>信息 | 无 |
| `WORLD103` | Deferred Preview | ℹ️ Info<br/>信息 | 无 |
| `WORLD107` | Base Game Version | ℹ️ Info<br/>信息 | 无 |
| `WORLD108` | World Name | ℹ️ Info<br/>信息 | 无 |
| `WORLD109` | World Description | ℹ️ Info<br/>信息 | 无 |

### World Data

- 源文件：`worlddata.md`
- 官方标题：`World Data Validation Rules`
- 官方范围说明：Analyzes world data including LevelDB chunks, command blocks, level.dat settings, and coordinates. Identifies command usage patterns and potential issues in saved world data.
- 规则数量：18

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `WORLDDATA101` | Function Command | 🟡 Warning<br/>警告 | 无 |
| `WORLDDATA102` | Block Command | 🟡 Warning<br/>警告 | 无 |
| `WORLDDATA103` | Min X | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA104` | Min Z | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA105` | Max X | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA106` | Max Z | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA112` | World Command | 🟡 Warning<br/>警告 | 无 |
| `WORLDDATA121` | Block Types | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA122` | Block States | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA123` | Command | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA124` | Execute Subcommand | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA125` | Level.dat Info | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA126` | Experiments | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA127` | Empty Chunks | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA128` | Chunk Count | ℹ️ Info<br/>信息 | 无 |
| `WORLDDATA212` | Outdated Command | 🟡 Warning<br/>警告 | 无 |
| `WORLDDATA400` | Processing Error | 🔴 Error<br/>错误 | 无 |
| `WORLDDATA401` | Unexpected Error | 🔴 Error<br/>错误 | 无 |

### World Pack Refs

- 源文件：`wpackrefs.md`
- 官方标题：`World Pack Refs Validation Rules`
- 官方范围说明：Validates pack references in world templates. Ensures that behavior_packs.json and resource_packs.json correctly reference the packs bundled with the world.
- 规则数量：7

| 规则ID | 规则名 | 严重性 | 自动修复 |
| --- | --- | --- | --- |
| `WPACKREFS201` | Invalid JSON | 🔴 Error<br/>错误 | 无 |
| `WPACKREFS202` | Missing References | 🟡 Warning<br/>警告 | 无 |
| `WPACKREFS203` | Invalid Pack ID | 🔴 Error<br/>错误 | 无 |
| `WPACKREFS204` | Missing Version | 🟡 Warning<br/>警告 | 无 |
| `WPACKREFS205` | Invalid Version | 🔴 Error<br/>错误 | 无 |
| `WPACKREFS206` | Pack Not Found | 🔴 Error<br/>错误 | 无 |
| `WPACKREFS207` | Processing Error | 🔴 Error<br/>错误 | 无 |

