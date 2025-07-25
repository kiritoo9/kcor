# KOCR

Aplikasi sederhana berbasis Python 3.10 untuk melakukan:
- Optical Character Recognition (OCR) dari gambar
- Pendeteksian wajah dari file gambar
- Deteksi teks dari video interview

## Fitur

- Membaca teks dari gambar menggunakan OCR
- Mendeteksi dan menyimpan wajah dari gambar menggunakan OpenCV
- Mengekstrak frame dari video dan mendeteksi teks di tiap frame

## Persyaratan

- Python 3.10
- ffmpeg (untuk ekstraksi video/audio)

## Instalasi

1. Clone repositori ini:
    ```bash
    cd kcor
    ```

2. Install ffmpeg:

   Debian/Ubuntu:
    ```bash
    sudo apt install ffmpeg
    ```

   macOS:
    ```bash
    brew install ffmpeg
    ```

3. Install virtualenv
    ```bash
    virutalenv -p python3.10 venv
    source venv/bin/activate
    ```

4. Install dependensi Python:
    ```bash
    pip install -r requirements.txt
    ```

## Cara Penggunaan

1. Membaca teks dari gambar + menyimpan foto:
    ```bash
    python app.py --media=image --source=./assets/file_name.jpg
    ```

2. Deteksi teks dari video:
    ```bash
    python app.py --media=video --source=./assets/file_name.mp4
    ```

## Version
v0.0.1