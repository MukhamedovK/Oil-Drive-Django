// function changeContent(element) {
//     element.innerHTML += <i class="fa-solid fa-arrow-right"></i>;
// }

document.getElementById("show_form_button").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "grid";
    document.getElementById("request_form_overlay").style.display = "block";
    document.getElementById("feedback-box").style.width = '520px';
    document.getElementById("overlay-title").style.fontSize = '14px';
    document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';
});

document.getElementById("overlay").addEventListener("click", function() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("request_form_overlay").style.display = "none";
});


// window.addEventListener('resize', function() {
//     var screenWidth = window.innerWidth
//     console.log(screenWidth)
//     if (screenWidth <= 768) {
//         console.log(screenWidth)
//         let searchBar = document.getElementById('search-bar')
//         let navBar = document.getElementById('navbar')

//         let navBarLogo = document.getElementById('navbar_logo')
//         navBarLogo.children[0].style.width = '100%'
//         navBarLogo.style.height = '100%'
//         navBarLogo.children[0].style.height = '100%'
//         let topHeader = document.getElementById('top-header')

//         navBar.appendChild(searchBar)
//         console.log(topHeader.children)
//         topHeader.insertBefore(navBarLogo, topHeader.children[1])
//     }
// }
// )

document.querySelector('.burger-menu').addEventListener('click', function() {
    document.querySelector('.burger-menu-items').classList.toggle('active');
});


window.addEventListener('scroll', function() {
    var headerMobile = document.getElementById('header-mobile');
    var navbar = document.getElementById('navbar');
    var scrollPosition = window.scrollY
    console.log(scrollPosition)
    // Если scroll больше 0, скрываем header-mobile и показываем navbar
    if (scrollPosition > 150) {
    //   headerMobile.style.display = 'none';
    //   navbar.style.display = 'flex';
       headerMobile.style.position = 'fixed';
    } else { // В противном случае, показываем header-mobile и скрываем navbar
        headerMobile.style.position = 'relative';
    }
})



