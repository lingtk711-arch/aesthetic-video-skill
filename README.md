# 野桃 · 审美穿搭视频创作 Skill v0.5

输入一个选题，生成原创完整口播，以及素材选择、组合、剪辑、字幕效果与声音制作计划。服务小红书和抖音。

## Google AI Studio：一个文件

下载 [野桃Skill单文件版](AI_STUDIO_YETAO_SKILL.txt)，上传到Google AI Studio，然后发送：

> 我的选题是「……」。按文件中的v0.5执行规则与v0.4创作引擎，直接给完整口播、逐句素材与剪辑声音方案。

无需连接GitHub。文件是静态快照，更新后需重新下载上传；它不包含原视频，不代表AI Studio自动看过原片。

## v0.5：补齐成片验收，而不只扩充创作框架

- [执行与复盘规则](skills/aesthetic-video-creation/references/production-review-v0.5.md)：首次兑现、词与衣物匹配、原图缺口、同源重复、响度与小屏验收。
- [已确认的制作差距](analysis/production-gap-v0.5.md)：这轮实际复核范围、时间码和执行责任，明确没有重新看完21条原片。
- [冰刃/霜雪原创改稿与15秒制作草案](examples/ice-snow-evidence-first-v0.5.md)：先给可见差异，再解释人物；未录音、未重新发布。
- `scripts/review_render.py`：时间线统计与音轨实测，不能替代人工看图、听校或证明留存。

v0.4的创作方法继续有效；v0.5主要修复“写了要求却没落实到成片”的执行漏洞。私人后台数据不公开，不承诺流量结果。

## v0.4创作基础（保留）

v0.3偏重通用制作配方，不能充分代表源账号的创作方法。v0.4以21条跨视频对照重写入口：从人物处境出题、用反例重定义、以两股相反力量构成气质、把物理细节接到身体与人的关系，再落回日常选择。保留单品、城市、产品、批评等不同路径，避免一个模板套全部。

- [21条逐条对照／126个画面锚点](analysis/cross-video-audit-v0.4.md)：每条的创作主张、功能链、画面含义、迁移与限制。
- [10条源样本创作规则与8类路径](skills/aesthetic-video-creation/references/creative-engine-v0.4.md)
- [口播句段语法](skills/aesthetic-video-creation/references/voice-and-language-v0.4.md)
- [选材、镜头组合、剪辑效果与声音执行](skills/aesthetic-video-creation/references/visual-editing-v0.4.md)
- [完整原创试运行：锋利，但不紧张](examples/sharp-without-tension-v0.4.md)：947个非空白字符、21段口播与对应制作表，时长待录音。
- [Skill入口](skills/aesthetic-video-creation/SKILL.md)

## 交付与边界

生成包包含完整口播、开头A/B、逐句画面、素材检索/自摄替代、字幕花字与效果理由、音乐与音效计划、双平台标题封面和一个测试方案。未取得素材、未录音、未选曲均须明确标识。

21条上传素材共约64分31秒。本轮重新完成1935张约2秒采样的字幕OCR提取、阅读候选文本、查看每条6个指定时刻的画面；不是完整人工逐字/逐镜校对。公开的文字是归纳释义，不是机器全稿。编号按上传顺序，不是表现或发布时间。

**原片声音的逐段听辨、可靠识曲、音效和卡点仍未完成。** 当前声音部分是可执行的原创设计要求，不能称已完整复刻参考声音。没有后台留存或各条表现数据，不保证万赞，也不能证明“为什么爆”。

v0.1–v0.3和旧black-coat示例保留作历史/格式参考，与v0.4冲突时使用v0.4。原素材、机器全文、模型和私人数据不发布。

## 项目使用

Canonical入口为`skills/aesthetic-video-creation`，项目发现入口`.agents/skills/aesthetic-video-creation`保持同步。[安装说明](INSTALL.md)。

新示例：[JSON](examples/sharp-without-tension-v0.4.json) / [镜头清单CSV](examples/sharp-without-tension-shotlist-v0.4.csv)。源映射：[规则JSON](analysis/creative-rules-v0.4.json)。

旧示例时间轴验证脚本只用于旧schema，不宣称验证了新示例的真实时长或成片效果。
