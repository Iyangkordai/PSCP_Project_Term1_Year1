const template_cost = document.getElementById("cost_list_template")
const template_else = document.getElementById("else_list_template")
const template_package = document.getElementById("package_list_template")
let cost_div = document.getElementById("cost_list_div")
let else_div = document.getElementById("else_list_div")
let package_div = document.getElementById("packgate_list_div")

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