function windchill(t, s){
    return 35.74 + (0.6215 * t) - (35.75 *(s**0.16)) + (0.4275 * t * (s ** 0.16));
}
var t1, s1;
    t1= document.getElementById("current-temp").innerHTML;
    s1 = document.getElementById("wind").innerHTML;  
    w1 = windchill(t1,s1);
    document.getElementById("chill").innerHTML = w1.toFixed(0);