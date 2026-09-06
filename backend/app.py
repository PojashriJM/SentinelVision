from flask import Flask, request, jsonify, send_from_directory
from vision.video_processor import load_video, get_video_info, read_frames, close_video

import os


app = Flask(__name__)

UPLOAD_FOLDER = "backend/uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():

    return send_from_directory("../frontend", "index.html")


@app.route("/<path:filename>")
def frontend_files(filename):

    return send_from_directory("../frontend", filename)


@app.route("/analyze", methods=["POST"])
def analyze():

    video = request.files.get("video")

    if video is None:
        return jsonify({
            "success": False,
            "message": "No video received"
        })


    # Save uploaded video

    video_path = os.path.join(
        UPLOAD_FOLDER,
        video.filename
    )

    video.save(video_path)


    try:

        # Open video using OpenCV

        cap = load_video(video_path)


        # Get video information

        video_info = get_video_info(cap)


        # Read all frames

        frames_read = read_frames(cap)


        # Release video

        close_video(cap)


        return jsonify({

            "success": True,

            "message": "Video processed successfully!",

            "filename": video.filename,

            "video_info": video_info,

            "frames_read": frames_read

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "message": str(e)

        })


if __name__ == "__main__":

    app.run(debug=True)