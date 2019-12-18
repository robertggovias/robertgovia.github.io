
const apiURL = 'https://api.openweathermap.org/data/2.5/weather?id=5604473&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845';

fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    document.getElementById('current-temp').textContent = jsObject.main.temp;
    document.getElementById('current').textContent = jsObject.weather[0].description;
    document.getElementById('humid').textContent = jsObject.main.humidity;
    document.getElementById('wind').textContent = jsObject.wind.speed;
    //icons

   
  });
  
  //5 daays temperature
  const apifiveURL = 'https://api.openweathermap.org/data/2.5/forecast?id=5604473&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845';
var ic, n, t, count,icp,j,k, mic, mn, mt, count,icp,j,k;
n=0;
ic=[];
t=[];
icp=[];
fetch(apifiveURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    for (let i = 0; i < jsObject.list.length; i++) {      
      if (jsObject.list[i].dt_txt.includes('18:00:00')) {
        t[n]= jsObject.list[i].main.temp.toFixed(0);        
        k="t"+n;
        document.getElementById(k).textContent = t[n];       
        ic[n]= jsObject.list[i].weather[0].icon;        
        icp[n]= "https://openweathermap.org/img/w/" + ic[n] + ".png";        
        j="i"+n;
        document.getElementById(j).setAttribute('src', icp[n]);
        n+=1;
        }
    }
    
    
  });
  
 
  