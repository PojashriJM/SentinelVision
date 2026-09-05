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

    document.getElementById("status").textContent =
        data.message;

});

});