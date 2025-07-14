import os
import whisper

from moviepy.editor import VideoFileClip

class VideoAnalyzer:

    def __init__(self, video_source: str):
        self.video_source = video_source

        # run process
        self.process()

    def converting_video(self):
        if not os.path.exists(self.video_source):
            print("file is not found!")
            return

        # converting video into .wav
        print("converting video..")
        video = VideoFileClip(self.video_source)

        # renaming file and moving to tmp folder
        file_name = os.path.splitext(self.video_source)[0] + ".wav"
        file_name = file_name.split("/")[-1]

        # creating dir
        output_dir = "./uploads/tmp"
        os.makedirs(output_dir, exist_ok=True)

        # writing file
        output_path = f"{output_dir}/{file_name}"
        video.audio.write_audiofile(output_path)

        return output_path

    def analyzing_text(self, file_source: str):
        print("start transcribing speech..")
        model = whisper.load_model("medium")
        result = model.transcribe(file_source, language="id")

        # print transcript
        for v in result["text"].split("."):
            print(v)

    def process(self):
        self.analyzing_text(self.converting_video())


