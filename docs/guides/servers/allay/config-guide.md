---
comments: true
---

# 配置文件

Allay提供了灵活的配置文件处理器，支持多种格式。本指南将展示如何使用`Config`类来管理插件中的配置文件。

## 支持的格式

Config类支持以下格式：

| 格式       | 文件扩展名              | 描述                     |
|----------|----------------------|------------------------|
| YAML     | `.yml`、`.yaml`      | 人类可读格式，支持嵌套数据 |
| JSON     | `.json`、`.js`       | 广泛使用的数据交换格式   |
| Properties| `.properties`、`.cnf` | 简单的键值对             |
| Enum     | `.txt`、`.list`      | 简单的值列表（每行一个） |

## 创建配置

### 基本用法

```java linenums="1"
import org.allaymc.api.utils.config.Config;

public class MyPlugin extends Plugin {
    private Config config;

    @Override
    public void onEnable() {
        // 在插件数据文件夹中创建配置文件
        File configFile = new File(
            getPluginContainer().dataFolder().toFile(), 
            "config.yml"
        );
        config = new Config(configFile, Config.YAML);
    }
}
```

### 带默认值

你可以提供默认值，如果配置文件不存在将使用这些默认值：

```java linenums="1"
import org.allaymc.api.utils.config.Config;
import org.allaymc.api.utils.config.ConfigSection;

ConfigSection defaults = new ConfigSection();
defaults.put("debug", false);
defaults.put("maxPlayers", 100);
defaults.put("welcomeMessage", "欢迎来到服务器！");

Config config = new Config(configFile, Config.YAML, defaults);
```

### 自动检测格式

如果你想让Config类根据文件扩展名自动检测格式：

```java linenums="1"
// 根据文件扩展名自动检测格式
Config config = new Config(configFile, Config.DETECT);
```

## 读取值

### 基本获取器

```java linenums="1"
// 使用特定类型的方法获取值
String name = config.getString("server.name");
int port = config.getInt("server.port");
double ratio = config.getDouble("settings.ratio");
boolean debug = config.getBoolean("settings.debug");
long timestamp = config.getLong("lastUpdate");

// 获取值，如果键不存在则返回默认值
String motd = config.getString("motd", "默认MOTD");
int maxPlayers = config.getInt("maxPlayers", 20);
boolean enabled = config.getBoolean("enabled", true);
```

## 写入和保存值

```java linenums="1"
// 设置值
config.put("player.name", "Steve");
config.put("server.port", 25565);
config.put("settings.debug", true);

// 保存到文件
config.save();
```

## 嵌套配置

```java linenums="1"
// 读取嵌套值
String serverName = config.getString("server.name");
String serverHost = config.getString("server.host");
int serverPort = config.getInt("server.port");

// 使用句号分隔符访问嵌套键
// 配置文件中：
// server:
//   name: "MyServer"
//   host: "0.0.0.0"
//   port: 25565
```

## 最佳实践

1. **始终使用默认值** - 这样可以确保配置始终有有效的值
2. **验证配置** - 在使用值之前检查它们是否有效
3. **保存更改** - 记住调用`save()`来持久化配置更改
4. **使用描述性的键名** - 使用`server.host`而不是`sh`

## 接下来

现在你已经了解了配置文件的基础。建议继续学习：

- [国际化](i18n-guide.md) - 多语言支持
- [权限系统](permission-guide.md) - 管理权限

