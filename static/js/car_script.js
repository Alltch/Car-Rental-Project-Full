const cib1 = document.getElementById('cib_1');
const cib2 = document.getElementById('cib_2');
const carImgsSlider = document.getElementById('car_imgs_slider')
const carImgCon = document.getElementsByClassName('car_img_con');

const carImgContainers = document.querySelectorAll('.car_img_con_data');
let currentImgIndex = 0;
let maxImgs = carImgContainers.length;

changeSlider = (pageIndex) => {
    carImgsSlider.style.transform = `translate(-${100*pageIndex}vw)`;
}

changeSlider = (pageIndex) => {
        carImgsSlider.style.transform = `translate(calc((var(--img-con-w)*${pageIndex} + var(--com-gap)*${2*pageIndex})*-1))`;
        for (let index = 0; index < carImgCon.length; index++) {
            var element = carImgCon[index];
            if(index != pageIndex){
                element.dataset.imgSeen = "false";
            } else {
                element.dataset.imgSeen = "true";
            }
        }
}

cib1.addEventListener('click', function(){
    if(currentImgIndex!=0){
        currentImgIndex--;
    }
    changeSlider(currentImgIndex)
})

cib2.addEventListener('click', function(){
    if(currentImgIndex!=maxImgs-1){
        currentImgIndex++;
    }
    changeSlider(currentImgIndex)
})

const menu = document.getElementById('menu')
const menuOpenBtn = document.getElementById('menu_open_btn')
const menuCloseBtn = document.getElementById('menu_close_btn')

menuOpenBtn.addEventListener('click', function(){
    menu.dataset.menuOpen = "true"
})
menuCloseBtn.addEventListener('click', function(){
    menu.dataset.menuOpen = "false"
})

const carImgsWrapper = document.getElementById('car_imgs_wrapper')


var swipeStart = 0
var swipeEnd = 0

swipeToRight = (where) => {
        if(where == "toLeft" && currentImgIndex!=0){
            currentImgIndex--;
        }
        if(where == "toRight" && currentImgIndex!=maxImgs-1){
            currentImgIndex++;
        }
    }

carImgsWrapper.addEventListener('touchstart', function(e){
    swipeStart = e.changedTouches[0].clientX
})
carImgsWrapper.addEventListener('touchend', function(e){
    carImgsWrapper.style.cssText = "scale: 1";
    swipeEnd = e.changedTouches[0].clientX
    if(swipeStart > swipeEnd){
        swipeToRight("toRight")
    } else {
        swipeToRight("toLeft")
    }
})
