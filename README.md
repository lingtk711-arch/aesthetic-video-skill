# 野桃 · 审美穿搭视频创作 Skill v0.3

输入一个选题，生成完整原创口播、逐句素材需求、素材组合与剪辑执行方案。服务小红书、抖音的野桃账号。

## 直接开始

> 使用 aesthetic-video-creation，为野桃创作「为什么黑色大衣有时清冷、有时沉重？」。交付完整口播、素材搜索单、逐句镜头表、字幕与效果参数、声音计划以及小红书/抖音发布方案。未取得的素材、未选音乐与估计时间明确标注。

只有选题也会先按默认约150秒、竖屏、解说主导产出，不先用一串问题阻断。用户要求优先于默认值。

## 先看这三份

- [Skill入口](skills/aesthetic-video-creation/SKILL.md)
- [完整原创制作示例](examples/black-coat-production.md)：573个有效字、估计156秒、30个镜头、11组素材任务；尚未拍摄/选曲。
- [本轮5条分析与制作升级](analysis/batch-003-summary.md)

## 生成包包括什么

1. 观众问题、核心观点、脚本结构与开头A/B。
2. 连续可读的完整口播，不止大纲。
3. 每句要找什么人物/衣物/动作/景别/细节，附中英文搜索式、淘汰条件和替代。
4. 素材如何顺序组合、何处对照、何处看局部、何处留图解释。
5. 镜头时间表、字幕层级、花字、转场、运动和效果参数起点，以及每次处理的理由。
6. 口播录音、音乐选择、音效和混音计划；没有选歌不编拍点。
7. 双平台标题封面与一个单变量复盘方案。

## 方法和配方

- [交付协议](skills/aesthetic-video-creation/references/generation-contract.md)
- [六种脚本结构](skills/aesthetic-video-creation/references/script-architectures.md)
- [素材搜索和四种组合配方](skills/aesthetic-video-creation/references/material-playbook.md)
- [十二种剪辑与包装配方](skills/aesthetic-video-creation/references/editing-recipes.md)
- [口播、音乐与混音](skills/aesthetic-video-creation/references/audio-playbook.md)
- [留人设计决策](skills/aesthetic-video-creation/references/retention-design.md)
- [五层分析表](templates/five-layer-analysis.md)

## 分析基础与边界

21条用户提供素材，总时长约64分31秒。建立1935个每2秒OCR采样、21条机器语音初稿与全时长视觉差异候选，另做抽帧与重点窗口检查。机器稿和候选切点不等于完整人工校对。

新增5条按选题、文案、画面、声音、留人机制分别成文：[V17](analysis/batch-003/V17-five-layer.md)、[V18](analysis/batch-003/V18-five-layer.md)、[V19](analysis/batch-003/V19-five-layer.md)、[V20](analysis/batch-003/V20-five-layer.md)、[V21](analysis/batch-003/V21-five-layer.md)。编号来自上传顺序，不是表现排名或发布时间。

**仍未完成可靠识曲、音效听辨、逐点卡拍、全文人工校对及逐镜人工确认。** 已测的混音响度也不能分解出BGM与人声比例。具体音乐/效果建议与参考片观察明确分开，不声称已找到全部爆款因果。

公开版本不含原视频、整份机器转写、模型或私人凭据。工作区的原始证据不在仓库内。

## 安装与校验

仓库自带`.agents/skills/aesthetic-video-creation`入口，canonical源位于`skills/aesthetic-video-creation`。在支持项目级skills的客户端打开仓库后，以客户端实际发现情况为准；这不表示已在所有会话全局安装。[安装说明](INSTALL.md)。

结构化示例：[JSON](examples/black-coat-production.json) / [镜头CSV](examples/black-coat-shotlist.csv)。

```sh
python scripts/validate_production.py examples/black-coat-production.json
```

检查脚本覆盖、时间衔接、素材ID和替代方案；不替代素材授权、音频试听或发布效果验证。GitHub负责版本管理，视频计算仍在云端工作区进行。
