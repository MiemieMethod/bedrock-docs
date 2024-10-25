# `/help`

> 文档版本：1.21.50.25

`/help`命令command.help.description

/// settings | 执行条件
该命令需要权限等级：`any`|`0`。
///

/// info | 别名
该命令还可以使用以下别名：`/?`。
///

## 用法

/// tab | 重载1
```mcfunction
/help [command:CommandName]
```

//// html | div.result
command.help.1.description

///// define
`command`：<!-- md:samp CommandName -->

- 枚举类型，可选。command.enum.commandname.description枚举值如下：

  |值|描述|
  |---|---|
  |`tag`|command.enum.commandname.tag|
  |`camera`|command.enum.commandname.camera|
  |`script`|command.enum.commandname.script|
  |`connect`|command.enum.commandname.connect|
  |`stop`|command.enum.commandname.stop|
  |`transfer`|command.enum.commandname.transfer|
  |`clear`|command.enum.commandname.clear|
  |`aimassist`|command.enum.commandname.aimassist|
  |`time`|command.enum.commandname.time|
  |`camerashake`|command.enum.commandname.camerashake|
  |`clearspawnpoint`|command.enum.commandname.clearspawnpoint|
  |`clone`|command.enum.commandname.clone|
  |`damage`|command.enum.commandname.damage|
  |`daylock`|command.enum.commandname.daylock|
  |`alwaysday`|command.enum.commandname.alwaysday|
  |`deop`|command.enum.commandname.deop|
  |`dialogue`|command.enum.commandname.dialogue|
  |`difficulty`|command.enum.commandname.difficulty|
  |`effect`|command.enum.commandname.effect|
  |`event`|command.enum.commandname.event|
  |`execute`|command.enum.commandname.execute|
  |`fill`|command.enum.commandname.fill|
  |`fog`|command.enum.commandname.fog|
  |`function`|command.enum.commandname.function|
  |`gamemode`|command.enum.commandname.gamemode|
  |`gamerule`|command.enum.commandname.gamerule|
  |`gametest`|command.enum.commandname.gametest|
  |`gettopsolidblock`|command.enum.commandname.gettopsolidblock|
  |`give`|command.enum.commandname.give|
  |`help`|command.enum.commandname.help|
  |`?`|command.enum.commandname.?|
  |`hud`|command.enum.commandname.hud|
  |`inputpermission`|command.enum.commandname.inputpermission|
  |`kick`|command.enum.commandname.kick|
  |`kill`|command.enum.commandname.kill|
  |`list`|command.enum.commandname.list|
  |`listd`|command.enum.commandname.listd|
  |`structure`|command.enum.commandname.structure|
  |`locate`|command.enum.commandname.locate|
  |`loot`|command.enum.commandname.loot|
  |`me`|command.enum.commandname.me|
  |`mobevent`|command.enum.commandname.mobevent|
  |`music`|command.enum.commandname.music|
  |`op`|command.enum.commandname.op|
  |`particle`|command.enum.commandname.particle|
  |`reload`|command.enum.commandname.reload|
  |`permission`|command.enum.commandname.permission|
  |`ops`|command.enum.commandname.ops|
  |`playanimation`|command.enum.commandname.playanimation|
  |`playsound`|command.enum.commandname.playsound|
  |`querytarget`|command.enum.commandname.querytarget|
  |`replaceitem`|command.enum.commandname.replaceitem|
  |`ride`|command.enum.commandname.ride|
  |`say`|command.enum.commandname.say|
  |`tickingarea`|command.enum.commandname.tickingarea|
  |`schedule`|command.enum.commandname.schedule|
  |`scoreboard`|command.enum.commandname.scoreboard|
  |`scriptevent`|command.enum.commandname.scriptevent|
  |`setblock`|command.enum.commandname.setblock|
  |`setmaxplayers`|command.enum.commandname.setmaxplayers|
  |`setworldspawn`|command.enum.commandname.setworldspawn|
  |`spawnpoint`|command.enum.commandname.spawnpoint|
  |`spreadplayers`|command.enum.commandname.spreadplayers|
  |`stopsound`|command.enum.commandname.stopsound|
  |`save`|command.enum.commandname.save|
  |`summon`|command.enum.commandname.summon|
  |`teleport`|command.enum.commandname.teleport|
  |`tp`|command.enum.commandname.tp|
  |`tell`|command.enum.commandname.tell|
  |`w`|command.enum.commandname.w|
  |`msg`|command.enum.commandname.msg|
  |`tellraw`|command.enum.commandname.tellraw|
  |`testforblock`|command.enum.commandname.testforblock|
  |`testforblocks`|command.enum.commandname.testforblocks|
  |`testfor`|command.enum.commandname.testfor|
  |`title`|command.enum.commandname.title|
  |`titleraw`|command.enum.commandname.titleraw|
  |`toggledownfall`|command.enum.commandname.toggledownfall|
  |`weather`|command.enum.commandname.weather|
  |`wsserver`|command.enum.commandname.wsserver|
  |`xp`|command.enum.commandname.xp|
  |`recipe`|command.enum.commandname.recipe|
  |`worldbuilder`|command.enum.commandname.worldbuilder|
  |`ability`|command.enum.commandname.ability|
  |`codebuilder`|command.enum.commandname.codebuilder|
  |`getchunkdata`|command.enum.commandname.getchunkdata|
  |`getchunks`|command.enum.commandname.getchunks|
  |`getspawnpoint`|command.enum.commandname.getspawnpoint|
  |`globalpause`|command.enum.commandname.globalpause|
  |`immutableworld`|command.enum.commandname.immutableworld|
  |`lesson`|command.enum.commandname.lesson|
  |`takepicture`|command.enum.commandname.takepicture|
  |`resourceuri`|command.enum.commandname.resourceuri|
  |`wb`|command.enum.commandname.wb|
  |`project`|command.enum.commandname.project|
  |`agent`|command.enum.commandname.agent|
  |`codebuilder_actorinfo`|command.enum.commandname.codebuilder_actorinfo|
  |`enchant`|command.enum.commandname.enchant|
  |`clearrealmevents`|command.enum.commandname.clearrealmevents|
  |`allowlist`|command.enum.commandname.allowlist|
  |`whitelist`|command.enum.commandname.whitelist|
  |`changesetting`|command.enum.commandname.changesetting|
  |`sendshowstoreoffer`|command.enum.commandname.sendshowstoreoffer|
  |`reloadconfig`|command.enum.commandname.reloadconfig|
  |`geteduserverinfo`|command.enum.commandname.geteduserverinfo|
  |`dedicatedwsserver`|command.enum.commandname.dedicatedwsserver|
  |`closewebsocket`|command.enum.commandname.closewebsocket|
  |`enableencryption`|command.enum.commandname.enableencryption|
  |`closechat`|command.enum.commandname.closechat|
  |`geteduclientinfo`|command.enum.commandname.geteduclientinfo|
  |`getlocalplayername`|command.enum.commandname.getlocalplayername|
  |`gametips`|command.enum.commandname.gametips|



/////

////

///

/// tab | 重载2
```mcfunction
/help <page:int>
```

//// html | div.result
command.help.2.description

///// define
`page`：<!-- md:samp int -->

- 基本类型。command.help.page.description


/////

////

///
