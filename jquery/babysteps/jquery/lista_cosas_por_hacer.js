$(function(){
    $("#nuevo").on("click", function(){
        // manejando un evento
        var val = $("input").val();
        if (val !== ""){
            var elemento = $("<li></li>").text(val);
            $(elemento).append("<button class='rem'>X</button>");
            $("#lista").append(elemento);
            $("input").val("");//borrar el input
        }
    });
});