let theme_btn = document.querySelector('#theme');
let mode_icon = document.querySelector('#mode');
let links = document.querySelector('a')
function thememode()
{
    console.log("btnpush");
    // console.log(document.body.style.backgroundColor = "#AA0000");
    document.body.classList.toggle("mode");

    mode_icon.innerHTML = mode_icon.classList.toggle("icon")?'🌞':'🌙';
    // links.classList.toggle('icon')
}

function ShowMenu()
{
    let op = document.querySelector('.options');
    
    if(op.classList.toggle('menu_toggle'))
    {
        op.classList.add('.menu_toggle')
    }
    else
    {
        op.classList.remove('.menu_toggle')
    }
    console.log('menu');
}

let home = document.querySelector('#home');
home.addEventListener('click',()=>
{
    location.assign('#')
})