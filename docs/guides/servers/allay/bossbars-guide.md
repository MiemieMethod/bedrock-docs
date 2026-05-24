---
comments: true
---

# Boss栏

Boss栏不仅能拿来做Boss血条，也很适合做倒计时、加载进度和阶段提示。本指南用最常见的几个场景带你快速上手。

## 先创建一个Boss栏

Allay里创建Boss栏的入口是`BossBar.create()`：

```java linenums="1"
import org.allaymc.api.bossbar.BossBar;
import org.allaymc.api.bossbar.BossBarColor;
import org.allaymc.api.bossbar.BossBarStyle;

BossBar bossBar = BossBar.create();
bossBar.setTitle("首领战");
bossBar.setProgress(1.0f);
bossBar.setColor(BossBarColor.RED);
bossBar.setStyle(BossBarStyle.SEGMENTED_10);
```

常用属性如下：

| 属性 | 默认值 | 说明 |
|------|--------|------|
| `title` | `""` | Boss栏标题。 |
| `progress` | `1.0` | 进度，范围是0到1。 |
| `color` | `PINK` | 颜色。 |
| `style` | `SOLID` | 分段样式。 |
| `darkenSky` | `false` | 是否在显示时加深天空。 |

## 显示给玩家

玩家本身就是Boss栏查看者，所以直接添加就行：

```java linenums="1"
bossBar.addViewer(player);
```

不需要时及时移除：

```java linenums="1"
bossBar.removeViewer(player);
bossBar.removeAllViewers();
```

/// tip | 更新会自动同步
Boss栏一旦已经显示给玩家，后续对标题、进度、颜色和样式的修改都会自动同步给当前查看者，不需要额外手动刷新。
///

## 做一个简单的倒计时

下面这个例子把Boss栏当作活动倒计时使用：

```java linenums="1"
import org.allaymc.api.bossbar.BossBar;
import org.allaymc.api.bossbar.BossBarColor;

public class EventTimer {
    private final BossBar bossBar = BossBar.create();
    private final int totalSeconds;
    private int remainingSeconds;

    public EventTimer(int seconds) {
        this.totalSeconds = seconds;
        this.remainingSeconds = seconds;
        bossBar.setColor(BossBarColor.BLUE);
        bossBar.setProgress(1.0f);
        bossBar.setTitle("活动开始倒计时");
    }

    public void showTo(EntityPlayer player) {
        bossBar.addViewer(player);
    }

    public void tick() {
        remainingSeconds--;
        float progress = (float) remainingSeconds / totalSeconds;
        bossBar.setProgress(Math.max(0.0f, progress));
        bossBar.setTitle("剩余" + remainingSeconds + "秒");

        if (progress < 0.25f) {
            bossBar.setColor(BossBarColor.RED);
        } else if (progress < 0.5f) {
            bossBar.setColor(BossBarColor.YELLOW);
        }
    }
}
```

如果你已经在用[任务调度](schedule-guide.md)，把`tick()`放进周期任务里就够了。

## 做一个多人共享的Boss血条

Boss栏完全可以让多个玩家同时观看：

```java linenums="1"
BossBar healthBar = BossBar.create();
healthBar.setTitle("远古守卫");
healthBar.setColor(BossBarColor.PURPLE);
healthBar.setStyle(BossBarStyle.SEGMENTED_20);
healthBar.setDarkenSky(true);

arenaPlayers.forEach(healthBar::addViewer);
```

Boss生命值变化时只要改进度：

```java linenums="1"
healthBar.setProgress(currentHealth / maxHealth);
```

## 颜色和样式怎么选

常见颜色有`PINK`、`BLUE`、`RED`、`GREEN`、`YELLOW`、`PURPLE`、`REBECCA_PURPLE`和`WHITE`。样式则包括：

- `SOLID`
- `SEGMENTED_6`
- `SEGMENTED_10`
- `SEGMENTED_12`
- `SEGMENTED_20`

经验上可以这样选：

- 持续性进度条：优先`SOLID`
- 倒计时或阶段条：优先分段样式
- 真正的Boss战：可以配合`darkenSky=true`

## 使用提醒

- `progress`必须保持在0到1之间。
- Boss栏不会替你自动清理查看者，事件结束后记得移除。
- `darkenSky`效果很强，适合少量关键场景，不适合常驻提示。