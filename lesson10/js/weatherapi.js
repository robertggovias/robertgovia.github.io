
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
var ic, n, t, count;
n=0;
ic=[];
t=[];
count=[];

fetch(apifiveURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    for (let i = 0; i < jsObject.list.length; i++) {
      document.getElementById("t3").innerHTML = i;
      if (jsObject.list[i].dt_txt.includes('18:00:00')) {
        t += jsObject.list[i].main.temp;
        document.getElementById("t0").innerHTML = t[0]+t[1]+t[2]+t[3];
        document.getElementById("t1").innerHTML = t[5]+t[6]+t[7]+t[8];
        document.getElementById("t2").innerHTML = t[10]+t[11]+t[12]+t[13];
        document.getElementById("t3").innerHTML = t[15]+t[16]+t[17]+t[18];
        document.getElementById("t4").innerHTML = t[20]+t[21]+t[22]+t[19]; 
        ic[n]= jsObject.list[i].weather[0].icon;
        count[n]=n;
        n+=1;
        
        document.getElementById("i0").innerHTML = ic[0];
        document.getElementById("i1").innerHTML = ic[1];
        document.getElementById("i2").innerHTML = ic[2];
        document.getElementById("i3").innerHTML = ic[3];
        document.getElementById("i4").innerHTML = ic[4];
        }
    }
    

  });
 
  