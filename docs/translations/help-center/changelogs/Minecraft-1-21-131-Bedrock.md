---
title: "Minecraft-1.21.131（基岩版）"
date: 2025-12-16T16:21:17Z
updated: 2025-12-16T16:21:42Z
categories: 发布日志
original_link: https://feedback.minecraft.net/hc/en-us/articles/41979788279181-Minecraft-1-21-131-Bedrock
hash:
  user-content-fixes: 修复
  user-content-general: 常规
  user-content-mounts-of-mayhem: 混乱坐骑
  user-content-spear: 长矛
  user-content-marketplace: 市场
  user-content-technical-updates: 技术更新
  user-content-api-infra: API基础设施
  user-content-graphical: 图形
---

**发布时间**：2025年12月16日

该修复版用于处理上一版本中发现的问题，将按平台逐步推送。

# 修复 {#fixes}

## 常规 {#general}

- 修复了在PC平台中，访问少于17个生物群系时仍可能解锁“探索时光”成就的问题（[MCPE-156784](https://bugs.mojang.com/browse/MCPE-156784)）。

## 混乱坐骑 {#mounts-of-mayhem}

### 长矛 {#spear}

- 提高了长矛蓄力阶段可触发击退的持续时间。
- 调整了蓄力攻击动画，使其与长矛的玩法阶段（投入、疲劳、脱离）对齐，以提升视觉反馈一致性。

## 市场 {#marketplace}

- 修复了在市场搜索后，按++esc++无法返回主菜单的问题（[MCPE-232316](https://bugs.mojang.com/browse/MCPE-232316)）。

# 技术更新 {#technical-updates}

## API基础设施 {#api-infra}

- 修复了在加载存档或创建世界时，启用多个附加包可能触发`Block`错误码的问题（[MCPE-232978](https://bugs.mojang.com/browse/MCPE-232978)）。

## 图形 {#graphical}

- 修复了Switch在加载附加包或连接服务器时，UI纹理显示异常的问题。
