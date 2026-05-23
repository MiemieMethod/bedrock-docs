# Nukkit-MOT API概览

本文列出Nukkit-MOT文档中出现的主要配置、插件开发入口和常用API主题。Nukkit-MOT是第三方自实现服务端，以下内容均属于Nukkit-MOT项目或Nukkit生态接口，不是BDS原生能力。

/// warning | 版本提示
Nukkit-MOT的接口、协议兼容范围和运行时行为会随项目构建变化。插件开发应以当前Nukkit-MOT源码、Javadoc、发行说明和目标插件依赖为准。
///

## 构建依赖

Nukkit-MOT文档给出的Maven仓库为：

```xml title="pom.xml"
<repositories>
    <repository>
        <id>repo-lanink-cn</id>
        <url>https://repo.lanink.cn/repository/maven-public/</url>
    </repository>
</repositories>
```

Maven依赖示例：

```xml title="pom.xml"
<dependencies>
    <dependency>
        <groupId>cn.nukkit</groupId>
        <artifactId>Nukkit</artifactId>
        <version>MOT-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

Gradle Kotlin DSL依赖示例：

```kotlin title="build.gradle.kts"
repositories {
    mavenCentral()
    maven("https://repo.lanink.cn/repository/maven-public/")
}

dependencies {
    compileOnly("cn.nukkit:Nukkit:MOT-SNAPSHOT")
}
```

## 常用配置项

| 配置项 | 示例值 | 说明 |
|--------|--------|------|
| `server-port` | `19132` | 服务端监听的UDP端口。 |
| `server-ip` | `0.0.0.0` | 绑定地址，`0.0.0.0`表示监听所有网络接口。 |
| `gamemode` | `0` | 默认游戏模式，常见值为0至3。 |
| `difficulty` | `1` | 默认难度，常见值为0至3。 |
| `max-players` | `20` | 最大玩家数。 |
| `white-list` | `false` | 是否启用白名单。 |
| `motd` | `A Nukkit Server` | 服务器列表中显示的描述。 |
| `xbox-auth` | `true` | 是否启用Xbox账号验证。 |
| `view-distance` | `8` | 服务端视距。降低该值可减少区块负载。 |
| `netease-client-support` | `true` | 启用网易我的世界客户端连接支持<!-- md:flag china -->。 |

## 方块API

Nukkit-MOT中的`Block`类位于`cn.nukkit.block`包，是表示和操作世界方块的核心类型。

| 主题 | 常用接口或类型 | 说明 |
|------|----------------|------|
| 获取方块 | `Level#getBlock(...)`、`Position#getLevel()` | 从世界坐标、`Position`或`Vector3`读取方块。 |
| 创建方块实例 | `Block.get(id)`、`Block.get(id, damage)` | 按方块ID和数据值创建方块实例。 |
| 设置方块 | `Level#setBlock(...)` | 直接写入方块。特殊方块可优先评估`Block#place()`。 |
| 破坏方块 | `Level#useBreakOn(...)` | 按工具和玩家上下文执行破坏逻辑。 |
| 查询属性 | `getId()`、`getDamage()`、`getFullId()`、`isSolid()`、`isTransparent()` | 获取ID、数据值、完整ID和基础物理性质。 |
| 方块属性 | `getHardness()`、`getResistance()`、`getLightLevel()`、`getFrictionFactor()` | 读取硬度、抗爆性、亮度和摩擦相关数据。 |
| 容器方块 | `BlockChest`、`BlockEntityChest` | 通过方块实体访问箱子物品栏。 |

批量改方块时，应先确认目标区块已经加载，避免无意触发新区块生成；大量写入可关闭即时更新并在完成后统一更新。液体和特殊方块可能触发额外更新逻辑，应单独测试。

## 物品栏API

Nukkit-MOT中的`Inventory`接口位于`cn.nukkit.inventory`包，用于管理玩家、容器和伪容器中的物品。

