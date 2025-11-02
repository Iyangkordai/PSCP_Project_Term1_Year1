var modal_manual = document.getElementById("manual")
var btn_manual = document.getElementById("user_manual_bt")
const carousel = document.getElementById('carousel')
const slides = document.querySelectorAll('.slide')
const prevBtn = document.getElementById('prevBtn')
const nextBtn = document.getElementById('nextBtn')

// แสดงผลคู่มือการใช้งานเว็บ
btn_manual.onclick = function() {
    modal_manual.classList.add("show");
}

modal_manual.onclick = function(event) {
    if (event.target == modal_manual) {
        modal_manual.classList.remove("show");
    }
}

//web sliding
let currentIndex = 0;
const totalSlides = slides.length;
function updateCarousel() {
    carousel.style.transform = `translateX(-${currentIndex * 100}%)`;
}

nextBtn.addEventListener('click', function() {
    currentIndex = currentIndex + 1;
        if (currentIndex >= totalSlides) {
            currentIndex = 0;
        }

        updateCarousel();
    });

prevBtn.addEventListener('click', function() {
    currentIndex = currentIndex - 1;
    if (currentIndex < 0) {
        currentIndex = totalSlides - 1;
    }

    updateCarousel();
});

updateCarousel();