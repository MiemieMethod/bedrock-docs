# 国际版开发入门<!-- md:flag vanilla -->

这是一份面向“已有中国版开发经验、准备进入国际版生态”的入门路线图。它不是API参考，而是学习顺序建议：先建立信息源，再按能力层级推进，并用本站现有文档作为主学习材料。

## 适用对象

- 已经做过中国版附加包或模组SDK开发。
- 需要迁移到国际版附加包与脚本API工作流。
- 想要获得“从零到可持续迭代”的学习路径，而不是零散知识点。

## 阶段0：先建立信息源

先把“资料入口”搭好，再开始做内容，效率会高很多。

### 官方渠道

- [Microsoft Learn基岩版创作者文档](https://learn.microsoft.com/zh-cn/minecraft/creator/)
- 官方帮助中心更新日志（可结合本站[翻译版更新日志](../translations/help-center/changelogs/index.md)）

### 社区渠道

- [基岩维基（翻译）](../translations/bedrock-wiki/index.md)
- [基岩版命令更新记录（翻译）](../translations/command-log/index.md)
- [《我的世界》基岩版开发维基](https://wiki.mcbe-dev.net/)

## 阶段1：完成初级目标

先建立“可落地制作”的基本能力，建议按下列顺序学习：

1. 认识附加包与JSON基础  
   - [认识附加包](addons/understanding-addons.md)  
   - [认识JSON](addons/understanding-json.md)
2. 处理命令与红石的基础逻辑  
   - [命令系统实践模板](misc/command-systems.md)  
   - [新版execute命令](misc/execute-command.md)
3. 完成基础资源与打包能力  
   - [本地化](addons/localization.md)  
   - [制作纹理包](addons/creating-texture-packs.md)  
   - [制作皮肤包](addons/creating-skin-packs.md)  
   - [创建世界模板](addons/create-a-world-template.md)
4. 开始数据驱动三大核心对象  
   - [自定义方块](addons/data-driven/blocks/index.md)  
   - [自定义物品](addons/data-driven/items/index.md)  
   - [自定义实体](addons/data-driven/entities/index.md)

## 阶段2：进入中级目标

这一阶段重点是“系统化组织玩法逻辑”和“提高内容复杂度”：

- 深入实体事件、组件组与行为编排。  
- 掌握NPC对话与结构方块工作流。  
- 将函数、命令、记分板作为可维护系统使用。  

建议结合以下内容推进：

- [实体事件相关教程集合](addons/data-driven/entities/index.md)
- [NPC对话进阶](addons/data-driven/entities/npc-dialogue.md)
- [命令系统专题集合](misc/index.md)

## 阶段3：冲刺高级目标

这一阶段关注“跨系统联动能力”和“兼容性控制能力”：

- 熟练使用Molang、粒子、迷雾等表现系统。
- 进入地物、维度、生物群系等世界生成内容。
- 进行脚本API与数据驱动的混合工作流设计。
- 必要时进行存档级调试与NBT核对。

建议配套阅读：

- [认识Molang](addons/data-driven/understanding-molang.md)
- [脚本API教程](addons/script-api/index.md)
- [地物与世界生成相关教程](addons/data-driven/index.md)
- [存档概念文档](../docs/save/save.md)

## 中国版迁移到国际版时的三条硬规则

1. 国际版不支持中国版模组SDK工作流。  
2. 面向玩家可见文本时，本地化要先做，不要后补。  
3. 命令、Molang、数据驱动格式都要按目标版本复核，不以旧项目经验直接套用。

## 建议的学习节奏

- 每周固定1次“版本差异复盘”：只看变更，不盲目追新。
- 每完成一个阶段，做一个最小可运行示例包并归档。
- 形成“概念文档→教程实践→参考检索”的闭环：  
  先看[文档](../docs/index.md)理解概念，再看教程做落地，最后去[参考](../refs/index.md)查字段和参数。
