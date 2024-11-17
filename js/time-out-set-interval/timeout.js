function hola(x,y){
    console.log(x);
}

setTimeout(hola,500,"va a explotar la bomba 💣 en:");
setTimeout(hola,1000,"5");
setTimeout(hola,2000,"4");
setTimeout(hola,3000,"3");
setTimeout(hola,4000,"2");
setTimeout(hola,5000,"1");
setTimeout(hola,5000,"boom");
setTimeout(hola,5500,"🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥");

function tictac(){
    console.log('tic');
}
let timerId = setInterval(tictac, 3000);

setTimeout(() => {clearInterval(timerId);console.log("stop");},10000);
let i = 1;
setInterval(function() {
  func(i++);
}, 100);