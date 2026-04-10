import cv2
import mediapipe as mp
from gtts import gTTS
import pygame
import threading
from io import BytesIO

pygame.mixer.init()

def mainkan_suara_google(teks):
    try:
        
        tts = gTTS(text=teks, lang='id')

        fp = BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        
       
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error memutar suara: {e}")

def proses_suara(teks):
    if not pygame.mixer.music.get_busy():
        t = threading.Thread(target=mainkan_suara_google, args=(teks,))
        t.start()

# 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_gesture(hand_landmarks):
  
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, 
            mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    pips = [mp_hands.HandLandmark.INDEX_FINGER_PIP, mp_hands.HandLandmark.MIDDLE_FINGER_PIP, 
            mp_hands.HandLandmark.RING_FINGER_PIP, mp_hands.HandLandmark.PINKY_PIP]
    
    jari_berdiri = []

    for tip, pip in zip(tips, pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            jari_berdiri.append(1) 
        else:
            jari_berdiri.append(0) 


    if jari_berdiri == [1, 0, 0, 1]: 
        return "Metal"
    elif jari_berdiri == [1, 1, 0, 0]:
        return "Peace"
    elif jari_berdiri == [0, 0, 0, 1]:
        return "Kelingking"
    elif jari_berdiri == [1, 0, 0, 0]:
        return "Telunjuk"
    elif jari_berdiri == [1, 1, 1, 0]:
        return "Tiga Jari"
    elif jari_berdiri == [0, 1, 1, 0]:
        return "Kelinci"
    elif jari_berdiri == [1, 1, 1, 1]:
        return "Halo/Dadah"
    elif jari_berdiri == [0, 0, 0, 0]:
        return "Kepal (Reset)" 
    
    return "Unknown"

gestur_sebelumnya = ""

print("Sistem AI Aktif dengan Gestur Lengkap. Bersiap menampilkan kamera...")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1) 
    h, w, c = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    results = hands.process(rgb_frame)
    
    
    cv2.putText(frame, "PANDUAN GESTUR JARVIS:", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
    cv2.putText(frame, "Metal: Nama | Peace: Kampus | Kelingking: Fakultas", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(frame, "Telunjuk: Hobi | Tiga Jari: Cita-cita | Kelinci: Penutup", (10, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(frame, "Halo(5 Jari): OYEEE! | Kepal: Reset", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
         
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
          
            gestur_sekarang = get_gesture(hand_landmarks)
            
            if gestur_sekarang != "Unknown":
                warna = (0, 255, 0) if gestur_sekarang != "Kepal (Reset)" else (0, 0, 255)
                cv2.putText(frame, f"Deteksi: {gestur_sekarang}", (w - 300, h - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, warna, 3)

            if gestur_sekarang != gestur_sebelumnya and gestur_sekarang != "Unknown" and gestur_sekarang != "Kepal (Reset)":
                if gestur_sekarang == "Metal":
                    proses_suara("Halo! Perkenalkan, nama saya Sofyan Ibnu Ghazali.")
                elif gestur_sekarang == "Peace":
                    proses_suara("Saya adalah mahasiswa di Universitas Islam Madura.")
                elif gestur_sekarang == "Kelingking":
                    proses_suara("Saya dari Fakultas Teknik Informatika.")
                elif gestur_sekarang == "Telunjuk":
                    proses_suara("Hobi saya adalah ngoding dan mempelajari kecerdasan buatan.")
                elif gestur_sekarang == "Tiga Jari":
                    proses_suara("Cita-cita saya adalah menjadi seorang Software Engineer yang hebat.")
                elif gestur_sekarang == "Kelinci":
                    proses_suara("Terima kasih sudah mendengarkan perkenalan saya. Sampai jumpa!")
                elif gestur_sekarang == "Halo/Dadah":
                    proses_suara("Mantap jiwa! Salam Teknik Informatika!")
                
                gestur_sebelumnya = gestur_sekarang
            
            
            if gestur_sekarang == "Kepal (Reset)":
                gestur_sebelumnya = ""

    cv2.imshow("JARVIS Sofyan - Edisi Lengkap", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()