
import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Kamera açılamadı")
    exit()

print("ArexCam çalışıyor | Çıkmak için Q")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Görüntü alınamadı")
        break

    cv2.imshow("ArexCam", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
