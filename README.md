# 🤖 AI Voice & Gesture Controller: JARVIS-style Intro

Selamat datang di proyek **AI Voice & Gesture Controller**! Proyek ini adalah sebuah sistem perkenalan diri interaktif berbasis *Computer Vision* dan *Artificial Intelligence*. Layaknya JARVIS, sistem ini dapat membaca gestur tangan manusia secara *real-time* melalui kamera dan meresponsnya dengan suara (*Text-to-Speech*).

Proyek ini dibuat oleh **Sofyan Ibnu Ghazali** dari **Fakultas Teknik Informatika, Universitas Islam Madura**. 

---

## ✨ Fitur Utama
* **Real-time Hand Tracking:** Mendeteksi kerangka tangan manusia secara presisi dengan sangat cepat menggunakan MediaPipe.
* **7 Kombinasi Gestur Unik:** Mampu membedakan berbagai formasi jari (Metal, Peace, Telunjuk, dll) untuk memicu respons percakapan yang berbeda.
* **Asynchronous Voice AI:** Menggunakan AI Voice Google (gTTS) yang berjalan di latar belakang (*threading*). Hal ini memastikan video dari kamera tetap berjalan mulus tanpa *lag* atau macet saat AI sedang berbicara.
* **Sistem Auto-Reset:** Gestur tangan mengepal (✊) digunakan sebagai "tombol reset" memori agar AI siap merespons input gestur selanjutnya.

---

## 🛠️ Teknologi yang Digunakan
* **Bahasa Pemrograman:** Python 3.12
* **Computer Vision:** OpenCV (`cv2`), MediaPipe
* **Text-to-Speech:** Google TTS (`gTTS`)
* **Audio Playback:** Pygame
* **Lain-lain:** Threading, BytesIO (In-Memory Processing)

---

## 💻 Cara Instalasi & Menjalankan Program

### 1. Persyaratan Sistem
Pastikan Anda sudah menginstal **Python 3.12** di komputer atau laptop Anda. Versi ini sangat direkomendasikan untuk menjaga stabilitas library.

### 2. Instalasi Library
Buka terminal atau Command Prompt Anda, lalu jalankan perintah berikut untuk menginstal semua *library* yang dibutuhkan:
```bash
pip install opencv-python mediapipe gtts pygame
