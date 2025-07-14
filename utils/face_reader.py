import io
import os
import cv2
import base64

from PIL import Image

class PhotoReader:

    def __init__(self, image_path: str):
        self.image_path = image_path
        self.result = None

        # run process
        self.process()

    def transform_to_base64(self, data):
        # convert OpenCV BGR to RGB
        face_rgb = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(face_rgb)

        buffer = io.BytesIO()
        pil_img.save(buffer, format="JPEG")

        # return as base64 string
        return base64.b64encode(buffer.getvalue()).decode("utf-8")
    
    def store_image(self, data):
        # creating dir
        output_dir = "./uploads/ektp/pass_photo"
        os.makedirs(output_dir, exist_ok=True)

        # getting file name
        names = self.image_path.split("/")
        filename = "pass-photo.jpg" if len(names) <= 0 else names[-1]

        # perform to upload
        save_path = os.path.join(output_dir, filename)
        cv2.imwrite(save_path, data)
        return f"{output_dir}/{filename}"

    def process(self):
        # load image and detect faces
        img = cv2.imread(self.image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # define usable vars
        to_base64 = False
        padding_pct = 0.2

        # perform to check multiple faces
        if len(faces) > 0:
            for i, (x, y, w, h) in enumerate(faces):
                print(f"executing face number {i}..")

                # crop face from image
                img_height, img_width = img.shape[:2]
                padding_w = int(w * padding_pct)
                padding_h = int(h * padding_pct)

                x1 = max(x - padding_w, 0)
                y1 = max(y - padding_h, 0)
                x2 = min(x + w + padding_w, img_width)
                y2 = min(y + h + padding_h, img_height)
                face = img[y1:y2, x1:x2]


                if to_base64 is True:
                    self.result = self.transform_to_base64(face)
                else:
                    self.result = self.store_image(face)