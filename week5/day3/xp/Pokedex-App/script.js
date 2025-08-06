const randomBtn = document.getElementById('randomBtn');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

const nameEl = document.getElementById('name');
const idEl = document.getElementById('id');
const heightEl = document.getElementById('height');
const weightEl = document.getElementById('weight');
const typeEl = document.getElementById('type');
const imgEl = document.getElementById('pokemonImg');

const loader = document.getElementById('loader');
const error = document.getElementById('error');

let currentId = 1;

async function fetchPokemon(id) {
  showLoader();
  try {
    const res = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
    if (!res.ok) throw new Error("Not found");

    const data = await res.json();
    displayPokemon(data);
    currentId = data.id;
  } catch (err) {
    showError();
  } finally {
    hideLoader();
  }
}

function displayPokemon(pokemon) {
  error.classList.add('hidden');

  nameEl.textContent = capitalize(pokemon.name);
  idEl.textContent = pokemon.id;
  heightEl.textContent = pokemon.height + " dm";
  weightEl.textContent = pokemon.weight + " hg";
  typeEl.textContent = pokemon.types.map(t => t.type.name).join(', ');
  imgEl.src = pokemon.sprites.front_default;
  imgEl.alt = pokemon.name;
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function showLoader() {
  loader.classList.remove('hidden');
  error.classList.add('hidden');
}

function hideLoader() {
  loader.classList.add('hidden');
}

function showError() {
  error.classList.remove('hidden');
  nameEl.textContent = "";
  idEl.textContent = "";
  heightEl.textContent = "";
  weightEl.textContent = "";
  typeEl.textContent = "";
  imgEl.src = "";
}

randomBtn.addEventListener('click', () => {
  const id = Math.floor(Math.random() * 898) + 1;
  fetchPokemon(id);
});

prevBtn.addEventListener('click', () => {
  if (currentId > 1) fetchPokemon(currentId - 1);
});

nextBtn.addEventListener('click', () => {
  if (currentId < 898) fetchPokemon(currentId + 1);
});

fetchPokemon(currentId);
