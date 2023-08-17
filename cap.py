import cv2
import os
import time

cap = cv2.VideoCapture(0)

# 촬영 간격 설정
capture_interval = 0.1

# 저장할 폴더 설정
output_folder = "captured_images"
os.makedirs(output_folder, exist_ok=True)
capture_count = 0

while True:
    ret, frame = cap.read()
    filename = os.path.join(output_folder, f"{time.time():.6f}.jpg")

    cv2.imwrite(filename, frame)
    capture_count += 1
    print(f"Captured {capture_count} images.")

    time.sleep(capture_interval)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
