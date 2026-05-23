# JSON UI进阶技巧<!-- md:flag vanilla -->

本组教程聚焦国际版JSON UI中的实战技巧：如何更稳地改HUD、如何用绑定做条件渲染、如何把字符串转成可计算数值，以及如何在界面里播放序列帧动画。

/// warning | 适用范围
本组内容基于国际版JSON UI。中国版模组SDK可通过专有接口实现更直接的界面逻辑，不必照搬这些方案。
///

/// html | div.grid.cards
- :material-shield-check: __[JSON UI最佳实践](best-practices.md)__
  学会在版本更新中尽量降低界面崩溃风险，并优化界面性能。
- :material-view-dashboard: __[向HUD添加元素](add-hud-elements.md)__
  通过`root_panel`和`modifications`安全插入自定义控件。
- :material-format-title: __[通过Title保留并更新HUD文本](preserve-title-texts.md)__
  仅在标题含特定标记时更新界面内容。
- :material-calculator-variant-outline: __[字符串转数值](string-to-number.md)__
  处理绑定字符串与数值比较、数值转文本显示。
- :material-filmstrip-box-multiple: __[使用Aseprite序列帧动画](aseprite-flipbook.md)__
  导出精灵表并在JSON UI中使用`aseprite_flip_book`。
///

## 学习前提

建议先阅读：

- [JSON UI](../../../docs/general/json-ui.md)
- [JSON UI文件参考](../../../refs/addon/json-ui.md)
- [Molang](../../../docs/general/molang.md)
