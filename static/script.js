const template_cost = document.getElementById("cost_list_template")
let cost_div = document.getElementById("cost_list_div")
function new_list_cost(){
    const child = template_cost.content.cloneNode(true)
    cost_div.appendChild(child)
    cost_div.lastElementChild.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
    })
}

cost_div.addEventListener('click', function(event){

    const delete_bt = event.target.closest('.delete_bt')
    if (delete_bt){
        event.preventDefault()

        const want_row = delete_bt.closest("#list_div")
        if (want_row && cost_div.childElementCount > 1){
            console.log("found want row ")
            want_row.remove()
        }
    }
})