// filters = {"filter1": [type1, type2, type3], "filter2"; [type1, type2, type3]}

const changeFilter = (evt) => {
    const currentFilter = evt.target.value;

    if (currentFilter !== "not-chosen"){
        if (previousFilter){

            const previouslySelectedElements = document.querySelectorAll(".selected");

            for (const element of previouslySelectedElements){
                element.classList.remove("selected")
            }

        }

        const types = filters[currentFilter];
        let currentTypeElements;
        for (const type_x of types){
            currentTypeElements = document.querySelectorAll(`${currentFilter}-${type_x}`);
            for (const element of currentTypeElements){
                element.classList.add("selected");
            }
        }

        //TODO need a logic to add sidebar
        const sidebar = document.querySelector(".sidebar");
        const numberOfPreviousTypes = sidebar.children.length;
        const numberOfCurrentTypes = filters[currentFilter].length;






        previousFilter = true;


    }

}

let previousFilter = false;
const filterElement = document.getElementById("filter");
filterElement.addEventListener("change", changeFilter);