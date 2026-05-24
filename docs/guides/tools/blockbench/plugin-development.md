# 插件开发

Blockbench插件适合处理“反复点很多次鼠标”的工作，例如批量改立方体属性、生成辅助骨骼、导出前检查模型结构，或给自己的团队增加一套专用按钮。它们不是基岩版运行时内容，而是只在Blockbench里生效的工具扩展。

## 什么时候值得写插件

只有当下面这些情况反复出现时，写插件才通常值得：

- 同一组操作需要在很多模型上重复执行。
- 现有插件做不到，但你的工作流很稳定。
- 需要把团队经验固化成按钮、对话框或校验步骤。
- 需要给建模、动画或贴图过程补一段自动化。

如果只是一次性修改几个数值，直接用表达式、复制粘贴或现有插件通常更划算。

## 最小文件结构

Blockbench插件的最小单位就是一个JavaScript文件。文件名去掉扩展名后的部分，必须与插件ID一致。例如：

```text
height_randomizer.js
```

文件内部通常用`Plugin.register`注册元数据和生命周期：

```javascript
Plugin.register('height_randomizer', {
  title: 'Height Randomizer',
  author: 'YourName',
  description: '随机调整选中立方体的高度',
  icon: 'bar_chart',
  version: '0.0.1',
  variant: 'both',
  onload() {
  },
  onunload() {
  }
})
```

常见字段含义如下：

| 字段 | 用途 |
| --- | --- |
| `title` | 在插件商店和菜单里显示的名称。 |
| `author` | 作者名称。 |
| `description` | 插件说明。 |
| `icon` | 图标名，使用Blockbench图标系统。 |
| `tags` | 最多三个标签。面向Minecraft的插件通常应使用`Minecraft`、`Minecraft: Java Edition`或`Minecraft: Bedrock Edition`之一。 |
| `version` | 插件版本号，建议遵循`semver`。 |
| `variant` | 可选`desktop`、`web`或`both`。 |
| `min_version` | 最低兼容Blockbench版本。 |
| `await_loading` | 插件必须先完成加载时可启用。 |
| `onload` | 插件载入或重载后执行。 |
| `onunload` | 插件卸载时执行清理。 |

## 开发环境

纯JavaScript就能写插件，但如果想要补全和类型提示，官方建议安装`blockbench-types`：

```bash
npm i --save-dev blockbench-types
```

这在使用TypeScript时尤其有用。Blockbench5.0开始把类型逐步迁回主仓库维护，因此类型通常比旧版社区说明更接近当前实现。

## 测试与重载

测试插件最直接的方式有两种：

1. 在插件菜单中从本地文件加载。
2. 把`.js`文件直接拖进Blockbench。

修改后，可以在插件菜单中重载，或使用++ctrl+J++/++cmd+J++重载当前插件。这样比反复重启Blockbench更快。

## 改模型时一定要接入撤销系统

只要插件会修改元素、纹理、动画或选择状态，就应该先调用`Undo.initEdit`，完成后再调用`Undo.finishEdit`。这样不仅能让用户撤销操作，也能在多人编辑会话中正确同步模型状态。

下面这个示例会给所有选中立方体随机改高度，并立即刷新视图：

```javascript
let button

Plugin.register('height_randomizer', {
  title: 'Height Randomizer',
  author: 'YourName',
  description: '随机调整选中立方体的高度',
  icon: 'bar_chart',
  version: '0.0.1',
  variant: 'both',
  onload() {
    button = new Action('randomize_height', {
      name: 'Randomize Height',
      description: '随机调整选中元素的高度',
      icon: 'bar_chart',
      click() {
        Undo.initEdit({ elements: Cube.selected })
        Cube.selected.forEach((cube) => {
          cube.to[1] = cube.from[0] + Math.floor(Math.random() * 8)
        })
        Canvas.updateView({
          elements: Cube.selected,
          element_aspects: { geometry: true },
          selection: true
        })
        Undo.finishEdit('Randomize cube height')
      }
    })
    MenuBar.menus.tools.addAction(button)
  },
  onunload() {
    button.delete()
  }
})
```

如果你的插件会新增或删除元素、纹理、关键帧等对象，就要把受影响对象放进`aspects`里，而不是只刷新界面。

## 常见交互方式

做插件时，经常需要和用户确认输入或反馈状态。Blockbench内置了几种足够常用的界面方法：

| 方法 | 作用 |
| --- | --- |
| `Blockbench.showMessageBox` | 弹出带按钮的消息框。 |
| `Blockbench.textPrompt` | 让用户输入或修改一段文本。 |
| `Blockbench.showToastNotification` | 在视口顶部显示短通知。 |
| `Blockbench.showQuickMessage` | 在界面中央显示短提示。 |
| `Blockbench.showStatusMessage` | 在状态栏显示提示文本。 |

如果只是提示“完成”“失败”或“已导出”，优先用轻量通知；只有需要用户确认或填写内容时，再弹对话框。

## Blockbench5.0需要注意的兼容变化

如果你维护的是旧插件，升级到Blockbench5.0时要重点检查这些点：

### 原生模块权限

桌面版不再默认把大多数Node模块暴露给插件。需要访问系统模块时，应按需调用`requireNativeModule`，并尽量在真正需要时再请求权限，而不是在插件加载时一次性全部申请。

```javascript
const child_process = requireNativeModule('child_process', {
  message: '此权限用于调用ffmpeg导出视频。'
})
```

### 受限文件系统

`fs`能力比旧版本更受限制。5.0还支持按目录申请作用域文件系统，这样插件只能读写指定目录，用户也更容易判断授权范围。

### 选中组接口变化

`Group.selected`不再返回单个组，而是返回顶层选中组数组。旧插件如果默认只处理一个组，应改成遍历数组，或改用`Group.first_selected`。

### 动画关键帧方向修正

旧版`.bbmodel`和部分基岩版动画导入导出会涉及关键帧方向修正。官方提供了`invertMolang`辅助函数，供插件在处理旧数据时使用。

## 发布与分发

如果插件只给自己或团队内部使用，从本地文件加载就足够。若希望进入官方插件生态，则需要把插件提交到`blockbench-plugins`仓库，并在仓库的插件清单中登记与插件文件一致的ID和元数据。

## 对基岩版创作者的实际建议

基岩版工作流里最适合做成插件的内容通常不是“完整导出器”，而是：

- 统一骨骼命名和层级检查。
- 批量修正轴心点或旋转值。
- 批量生成占位动画或辅助关键帧。
- 导出前检查贴图尺寸、命名空间和文件名。

先把自己的手工流程做稳定，再把其中最枯燥、最容易出错的一段自动化，插件才会真正帮上忙。