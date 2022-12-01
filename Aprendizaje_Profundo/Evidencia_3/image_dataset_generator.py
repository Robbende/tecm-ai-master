import cv2
import time
import os

print("getting camera...")
cap = cv2.VideoCapture(1)
print("getting camera: Done")

NUMBER_QTY = 2

FOTO_NUMBERS = 55
FOTO_DIR_PATH = "C:\\Users\\Ruben\\OneDrive\\Documents\\Master\\tecm-ai-master\\Aprendizaje_Profundo\\Evidencia_3\\pictures2\\"

for i in range(2, NUMBER_QTY+1):
    #user_input_number = input("Enter Number Category: ")
    print("sleeping 3 sec...")
    time.sleep(3)

    picture_folder_name = os.path.join(FOTO_DIR_PATH, str(i))

    if not os.path.exists(picture_folder_name):
        # create folder
        os.mkdir(picture_folder_name)

    pic_idx = 1
    while pic_idx <= FOTO_NUMBERS:
        time.sleep(0.2)
        ret, frame = cap.read()
        cv2.imshow("Live Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # code to save picture here
        #
        picture_name = f"picture_{i}_{pic_idx}.jpg"
        picture_full_path = os.path.join(picture_folder_name, picture_name)

        print(
            f"saving picture #{pic_idx}, category: {i}, path: {picture_full_path}")
        cv2.imwrite(picture_full_path, frame)
        print("image saved...")

        pic_idx += 1

cap.release()
cv2.destroyAllWindows()
