import numpy as np
import cv2

cap = cv2.VideoCapture(0) #perintah ini digunakan untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada notebook.
print(cap.isOpened())


while(True): #perintah ini digunakan untuk looping imshow (looping menampilkan objek melalui webcam), sehingga webcam akan mengambil objek gambar secara realtime.
    ret, frame = cap.read() #perintah ini digunakan untuk mengambil objek gambar dengan format berwarna atau BGR.
    bright = cv2.addWeighted(frame,1.5, np.zeros(frame.shape, frame.dtype), 0, 25) #perintah ini digunakan untuk meningkatkan nilai kecerahan objek gambar.
    cv2.imshow('webcam',bright) #perintah ini digunakan untuk menampilkan gambar yang telah diubah nilai kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah ini digunakan untuk menghentikan program dengan menekan tombol c pada keyboard notebook.
        break

cap.realease()
cv2.destroyAllwindows()
