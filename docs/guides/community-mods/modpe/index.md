# ModPE

ModPE是BlockLauncher时代的旧客户端脚本生态。它在基岩版早期Android模组开发中很重要，但没有确认到独立、系统、可直接改写为本站教程的ModPE资料；目前只在InnerCore文档中确认到对BlockLauncher和ModPE的比较、替代和兼容提及。因此，本页不编写具体ModPE API教程，只作为旧生态辨析和迁移入口。

## 已能确认的事实

Nernar维护的InnerCore文档说明，InnerCore的思路基于BlockLauncher，但旧BlockLauncher的能力集合较少，长期主要在修复现有接口，而不是持续扩展新接口。InnerCore相对BlockLauncher的变化包括：

- 模组不再只是一个脚本，而是包含`build.config`、脚本、资源、图标和设置的文件夹。
- 脚本可以拆分为多个文件和执行上下文。
- 资源加载通过构建配置描述，不必全部绑定到主目录。
- 可以结合Java或原生代码进行扩展。

InnerCore旧更新记录还提到过CoreEngine for BlockLauncher和ModPE Loader，并说明后者曾尝试从特殊目录加载并运行ModPE脚本，处理ID冲突等问题。暂无公开资料提供足够资料说明这些兼容层在当前环境下的可用性。

## 维护旧ModPE脚本时怎么做

1. 先固定目标环境：Minecraft版本、Android版本、BlockLauncher版本和脚本来源。
2. 不要先重写，先记录脚本使用的事件、物品、方块、实体和全局变量。
3. 如果目标是迁移到ICMod，先把单脚本逻辑拆成资源、注册逻辑和回调逻辑。
4. 如果目标是迁移到官方附加包，先判断哪些内容可以转成数据驱动，哪些必须改用脚本API或服务器插件。

## 当前限制

缺少相关内容：没有独立ModPE API参考、没有系统教程、没有可确认的当前兼容性表。因此，本站暂时不提供“第一个ModPE脚本”这类步骤教程。后续如果补充了可靠资料，再继续扩展本页。