# 使用指南

这一页用一个“练习实体”的视觉资源来熟悉Blockbench。目标不是做出复杂作品，而是走完“新建模型—设置骨骼—绘制纹理—制作动画—导出文件”的完整流程。

## 新建基岩版模型

1. 打开Blockbench。
2. 选择**File**→**New**→**Bedrock Model**。
3. 在项目设置里填写模型名，例如`practice_robot`。模型标识符和骨骼名都尽量使用小写字母、数字、下划线和点号。
4. 保持`Box UV`开启。基岩版实体模型常用盒式UV，Blockbench能自动展开立方体的UV。
5. 纹理尺寸先使用`64×64`。练习阶段不要急着做高分辨率纹理，先保证结构正确。

/// warning | 不要只保存导出文件
`.geo.json`是给游戏读的，`.bbmodel`才是给你继续编辑的。每完成一段明显进度，都用**File**→**Save Model**保存`.bbmodel`。
///

## 建骨骼和形状

在右侧大纲中新建一个根骨骼`root`，再把其他骨骼放进去。一个简单实体可以这样组织：

/// html | div.treeview
- root
    - body
        - head
        - left_arm
        - right_arm
    - left_leg
    - right_leg
///

接着给每个骨骼添加立方体：

1. 选中骨骼，点击添加立方体。
2. 使用移动、缩放和旋转工具摆出基本轮廓。
3. 对称部件先做一侧，再复制并翻转到另一侧。
4. 对会旋转的部件，按++p++或选择轴心点工具，把轴心点移动到关节处。

/// tip | 做得“像Minecraft”比做得“细”更重要
Minecraft风格强调少量元素概括形体。能用一个立方体表达的结构，不要拆成十几个小立方体；能用透明纹理表达的薄片，也不一定要堆很多实体几何。
///

## 创建纹理

1. 在左侧纹理面板点击**Create Texture**。
2. 填写纹理名，例如`practice_robot`。
3. 勾选**Template**，让Blockbench按当前模型生成UV模板。
4. 切换到**Paint**模式。
5. 先用油漆桶工具给不同部件铺中间色，再逐步添加阴影和高光。

绘制时记住三点：

- 直接在三维预览上画可以快速判断整体效果。
- 在UV面板中画适合处理边缘和小像素。
- 如果想用外部图像编辑器，保存纹理后再从外部编辑；Blockbench会在文件更新后显示结果。

## 制作一个循环动画

1. 切换到**Animate**模式。
2. 点击动画列表中的添加按钮，新建`animation.practice_robot.idle`。
3. 在`0.0`秒为`body`骨骼添加位置或旋转关键帧。
4. 在`0.5`秒稍微移动或旋转`body`。
5. 在`1.0`秒复制`0.0`秒的关键帧。
6. 右键动画，把动画设置为循环。

导出后，实体并不会自动播放动画。你还需要在客户端实体文件里把动画登记到`animations`，再在`scripts/animate`或动画控制器中播放它。

```json
{
  "animations": {
    "idle": "animation.practice_robot.idle"
  },
  "scripts": {
    "animate": [
      "idle"
    ]
  }
}
```

## 导出到资源包

完成后按下面的方式保存：

| 内容 | 推荐位置 |
| --- | --- |
| 几何体 | `RP\models\entity\practice_robot.geo.json` |
| 纹理 | `RP\textures\entity\practice_robot.png` |
| 动画 | `RP\animations\practice_robot.animation.json` |
| 工程源文件 | 项目源文件夹中的任意安全位置，例如`source\practice_robot.bbmodel` |

最后在游戏中测试前，检查客户端实体文件是否同时引用了正确的几何体、纹理、材质、动画和渲染控制器。若模型不显示，优先查看内容日志，再检查标识符和文件路径是否一致。
