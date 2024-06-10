import cv2
import numpy as np

def start_video_object_detection():
    while True:
        try:
            video_camera_capture = cv2.VideoCapture("https://www.webcam-oko.ru/barbershop-supermen-moskva/")
            while video_camera_capture.isOpened():
                ret, frame = video_camera_capture.read()
                if not ret:
                    break

                frame = apply_yolo_object_detection(frame)
                frame = cv2.resize(frame, (1920 // 2, 1080 // 2))
                cv2.imshow("Video Capture", frame)
                if cv2.waitkey(0):
                    break

            video_camera_capture.releas()
            cv2.destroyAIIWindows()

        except KeyboardInterrupt:
            pass