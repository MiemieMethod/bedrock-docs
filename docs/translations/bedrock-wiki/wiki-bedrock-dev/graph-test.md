---
标题：Molang图
显示贡献者：否
显示大纲：否
隐藏：是
---

<MolangGraph code="query.anim_time" :fromX="-1" :toX="2" :fromY="-1.1" :toY="1.1" :stepSize="0.02"/>

<MolangGraph code="math.cos(query.anim_time * 360)" :fromX="-2" :toX="2" :fromY="-1.1" :toY="2" :stepSize="0.02"/>

<MolangGraph code="q.anim_time == 0 ? 0 : q.anim_time == 1 ? 1 : math.pow(2, -10 * math.clamp(q.anim_time, 0, 1)) * math.sin((math.clamp(q.anim_time, 0, 1) * 10 - 0.75) * 120) + 1" :toY="2" :stepSize="0.001"/>

<MolangGraph code="q.anim_time == 0 ? 0 : q.anim_time == 1 ? 1 : q.anim_time < 0.5 ? -(math.pow(2, 20 * math.clamp(q.anim_time, 0, 1) - 10) * math.sin((20 * math.clamp(q.anim_time, 0, 1) - 11.125) * 80)) / 2 : (math.pow(2, -20 * math.clamp(q.anim_time, 0, 1) + 10) * math.sin((20 * math.clamp(q.anim_time, 0, 1) - 11.125) * 80)) / 2 + 1"  :fromY="-1" :toY="2" :stepSize="0.001"/>

<MolangGraph code="q.anim_time < 0.5 ? (math.pow(2 * math.clamp(q.anim_time, 0, 1), 2) * ((2.5949095 + 1) * 2 * math.clamp(q.anim_time, 0, 1) - 2.5949095)) / 2 : (math.pow(2 * math.clamp(q.anim_time, 0, 1) - 2, 2) * ((2.5949095 + 1) * (math.clamp(q.anim_time, 0, 1) * 2 - 2) + 2.5949095) + 2) / 2" :fromY="-1"  :toY="2" :stepSize="0.001"/>