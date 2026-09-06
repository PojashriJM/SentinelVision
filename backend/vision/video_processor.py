import cv2


def load_video(video_path):
    """
    Open the uploaded video using OpenCV.
    """

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Could not open the video.")

    return cap


def get_video_info(cap):
    """
    Get basic information about the video.
    """

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    duration = frame_count / fps if fps > 0 else 0

    return {
        "fps": fps,
        "frame_count": frame_count,
        "width": width,
        "height": height,
        "duration": duration
    }


def read_frames(cap):
    """
    Read the video frame by frame.
    """

    frames_read = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        frames_read += 1

    return frames_read


def close_video(cap):
    """
    Release the video resource.
    """

    cap.release()