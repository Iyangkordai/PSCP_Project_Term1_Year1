const template_cost = document.getElementById("cost_list_template")
let cost_div = document.getElementById("cost_list_div")
function new_list_cost(){
    console.log("hello")
    const child = template_cost.content.cloneNode(true)
    cost_div.appendChild(child)
    cost_div.lastElementChild.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
    })
}