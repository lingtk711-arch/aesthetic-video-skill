"""Build the portable AI Studio text from canonical sources without media or analytics."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'skills/aesthetic-video-creation'
SECTIONS = [
    ('核心执行规则', BASE / 'SKILL.md'),
    ('创作引擎与八种路径', BASE / 'references/creative-engine-v0.4.md'),
    ('口播语法', BASE / 'references/voice-and-language-v0.4.md'),
    ('穿搭推荐话术专项', BASE / 'references/recommendation-speech-study.md'),
    ('画面与声音设计', BASE / 'references/visual-editing-v0.4.md'),
    ('真实成片与留存复盘', BASE / 'references/production-review-v0.5.md'),
    ('制作包交付协议', BASE / 'references/generation-contract.md'),
    ('21条已有对照证据', ROOT / 'analysis/cross-video-audit-v0.4.md'),
    ('本轮制作差距与证据范围', ROOT / 'analysis/production-gap-v0.5.md'),
    ('原创证据前置改稿示例', ROOT / 'examples/ice-snow-evidence-first-v0.5.md'),
    ('v0.4完整原创试运行（历史）', ROOT / 'examples/sharp-without-tension-v0.4.md'),
]
intro = '''野桃审美穿搭创作Skill｜Google AI Studio单文件版｜v0.5｜2026-11-17

上传本文件即可使用，不需要模型再访问仓库。用户当次要求优先。
本文件保留v0.4创作研究，增加v0.5真实成片验收；不是原片、私人后台或完整机器转写。
来源：21条既有分析；本轮只重查一条可访问补充参考的采样/局部与本地项目成片。没有重新看完21条，没有完成参考音轨听辨，不保证流量。
用户给选题则生成完整原创稿；给定稿/录音则先清点真实可读素材并核对画面证据；给成片/数据则先做有时间码的诊断再改规则。读取本文件不等于已经看过视频。
内含的时间、响度与审美目标均区分观察和制作建议，不能当平台规定。公开内容不包含项目私人数据。

'''
parts = [intro]
for title, path in SECTIONS:
    text = path.read_text()
    for target_title, target_path in SECTIONS:
        # Make the canonical reading list self-contained for a one-file upload.
        try: short = str(target_path.relative_to(BASE))
        except ValueError: short = str(target_path.relative_to(ROOT))
        text = text.replace('`' + short + '`', '本文件「' + target_title + '」')
    parts += ['\n========== ' + title + ' ==========\n\n', text, '\n']
out = ROOT / 'AI_STUDIO_YETAO_SKILL.txt'
out.write_text(''.join(parts).rstrip() + '\n')
print(f'Built {out.name}: {out.stat().st_size} bytes, {len(SECTIONS)} sections')
