$(document).ready(function() {

    function post_chat(message){
        $.ajax({
                type: "POST",
                url: "/chat/",
                data: { message: message}
               }).done(function(html){
            $('#messages').html(html)
        });
    }

    $("[class='chat-submit']").click(function(){
        var m = $('[name="message-area"]').val();
        post_chat(message);
    });
});
