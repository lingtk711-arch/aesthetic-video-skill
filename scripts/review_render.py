"""Inspect an actual edit and its timeline; never certify aesthetics or retention.

Usage: python scripts/review_render.py timeline.json --media rendered.mp4 --output review.json
Timeline: {fps, duration, shots:[{start,duration,source,in_point,out_point,detail?}]}
A still may use out_point='s'. Optional origin_id merges duplicate source files.
"""
import argparse
import collections
import json
import math
import re
import statistics
import subprocess
from pathlib import Path


def inspect_timeline(data):
    shots = data.get('shots', [])
    errors, warnings = [], []
    if not shots:
        return {'errors': ['No shots'], 'warnings': [], 'shot_count': 0}
    duration = float(data.get('duration', 0))
    fps = float(data.get('fps', 24))
    if not math.isfinite(fps) or fps <= 0:
        return {'errors': ['Invalid fps'], 'warnings': [], 'shot_count': len(shots)}
    cursor, still_seconds = 0.0, 0.0
    totals, exact = collections.defaultdict(float), collections.Counter()
    source_uses, near_reuse = collections.defaultdict(list), []
    lengths = []
    for i, shot in enumerate(shots):
        start, length = float(shot['start']), float(shot['duration'])
        if not math.isfinite(start) or not math.isfinite(length) or length <= 0:
            errors.append(f'shot {i}: invalid time'); continue
        if abs(start - cursor) > .51 / fps:
            errors.append(f'shot {i}: gap or overlap at {start}')
        cursor = start + length
        lengths.append(length)
        origin = str(shot.get('origin_id', shot.get('source', 'unknown')))
        totals[origin] += length
        source_in, source_out = shot.get('in_point'), shot.get('out_point')
        is_still = source_out == 's' or bool(shot.get('still', False))
        if is_still: still_seconds += length
        exact[(origin, source_in, source_out, str(shot.get('detail', '')))] += 1
        # Warnings include a different crop and overlapping neighboring intervals.
        if isinstance(source_in, (int, float)):
            end = source_in if is_still else source_out
            if isinstance(end, (int, float)):
                if end < source_in: errors.append(f'shot {i}: negative source interval')
                for j, a, b in source_uses[origin]:
                    if source_in <= b + .12 and end >= a - .12:
                        near_reuse.append({'first': j, 'next': i, 'origin': origin,
                                           'purpose': shot.get('reuse_purpose', 'not recorded')})
                source_uses[origin].append((i, source_in, end))
    if abs(cursor - duration) > .51 / fps:
        errors.append('Declared duration differs from last shot')
    if near_reuse: warnings.append('Same-source overlap/nearby frames need visual review; crop changes do not prove novelty')
    warnings.append('Different files may contain the same underlying shot; origin_id mapping requires human review')
    return {'duration_seconds': duration, 'shot_count': len(shots),
            'median_shot_seconds': statistics.median(lengths) if lengths else None,
            'still_seconds': still_seconds, 'source_seconds': dict(totals),
            'exact_repeat_placements': sum(n - 1 for n in exact.values()),
            'same_source_review_pairs': near_reuse, 'errors': errors, 'warnings': warnings,
            'human_review_required': ['spoken noun vs visible garment', 'original image availability',
                                      'new information per shot', 'small-screen readability',
                                      'voice intelligibility and mix audition', 'claim/evidence scope']}


def inspect_audio(media):
    cmd = ['ffmpeg', '-hide_banner', '-nostdin', '-i', str(media), '-vn', '-af',
           'loudnorm=I=-16:TP=-1:LRA=11:print_format=json', '-f', 'null', '-']
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    match = re.search(r'\{\s*"input_i".*?\}', result.stderr, re.S)
    if not match: raise ValueError('No loudnorm measurement; check that media has an audio track')
    parsed = json.loads(match.group(0))
    return {'integrated_lufs': parsed['input_i'], 'true_peak_dbtp': parsed['input_tp'],
            'lra_lu': parsed['input_lra'], 'measurement': 'ffmpeg loudnorm mixed track input only',
            'note': 'No gain applied. Measurement is not listening, music identification or a platform loudness requirement.'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('timeline', type=Path)
    ap.add_argument('--media', type=Path)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    report = inspect_timeline(json.loads(args.timeline.read_text()))
    if args.media:
        report['audio'] = inspect_audio(args.media)
        loudness = float(report['audio']['integrated_lufs'])
        if loudness < -24: report['warnings'].append('Low local loudness: inspect intelligibility before delivery; -24 is a review trigger, not a platform rule')
    else:
        report['warnings'].append('Audio was not measured')
    report['status'] = 'needs-human-review' if not report['errors'] else 'invalid-timeline'
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output: args.output.write_text(payload + '\n')
    print(payload)
    return 1 if report['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
