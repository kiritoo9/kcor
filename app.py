import json
import time
import argparse

from utils.ocr import OCR
from utils.video_analyzer import VideoAnalyzer

if __name__ == "__main__":
    # define arguments
    parser = argparse.ArgumentParser(description="OCR+image capture from image file and Video-to-text recognition")
    parser.add_argument(
        "--media", "-m",
        type=str,
        default="image",
        help="Media type you want to analyze"
    )
    args = parser.parse_args()
    media = args.media

    # start processing data
    start_time = time.time()
    print(f"Start to processing {media} data..")

    if media == "image":
        img_source = "./assets/ktp-example2.jpg"

        # perform to run OCR and analyzing+capture photo
        ocr = OCR(img_source)
        print(json.dumps(ocr.data, indent=4))
    elif media == "video":
        video_source = "./assets/interview.mp4"

        # perform to analyze video
        result = VideoAnalyzer(video_source)
    else:
        print("no media recognized! skipping process..")

    # set as completed process
    print("Process completed in:", time.time() - start_time)