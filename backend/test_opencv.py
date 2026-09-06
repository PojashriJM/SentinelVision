import cv2
file=cv2.load_video()
info=cv2.get_video_info(file)
read=cv2.read_frames(file)