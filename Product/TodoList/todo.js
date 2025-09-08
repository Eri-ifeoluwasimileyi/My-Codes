const addForm = document.getElementById('add-task');
const taskList = document.querySelector('#task-list ul');
const searchForm = document.getElementById('search-tasks');


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
    }
});


taskList.addEventListener('click', function(e) {
    if (e.target.classList.contains('delete')) {
        const li = e.target.parentElement;
        taskList.removeChild(li);
    }
});


searchForm.addEventListener('input', function(e) {
    const term = e.target.value.toLowerCase();
    Array.from(taskList.children).forEach(function(li) {
        const name = li.querySelector('.name').textContent.toLowerCase();
        li.style.display = name.includes(term) ? '' : 'none';
    });
});