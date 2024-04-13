# `/enableencryption`

> 文档版本：1.21.0.21

`/enableencryption`命令command.enableencryption.description

/// settings | 执行条件
该命令需要权限等级：`any`|`0`。该命令需要开启作弊。
///

## 用法

/// tab | 重载1
```mcfunction
/enableencryption <publicKey:string> <salt:string> [ciper_mode:EncryptionCommandCipher]
```

//// html | div.result
command.enableencryption.1.description

///// define
`publicKey`：<!-- md:samp string -->

- 基本类型。command.enableencryption.publicKey.description

`salt`：<!-- md:samp string -->

- 基本类型。command.enableencryption.salt.description

`ciper_mode`：<!-- md:samp EncryptionCommandCipher -->

- 枚举类型，可选。command.enum.encryptioncommandcipher.description枚举值如下：

  |值|描述|
  |---|---|
  |`cfb8`|command.enum.encryptioncommandcipher.cfb8|
  |`cfb128`|command.enum.encryptioncommandcipher.cfb128|
  |`cfb`|command.enum.encryptioncommandcipher.cfb|



/////

////

///
