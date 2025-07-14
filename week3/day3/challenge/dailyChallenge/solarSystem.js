// Define planets with their names, colors, and number of moons
const planets = [
  { name: "Mercury", color: "gray", moons: 0 },
  { name: "Venus", color: "orange", moons: 0 },
  { name: "Earth", color: "blue", moons: 1 },
  { name: "Mars", color: "red", moons: 2 },
  { name: "Jupiter", color: "brown", moons: 79 },
  { name: "Saturn", color: "goldenrod", moons: 83 },
  { name: "Uranus", color: "lightblue", moons: 27 },
  { name: "Neptune", color: "darkblue", moons: 14 },
];

const section = document.querySelector(".listPlanets");

planets.forEach((planet, index) => {
  // Create planet div
  const planetDiv = document.createElement("div");
  planetDiv.classList.add("planet");
  planetDiv.style.backgroundColor = planet.color;
  planetDiv.textContent = planet.name;
  planetDiv.style.color = "white";

  // Create moons
  for (let i = 0; i < planet.moons; i++) {
    const moon = document.createElement("div");
    moon.classList.add("moon");

    // Position moons in a circular pattern
    const angle = (i / planet.moons) * 2 * Math.PI;
    const radius = 70 + (i % 3) * 10; // Spread them out
    const x = radius * Math.cos(angle);
    const y = radius * Math.sin(angle);

    moon.style.left = `${50 + x}px`;
    moon.style.top = `${50 + y}px`;

    planetDiv.appendChild(moon);
  }

  section.appendChild(planetDiv);
});
