var modal_manual = document.getElementById("manual")
var btn_manual = document.getElementById("user_manual_bt")

// แสดงผลคู่มือการใช้งานเว็บ
btn_manual.onclick = function() {
    modal_manual.classList.add("show");
}

modal_manual.onclick = function(event) {
    if (event.target == modal_manual) {
        modal_manual.classList.remove("show");
    }
}