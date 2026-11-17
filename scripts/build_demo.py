"""Build the authored production example and validate its timing/asset contract."""
from pathlib import Path
import json,csv,re
r=Path(__file__).resolve().parents[1];out=r/'examples';out.mkdir(exist_ok=True)
text=[
'同一件黑色大衣，',
'为什么有时清冷，有时却显得沉重？',
'先别急着换衣服。我们用同一套搭配，只改三个位置。',
'第一处，是脸和领口的关系。',
'高领、厚围巾和垂下的头发挤在一起时，深色容易连成一整块。',
'你先看到的，可能就是这块面积，而不是人。',
'把头发移到一侧，围巾松一点，给颈部留出一条边界。',
'再看前后对比。衣服没有换，轮廓却有了停顿。',
'第二处，看面料怎么接在一起。',
'同样是黑色，羊毛、针织和棉布的表面也不一样。',
'如果两件都很厚、很蓬松，量感会重复；换一件更平整的内搭，再观察。',
'先看全身，再靠近看织物，不要只凭远景猜材质。',
'这里也不是越亮越好。',
'光泽太强，或者布料贴得太紧，都可能改变你想要的安静感。',
'我们要做的是区分层次，而不是堆更多细节。',
'第三处，让大衣进入真实动作：走几步、坐下、把包拿起来。',
'如果你一直要拉袖口、拽下摆，先检查尺码和活动空间。',
'松弛感至少应该允许身体自然行动，而不只在照片里成立。',
'最后，再看一眼包和鞋。',
'它们可以延续整套的安静，也可以成为一个重点，但不必同时争抢注意。',
'想做对比，就保持同一机位和光线，一次只换一个配件。',
'这样你才知道，究竟是哪一处改变了整体。',
'下次穿黑色大衣，先不问自己像不像某种风格。',
'先看颈部有没有边界，面料有没有层次，动作有没有余地。',
'剩下的就交给你自己的生活。',
'去走路、坐车、见朋友，看看这件衣服能不能陪你自在地过完一天。',
'今天的三步可以留下：整理边界，区分材质，检查活动空间。',
'不要同时改变全部搭配。先试一个位置，再拍同条件的对比。',
'好看的判断，才会慢慢变成你自己的经验。',
'我是野桃。下次选衣服，我们继续从看得见的细节开始。']
assets=[
('A01','状态/对照','同一位模特同一件黑色大衣，拍两个颈部造型','同机位中景，领口和头发清楚；只改颈部处理','黑色大衣 高领 围巾 头发 领口 对比','black coat neckline scarf hair comparison','自摄优先；若无法控制变量，明确为示意图','找不到则用自己衣橱的深色外套，随之改口播'),
('A02','局部证据','高领、厚围巾、发丝重叠','颈部特写，能分辨三种物体，不用大景代替','围巾 高领 头发 领口 特写','scarf turtleneck hair neckline close up','自摄或已获许可素材','用手把衣物摆在台面示意，标示意'),
('A03','操作','移开发丝、松开围巾','固定机位完整拍出动作起止，不用不同衣服拼成前后','整理围巾 露出领口 动作','adjust scarf neckline demonstration','自摄','只拍颈部以下，旁白相应调整'),
('A04','材质证据','黑色羊毛、针织、棉布','同一自然光，近景能看到纤维和表面，旁注材质','黑色 羊毛 针织 棉布 面料 特写','black wool knit cotton fabric close up','自摄/明确材质的授权素材','材质不明时改说表面视觉差异，不命名纤维'),
('A05','前后对照','同一大衣搭厚内搭和较平整内搭','保持光线人物和机位，保证差异清楚','黑色大衣 内搭 厚薄 对比','black coat layering bulky versus smooth','自摄','无可比素材则删因果口吻，只作搭配示例'),
('A06','反例','过强光泽或过度贴身的内搭示例','只演示视觉变化，不评价人物身材','黑色大衣 光泽 内搭 对比','black coat shiny top layering detail','自摄优先','用布样放在大衣旁作材质对照'),
('A07','动作证据','穿大衣行走、坐下、拿包','连续动作，手脚及衣物活动范围可见，留现场声备用','穿大衣 坐下 行走 拿包 动作','coat walking sitting picking up bag','自摄/有许可视频','自摄无脸半身，替代远景街拍'),
('A08','检查证据','拉袖口和拽下摆的动作','演员演示标为示例，不把别人动作当不合身诊断','大衣 袖长 下摆 活动空间 示范','coat sleeve hem fit movement demonstration','自摄','改成衣物平铺尺寸检查'),
('A09','配件对照','同一套衣服只换包，再只换鞋','三段等景别，对比时不同时改两件','黑色大衣 换包 换鞋 同套搭配','black coat bag shoe styling comparison','自摄','手头仅有一只包则只做一个变量'),
('A10','总结卡','三步：边界、材质、活动空间','原创文字卡与本人图像，手机能读清','不需要外部搜索','no external search required','原创制作','用三帧证据图加短标签'),
('A11','生活情境','走路、坐车、与朋友见面','连续日常动作，不拍他人可识别隐私，环境不掩盖衣物','黑色大衣 日常 行走 通勤','black coat everyday walking commute','自摄/有许可素材','在家门口或走廊自摄')]
lookup={a[0]:a for a in assets}
assign=[['A01'],['A01'],['A01','A10'],['A02'],['A02'],['A02'],['A03'],['A01'],['A04'],['A04'],['A05'],['A04','A05'],['A06'],['A06'],['A05'],['A07'],['A08'],['A07'],['A09'],['A09'],['A09'],['A09'],['A01'],['A10'],['A11'],['A11'],['A10'],['A01','A03'],['A11'],['A10']]
fx=['E03','E01','E06','E02','E02','E10','E01','E03','E06','E02','E03','E02','E10','E01','E01','E01','E02','E01','E10','E01','E03','E10','E01','E06','E01','E01','E06','E03','E01','E06']
phase=[]
for i in range(30):phase.append('钩子' if i<3 else '颈部机制' if i<8 else '材质机制' if i<15 else '动作机制' if i<18 else '配件对照' if i<22 else '落地收束')
count=lambda x:len(re.findall(r'[\u4e00-\u9fffA-Za-z0-9]',x))
# Frame based durations: estimated delivery at 4.2 characters/s, with longer visual holds.
durs=[max(75,round(count(s)/4.2*30)+12) for s in text]
for i in [7,11,20,26,29]:durs[i]+=45
shots=[];frame=0
for i,(s,ids,f,d) in enumerate(zip(text,assign,fx,durs),1):
 row={'shot_id':f'S{i:02d}','start_frame':frame,'end_frame':frame+d,'start_s':round(frame/30,3),'end_s':round((frame+d)/30,3),'voiceover':s,'asset_ids':ids,'function':phase[i-1],'effect_id':f,'source_in_out':'素材未拍/未取得，待填实际入出点','visual_instruction':'; '.join(lookup[a][3] for a in ids),'cut_reason':('任务从上一段改变为'+phase[i-1]) if i==1 or phase[i-1]!=phase[i-2] else '用对应证据替换或推进到该句细节；若没有新增信息可留图','subtitle':s,'emphasis':{'4':'领口边界','9':'材质层次','16':'活动空间','27':'三步检查'}.get(str(i),''),'audio_action':'A1口播；A3音乐为选曲后待混音，未标实际拍点'}
 shots.append(row);frame+=d
