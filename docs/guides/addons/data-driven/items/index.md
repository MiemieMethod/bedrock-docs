---
hide:
  - toc
---

# 自定义物品

本系列教程涵盖基岩版附加包中自定义物品的所有核心主题，从入门的物品创建到进阶的脚本事件与附着物，由浅入深地带你掌握物品系统的方方面面。

## 入门

/// html | div.grid.cards
- :material-cube-send: __[添加自定义物品](adding-custom-items.md)__

    从零开始创建一个自定义物品，了解物品JSON的基本结构、图标注册与显示名称。

- :material-format-list-bulleted: __[物品组件总览](item-components.md)__

    一览全部可用的物品组件，了解它们的分类与用途。

- :material-label: __[物品标签](item-tags.md)__

    为物品添加标签，并在过滤器、Molang查询与配方中使用标签批量匹配物品。
///

## 功能性物品

/// html | div.grid.cards
- :material-food-apple: __[自定义食物](custom-food.md)__

    制作可食用物品，通过脚本API在食用时给予玩家状态效果。

- :material-sword: __[自定义武器](custom-weapons.md)__

    制作具有攻击伤害、附魔和修复属性的近战武器。

- :material-shield: __[自定义盔甲](custom-armor.md)__

    制作完整的四件套盔甲，配置纹理、附着物和套装效果。

- :material-timer-sand: __[物品耐久](item-durability.md)__

    为物品添加耐久消耗机制，通过脚本API精确控制每次损耗量。

- :material-rocket-launch: __[可投掷物品](throwable-items.md)__

    制作可以投掷的物品，命中时触发自定义效果。
///

## 脚本与进阶

/// html | div.grid.cards
- :material-code-tags: __[物品事件](item-events.md)__

    通过脚本API注册自定义组件，响应使用、命中、消耗等物品事件。

- :material-human: __[物品附着物](item-attachables.md)__

    使用附着物在玩家手持或穿戴物品时渲染3D模型。

- :material-flash: __[装备物品效果](equipped-item-effects.md)__

    检测玩家持有或穿戴特定物品，并给予相应的状态效果。

- :material-drop: __[在世界中生成物品](spawning-items.md)__

    通过命令、战利品表、虚假实体等方法在世界中放置物品掉落物。

- :material-pot-mix: __[自定义陶片](custom-pottery-sherds.md)__

    制作可用于装饰陶罐的自定义陶片，并注册图案纹理。
///