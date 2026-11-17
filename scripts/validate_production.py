"""Validate a generated production JSON without claiming media or audio was verified."""
import json,sys,re
from pathlib import Path
p=Path(sys.argv[1]);d=json.loads(p.read_text());errors=[]
shots=d.get('shots',[]);assets=d.get('assets',[]);ids=[a.get('asset_id') for a in assets]
if not shots:errors.append('No shots')
if len(ids)!=len(set(ids)):errors.append('Duplicate asset IDs')
shotids=[s.get('shot_id') for s in shots]
if len(shotids)!=len(set(shotids)):errors.append('Duplicate shot IDs')
fps=d.get('fps',0)
if not isinstance(fps,(int,float)) or fps<=0:errors.append('Invalid fps')
for n,s in enumerate(shots):
 if s.get('end_frame',0)<=s.get('start_frame',0):errors.append(f'{n}: non-positive duration')
 if n and shots[n-1].get('end_frame')!=s.get('start_frame'):errors.append(f'{n}: timeline gap or overlap')
 if not s.get('voiceover','').strip():errors.append(f'{n}: empty voiceover')
 if not s.get('asset_ids'):errors.append(f'{n}: no asset assignment')
 for a in s.get('asset_ids',[]):
  if a not in ids:errors.append(f'{n}: unknown asset {a}')
 if not s.get('cut_reason'):errors.append(f'{n}: no purpose for shot')
 for key,framekey in [('start_s','start_frame'),('end_s','end_frame')]:
  if fps and key in s and abs(s[key]-s[framekey]/fps)>.002:errors.append(f'{n}: seconds/frame mismatch')
if shots and shots[0].get('start_frame')!=0:errors.append('Timeline must begin at zero')
if ''.join(s.get('voiceover','') for s in shots)!=d.get('voiceover',''):errors.append('Voiceover coverage differs from full script')
if shots and fps and abs(shots[-1]['end_frame']/fps-d.get('estimated_duration_s',0))>.002:errors.append('Duration differs from last frame')
for a in assets:
 if not a.get('required_evidence'):errors.append(f'{a.get("asset_id")}: missing visible evidence requirement')
 if not a.get('fallback'):errors.append(f'{a.get("asset_id")}: no fallback')
 if not a.get('rights_status'):errors.append(f'{a.get("asset_id")}: missing source/use status')
if errors:
 print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(shots)} shots, {len(assets)} assets, script coverage and timeline are consistent. This does not verify footage, timing after recording, rights, music or audience performance.')
