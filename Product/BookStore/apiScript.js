const bookList = document.querySelector("#book-list ul")
//we chained two selectors together

//type tag name alone to find by tag
//type id name with '#' to find by id
//type class name with '.' to find by class
//combine different selectors to be more specifc

bookList.addEventListener("click", (event) => {
    if(event.target.textContent == "delete"){
        //let listItem = event.target.closest("li");
        let listItem = event.target.parentElement;
        listItem.remove()
    }
})

//target finds the element that the event happened in
//textContent is the text in between the element tags

const addForm = document.getElementById("add-book");

addForm.addEventListener("submit", (onSubmit) => {
    onSubmit.preventDefault();
    const value = document.querySelector("#add-book input").value.trim();
    //get the value that was entered in the input tag

    if(value){
        bookList.innerHTML += `
            <li>
	    		<span class="name">${value}</span>
	    		<span class="delete">delete</span>
	    	</li>
        `
        //using '=' wil replace the current inner html code with yours
        //use '+=' to add your inner html to the current inner html code
        

        // let newLi = document.createElement("li");
        // let newSpan1 = document.createElement("span");
        // let newSpan2 = document.createElement("span");
        //create a new html element

        // newSpan1.classList.add("name");
        // newSpan2.classList.add("delete");
        //add a class name to an html element
        //you can also use newSpan1.className = "name"

        // newSpan1.textContent = value;
        // newSpan2.textContent = "delete";
        //add text in between the tags of the element


        // newLi.appendChild(newSpan1);
        // newLi.appendChild(newSpan2);
        // bookList.appendChild(newLi);
        //make an element a child of another element

        addForm.reset();
        //resets the form to its original state
    }
    else{
        alert("stop pressing this button with no input")
    }
})


const searchInput = document.querySelector("#search-books input")
//we chained two selectors together

searchInput.addEventListener("keyup", (onKeyUp) => {
    let value = onKeyUp.target.value.toLowerCase();
    let books = bookList.getElementsByTagName("li");
    //this gets a collection of html elements
    //you must change to an array to loop through

    Array.from(books).forEach(book => {
        const bookTitle = book.firstElementChild.textContent.toLowerCase();
        //this gets the text in the first child element of li, which is span.

        if(bookTitle.startsWith(value)){
             book.style.display = "block"
        }
        else{
            book.style.display = "none"
        }

        //you can access css properties from here
    })
})
