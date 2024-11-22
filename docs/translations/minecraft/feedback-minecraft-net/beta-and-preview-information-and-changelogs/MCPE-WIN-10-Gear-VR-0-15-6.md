---
标题: MCPE/WIN 10/Gear VR - 0.15.6
日期: 2018-05-23T08:57:55Z
更新: 2018-05-23T21:24:40Z
类别: 测试版和预览信息及更新日志
标签:
  - windows_10
  - gear_VR
  - mcpe
  - 0.15.6
链接: https://feedback.minecraft.net/hc/en-us/articles/360004166531-MCPE-WIN-10-Gear-VR-0-15-6
---

关于Minecraft: Windows 10版测试版与Oculus Rift支持的常见问题解答

问: 我没有Windows 10——我在运行Windows 7/Windows 8/Linux/OSX。我可以使用Minecraft: Windows 10版测试版与Oculus Rift支持吗？

答: 您需要运行Windows 10操作系统才能使用Minecraft: Windows 10版测试版。

问: Oculus启动器崩溃并显示错误0x80070422。我该怎么办？

答: 确保您已启用Windows更新。

1. 按下Windows键
2. 输入“服务”
3. 向下滚动到Windows更新并右键点击。
4. 从菜单中选择“启动”。

问: 我的Oculus启动器崩溃，但它在ucrtbase.dll中给我一个异常。

或者我的Oculus启动器提示需要Windows 10，更新1511。我该怎么办？

答: 这可能是由于Windows更新失败或未应用导致的。

1. 在此下载并运行官方Windows更新故障排除工具：http://download.microsoft.com/download/F/E/7/FE74974A-9029-41A0-9EB2-9CCE3FC20B99/WindowsUpdateDiagnostic.diagcab
2. 按下Windows键。
3. 输入“检查更新”
4. 检查并安装任何缺失的Windows更新
5. 使用电源菜单中的“重启”选项重启计算机。

问: Oculus启动器告诉我启动Minecraft“失败”？

答: 检查确保您没有已经在运行Minecraft: Windows 10版测试版。如果您已经在运行，请确保先关闭该应用程序，然后再尝试从Oculus启动器启动。如果问题仍然存在，尝试通过Xbox应用程序运行Minecraft: Windows 10版测试版。这可能会让您更清楚为什么游戏无法运行。

问: Oculus启动器报告2015.3 x86重分发DLL的签名问题。

或者Oculus启动器崩溃，而我的主要语言文件不是英语。

答: 好消息——我们推出了一个修复，应该能解决这两个问题。只需重启您的Oculus商店，并接受您在Minecraft中看到的更新。

问: 当我尝试玩游戏时，看到奇怪的图形问题。

答: 确保您的图形驱动程序是最新的。如果您有Nvidia显卡，可能需要手动访问Nvidia网站以获取您显卡的最新驱动程序。下载并安装新驱动程序，然后使用电源菜单中的重启选项重启计算机。

问: 我有双显卡和多个显示器。我能听到Minecraft的音乐，但Minecraft卡在一个显示“请稍候”的白屏上。

答: 这可能是由于您的显卡在HDMI输入和Rift之间的某些混淆。如果您有HDMI输入连接到两个显卡，请拔掉与Oculus Rift无关的HDMI输入。

由于此更新主要集中在Oculus Rift支持上，我们在上面包含了Oculus常见问题解答的更新日志。和往常一样，如果您遇到任何漏洞，请在Jira上报告！我们想知道您对我们Oculus Rift集成的看法。点击这里给我们反馈！

新特性：

- Minecraft: Windows 10版测试版现在支持Oculus Rift！

调整：

- 在启用Oculus Rift时，键盘和鼠标支持更好。
- 在Oculus Rift模式下调整Windows 10用户界面以提高可用性。

漏洞修复：

- Oculus平台启动器更新了本地化处理修复和正确的虚拟工作室重分发包。
- 音频现在通过用户选择的音频设备播放。
- 您可以使用键盘上的“C”键在电视模式和沉浸模式之间切换。
- 修复了一些本地化字体（所有版本）。
- 修复了Gear VR版的一个小崩溃问题。