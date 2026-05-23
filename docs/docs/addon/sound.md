# 声音

**声音（Sound）**泛指Minecraft基岩版中所有音频内容的系统。基岩版通过资源包中的声音定义文件控制游戏中音效的播放方式，允许附加包添加自定义音效或覆盖原版音效。

## 概述

基岩版的声音系统围绕**声音事件（Sound Event）**组织。游戏中的各种行为（如方块放置、实体受伤、环境音等）触发对应的声音事件，引擎根据资源包中的声音定义查找该事件应播放的音频文件及其播放参数。

资源包中与声音相关的主要文件有两个：`sounds/sound_definitions.json`用于定义声音事件与音频文件的对应关系，`sounds.json`用于将声音事件绑定到实体、方块和交互行为的自动触发逻辑上。

## 声音定义文件

{{file|sounds/sound_definitions.json}}以JSON格式定义所有自定义声音事件。通过此文件定义声音短名称后，即可通过`/playsound`命令或`sounds.json`引用。

每个声音事件的顶层字段包括：

/// define
`category`

- 声音所属的分类，影响其受哪个音量滑块控制。可选值详见下方分类表。

`min_distance`

- 声音开始衰减的最小距离（浮点数），默认`0.0`。

`max_distance`

- 声音衰减至最弱的最大距离（浮点数）。若未设置，则可听范围由`/playsound`音量参数决定，计算式为`playsound_volume × 16`（最小16）。

`sounds`

- 音频文件路径的数组。触发时从中随机选取一个播放。每项可以是字符串路径，也可以是包含详细参数的对象。

///

```json title="sound_definitions.json示例"
{
  "format_version": "1.14.0",
  "sound_definitions": {
    "custom.sound.example": {
      "category": "block",
      "sounds": [
        "sounds/custom/example1",
        {
          "name": "sounds/custom/example2",
          "volume": 0.8,
          "pitch": [0.9, 1.1]
        }
      ]
    }
  }
}
```

### 分类

`category`字段控制声音所受的音量设置影响：

| 分类 | 说明 |
|------|------|
| `weather` | 天气音效 |
| `block` | 方块交互音效 |
| `bucket` | 桶类操作音效 |
| `bottle` | 玻璃瓶操作音效 |
| `ui` | 界面音效（不受距离限制） |
| `player` | 玩家相关音效 |
| `hostile` | 敌对生物音效 |
| `music` | 背景音乐 |
| `record` | 唱片机音效 |
| `neutral` | 中立生物音效 |

### `sounds`数组的对象式参数

当`sounds`数组中的条目为对象时，支持以下参数：

/// define
`name`

- 音频文件路径，如`"sounds/music/game/creative/creative1"`，不含扩展名。

`stream`

- 启用流式加载。适用于较长音频，可降低内存占用。

`volume`

- 音量比例（0.0–1.0，可超过1.0）。

`pitch`

- 音调倍率，如`2.3`表示以2.3倍速播放。可指定为`[min, max]`格式以随机化。

`is3D`

- 是否启用3D空间音效。音乐和界面分类会自动禁用。

`weight`

- 随机权重。权重为10的条目被选中的概率是权重为2的条目的5倍。

`interruptible`

- 是否可被其他声音中断，默认`true`。

`subtitle`

- 字幕键名。当该声音播放时，若玩家开启了隐藏字幕功能，界面会显示对应本地化文本。

`load_on_low_memory`

- 在低内存设备上强制加载该声音。此参数已于1.16.0弃用。

///

## sounds.json

{{file|sounds.json}}位于资源包根目录，用于将声音事件绑定到游戏内的自动触发逻辑。它包含以下分类：

| 分类 | 说明 |
|------|------|
| `individual_event_sounds` | 独立事件音效，如信标激活 |
| `block_sounds` | 方块交互音效 |
| `entity_sounds` | 实体生命周期音效，包括自定义实体 |
| `interactive_sounds` | 玩家交互音效 |

### 实体音效

`entity_sounds`下的常见生命周期事件：

| 事件 | 触发时机 |
|------|----------|
| `ambient` | 随机环境音（如生物低鸣） |
| `hurt` | 受伤时 |
| `death` | 死亡时 |
| `step` | 移动时 |
| `fall.big` | 高处跌落 |
| `fall.small` | 低处跌落 |
| `splash` | 溅水 |
| `attack` | 近战攻击 |
| `shoot` | 远程射击 |

```json title="sounds.json实体音效示例"
{
  "entity_sounds": {
    "entities": {
      "wiki:elephant": {
        "volume": 1,
        "pitch": [0.9, 1.0],
        "events": {
          "step": {
            "sound": "elephant.step",
            "volume": 0.18,
            "pitch": 1.1
          },
          "ambient": {
            "sound": "elephant.trumpet",
            "volume": 0.11,
            "pitch": 0.9
          }
        }
      }
    }
  }
}
```

## 音频文件格式

基岩版支持的音频文件格式为`.ogg`（Ogg Vorbis）、`.wav`和`.fsb`（FMOD音频库）。自定义音效通常使用`.ogg`或`.wav`格式。音频文件位于资源包的`sounds/`目录中，在声音定义中引用时不需要包含文件扩展名。

/// warning | 新增声音文件需完整重启
新增声音文件后需要完全重启客户端才能生效。仅重新加载世界不足以使新音频被加载。
///

## 声音播放

声音可以通过以下方式触发播放：

- **游戏内部**：引擎在执行特定逻辑时自动触发关联的声音事件，如方块交互、实体行为、界面操作等。
- **`/playsound`命令**：通过命令播放指定的声音事件，可以指定目标玩家、位置、音量和音调参数。`/playsound`的最大可听范围由以下公式决定：若声音定义中未设置`max_distance`，则可听范围为 $\min(\text{max\_distance}, \max(\text{volume} \times 16, 16))$；未设置`max_distance`时等同于 $\text{volume} \times 16$（最小16格）。游戏在将音量传入声音定义内部参数前会先将其钳制到1.0，最终音量为 $\min(\text{playsound\_volume}, 1.0) \times \text{衰减因子} \times \text{声音定义音量}$。
- **动画**：在客户端实体定义中声明`sound_effects`短名称，再在动画文件的时间轴中绑定音效触发点。
- **动画控制器**：在状态的`sound_effects`数组中指定短名称，当控制器进入该状态时触发。
- **粒子特效**：粒子系统中可以关联声音事件。
- **脚本API**：通过脚本在世界中播放声音。<!-- md:flag vanilla -->

## 音乐

游戏的背景音乐同样通过声音系统管理。音乐相关的声音事件归属`music`分类，受音乐音量滑块控制。音乐的播放逻辑由引擎内部控制，根据玩家所处的生物群系、维度和游戏状态选择播放对应的音乐曲目。

附加包目前不支持通过数据驱动方式完全自定义音乐播放逻辑，但可以通过`/music`命令控制音乐的播放和停止。
