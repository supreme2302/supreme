/**
 * Created by petrosadaman on 11.12.2017.
 */

function like(user, quest, positive) {
            $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });

            $.ajax({
                url : "like",
                type : "POST",
                data : {user: user, question: quest, positive: positive },
                success : function(json) {

                        var button = document.getElementById('rating'+quest)
                        button.innerText = json.rating

                    button.isDisabled = true
                },

                error : function (json) {
                    console.log(json.ErrorMSG)
                }
            })
};



function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {

    $('.modal1').click( function(event){
        event.preventDefault();
        $('#overlay1').fadeIn(400, // анимируем показ обложки
            function(){ // далее показываем мод. окно
                $('#modal_form1')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
        });
    });


    $('.modal2').click( function(event){
        event.preventDefault();
        $('#overlay2').fadeIn(400, // анимируем показ обложки
            function(){ // далее показываем мод. окно
                $('#modal_form2')
                    .css('display', 'block')
                    .animate({opacity: 1, top: '50%'}, 200);
        });
    });


    // закрытие модального окна
    $('#modal_close1, #overlay1').click( function(){
        $('#modal_form1')
            .animate({opacity: 0, top: '45%'}, 200,  // уменьшаем прозрачность
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // скрываем окно
                    $('#overlay1').fadeOut(400); // скрывaем пoдлoжку
                }
            );
    });


    // закрытие модального окна
    $('#modal_close2, #overlay2').click( function(){
        $('#modal_form2')
            .animate({opacity: 0, top: '45%'}, 200,  // уменьшаем прозрачность
                function(){ // пoсле aнимaции
                    $(this).css('display', 'none'); // скрываем окно
                    $('#overlay2').fadeOut(400); // скрывaем пoдлoжку
                }
            );
    });

});


function scr(page) {
    $.ajaxSetup({
           beforeSend: function(xhr, settings){
                xhr.setRequestHeader( "X-CSRFToken", getCookie('csrftoken') )
           }
        });
    console.log("is here")
       $.ajax({
            type: 'GET',
            url: "scroll", //Ссылка на вьюху
            data:{'page':page},//Здесь можно передать данные в GET запросе, например сколько значений получить
            success: function(jso) {
                console.log("success")
                var div=document.getElementById("cont")
//hello
                div.innerHTML+=jso
                var button=document.getElementById('btn'+page)
                button.parentNode.removeChild(button)
                // Ответ приходит в переменную data. Её и рендерим на страницу
            },
            error:function () {
                console.log("error")
            }
        });

};


$(document).ready(function() {

    $('.sidebar-menu').click(function (event) {
        $('.right-sidebar').toggleClass('active');
    });
});