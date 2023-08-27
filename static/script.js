// const fontTypeSelector = (fontsUsed) => {
//     fontsUsed.forEach(
//
//
//
//     )
// }
//
//
//
// const selectcolor = (fontclass) => {
//     const marks = document.getElementsByClassName(".".concat("", fontclass));
//     marks.addventListner("hover", () => {
//         for (const mark in marks){
//             mark.style.
//         }
//
//     })
// }


const changeTabTo = (tabName) => {
    // setting all contents to be invisible
    const tabContents = document.getElementsByClassName("tab-content");
    for (const content in tabContents){
        content.style.display = "none";
    }

    // remove the "active" class from all buttons
    const tabButtons = document.getElementsByClassName("tab-button");
    for (const button in tabButtons){
        button.style.backgroundColor = "inherit";
    }

    // make the selected tab content visible AND set the class "active"
    document.getElementById(tabName.concat("-tab-content")).style.display = "block";
    document.getElementById(tabName.concat("-button")).style.backgroundColor = "#ccc";
}

const switchTabFrom = (tabName) => {
    if (tabName === "info"){
        document.getElementById(tabName.concat("-tab-content")).style.display = "block";
        document.getElementById(tabName.concat("-button")).style.backgroundColor = "#ccc";
        document.getElementById("filter".concat("-tab-content")).style.display = "none";
        document.getElementById("filter".concat("-button")).style.backgroundColor = "inherit";
    }else{
        document.getElementById(tabName.concat("-tab-content")).style.display = "block";
        document.getElementById(tabName.concat("-button")).style.backgroundColor = "#ccc";
        document.getElementById("info".concat("-tab-content")).style.display = "none";
        document.getElementById("info".concat("-button")).style.backgroundColor = "inherit";
    }
}