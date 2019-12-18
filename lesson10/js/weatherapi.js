
const apiURL = 'https://api.openweathermap.org/data/2.5/weather?id=5604473&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845';

fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    document.getElementById('current-temp').textContent = jsObject.main.temp;
    document.getElementById('current').textContent = jsObject.weather[0].description;
    document.getElementById('humid').textContent = jsObject.main.humidity;
    document.getElementById('wind').textContent = jsObject.wind.speed;
    //icons

    const imagesrc = 'https://openweathermap.org/img/w/' + jsObject.weather[0].icon + '.png';  // note the concatenation
const desc = jsObject.weather[0].description;  // note how we reference the weather array
//document.getElementById('imagesrc').textContent = imagesrc;  // informational specification only
document.getElementById('icon').setAttribute('src', imagesrc);  // focus on the setAttribute() method
document.getElementById('icon').setAttribute('alt', desc);
  });
  
  //5 daays temperature
  const apifiveURL = 'https://api.openweathermap.org/data/2.5/forecast?id=5604473&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845';
var dtemp=["hola","amigo"];
var t=[];

fetch(apifiveURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    for (let i = 0; i < jsObject.list.length; i++) {
      document.getElementById("t3").innerHTML = i;
      if (jsObject.list[i].dt_txt.includes('18:00:00')) {
        t += jsObject.list[i].main.temp;
        document.getElementById("t0").innerHTML = t[0]+t[1];
        document.getElementById("t1").innerHTML = t[5]+t[6];
        document.getElementById("t2").innerHTML = t[10]+t[11];
        document.getElementById("t3").innerHTML = t[15]+t[16];
        document.getElementById("t4").innerHTML = t[20]+t[21];        
              }
    }
    

  });
 
  