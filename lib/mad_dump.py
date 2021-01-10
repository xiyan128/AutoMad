from lib import find_scenes
from lib import composite
# from .util import scene_length
import moviepy.editor as mpe
from moviepy.video.io.VideoFileClip import VideoFileClip


class MadDump:
    videos = []
    scenes = []
    audio = ""

    def __init__(self, *video_paths, audio=None):
        self.audio = audio
        self.videos = [VideoFileClip(path) for path in video_paths]

    def find_all_scenes(self, threshold=30.0):
        for vid in self.videos:
            for scene in find_scenes(vid.filename, threshold):
                self.scenes.append((vid, scene))

    def composite(self):
        return composite.composite_along_beats(self.scenes.copy(), audio_path=self.audio)

    def export(self, file_name="out.mp4"):
        background_music = mpe.AudioFileClip(self.audio)
        with_music = self.composite().set_audio(background_music)
        with_music.write_videofile(file_name)
