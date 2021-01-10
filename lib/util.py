from aubio import source, tempo
import numpy as np


def scene_length(scene):
    return (scene[1] - scene[0]).get_seconds()


def get_beats(path):
    samplerate, win_s, hop_s = 44100, 1024, 512
    s = source(path, samplerate, hop_s)
    samplerate = s.samplerate
    o = tempo("specdiff", win_s, hop_s, samplerate)
    beats = []
    total_frames = 0
    while True:
        samples, read = s()
        is_beat = o(samples)
        if is_beat:
            this_beat = o.get_last_s()
            beats.append(this_beat)
        total_frames += read
        if read < hop_s:
            break
    return beats


def find_nearest(array, value):
    arr = np.array([scene_length(s) for s in list(zip(*array))[1]])
    idx = abs(arr - value).argmin()
    return array[idx]
