import easyocr
from .ektp_reader import EktpReader
from .face_reader import PhotoReader

class OCR:
    def __init__(self, image_path: str):
        # define global vars
        self.image_path = image_path
        self.data = None

        # run process
        self.read()

    def read(self):
        # reading text from file
        reader = easyocr.Reader(["en", "id"])
        results = sorted(
            reader.readtext(self.image_path), 
            key=lambda r: (r[0][0][1], r[0][0][0])
        )

        # read e-ktp format
        ektp_data = EktpReader(results)

        # read pass photo
        photo_data = PhotoReader(self.image_path)
        
        # updating global vars
        self.data = {
            "ektp_data": ektp_data.result,
            "face_image": photo_data.result
        }