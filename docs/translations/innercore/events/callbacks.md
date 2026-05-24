# 回调

/// details-info | 来源信息
- 原文仓库：[github.com/nernar/nernar.github.io](https://github.com/nernar/nernar.github.io)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


/// details-info | 署名信息
- 该页面内容翻译自[nernar.github.io](https://nernar.github.io/docs/events/callbacks)
- 原文档采用[GNU通用公共许可证第3版](https://www.gnu.org/licenses/gpl-3.0.html)（GPL-3.0）授权
///

回调用于为事件注册处理函数。原文档推荐使用`Callback.addCallback`注册，并通过优先级控制执行顺序。

## 基础示例

```javascript
Callback.addCallback("EventName", function() {
  // 事件处理逻辑
}, 0);
```

## 关键原则

1. 不要在事件回调内部重复注册新的同类回调，否则会导致处理器叠加。
2. 先做轻量条件判断，再执行高成本逻辑。
3. 同一事件尽量集中管理，避免多处重复监听。
4. 高负载逻辑应拆分到多个刻执行，降低卡顿风险。

## 自定义事件

原文档也支持通过`Callback.invokeCallback`触发自定义事件，用于组织模组内部流程。该能力不应用于伪造游戏内置事件。