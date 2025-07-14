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
    parser.add_argument(
        "--source", "-s",
        type=str,
        help="File source"
    )

    args = parser.parse_args()
    media = args.media
    source = args.source
    if source is None or source == "":
        print("No file selected!")
        exit()

    # start processing data
    start_time = time.time()
    print(f"Start to processing {media} data..")

    if media == "image":
        # perform to run OCR and analyzing+capture photo
        ocr = OCR(source)
        print(json.dumps(ocr.data, indent=4))
    elif media == "video":
        # perform to analyze video
        result = VideoAnalyzer(source)
    else:
        print("no media recognized! skipping process..")

    # set as completed process
    print("Process completed in:", time.time() - start_time)