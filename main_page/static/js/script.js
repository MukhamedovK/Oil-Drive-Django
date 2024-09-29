// function changeContent(element) {
//     element.innerHTML += <i class="fa-solid fa-arrow-right"></i>;
// }

if (document.getElementById("show_form_button")) {
    document.getElementById("show_form_button").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "grid";
        document.getElementById("request_form_overlay").style.display = "block";
        document.getElementById("feedback-box").style.width = '520px';
        document.getElementById("overlay-title").style.fontSize = '14px';
        document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';


        document.getElementById("overlay-form").action += '?from=Основная';
    });
}

if (document.getElementById("show_form_button_e")) {
    document.getElementById("show_form_button_e").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "grid";
        document.getElementById("request_form_overlay").style.display = "flex";
        document.getElementById("request_form_overlay").style.zIndex = "4";
        document.getElementById("feedback-box").style.width = '300px';
        document.getElementById("overlay-title").style.fontSize = '14px';
        document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';

        document.getElementById("overlay-form").action += `?from=${this.getAttribute('data-product')}`;
    });
}

if (document.getElementById("show_form_button_n")) {
    document.getElementById("show_form_button_n").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "grid";
        document.getElementById("request_form_overlay").style.display = "block";
        document.getElementById("feedback-box").style.width = '520px';
        document.getElementById("overlay-title").style.fontSize = '14px';
        document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';
    });
}
if (document.getElementById("show_form_button_mobile")) {
    document.getElementById("show_form_button_mobile").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "grid";
        document.getElementById("request_form_overlay").style.display = "flex";
        document.getElementById("request_form_overlay").style.zIndex = "4";
        document.getElementById("feedback-box").style.width = '300px';
        document.getElementById("overlay-title").style.fontSize = '14px';
        document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';
        console.log('hello')
    });
}
if (document.getElementById("show_form_button_f")) {
    document.getElementById("show_form_button_f").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "grid";
        document.getElementById("request_form_overlay").style.display = "block";
        document.getElementById("feedback-box").style.width = '520px';
        document.getElementById("overlay-title").style.fontSize = '14px';
        document.getElementById("feedback-box").style.gridTemplateColumns = '1fr';
    });
}

if (document.getElementById("overlay")) {
    document.getElementById("overlay").addEventListener("click", function() {
        document.getElementById("overlay").style.display = "none";
        document.getElementById("request_form_overlay").style.display = "none";
    });
}


// document.querySelector('.burger-menu').addEventListener('click', function() {
//     document.querySelector('#burger-menu-items').classList.toggle('active');
// });
document.querySelector('.burger-menu').addEventListener('click', function() {
    document.querySelector('.nav-menu-adaptive').style.display = 'grid'
    // document.querySelector('#overlay').style.display = 'grid'
});

document.querySelector('.close-button').addEventListener('click', function() {
    document.querySelector('.nav-menu-adaptive').style.display = 'none'
    // document.getElementById("overlay").style.display = "none";
});

window.addEventListener('scroll', function() {
    let headerMobile = document.getElementById('header-mobile');
    let search_input = document.querySelector('.search-bar');
    // var navbar = document.getElementById('navbar');
    let scrollPosition = window.scrollY
    // console.log(scrollPosition)
    // Если scroll больше 0, скрываем header-mobile и показываем navbar
    if (scrollPosition > 150) {
    //   headerMobile.style.display = 'none';
    //   navbar.style.display = 'flex';
       search_input.style.display = 'none';
       headerMobile.style.position = 'fixed';
    } else { // В противном случае, показываем header-mobile и скрываем navbar
        headerMobile.style.position = 'relative';
        search_input.style.display = 'flex';
    }
})


document.addEventListener('DOMContentLoaded', function() {
  const toggles = document.querySelectorAll('.question');

  toggles.forEach(function(toggle) {
    toggle.addEventListener('click', function() {
      const answer = this.parentElement.querySelector('.answer');
      if (answer.style.display === 'block') {
        answer.style.display = 'none';
      } else {
        answer.style.display = 'block';
        answer.style.padding = '10px 0px';
      }
    });
  });
});



