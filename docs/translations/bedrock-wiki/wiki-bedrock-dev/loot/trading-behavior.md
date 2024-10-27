---
title: 交易行为
category: 一般
nav_order: 2
mentions:
    - Ciosciaa
    - MedicalJewel105
description: 使您的实体具备像村民一样交易的能力。
---

使实体成为交易者可以通过 `minecraft:trade_table` 或 `minecraft:economy_trade_table` 组件来实现。这两者都会从给定路径打开交易用户界面，但经济交易组件有一些额外选项，涉及到一些村庄与掠夺的交易机制。您还需要其他 AI 目标，如 `minecraft:behavior.trade_with_player`，可选的 `minecraft:behavior:trade_interest`（允许生物持有/提供物品），以及可能的 `"minecraft:trade_resupply": {}`。

对于简单的交易用户界面，`trade_table` + `trade_with_player` 组件应该就足够了。

1. 在您的实体组件中添加 `"minecraft:behavior.trade_with_player": {}`。
2. 将以下代码复制到您的实体的组件组中。我将其称为 `"wiki:trader"`；

<CodeHeader>BP/entities/trader.json</CodeHeader>

```json
"minecraft:trade_table": {
	"display_name": "交易实体", // 显示的文本。
	"table": "trading/trading_entity_trades.json", // 交易表文件的路径
	"new_screen": true // 如果设置为 false，用户界面将显示为预 Village&Pillage 版本。
}
```

3. 现在确保通过事件将组件组添加到实体中。最好在 `minecraft:entity_spawned` 事件中添加，因为它在实体生成时触发。
如果您对事件和组件组不太自信，请确保您熟悉实体定义规则/概念。请参见 [实体简介](../entities/entity-intro-bp.md)。

:::warning
如果您在组件中添加该组件，将会导致各种问题，包括世界中所有实体的交易用户界面为空白。由于交易 AI 目标存在问题，必须在组件组中添加它们。
:::