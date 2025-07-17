function playSound(key) {
  const audio = document.getElementById(key);
  const button = document.querySelector(`.drum[data-key="${key}"]`);

  if (!audio || !button) return;

  audio.currentTime = 0; // rewind
  audio.play();

  button.classList.add("playing");
  setTimeout(() => button.classList.remove("playing"), 200);
}

// Keyboard press
document.addEventListener("keydown", (event) => {
  const key = event.key.toUpperCase();
  playSound(key);
});

// Mouse click
document.querySelectorAll(".drum").forEach(button => {
  button.addEventListener("click", () => {
    const key = button.getAttribute("data-key");
    playSound(key);
  });
});
