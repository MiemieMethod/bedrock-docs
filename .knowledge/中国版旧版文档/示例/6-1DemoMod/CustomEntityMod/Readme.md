# 自定义生物mod

该mod有以下功能：

1.自定义材质：custom_player_bloom，使用额外的宏USE_BLOOM

2.重写猪的行为：攻击人并且爆炸（纯配置json，无python代码）

3.重写猪的外观：简单替换了贴图、使用了自定义材质（纯配置json，无python代码）

4.使用python接口修改玩家的材质

   玩家（第三人称下）第一次攻击生物时修改（本地玩家的皮肤稍微变亮），第二次时还原

5.自定义一个生物netease:squirrel，并且在玩家进入世界时使用接口召唤该生物

6.动画控制netease:squirrel

   玩家攻击生物netease:squirrel改变动画状态