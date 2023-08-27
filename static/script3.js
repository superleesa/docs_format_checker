const paragraphs = [[[[class1, class2, class3], sometext]], ["br"], []]


const mainTextDiv = document.getElementById("main-text");
const innerParagraphs = [];

for (const paragraph of paragraphs){

    if (paragraph === ["br"]){
        const breakElement = document.createElement("br")
        innerParagraphs.push(breakElement)
    }else{
        const pElement = document.createElement("p");
        const innerSpans = [];

        for (const span of paragraph){
            const spanElement = document.createElement("span");

            for (const class_name in span[0]){
                spanElement.classList.add(class_name);
            }
            spanElement.innerText = paragraph[1];
            innerSpans.push(spanElement)
        }

        pElement.replaceChildren(innerSpans);
    }
    innerParagraph.push(pElement)

}
mainTextDiv.replaceChildren(innerParagraphs)

