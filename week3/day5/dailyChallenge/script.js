const form = document.getElementById("taskForm");
const input = document.getElementById("taskInput");
const listDiv = document.querySelector(".listTasks");

let tasks = [];
let idCounter = 0;

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const text = input.value.trim();
  if (text === "") return;

  const task = {
    task_id: idCounter++,
    text: text,
    done: false,
  };

  tasks.push(task);
  input.value = "";
  renderTasks();
});

function renderTasks() {
  listDiv.innerHTML = "";
  tasks.forEach(task => {
    const taskDiv = document.createElement("div");
    taskDiv.className = "task";
    if (task.done) taskDiv.classList.add("done");
    taskDiv.setAttribute("data-task-id", task.task_id);

    // delete button
    const deleteBtn = document.createElement("i");
    deleteBtn.className = "fa-solid fa-xmark";
    deleteBtn.addEventListener("click", () => deleteTask(task.task_id));

    // checkbox
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.addEventListener("change", () => toggleDone(task.task_id));

    // label
    const label = document.createElement("label");
    label.textContent = task.text;

    taskDiv.append(deleteBtn, checkbox, label);
    listDiv.appendChild(taskDiv);
  });
}

function toggleDone(id) {
  const task = tasks.find(t => t.task_id === id);
  if (task) {
    task.done = !task.done;
    renderTasks();
  }
}

function deleteTask(id) {
  tasks = tasks.filter(t => t.task_id !== id);
  renderTasks();
}
