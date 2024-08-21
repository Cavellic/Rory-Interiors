// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// overlay menu
function openNav() {
    document.getElementById("myNav").classList.toggle("menu_width");
    document.querySelector(".custom_menu-btn").classList.toggle("menu_btn-style");
}


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// lightbox gallery
$(document).on("click", '[data-toggle="lightbox"]', function (event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

document.addEventListener('DOMContentLoaded', () => {

    const caroS = document.querySelector(`.carousel-slider`);
    const caroSlider = new MicroSlider(caroS, {indicators: true, indicatiorText: ''});
    const hammer = new Hammer(caroS);
    const caroSTimer = 2000;
    let caroAutoPlay = setInterval(() => caroSlider.next(), caroSTimer);

    caroS.onmouseenter = function(e) {
        clearInterval(caroAutoPlay);
        console.log(e.type + 'mouse detected');
    }

    caroS.onmouseleave = function(e) {
        clearInterval(caroAutoPlay);
        caroAutoPlay = setInterval(() => caroSlider.next(), caroSTimer);
        console.log(e.type + 'mouse detected');
    }

    caroS.onclick = function(e) {
        clearInterval(caroAutoPlay);
        console.log(e.type + 'mouse detecte');
    }

    hammer.on('tap', function(e) {
        clearInterval(caroAutoPlay);
        console/log(e.type + 'gesture detected');
    });

    hammer.on('swipe', function(e) {
        clearInterval(caroAutoPlay);
        caroAutoPlay = setInterval(() => caroSlider.next(), caroSTimer);
        console.log(e.type + 'gesture detected');
    });

    let slideLink = document.querySelectorAll('.slider-item');
    if (slideLink && slideLink!== null && slideLink.length > 0 ){
        slideLink.forEach( el => el.addEventListener('click', e => {
            e.preventDefault();
            let href = el.dataset.href;
            let target = el.dataset.target;

            if (href !== '#') wimdow.open(href, target);
        }));
    }
    

})