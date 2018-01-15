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