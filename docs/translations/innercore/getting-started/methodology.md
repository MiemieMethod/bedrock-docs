# 方法论

/// details-info | 来源信息
- 原文仓库：[github.com/nernar/nernar.github.io](https://github.com/nernar/nernar.github.io)
- 许可说明：以原仓库或原站点公开许可声明为准。
///


/// details-info | 署名信息
- 该页面内容翻译自[nernar.github.io](https://nernar.github.io/docs/getting-started/methodology)
- 原文档采用[GNU通用公共许可证第3版](https://www.gnu.org/licenses/gpl-3.0.html)（GPL-3.0）授权
///

方法论用于建立统一语境：世界由方块、物品、生物、地形生成与游戏模式等要素共同构成；模组项目则由概念设计、代码实现、美术资源、测试调试与打包发布组成。

## 引擎、包与启动器

InnerCore生态可概括为一条链路：Horizon启动器加载InnerCore包，InnerCore包再加载CoreEngine接口，模组最终通过CoreEngine与游戏交互。该结构解释了“为什么旧客户端模组通常依赖特定启动器与包版本”。

## 模组与模组包

- **模组**是包含脚本、资源与配置的功能单元。
- **模组包**是多个模组与其配置的集合，通常带有独立世界与独立设置。

理解这一层级关系后，再进入安装与环境配置会更清晰。