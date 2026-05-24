# 网络协议

**网络协议（Network Protocol）**是Minecraft基岩版客户端与服务端之间进行数据通信所遵循的规则和格式。协议定义了双方交换信息的数据包结构、字段编码方式、状态同步方式和交互流程。

## 概述

基岩版使用自有的网络协议栈进行客户端与服务端之间的通信。协议的底层传输基于**RakNet**，一种面向游戏优化的UDP网络库，在其上封装了基岩版特有的数据包格式、序列化规则和同步逻辑。

每个基岩版版本都有一个对应的**协议版本号（Protocol Version）**。协议版本号与[游戏版本](../general/version.md#游戏版本)相关，但不是同一种版本号。客户端与服务端在登录阶段会比较协议版本号；当双方协议版本不兼容时，连接将被拒绝，玩家通常会看到客户端过旧或服务器过旧一类的提示。

Mojang为服务器合作方维护了基岩版网络协议文档仓库。该仓库以树状图描述**数据包（Packet）**、相关类型和枚举的结构，并在变更记录中按协议版本列出字段、枚举和数据包的增删改。由于协议会随版本发布而改变，第三方服务器和协议库通常需要按目标协议版本实现并维护独立的兼容层。

## 协议层次

基岩版的网络通信可以分为以下层次：

### 传输层

基岩版使用[RakNet](raknet.md)作为面向外部服务器的传输层协议。RakNet在UDP之上提供可靠性保证、数据包排序、分片重组和连接管理等功能。RakNet握手过程大致包括：

1. 客户端发送Unconnected Ping。
2. 服务端回复Unconnected Pong（包含服务器信息，即MOTD）。
3. 客户端发起Open Connection Request，协商MTU大小。
4. 双方完成RakNet连接建立。

RakNet的数据类型、握手数据包格式和MOTD格式详见[RakNet](raknet.md)。

对于通过Xbox Live会话（好友、邀请、Realms）发起的连接，基岩版使用另一种协议[NetherNet](nethernet.md)，该协议基于WebRTC，通过Xbox Live的信令服务建立连接，不依赖固定的公网IP和端口。

### 游戏层

在RakNet连接建立后，客户端和服务端开始交换游戏数据包。游戏层的数据包使用统一的包装格式，每个数据包由数据包ID和载荷组成。数据包ID标识数据包的类型，载荷则按该类型对应的字段结构序列化。

游戏层数据包不仅承载玩家移动、方块变化和实体同步等实时状态，也承载登录、资源包协商、区块传输、物品栏交互、命令请求和诊断数据。同一数据包的字段顺序、字段含义和内部序列化实现都可能在相邻协议版本之间发生变化；部分数据包在转换为Cereal序列化后还会破坏旧二进制兼容。

#### 游戏数据包头

每个游戏数据包由一个**游戏数据包头（GamePacket Header）**和载荷组成，完整结构如下：

- **游戏数据包长度**（varint u32）：数据包总大小，包含头和载荷。
- **游戏数据包头**（14位，编码为varint u32）：
  - **游戏数据包ID**（10位）：标识具体的数据包类型，最大值为1023（即2¹⁰−1）。
  - **子客户端发送方ID**（2位）：标识发送方客户端，用于多客户端共享连接（如分屏）的场景。
  - **子客户端目标ID**（2位）：标识目标客户端，同上。

游戏数据包ID最大为10位，因此最多有1024个不同的数据包ID。其中200至299号ID保留用于基岩版衍生版本，不由官方协议占用，自定义协议实现可将该范围用于自定义数据包。

## 登录流程

客户端加入服务器的登录流程会受在线认证、资源包要求、实验性功能和具体版本影响。典型流程大致如下：

1. **Login**：客户端发送登录请求，包含玩家身份信息和客户端数据。
2. **Server To Client Handshake**：服务端发送握手数据包，包含用于加密协商的数据。
3. **Client To Server Handshake**：客户端完成加密握手。
4. **Play Status**：服务端确认登录成功。
5. **Resource Packs Info**：服务端告知客户端所需的资源包列表。
6. **Resource Pack Stack**：服务端发送资源栈信息。
7. **Start Game**：服务端发送世界初始化数据，包括世界种子、游戏规则、玩家位置等。
8. **客户端加载完成**：客户端完成区块加载后通知服务端，进入游戏。

`StartGamePacket`是登录末期的重要数据包。它不仅携带世界初始状态，也携带若干会影响后续协议行为的开关，例如运动权威模式、物品栈网络管理相关配置，以及某些服务端权威验证功能是否启用。

## 数据包类型

基岩版协议定义了数百种数据包类型，涵盖游戏的各个方面：

- **移动类**：玩家移动、实体移动、传送等。
- **方块类**：方块更新、方块实体数据等。
- **物品栏类**：背包操作、容器交互等。
- **实体类**：实体生成、属性更新、事件触发等。
- **命令类**：命令执行、自动补全等。
- **世界类**：区块数据、维度切换、天气变化等。
- **界面类**：窗口打开和关闭、表单数据等。

许多系统不是由单个数据包独立完成，而是由一组数据包共同维护。以玩家移动为例，现代协议主要通过`PlayerAuthInputPacket`从客户端向服务端提交输入、预测位置和相关动作；服务端可以使用`CorrectPlayerMovePredictionPacket`修正客户端预测，也可以在带有滴答标识的数据包中让客户端回退至指定历史帧后重新模拟。以方块破坏为例，客户端会预测挥动动画、方块破坏和工具耐久变化，而服务端负责校验进度、广播裂纹与粒子效果，并在预测不一致时通过`UpdateBlockPacket`、`InventorySlotPacket`或`ItemStackResponsePacket`纠正客户端。

除玩法同步外，近年的协议变更还持续把诊断、呈现配置、商店入口、存在信息和数据驱动界面等元数据通道纳入游戏层。例如，`ServerboundDiagnosticsPacket`已逐步承载客户端内存分类、实体系统和分析器范围等诊断数据；`GraphicsOverrideParameterPacket`开始支持按玩家下发图形覆盖；`ServerStoreInfoPacket`与`ServerPresenceInfoPacket`则用于传递商店入口与`PresenceConfiguration`。这意味着第三方服务端在追踪协议兼容性时，不能只关注移动、区块和物品栏，还需要同时关注登录期与运行期的配置分发路径。

### 当前协议中的创作与呈现通道

在1.26.30对应的协议1001中，协议层已经直接承载创作工具、界面和声音控制等更高层能力，而不只是传统的世界同步。

- `EditorNetworkPacket`是编辑器专用的通用载荷包，使用“路由到管理器+变体名+变体数据”的结构传输编辑器侧消息。这说明编辑器会话并非只依赖本地工具状态，而是已经拥有独立的游戏层消息通道。
- `ClientboundDataDrivenUIShowScreenPacket`、`ClientboundDataDrivenUICloseScreenPacket`与`ClientboundDataDrivenUIReloadPacket`表明，服务端可以要求客户端显示、关闭或重载数据驱动界面实例。这一方向与资源包覆写JSON UI不同，更接近运行期界面调度。
- `ServerPresenceInfoPacket`当前直接下发`PresenceConfiguration`，其中包括`experienceName`、`worldName`与`richPresenceId`。这说明“世界叫什么、体验如何在存在信息中呈现”也已进入会话级协议配置。
- `GraphicsOverrideParameterPacket`当前不仅可以按生物群系覆盖图形参数，还带有`Player Identifier`字段，说明图形覆盖已具备更细粒度的目标范围。
- 声音同步路径也在扩张。`LevelSoundEventPacket`中的声音标识已不再局限于旧式固定枚举，而是以`SoundEventIdentifier`形式承载；同时，`ClientboundUpdateSoundDataPacket`又提供了基于服务器声音句柄的更新路径。

## 数据编码

协议中的数据字段使用多种编码方式：

- **VarInt/VarLong**：可变长度整数编码，用于节省带宽。
- **ZigZag编码**：对有符号整数进行编码，使小绝对值的负数也能高效编码。
- **Little Endian**：基岩版协议中多数固定长度整数使用小端序。
- **字符串**：使用VarInt前缀长度加UTF-8编码的字节序列。
- **NBT**：部分数据包中的复合数据使用NBT格式编码（基岩版使用小端序NBT变体）。

协议还广泛使用运行时标识符、网络ID、枚举值和位标志。某些ID只在一次连接内有效，例如创造物品网络ID、配方网络ID和物品栈网络ID。对于这类字段，服务端通常需要保证非零、唯一或与服务端所知状态一致，否则客户端可能拒绝相关数据或丢弃预测结果。

字段编码形式本身也可能随版本演进。例如，部分数据包在切换到Cereal序列化后会收紧必选字段和可选字段约束；某些原本固定为枚举的字段，也可能改为“枚举或字符串变体”一类更宽的表示形式。实现方若假定字段始终保持旧版的二进制布局或单一整型表示，往往会在跨版本兼容时直接失效。

## 加密

基岩版的网络通信在登录握手完成后启用**AES-256-CFB8**加密。加密密钥通过ECDH密钥交换协议在握手过程中协商。启用加密后，所有后续的数据包载荷均为加密状态。

## 压缩

游戏数据包在发送前会进行压缩。基岩版支持**Zlib**、**Snappy**和不压缩三种模式，压缩模式在连接建立时由服务端通过NetworkSettings数据包指定。

每个数据包载荷之前存储一个`u8`类型的压缩标识符，用于标识该载荷使用的压缩算法：

| 标识符 | 压缩算法 | 说明 |
|--------|----------|------|
| `0x00` | Zlib | 可配置压缩级别，压缩率与速度可均衡，适合生产环境 |
| `0x01` | Snappy | 以速度为优先，压缩率低于Zlib |
| `0xFF` / `0xFFFF` | 不压缩 | 数据包大小低于阈值时，或调试时跳过压缩 |

NetworkSettings数据包中的压缩标识符以`u16`存储，其余位置以`u8`存储。仅当数据包大小超过预设阈值时才启用压缩，低于阈值的小数据包直接以不压缩形式发送。

## 服务器权威系统

基岩版网络协议经历了从客户端权威向服务端权威逐步迁移的过程。**客户端权威（Client Authority）**表示客户端对某些结果拥有较高决定权，服务端主要接受并广播结果；**服务端权威（Server Authority）**表示服务端根据客户端输入自行验证或模拟结果，并向客户端发送确认或修正。

### 运动

**服务端权威运动模式（Server Authoritative Movement Mode）**要求客户端在每个模拟帧发送输入和预测结果，服务端在收到输入后模拟玩家运动，并将服务端结果与客户端预测比较。当差异超过阈值时，服务端发送修正。客户端收到带滴答标识的修正后，会回退到对应历史状态，应用修正，然后重新模拟其后的输入。

这种机制并非只用于反作弊。即使客户端没有作弊，延迟、击退、潜行状态变化、特性更新和传送等事件也可能使客户端预测与服务端状态暂时分歧。回退与重放能够减少直接瞬移式修正带来的体验问题。

客户端会把带滴答标识的入站数据包暂存到历史窗口，再在后续模拟刻执行“回退—应用—重放”。若滴答标识已经超出历史窗口，则该包会按普通数据包立即生效。常见带滴答标识的客户端入站数据包包括`CorrectPlayerMovePredictionPacket`、`MovePlayerPacket`、`SetActorDataPacket`和`UpdateAttributesPacket`。

#### 迁移与弃用

运动协议正从旧的客户端权威路径迁移到**服务端权威第三版（ServerAuthoritativeV3）**。在迁移过程中，`MovePlayerPacket`、`MoveActorAbsolutePacket`、`PassengerJumpPacket`、`PlayerInputPacket`以及部分`PlayerActionPacket`和`AnimatePacket`字段，已被标记为客户端到服务端方向的弃用路径。`PlayerAuthInputPacket`成为主要输入通道，`CorrectPlayerMovePredictionPacket`成为标准修正通道。

是否发送修正由服务端“实算结果与客户端预测结果”的差值阈值决定。阈值由服务端反作弊配置控制，不同服务端实现暴露的具体键名可能不同。

在基岩版专用服务器中，这套反作弊与回退修正机制默认处于关闭状态，需要通过`server.properties`开启；客户端是否进入该模式，则由服务端在`StartGamePacket`中明确告知。

### 方块交互

服务端权威方块破坏启用后，客户端仍负责采集目标方块并提交输入，服务端则根据玩家状态、物品状态和方块破坏进度验证结果。目标方块本身仍带有客户端权威性质，但服务端会进行距离等检查。创造模式是重要例外，其快速破坏路径仍具有较强客户端权威特征。

方块建造和破坏逻辑在服务端权威化后更强调模拟刻边界。客户端会在渲染帧中累计命中结果，并在下一次模拟刻集中处理，以避免高速飞行建造或破坏时跳过中间方块；服务端只按模拟刻处理输入，从而能够更精确地复现客户端预测。

在该机制下，客户端通常会预测挥动动画、方块消失和工具耐久变化；服务端则负责广播方块裂纹进度、挖掘粒子和破坏音效，并在预测不一致时通过`UpdateBlockPacket`、`InventorySlotPacket`或`ItemStackResponsePacket`修正。

`server.properties`中的`server-authoritative-block-breaking`用于开关服务端权威方块破坏，`server-authoritative-block-breaking-pick-range-scalar`用于配置服务端距离校验放宽系数。

### 物品栏

物品栏协议引入了`ItemStackNetManager`一类请求—响应式机制。客户端可以先本地预测容器操作、合成、交易或工具耐久变化，服务端再按请求作出接受或拒绝。请求通常引用物品栈网络ID，而不是只提交完整物品栈。服务端接受请求时可以返回新的网络ID或修正后的耐久，拒绝请求时客户端丢弃相应预测。

玩家界面容器用于表示光标、玩家合成栏、铁砧输入、织布机输入、信标支付槽等玩家专属界面槽位。该容器使服务端能够获知客户端正在使用的界面槽位，是物品栏逐步服务端权威化的基础设施之一。历史实现中，容器ID`124`被复用于玩家界面容器，槽位总数为51，索引`50`为统一的新建物品输出槽位。

### 第三方实现中的抓包经验

自实现服务端和协议库往往还会通过抓包验证客户端的真实行为。Allay旧协议研究资料给出了一些具有代表性的例子：

- 丢弃物品时，客户端会发送`InventoryTransactionPacket`并伴随`MobEquipmentPacket`；服务端接受后，掉落物通常以`AddItemEntityPacket`形式出现在世界中。
- 现代合成流程通常围绕`ItemStackRequestPacket`和`ItemStackResponsePacket`展开；合成示例包含`CraftRecipeAction`、`ConsumeAction`、`CreateAction`和`TakeAction`等动作。
- 放置方块时，客户端会先经过`START_ITEM_USE_ON`与`STOP_ITEM_USE_ON`之类的交互阶段，成功放置后再表现为`ITEM_USE(action=0)`路径。
- 创造模式破坏方块与生存模式破坏方块的上行路径并不相同。旧研究中，创造模式快速破坏使用`DIMENSION_CHANGE_REQUEST_OR_CREATIVE_DESTROY_BLOCK`，而生存模式会额外伴随裂纹进度、更新与校正相关流程。
- 同一种物品栏操作在不同平台上也可能有不同动作组合。Allay旧研究曾记录到移动端与Windows版在物品栈请求中分别偏向`SwapAction`与`PlaceAction`、`DestroyAction`等不同组合。

这些例子说明，协议字段表之外还存在大量“由客户端行为决定的顺序和组合”。第三方实现只照抄单个数据包结构，往往仍不足以完全复现真实交互。

物品栏从旧协议向`ItemStackNetManager`迁移时，存在一个“系统禁用但协议字段已上线”的过渡期：服务端会在`StartGamePacket`中显式关闭该系统，同时仍需为`InventoryContentPacket`、`InventorySlotPacket`、`CreativeContentPacket`和`CraftingDataPacket`等数据包写入网络ID字段，以满足客户端校验。

## 区块与缓存

世界数据传输是网络协议中带宽占用较大的部分。1.18地形高度变化后，完整发送一个区块柱会显著增加传输量，因此协议引入了**子区块请求系统（SubChunk Request System）**。服务端可以在`LevelChunkPacket`中发送骨架区块，客户端再按可见性和客户端常加载范围请求需要的子区块。`SubChunkPacket`返回子区块数据、请求结果、高度图和可选的Blob缓存ID。

骨架区块模式最初通过子区块计数`0xffffffff`启用。后续优化中，协议新增“已知全空气子区块”提示路径，可通过`0xffffffff-1`配合“最高非空气子区块索引”降低请求量。对应地，`SubChunkRequestPacket`与`SubChunkPacket`也演进为“中心坐标+多个偏移”的批量模式，偏移以`int8`编码，并新增`SuccessAllAir`结果码。

Blob缓存用于避免重复传输相同的大块二进制数据。客户端在处理`ClientCacheMissResponsePacket`时应只接受自己请求过的BlobID，并使用XXHash64重新计算数据哈希，确认哈希与BlobID一致。这种校验用于防止恶意服务端向客户端缓存写入与请求不匹配的数据。

## 版本变更

协议版本变更记录通常包含以下内容：

| 类型 | 说明 |
|------|------|
| 新增数据包 | 为新玩法、诊断、编辑器、图形配置、音效同步等系统添加新的数据包 |
| 修改数据包 | 为既有数据包添加字段、改变字段类型、调整读写顺序或改变内部序列化实现 |
| 删除或弃用数据包 | 将旧数据包替换为新流程，或在服务端权威系统迁移中弃用客户端到服务端的旧输入路径 |
| 枚举和类型变更 | 增加新的音效、动画、物品交互、运动效果、图形参数或结构化类型 |
| 序列化迁移 | 将部分数据包或类型转换到新的序列化实现，可能破坏旧协议布局 |
| 元配置扩张 | 将诊断、遥测、图形覆盖、存在信息、商店入口和聊天记录开关等会话配置纳入协议字段 |

协议版本变更并不总是对应显眼的玩法变化。一些变化只影响字段排列、可选字段、枚举值或客户端验证逻辑，但仍足以使第三方服务器或代理无法与新客户端兼容。因此，实现协议时通常需要同时参考目标版本的数据包结构和对应变更记录。

## 官方协议文档

Mojang官方协议仓库主要面向服务器实现者，而不是附加包作者。该仓库使用自定义的viz语言生成树状结构图，用于描述数据包、类型和枚举之间的结构关系；同时提供若干补充文档，说明服务端权威运动、方块破坏、子区块请求、客户端缓存和物品栏迁移等系统的设计意图。

这些资料适合作为第三方服务器、代理、协议库和抓包分析工具的参考。它们不构成稳定API，也不保证跨版本兼容；在实际实现中，目标游戏版本、协议版本号和客户端行为必须同时匹配。

## 官方协议参考库

Mojang在GitHub上维护的[基岩版网络协议文档仓库](https://github.com/Mojang/bedrock-protocol-docs)是最权威的协议参考资源。该仓库使用自定义的viz语言生成树状结构图，详细定义了每个数据包的字段、各种复合类型和枚举值。若需要先熟悉来源仓库的HTML入口与当前页面结构，可以先阅读[基岩版协议库翻译](../../translations/protocol/index.md)。

### 数据包结构

项目仓库中的数据包分为以下几大类：

- **登录与握手**：`LoginPacket`、`ServerToClientHandshakePacket`、`ClientToServerHandshakePacket`、`PlayStatusPacket`
- **资源包**：`ResourcePackDataInfoPacket`、`ResourcePackStackPacket`、`ResourcePacksReadyForValidationPacket`
- **世界初始化**：`StartGamePacket`、`BiomeDefinitionListPacket`、`FeatureRegistryPacket`
- **玩家移动**：`PlayerAuthInputPacket`、`CorrectPlayerMovePredictionPacket`、`MoveActorAbsolutePacket`
- **方块交互**：`UpdateBlockPacket`、`BlockEventPacket`、`BlockActorDataPacket`
- **物品栏**：`InventoryTransactionPacket`、`InventoryContentPacket`、`ItemStackResponsePacket`
- **实体同步**：`AddActorPacket`、`RemoveActorPacket`、`SetActorDataPacket`、`SyncActorPropertyPacket`
- **命令与输出**：`CommandRequestPacket`、`CommandOutputPacket`、`AvailableCommandsPacket`
- **区块传输**：`LevelChunkPacket`、`SubChunkPacket`、`SubChunkRequestPacket`
- **其他系统**：声音、粒子、教育功能、编辑器集成等

### 查询协议文档

访问项目仓库的HTML视图，可以直接查看：

1. **数据包列表**：检查`/docs`文件夹下按名称按字母序排列的HTML文件
2. **树状结构**：展开树状图查看字段定义、类型引用和枚举值
3. **变更记录**：查阅`previous_changelogs`或主说明页中列出的版本变更，了解协议在各版本的演变

### 版本兼容性

在使用协议文档时，务必注意：

- 查询时指定正确的**协议版本号**（不是游戏版本号）
- 同一数据包在不同版本可能有不同的字段结构、字段顺序或类型编码
- 部分数据包在序列化方案迁移后可能破坏了旧的二进制兼容性
- 新增的可选字段往往需要特殊处理以支持跨版本通信

### 协议库推荐

对于第三方服务器和协议库，以下开源项目提供了基岩版协议的参考实现：

- **LeviLamina**：面向服务器的模组加载框架，包含完整的协议实现
- **Endstone**：基于BDS的插件加载器，面向Python与C++插件
- **Allay**：面向Java与Kotlin等JVM语言的自实现服务端
- **SerenityJS**：面向TypeScript与JavaScript生态的自实现服务端
- **Nukkit**：Java生态的服务器软件