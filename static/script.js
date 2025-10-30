const template_cost = document.getElementById("cost_list_template")
const template_else = document.getElementById("else_list_template")
const template_package = document.getElementById("package_list_template")
let cost_div = document.getElementById("cost_list_div")
let else_div = document.getElementById("else_list_div")
let package_div = document.getElementById("packgate_list_div")
let labor_div = document.getElementById("labor_div")
// รวมฟังก์ชั่นการเพิ่มตาราง

// ฟังก์ชั่นเพิ่มตารางของ วัตถุดิบ
function new_list_cost(){
    const child = template_cost.content.cloneNode(true) //สร้างตัวแปรที่เก็บค่าที่โคลนนิ่งมาจากเทรมเพลต
    cost_div.appendChild(child) // stack ตัวแปรที่โคลนเทรมเพลตมาไปไว้ที่ div ที่เก็บคอลัมน์ทั้งหมด
    // ทำให้มัน scoll ไปที่ element ล่าสุดที่เพิ่มเข้ามา
    cost_div.lastElementChild.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
    })
}

// ฟังก์ชั่นเพิ่มตารางของ ค่าเสื่อม
function new_list_else(){
    const child = template_else.content.cloneNode(true)
    else_div.appendChild(child)
    else_div.lastElementChild.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
    })
}

// ฟังก์ชั่นเพิ่มตารางของ ค่าบรรจุภัณฑ์
function new_list_package(){
    const child = template_package.content.cloneNode(true)
    package_div.appendChild(child)
    package_div.lastElementChild.scrollIntoView({
        behavior: 'smooth',
        block: 'nearest'
    })
}

// รวมฟังก์ชั่นกสนลบตาราง

// ฟังก์ชั่นการลบตารางของ ต้นทุนวัตถุดิบ
//ให้ JS ค่อยจับตาดูว่า div ของต้นทุนวัตถุดิบมีการกดไหม แล้วตัวแปร event คือตัวแปรที่จะรายงานว่าตัวที่ถูกกดคืออะไร
cost_div.addEventListener('click', function(event){

    const delete_bt = event.target.closest('.delete_bt') // เช็คว่าตัวแปร event อยู่ภายใต้ div ที่มี class = delete_bt ไหม
    if (delete_bt){
        const want_row = delete_bt.closest("#list_div") // ให้ตัวแปร want_row เก็บค่า div ที่เป็น coloumn หนึ่ง (เป็น div ที่เป็นตารางแต่ละคอลัมน์) ที่ปุ่มลบอยู่ภายใต้
        if (want_row && cost_div.childElementCount > 1){ // เช็คว่าปุ่มลบนั้นอยู่ภายใต้ div id = list_div และ div ที่เก็บคอลัมน์ทั้งหมด ต้องมีลูกมากกว่า 1 กันผู้ใช้ลบตารางจนหมด
            console.log("found want row ") // เอาไว้เช็คว่ามันเข้าเงื่อนไขนี้ไหม
            want_row.remove() // ลบตารางอันนั้นออกไป
        }
    }
})

// ฟังก์ชั่นการลบตารางของ ค่าเสื่อม
else_div.addEventListener('click', function(event){

    const delete_bt = event.target.closest('.delete_bt')
    if (delete_bt){
        const want_row = delete_bt.closest("#list_div")
        if (want_row && else_div.childElementCount > 1){
            console.log("found want row ")
            want_row.remove()
        }
    }
})

// ฟังก์ชั่นการลบตารางของ บรรจุภัณฑ์
package_div.addEventListener('click', function(event){

    const delete_bt = event.target.closest('.delete_bt')
    if (delete_bt){
        const want_row = delete_bt.closest("#list_div")
        if (want_row && package_div.childElementCount > 1){
            console.log("found want row ")
            want_row.remove()
        }
    }
})

// รวมฟังก์ชันการคำนวณ

function cost_cal(cost_input_list){
    let cost_price = cost_input_list.querySelector('[name="cost_price"]')
    let cost_amount = cost_input_list.querySelector('[name="cost_amount"]')
    let cost_used = cost_input_list.querySelector('[name="cost_used"]')
    let item_amount = document.getElementById("amount_div")
    let result_output = cost_input_list.querySelector('[class="cost_result"]')
    let cost_result = 0
    item_amount = item_amount.querySelector('[name="amount"]')
    item_amount = parseFloat(item_amount.value) || 0
    cost_price = parseFloat(cost_price.value) || 0
    cost_amount = parseFloat(cost_amount.value) || 0
    cost_used = parseFloat(cost_used.value) || 0
    if (cost_amount > 0 && item_amount > 0 && cost_used <= cost_amount){
        cost_result = ((cost_price / cost_amount) * cost_used) / item_amount
    }
    if (result_output && cost_used <= cost_amount){
        result_output.textContent = cost_result.toFixed(3)
    }
    else if(cost_used > cost_amount){
        result_output.textContent = "จำนวนที่ใช้ไม่สามารถมากกว่าปริมาณได้"

    }
}

cost_div.addEventListener('input', function(event){
    if (event.target.classList.contains("input_cost")){
        const row = event.target.closest("#list_div")
        if (row){
            cost_cal(row)
        }
    }
})

function else_cal(else_input_list){
    let expenses = else_input_list.querySelector('[name="expenses"]')
    let amount = else_input_list.querySelector('[name="product_amount"]')
    let else_result = 0
    let else_output = else_input_list.querySelector('[class="else_result"]')
    expenses = parseFloat(expenses.value) || 0
    amount = parseFloat(amount.value) || 0
    if (expenses > 0 && amount > 0){
        else_result = expenses / amount
    }
    if (else_output){
        else_output.textContent = else_result.toFixed(3)
    }
}

else_div.addEventListener('input', function(event){
    if (event.target.classList.contains("input_cost")){
        const row = event.target.closest("#list_div")
        if (row){
            else_cal(row)
        }
    }
})

function package_cal(package_input_list){
    let price = package_input_list.querySelector('[name="package_price"]')
    let amount = package_input_list.querySelector('[name="package_amount"]')
    let package_result = 0
    let package_output = package_input_list.querySelector('[class="package_result"]')
    price = parseFloat(price.value) || 0
    amount = parseFloat(amount.value) || 0

    if(amount > 0 && price > 0){
        package_result = price / amount
    }
    if(package_output){
        package_output.textContent = package_result.toFixed(3)
    }
}

package_div.addEventListener('input', function(event){
    if (event.target.classList.contains("input_cost")){
        const row = event.target.closest("#list_div")
        if (row){
            package_cal(row)
        }
    }
})

function labor_cal(labor_input){
    let salary = labor_input.querySelector('[name="all_labor"]')
    let amount = labor_input.querySelector('[name="amount_labor"]')
    let labor_result = 0
    let labor_output = labor_input.querySelector('[class="labor_result"]')
    salary = parseFloat(salary.value) || 0
    amount = parseFloat(amount.value) || 0

    if(salary > 0 && amount > 0){
        labor_result = salary / amount
    }
    if(labor_output){
        labor_output.textContent = labor_result.toFixed(3)
    }
}

labor_div.addEventListener('input', () => {
    labor_cal(labor_div)
})