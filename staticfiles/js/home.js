const VIDEO_ID = "dQw4w9WgXcQ"; // YouTube video ID ni o'zgartiring

function openVideo() {
  document.getElementById(
    "videoFrame"
  ).src = `https://www.youtube.com/embed/${VIDEO_ID}?autoplay=1`;
  document.getElementById("videoModal").classList.remove("hidden");
}

function closeVideo() {
  document.getElementById("videoFrame").src = "";
  document.getElementById("videoModal").classList.add("hidden");
}

// Tashqariga bosganda yopish
document.getElementById("videoModal").onclick = function (e) {
  if (e.target === this) closeVideo();
};
