$(function(){
   
    $("#start").html("substituir");
    $("#pepe").append(" despues");
    $("#pepe").prepend("antes ");
    $("#pepe").after (" despues del final");
    $("#pepe").before (" antes del comienzo");
    var txt = $("<p></p>").text("Hi");
    $("#pepe").before (txt);
    $("#nuevoEstilo").css("color", "white");
    $("#nuevoEstilo").css("background-color", "green");
    $("div").eq(1).append(" segundo div")
    $("div").eq(1).css("background-color", "green");
    $("div").eq(1).css("color", "yellow");
    $("#starting").click(function() {
        $("body").append(Date());
    })
    $("#pepe").on("click", function() {
        $("body").append(Date());
        })
     
})