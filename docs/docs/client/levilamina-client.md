# LeviLamina客户端模组

**LeviLamina客户端模组（LeviLamina Client Mod）**是基于LeviLamina客户端构建的原生扩展形态。该形态通过PreLoader将LeviLamina客户端构建加载到受支持的Windows版Minecraft客户端进程，并由LeviLamina提供模组生命周期与接口能力。

## 定位

LeviLamina客户端模组不属于官方附加包体系，也不等同于Android旧生态中的ModPE或InnerCore。它属于面向原生二进制接入的客户端扩展路线，通常使用C++实现。

## 与LeviLamina服务端模组的关系

LeviLamina客户端模组与LeviLamina服务端模组共享部分通用API与工程体系，但目标进程、可用模块和兼容边界不同。服务端相关背景见[LeviLamina](../server/levilamina.md)。

## 兼容性边界

LeviLamina客户端模组的可用性受LeviLamina版本、目标客户端版本、平台与二进制接口稳定性影响。基岩版更新可能导致旧版客户端模组失效，因此其版本维护策略通常比高层数据驱动内容更严格。
