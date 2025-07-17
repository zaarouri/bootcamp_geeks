const colors = [
  "red", "orange", "yellow", "green", "lightgreen",
  "cyan", "skyblue", "blue", "purple", "violet",
  "pink", "gray", "black", "white"
];

const palette = document.getElementById("palette");
const grid = document.getElementById("grid");
const clearBtn = document.getElementById("clear");

let selectedColor = "black";
let isDrawing = false;

// Create palette buttons
colors.forEach(color => {
  const swatch = document.createElement("div");
  swatch.className = "color-swatch";
  swatch.style.backgroundColor = color;
  swatch.addEventListener("click", () => {
    selectedColor = color;
    document.querySelectorAll(".color-swatch").forEach(el => el.classList.remove("selected"));
    swatch.classList.add("selected");
  });
  palette.appendChild(swatch);
});
palette.firstChild.classList.add("selected");

// Create grid
for (let i = 0; i < 50 * 25; i++) {
  const cell = document.createElement("div");
  cell.className = "cell";

  cell.addEventListener("mousedown", () => {
    isDrawing = true;
    cell.style.backgroundColor = selectedColor;
  });

  cell.addEventListener("mouseover", () => {
    if (isDrawing) {
      cell.style.backgroundColor = selectedColor;
    }
  });

  cell.addEventListener("mouseup", () => {
    isDrawing = false;
  });

  grid.appendChild(cell);
}

// Clear button
clearBtn.addEventListener("click", () => {
  document.querySelectorAll(".cell").forEach(cell => {
    cell.style.backgroundColor = "white";
  });
});

// Global mouseup
document.body.addEventListener("mouseup", () => {
  isDrawing = false;
});
