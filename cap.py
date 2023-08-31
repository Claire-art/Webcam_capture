import cv2
import os
import time



# 촬영 간격 설정
capture_interval = 0.1

# 저장할 폴더 설정
output_folder = "/home/jua/daon/custom/ghana_2"
os.makedirs(output_folder, exist_ok=True)
capture_count = 0

cap = cv2.VideoCapture(2)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)  #해상도 조절해주기,웹캠사용시 필요
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)

while True:
    ret, frame = cap.read()
    cv2.imshow("VideoFrame", frame)
    filename = os.path.join(output_folder, f"{time.time():.6f}.jpg")


    cv2.imwrite(filename, frame)
    capture_count += 1
    print(f"Captured {capture_count} images.")

    time.sleep(capture_interval)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