payload={'title':'为什么黑色大衣有时清冷，有时沉重？','account':'野桃','version':'v0.3','status':'原创完整制作示例；非已制成视频，未找齐素材，未选歌，未试听','fps':30,'estimated_duration_s':round(frame/30,3),'spoken_character_count':sum(map(count,text)),'timing_basis':'4.2有效字/秒的排练起点，加停顿与阅读时间；录音后重排，非参考作者实测','voiceover':''.join(text),'assets':[{'asset_id':a[0],'role':a[1],'subject':a[2],'required_evidence':a[3],'query_zh':a[4],'query_en':a[5],'source_plan':a[6],'fallback':a[7],'actual_url':None,'rights_status':'未取得素材，待核验'} for a in assets],'shots':shots,'music_status':'未选曲，语义占位'}
(out/'black-coat-production.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2))
with (out/'black-coat-shotlist.csv').open('w',newline='') as f:
 keys=['shot_id','start_s','end_s','function','voiceover','asset_ids','visual_instruction','effect_id','cut_reason','source_in_out','audio_action'];w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore');w.writeheader()
 for sh in shots:w.writerow({**sh,'asset_ids':'+'.join(sh['asset_ids'])})
lines=['# 野桃原创制作示例：为什么黑色大衣有时清冷，有时沉重？','',f'状态：制作方案，尚未拍摄或生成成片。{payload["spoken_character_count"]}个有效字，估计{payload["estimated_duration_s"]:.1f}秒；录音后重新锁时。','', '## 完整口播','']
for a,b in [(0,3),(3,8),(8,15),(15,18),(18,22),(22,30)]:lines.extend([''.join(text[a:b]),''])
lines+=['## 素材采购单','','|ID|任务|必须看见|中文搜索式|英文搜索式|替代|','|---|---|---|---|---|---|']
for a in assets:lines.append('|'+ '|'.join([a[0],a[2],a[3],a[4],a[5],a[7]])+'|')
lines+=['','所有搜索式是待执行任务，不是已经找到的素材。优先自摄；不声称已获使用许可。','', '## 镜头执行表','','|镜头|估计秒数|口播|素材|效果|','|---|---|---|---|---|']
for sh in shots:lines.append(f'|{sh["shot_id"]}|{sh["start_s"]:.2f}–{sh["end_s"]:.2f}|{sh["voiceover"]}|{"+".join(sh["asset_ids"])}|{sh["effect_id"]}|')
lines+=['','效果参数与关闭条件见skills/aesthetic-video-creation/references/editing-recipes.md。单个镜头里多份素材的具体切点，须依真实录音安排；不是默认平均分配。','', '## 声音与发布计划','', '先用A1录清楚口播。A3选低干扰、无主唱、有适量脉冲的器乐；从开头问题到材质、动作说明保持连贯，三步总结处可减少配器或降低音乐。尚未选曲，没有真实BPM和拍点，全部按语义占位。局部动作原声可保留，不默认添加叮声。', '', '小红书标题实验：黑色大衣显沉重？先检查这3个位置。封面：同一件大衣，差在哪？', '', '抖音标题实验：换衣服之前，先改这三个位置。开头可先展示同衣物A/B，再进入问题。两种版本都是实验方案，未声称平台偏好。', '', '首轮只测试开头“先提问”与“先展示A/B”的差异，其余内容不变；记录平台可提供的前段留存。未发布，因此没有测试结果。']
(out/'black-coat-production.md').write_text('\n'.join(lines)+'\n')
assert ''.join(s['voiceover'] for s in shots)==payload['voiceover']
assert all(s['end_frame']>s['start_frame'] for s in shots)
assert all(a['end_frame']==b['start_frame'] for a,b in zip(shots,shots[1:]))
assert all(a in lookup for s in shots for a in s['asset_ids'])
print('Demo:',payload['spoken_character_count'],'chars,',payload['estimated_duration_s'],'seconds,',len(shots),'shots,',len(assets),'assets; coverage/timing/IDs checked.')
