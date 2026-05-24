# 模组结构

/// details-info | 署名信息
- 该页面内容翻译自[nernar.github.io](https://nernar.github.io/docs/basics/mod-structure)
- 原文档采用[GNU通用公共许可证第3版](https://www.gnu.org/licenses/gpl-3.0.html)（GPL-3.0）授权
///

InnerCore模组本质上是一个文件夹，其核心是`build.config`。该文件描述资源目录、脚本构建、编译入口以及Java/C++目录位置。

## 常见模板结构

/// html | div.treeview
- 模组根目录
    - `.dex`
    - `dev/`
        - `.includes`
        - `header.js`
    - `assets/`
        - `resources/`
        - `gui/`
    - `launcher.js`
    - `build.config`
    - `mod.info`
    - `mod_icon.png`
    - `config.json`
    - `config.info.json`
///

## 关键文件职责

- `mod.info`：展示名称、作者、版本与简介。
- `config.json`：保存可持久化的模组设置。
- `build.config`：定义资源加载、脚本构建与编译行为。

## 构建要点

`build.config`常见字段包括：

- `defaultConfig`：基础构建配置与API类型。
- `resources`：资源目录列表及类型。
- `buildDirs`：按`.includes`聚合脚本的目录。
- `compile`：最终入口脚本及来源类型。

旧项目维护时，应优先核对这些字段是否与目标运行环境匹配。