from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


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

    print("Video received:", video.filename)

    return jsonify({
        "success": True,
        "message": "Video received successfully!",
        "filename": video.filename
    })


if __name__ == "__main__":
    app.run(debug=True)