// DOM Elements
const button = document.getElementById('getCharacter');
const nameEl = document.getElementById('name');
const heightEl = document.getElementById('height');
const genderEl = document.getElementById('gender');
const birthYearEl = document.getElementById('birthYear');
const homeworldEl = document.getElementById('homeworld');

const loader = document.getElementById('loader');
const error = document.getElementById('error');
const characterCard = document.getElementById('characterInfo');

// Fetch random character
async function fetchCharacter() {
  const id = Math.floor(Math.random() * 83) + 1; // 1 to 83
  const url = `https://www.swapi.tech/api/people/${id}`;

  showLoader();
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error('Fetch failed');

    const data = await response.json();
    const character = data.result.properties;

    const homeworldName = await fetchHomeworld(character.homeworld);

    displayCharacter({
      name: character.name,
      height: character.height,
      gender: character.gender,
      birth_year: character.birth_year,
      homeworld: homeworldName
    });

  } catch (err) {
    showError();
    console.error(err);
  } finally {
    hideLoader();
  }
}

// Fetch homeworld name
async function fetchHomeworld(url) {
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error('Homeworld fetch failed');
    const data = await res.json();
    return data.result.properties.name;
  } catch {
    return 'Unknown';
  }
}

// Display character info on DOM
function displayCharacter(char) {
  error.classList.add('hidden');
  characterCard.classList.remove('hidden');
  nameEl.textContent = char.name;
  heightEl.textContent = char.height;
  genderEl.textContent = char.gender;
  birthYearEl.textContent = char.birth_year;
  homeworldEl.textContent = char.homeworld;
}

function showLoader() {
  loader.classList.remove('hidden');
  characterCard.classList.add('hidden');
  error.classList.add('hidden');
}

function hideLoader() {
  loader.classList.add('hidden');
}

function showError() {
  characterCard.classList.add('hidden');
  error.classList.remove('hidden');
}

// Event listener
button.addEventListener('click', fetchCharacter);
