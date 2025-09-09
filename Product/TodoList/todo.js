const addForm = document.getElementById('add-task');
const taskList = document.querySelector('#task-list ul');
const searchForm = document.getElementById('search-tasks');

let storedTasks = JSON.parse(localStorage.getItem("tasks")) || [];


if (storedTasks.length === 0) {
    let initialTasks = [];
    taskList.querySelectorAll("li").forEach(li => {
        initialTasks.push({
            name: li.querySelector(".name").textContent,   
            completed: li.querySelector(".tick-box")?.checked || false
        });
    });
    localStorage.setItem("tasks", JSON.stringify(initialTasks));
    storedTasks = initialTasks;
}

// Clear whatever was in HTML and rebuild from localStorage
taskList.innerHTML = "";
storedTasks.forEach(task => {
    const li = document.createElement("li");
    li.innerHTML = `
        <input type="checkbox" class="tick-box" ${task.completed ? "checked" : ""}>
        <span class="name ${task.completed ? "completed" : ""}">${task.name}</span>
        <span class="delete">delete</span>
    `;
    taskList.appendChild(li);
});

addForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const value = addForm.querySelector('input[type="text"]').value.trim();
    if (value) {
        const li = document.createElement('li');
        li.innerHTML = `
            <input type="checkbox" class="tick-box">
            <span class="name">${value}</span>
            <span class="delete">delete</span>
        `;
        taskList.appendChild(li);
        addForm.reset();


        let tasks = []
        taskList.querySelectorAll("li").forEach(li => {
            tasks.push({
                name: li.querySelector(".name").textContent,
                completed: li.querySelector(".tick-box").checked
            });
        });
        localStorage.setItem("tasks", JSON.stringify(tasks));
    }
});


taskList.addEventListener('click', function(e) {
    if (e.target.classList.contains('delete')) {
        const li = e.target.parentElement;
        taskList.removeChild(li);
    }

    let tasks = []
    taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
            name: li.querySelector(".name").textContent,
            completed: li.querySelector(".tick-box").checked
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
});


searchForm.addEventListener('input', function(e) {
    const term = e.target.value.toLowerCase();
    Array.from(taskList.children).forEach(function(li) {
        const name = li.querySelector('.name').textContent.toLowerCase();
        li.style.display = name.includes(term) ? '' : 'none';
    });

    let tasks = []
    taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
            name: li.querySelector(".name").textContent,
            completed: li.querySelector(".tick-box").checked
        });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
});



taskList.addEventListener("change", (event) => {
    if (event.target.classList.contains("tick-box")) {
        let taskName = event.target.nextElementSibling;
        if (event.target.checked) {
            taskName.classList.add("completed");
        } else {
            taskName.classList.remove("completed");
        }
    }

    let tasks = []
    taskList.querySelectorAll("li").forEach(li => {
        tasks.push({
            name: li.querySelector(".name").textContent,
            completed: li.querySelector(".tick-box").checked
        });
    })
    localStorage.setItem("tasks", JSON.stringify(tasks));
});

