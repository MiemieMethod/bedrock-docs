# 坐标空间变换

在客户端实体定义中，不同坐标系之间存在差异，有时需要在世界空间、实体空间和骨骼局部空间之间进行转换。本文讨论这些坐标系的关系与转换方法。

## 应用场景

你可能需要进行坐标空间变换的场合包括：

- 使用薄立方体绘制三维线段来可视化某个空间位置
- 进行精确的头部追踪，测量从实体特定关节到目标的角度
- 从武器尖端精确发射弹射物
- 解算IK骨骼链使肢体接触地面

## 背景知识：矩阵

三维变换通常使用矩阵表示。一个3×3的旋转矩阵由三个轴向量组成：

```
[ XAxis.x  YAxis.x  ZAxis.x ]
[ XAxis.y  YAxis.y  ZAxis.y ]
[ XAxis.z  YAxis.z  ZAxis.z ]
```

矩阵乘法的顺序非常重要。**列主序**（column-major）下向量从右向左乘：

```
Entity × RootBone × Pelvis × Spine × Shoulder × Elbow × Hand × point
```

在命名变换时建议使用`A_To_B`的格式来表示从A空间到B空间的变换，便于验证计算链：

```
A_To_B = A_To_C × C_To_B   （中间部分 C 互相抵消）
```

## Minecraft的坐标系特点

理解Minecraft实体中的坐标系有三个关键点：

1. **实体坐标系相对世界旋转了180度**：实体默认面朝北（游戏世界的-Z方向），但在Blockbench中，North是负Z，而世界坐标的北也是负Z，所以模型是正确朝向的。
2. **动画中X轴方向与位置中相反**：在Blockbench的动画标签中，沿正X方向拖动骨骼手柄，数值显示为负值。这意味着动画骨骼使用的是左手坐标系（X翻转），而不是几何体使用的右手坐标系。
3. **实体单位是世界单位的16倍**：1个世界方块 = 16个实体单位。

## 世界坐标到实体骨骼坐标的变换

若要在Molang的`pre_animation`脚本中将一个世界坐标点转换为实体骨骼空间坐标，需要依次执行：

1. 减去实体位置（平移逆变换）
2. 应用偏航角旋转的逆变换
3. 乘以缩放因子16，并翻转Z轴

### 完整Molang脚本示例

在`pre_animation`中将世界坐标`(10, y, 10)`转换为骨骼坐标：

```molang
v.target.x = 10;
v.target.y = q.position(1);
v.target.z = 10;

v.target.x = v.target.x - q.position(0);
v.target.y = v.target.y - q.position(1);
v.target.z = v.target.z - q.position(2);

t.cos_yaw = math.cos(q.body_y_rotation);
t.sin_yaw = math.sin(q.body_y_rotation);
t.x = v.target.x;
v.target.x = t.cos_yaw * t.x + t.sin_yaw * v.target.z;
v.target.z = -t.sin_yaw * t.x + t.cos_yaw * v.target.z;

v.target.x = v.target.x * 16;
v.target.y = v.target.y * 16;
v.target.z = -v.target.z * 16;
```

### 各步骤说明

**步骤一：平移逆变换**

正向变换（实体空间→世界空间）是加上实体位置，所以逆变换是减去：

```molang
v.target.x = v.target.x - q.position(0);
v.target.y = v.target.y - q.position(1);
v.target.z = v.target.z - q.position(2);
```

**步骤二：偏航角旋转逆变换**

使用`q.body_y_rotation`查询实体偏航角。正旋转方向是向左转（X增大方向），正弦项取负号：

```molang
t.cos_yaw = math.cos(q.body_y_rotation);
t.sin_yaw = math.sin(q.body_y_rotation);
t.x = v.target.x;
v.target.x = t.cos_yaw * t.x + t.sin_yaw * v.target.z;
v.target.z = -t.sin_yaw * t.x + t.cos_yaw * v.target.z;
```

俯仰角（pitch）的逆变换在此示例中略去，可按相同思路自行实现。

**步骤三：缩放与Z轴翻转**

乘以16倍将世界单位转为实体单位，同时翻转Z轴以适应动画坐标系的方向差异：

```molang
v.target.x = v.target.x * 16;
v.target.y = v.target.y * 16;
v.target.z = -v.target.z * 16;
```

## 使用方法

在实体资源包定义的`scripts`中配置：

```json title="RP/entities/my_entity.json（description）"
"scripts": {
    "pre_animation": [
        "v.target.x = 10; v.target.y = q.position(1); v.target.z = 10; v.target.x = v.target.x - q.position(0); v.target.y = v.target.y - q.position(1); v.target.z = v.target.z - q.position(2); t.cos_yaw = math.cos(q.body_y_rotation); t.sin_yaw = math.sin(q.body_y_rotation); t.x = v.target.x; v.target.x = t.cos_yaw * t.x + t.sin_yaw * v.target.z; v.target.z = -t.sin_yaw * t.x + t.cos_yaw * v.target.z; v.target.x = v.target.x * 16; v.target.y = v.target.y * 16; v.target.z = -v.target.z * 16;"
    ],
    "animate": ["myAnim"]
},
"animations": {
    "myAnim": "animation.my_entity.move"
}
```

然后在骨骼动画中，将目标骨骼的`position`关键帧表达式设置为：

```
v.target.x, v.target.y, v.target.z
```

## 验证建议

在Blockbench中创建一个包含三个方向轴可视化对象的测试实体，先确认各轴的实际方向，再实现变换逻辑。特别注意：

- Blockbench中的模型朝向与动画骨骼偏移的X轴方向不一致
- 先测试简单的静态目标点（如硬编码的`10, y, 10`），验证变换正确后再接入动态参数