| 主题 | 常用接口或类型 | 说明 |
|------|----------------|------|
| 玩家物品栏 | `Player#getInventory()` | 获取玩家主物品栏。 |
| 副手物品栏 | `Player#getOffhandInventory()` | 读取或设置副手槽物品。 |
| 读取内容 | `Inventory#getContents()`、`Inventory#getItem(slot)` | 获取全部物品或指定槽位物品。 |
| 写入内容 | `Inventory#setContents(...)`、`Inventory#setItem(...)`、`Inventory#clear(slot)` | 批量或单槽位修改物品。 |
| 客户端同步 | `sendContents(...)`、`sendSlot(...)` | 修改后强制刷新客户端视图。 |
| 离线玩家数据 | `Server#getOfflinePlayerData(uuid)`、`Server#saveOfflinePlayerData(...)` | 读取和保存离线玩家NBT数据。 |
| 物品NBT转换 | `NBTIO.putItemHelper(...)`、`NBTIO.getItemHelper(...)` | 在`Item`与`CompoundTag`之间转换。 |

### 玩家槽位

| 槽位范围或标识 | 对应区域 | API槽位 | NBT存储槽位 |
|----------------|----------|---------|-------------|
| `0`至`8` | 快捷栏 | `0`至`8` | `0`至`8` |
| `9`至`35` | 主物品栏 | `9`至`35` | `9`至`35` |
| `36`至`39` | 盔甲槽 | `36`至`39` | `100`至`103` |
| 副手 | 副手槽 | 通过`getOffhandInventory()`访问 | `-106` |

伪容器可用于创建自定义GUI。Nukkit-MOT文档中使用`ChestFakeInventory`示例，并通过`player.addWindow(menu)`显示给玩家。该能力依赖Nukkit-MOT及相关库，不能直接套用于BDS或其他插件系统。

## 世界API

Nukkit-MOT以`Level`表示已加载的世界。世界名称查找通常按`worlds`目录下的文件夹名进行。

| 主题 | 常用接口或类型 | 说明 |
|------|----------------|------|
| 获取服务器 | `Server.getInstance()` | 取得服务端实例。 |
| 默认世界 | `Server#getDefaultLevel()` | 获取默认世界。 |
| 查找世界 | `Server#getLevelByName(name)` | 返回已加载世界；不应假定它会自动加载。 |
| 加载世界 | `Server#loadLevel(name)` | 显式加载已有世界。 |
| 创建世界 | `Server#generateLevel(...)` | 创建并加载新世界。 |
| 生成器 | `Generator.getGenerator(name)`、`Generator.getGeneratorList()` | 获取注册的世界生成器。 |
| 维度数据 | `Level#getDimension()`、`Level#getDimensionData()` | 读取维度ID和维度元数据。 |
| 高度范围 | `Level#getMinBlockY()`、`Level#getMaxBlockY()` | 读取实际可用高度范围。 |
| 区块状态 | `isChunkLoaded(...)`、`loadChunk(...)`、`isChunkGenerated(...)`、`isChunkPopulated(...)` | 检查和加载区块。 |
| 常加载区域 | `Server#getTickingAreaManager()`、`TickingArea` | 管理需要保持加载的区块区域。 |
| 粒子与声音 | `Level#addParticle(...)`、`Level#addSound(...)`、`Level#addParticleEffect(...)` | 向世界或附近玩家广播效果。 |

### 生成器名称

| 名称 | 典型用途 |
|------|----------|
| `normal`或`default` | 标准主世界地形。 |
| `oldnormal` | 旧版普通地形。 |
| `flat` | 平坦大厅或测试地图。 |
| `void` | 空地图、小游戏底图或自定义建筑图。 |
| `nether` | 下界维度世界。 |
| `the_end` | 末地维度世界。 |

### 默认维度高度

| 维度 | ID | 默认Y范围 |
|------|----|-----------|
| 主世界 | `0` | `-64`至`319` |
| 下界 | `1` | `0`至`127` |
| 末地 | `2` | `0`至`255` |

插件不应把主世界高度硬编码为`0..255`。Nukkit-MOT文档建议从`Level`读取实际高度范围；部分世界提供器也可能回退到旧版高度行为。

## 线程与数据安全

Nukkit-MOT文档提示，方块、区块、实体、玩家、世界和物品栏操作应视为主线程API。耗时I/O或计算可以放到异步任务中，但真正访问`Level`、`Player`、`Entity`、区块或物品栏数据前应切回主服务器线程。

修改离线玩家NBT数据后必须显式保存。在线玩家数据虽然会自动保存，但关键操作后也可调用`player.save()`。读取或写入离线数据时应处理损坏文件、缺失玩家和槽位转换错误。
