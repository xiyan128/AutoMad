from moviepy.video.compositing.concatenate import concatenate_videoclips
from .util import get_beats, find_nearest, scene_length

def composite_by_order(scenes):
    clips = []
    for scene in scenes:
        start_sec = scene[1][0].get_seconds()
        end_sec = scene[1][1].get_seconds()
        clips.append(scene[0].subclip(start_sec+0.05, end_sec-0.05))
    return concatenate_videoclips(clips)

def composite_along_beats(scenes, audio_path):
    beats = get_beats(audio_path)
    prev = 0
    clips = []
    for beat in beats:
        if len(scenes) == 0:
            break
        interval = beat - prev
        clip = find_nearest(scenes, interval)
        scenes.remove(clip)
        start_sec = clip[1][0].get_seconds()
        end_sec = start_sec + interval
        clips.append(clip[0].subclip(start_sec, end_sec))
        prev = beat
    return concatenate_videoclips(clips)
