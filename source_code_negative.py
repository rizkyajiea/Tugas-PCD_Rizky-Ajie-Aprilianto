import numpy as np
import cv2

cap = cv2.VideoCapture(0) #perintah ini digunakan untuk melakukan inisialisasi pada webcam. angka "0" menunjukkan bahwa yang digunakan adalah webcam internal pada notebook.
print(cap.isOpened())

while(True): #perintah ini digunakan untuk looping imshow (looping menampilkan objek melalui webcam), sehingga webcam akan mengambil objek gambar secara realtime.
    ret, frame = cap.read() #perintah ini digunakan untuk mengambil objek gambar dengan format berwarna atau BGR.
    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #perintah ini digunakan untuk mengubah objek gambar yang awalnya berwarna (BGR) menjadi grayscale sebelum diubah menjadi gambar negatif.
    cv2.imshow('webcam', 255-grey) #perintah ini digunakan untuk mengubah obyek gambar dari skala keabuan menjadi gambar dengan skala negatif. 
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah ini digunakan untuk menghentikan program dengan menekan tombol c pada keyboard notebook.
        break

cap.realease()
cv2.destroyAllwindows()