
const caption = document.getElementById('caption')
const toUp = document.getElementById('ToUp')

window.addEventListener('scroll', function(){
    sY = this.window.scrollY
    if(sY > 50){
        caption.dataset.capScroll = "true";
    } else {
        caption.dataset.capScroll = "false";
    }
    if(sY > 500){
        toUp.dataset.upScroll = "true";
    } else {
        toUp.dataset.upScroll = "false";
    }
})

const details = document.getElementsByClassName('details')

for(let i=0; i<details.length; i++){
    let detail = details[i];
    console.log(detail)
    detail.addEventListener('click', function(){
        if(detail.dataset.open == "false"){
            detail.dataset.open = "true";
        } else {
            detail.dataset.open = "false";
        }
    })
}

const menu = document.getElementById('menu')
const menuOpenBtn = document.getElementById('menu_open_btn')
const menuCloseBtn = document.getElementById('menu_close_btn')

menuOpenBtn.addEventListener('click', function(){
    menu.dataset.menuOpen = "true"
})
menuCloseBtn.addEventListener('click', function(){
    menu.dataset.menuOpen = "false"
})