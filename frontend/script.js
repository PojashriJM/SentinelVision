const videoInput = document.getElementById("videoInput");
const uploadBtn = document.getElementById("uploadBtn");
const analyzeBtn = document.getElementById("analyzeBtn");


uploadBtn.addEventListener("click", function () {

    videoInput.click();

});
videoInput.addEventListener("change", function () {

    const file = videoInput.files[0];

    if (file) {
        document.getElementById("fileName").textContent = file.name;
    }

});

analyzeBtn.addEventListener("click", function () {

    const file = videoInput.files[0];

    if (!file) {
        alert("Please select a video first.");
        return;
    }

    const formData = new FormData();

    formData.append("video", file);

  fetch("/analyze", {
    method: "POST",
    body: formData
})
.then(response => response.json())
.then(data => {

    console.log(data);

    if (data.success) {

        status.textContent = data.message;

        console.log("Video:", data.filename);

        console.log("Video information:", data.video_info);

        console.log("Frames read:", data.frames_read);

    } 
    else {

        status.textContent = data.message;

    }

})
.catch(error => {

    console.error("Error:", error);

    status.textContent = "Something went wrong.";

});

});