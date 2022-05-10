# import the module for openCV
import cv2

# connect the camera
cam_h = cv2.VideoCapture(1)

# to check if the camera is connected correctly.
if cam_h.isOpened():
    while True:
        # to read the images from camera
        ret, img = cam_h.read()
        if ret:
            # to visualize the images
            cv2.imshow("webcam", img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print("Frame Error")
            break
else:
    print("Cannot open camera!")

# to disconnect the camera
cam_h.release()
# to destroy the windows
cv2.destroyAllWindows()

