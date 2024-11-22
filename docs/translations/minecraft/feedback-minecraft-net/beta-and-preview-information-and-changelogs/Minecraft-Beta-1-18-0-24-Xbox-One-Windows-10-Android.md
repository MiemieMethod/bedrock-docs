---
title: Minecraft Beta - 1.18.0.24 (Xbox One/Windows 10/Android)
date: 2021-10-27T13:04:24Z
updated: 2021-10-27T15:47:31Z
categories: Beta和预览信息与更新日志
tags:
  - beta
  - beta_changelog
  - caves&cliffs
link: https://feedback.minecraft.net/hc/en-us/articles/4412150636941-Minecraft-Beta-1-18-0-24-Xbox-One-Windows-10-Android
---

**发布于：** 2021年10月27日

**在参与Minecraft Beta之前，请阅读：**

- 加入测试版将用一个正在开发中的Minecraft版本替换您的游戏
- 您将无法访问领域，并且在预览测试版时无法加入非测试版玩家
- 在测试版中游玩的任何世界无法在游戏的先前版本中打开，因此请制作世界的副本以防丢失
- 测试版构建可能不稳定，并不代表最终版本的质量
- 测试版仅在Xbox One、Windows 10和Android（Google Play）上提供。要加入或退出测试版，请参见[aka.ms/JoinMCBeta](https://aka.ms/JoinMCBeta)以获取详细说明

![modal_crop.jpg](https://feedback.minecraft.net/hc/article_attachments/4412158002061/modal_crop.jpg)

 

又到了Bedrock测试版的时间！和往常一样，我们非常感谢您发送到[aka.ms/CavesCliffsFeedback](http://aka.ms/CavesCliffsFeedback)的所有反馈，请在[bugs.mojang.com](http://bugs.mojang.com/)报告您可能发现的任何漏洞。

另外！在本周测试版的更改之后，我们计划更新游戏内的种子选择器，添加一些新的种子，我们希望听到您发现的具有特定地物和生物群系的种子！请在此线程中分享任何优秀的种子建议：<https://aka.ms/MCSeedPicker>，并查看此[常见问题解答](https://aka.ms/SeedPickerFAQ)以获取更多信息！

# **地物和漏洞修复**

## **方块**

- 玩家现在可以再次通过按住“放置”按钮连续放置水、熔岩和细雪（[MCPE-139671](https://bugs.mojang.com/browse/MCPE-139671)）
- 光源方块不再支持需要支撑的方块，例如床和画（[MCPE-144311](https://bugs.mojang.com/browse/MCPE-144311)）

### **废弃矿井**

- 废弃矿井的支柱不再生成在熔岩中（[MCPE-135221](https://bugs.mojang.com/browse/MCPE-135221)）
- 废弃矿井不再生成泥土地面（[MCPE-141583](https://bugs.mojang.com/browse/MCPE-141583)）
- 废弃矿井现在使用原木方块来创建支撑柱（[MCPE-125133](https://bugs.mojang.com/browse/MCPE-125133)）

## **游戏玩法**

- 修复了导致某些世界大小增加的问题，从而导致高内存使用（[MCPE-143156](https://bugs.mojang.com/browse/MCPE-143156)）
- 修复了在持有小滴叶时，浅水在瞄准时变亮的问题（[MCPE-123373](https://bugs.mojang.com/browse/MCPE-123373)）
- 高大的花朵在被放置在花的上半部分的水破坏时现在只会掉落一个物品（[MCPE-142799](https://bugs.mojang.com/browse/MCPE-142799)）
- 修复了可以透过地形看到的问题
- 教育功能：NPC不再有闲置声音（[MCPE-141856](https://bugs.mojang.com/browse/MCPE-141856)）
- 紫颂果现在在负Y坐标下正常工作（[MCPE-135951](https://bugs.mojang.com/browse/MCPE-135951)）

## **物品**

- 调整了被激活的TNT、滞留药水、喷溅药水和附魔之瓶在远离玩家时的移动平滑度（[MCPE-101102](https://bugs.mojang.com/browse/MCPE-101102)）
- 多个教育版物品不再显示“craftingScreen.tab.none”提示框（[MCPE-102444](https://bugs.mojang.com/browse/MCPE-102444)）
- 现在所有地面植被都可以放置在菌丝体上（[MCPE-125928](https://bugs.mojang.com/browse/MCPE-125928)）

## **生物**

- 增加了美西螈在繁茂洞穴自然生成的几率
- 鱼类现在会试图避开美西螈
- 岩浆怪现在对铁傀儡表现出正确的攻击性，而史莱姆不再对雪傀儡表现出攻击性（[MCPE-51162](https://bugs.mojang.com/browse/MCPE-51162)）
- 幻翼现在应该能够在试图路径寻找进入山脉时自我解脱（[MCPE-119773](https://bugs.mojang.com/browse/MCPE-119773)）

## **世界生成**

- 矿团生成现已调整为与Java版保持一致
- 沙砾现在可以在世界生成时正确替代深板岩（[MCPE-144080](https://bugs.mojang.com/browse/MCPE-144080)）
- 恶地生物群系中的金矿石不再生成过多
- 冻洋生物群系中不再生成熔岩源（[MCPE-144733](https://bugs.mojang.com/browse/MCPE-144733)）
- 深层铜矿石变种现在在世界中正确生成
- 更新了新的洞穴与山崖山脉生物群系的命名，以更好地与基岩版和Java版之间保持一致

## **用户界面**

- 修复了文本中图标的渲染，使颜色不再失真

# **技术更新**

## **生物**

- 修复了在JSON中未指定时生物的默认召唤能力

## **远程攻击目标**

- 改进了不移动的生物在“远程攻击目标”中的性能