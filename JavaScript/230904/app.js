<<<<<<< HEAD
const addButton = document.querySelector('#add-button');

addButton.addEventListener('click', () => {
  const input = document.querySelector('#input');
  const text = input.value.trim();

  if (text !== '') {
    addToList(text);
    input.value = '';
    input.focus();
  }
});

function addToList(text) {
  const list = document.querySelector('#list');

  const newListItem = document.createElement('li');
  newListItem.classList.add('list-item'); 

  newListItem.innerHTML = text;

  list.appendChild(newListItem);
=======
const addButton = document.querySelector('#add-button');

addButton.addEventListener('click', () => {
  const input = document.querySelector('#input');
  const text = input.value.trim();

  if (text !== '') {
    addToList(text);
    input.value = '';
    input.focus();
  }
});

function addToList(text) {
  const list = document.querySelector('#list');

  const newListItem = document.createElement('li');
  newListItem.classList.add('list-item'); 

  newListItem.innerHTML = text;

  list.appendChild(newListItem);
>>>>>>> 9a90d68d7dd280c6eb2ddb8593ddd444feff7f3f
}