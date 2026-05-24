# LeviLamina客户端模组

**LeviLamina客户端模组（LeviLamina Client Mod）**是LeviLamina面向Windows版Minecraft客户端的原生模组形态。它通过PreLoader加载到受支持的`Minecraft.Windows.exe`进程，并在客户端构建中提供模组生命周期、输入、渲染、界面和部分引擎访问能力。

## 定位

LeviLamina客户端模组不属于官方附加包体系，也不等同于Android旧生态中的ModPE或InnerCore。它属于面向原生二进制接入的客户端扩展路线，通常使用C++实现，并且必须与目标客户端版本和LeviLamina版本保持匹配。

## 构建目标

- 客户端构建目标为`client`。
- 通用代码位于`src/`，客户端专用代码位于`src-client/`。
- 客户端相关头文件位于`src-client/ll/api/`。
- 客户端构建使用`bedrockdata:client.9`一类的客户端头文件。

## 可用能力

客户端构建中最典型的专用能力包括：

- 键盘和鼠标输入绑定。
- 客户端生命周期事件。
- 输入事件、渲染事件和界面渲染前后事件。
- 与客户端进程相关的Bedrock对象访问。

部分通用模块，例如事件系统和服务系统，也可以在客户端构建中使用；但其具体触发时机、返回对象和可用范围仍然受目标环境限制。

## 前提条件

- Windows10或Windows11。
- Visual C++运行库。
- LeviLauncher。
- lip。

## 安装方式

客户端侧通常先通过LeviLauncher安装受支持的Minecraft基岩版客户端版本，再通过启动器的插件管理功能安装LeviLamina。若需要手动安装，也可以在客户端目录中执行lip命令，例如：

```shell
lip install github.com/LiteLDev/LeviLamina#client@26.10.3
```

升级时可以直接使用：

```shell
lip update github.com/LiteLDev/LeviLamina#client@26.10.3 github.com/LiteLDev/bedrock-runtime-data@1.21.132-client.3
```

具体支持的客户端版本与LeviLamina版本对应关系，请查看[支持的版本](../../translations/levilamina/versions.md)。

## 与服务端模组的关系

LeviLamina客户端模组与LeviLamina服务端模组共享部分通用API与工程体系，但目标进程、可用模块和兼容边界不同。服务端相关背景见[LeviLamina](../server/levilamina.md)，构建细节见[构建指南](../../guides/servers/levilamina/build-guide.md)。

## 兼容性边界

LeviLamina客户端模组的可用性受LeviLamina版本、目标客户端版本、平台与二进制接口稳定性影响。基岩版更新可能导致旧版客户端模组失效，因此其版本维护策略通常比高层数据驱动内容更严格。

## 相关页面

- [LeviLamina文档归档](../../translations/levilamina/index.md)
- [在客户端上安装](../../translations/levilamina/install-client.md)
- [支持的版本](../../translations/levilamina/versions.md)
- [LeviLamina](../server/levilamina.md)
- [LeviLamina详细指南](../../guides/servers/levilamina/index.md)
- [LeviLamina API模块](../../refs/server/levilamina-api.md)
