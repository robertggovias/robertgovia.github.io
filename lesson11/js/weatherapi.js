var iidd, iid, twnname, twnname0, twnname1, twnname2, twnnamel, preston, soda, haven, http, unitapk, ic, n, nnn, t, icp, j, k, mic, mn, mt;
http = "https://api.openweathermap.org/data/2.5/"
unitapk = "&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845"
twnname = document.getElementById('twn_name').textContent;

preston = 5604473;
soda = 5607916;
haven = 5585010;
twnnamel = ["Preston","Soda Spring","Fish Haven"];

switch (twnname) {
  case twnnamel[0]:
    iid = preston;
    break;
  case twnnamel[1]:
    iid = soda;
    break;
  case twnnamel[2]:
    iid = haven;
}

document.getElementById("testing").innerHTML = iid;
var apiURL = http+"weather?id="+iid+unitapk;
fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    document.getElementById('current-temp').textContent = jsObject.main.temp;
    document.getElementById('current').textContent = jsObject.weather[0].description;
    document.getElementById('humid').textContent = jsObject.main.humidity;
    document.getElementById('wind').textContent = jsObject.wind.speed;
  });

const  apifiveURL = http+"forecast?id="+iid+unitapk;
n = 0;
ic = [];
t = [];
icp = [];
fetch(apifiveURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
    for (let i = 0; i < jsObject.list.length; i++) {
      if (jsObject.list[i].dt_txt.includes('18:00:00')) {
        t[n] = jsObject.list[i].main.temp.toFixed(0);
        k = "t" + n;
        document.getElementById(k).textContent = t[n];
        ic[n] = jsObject.list[i].weather[0].icon;
        icp[n] = "https://openweathermap.org/img/w/" + ic[n] + ".png";
        j = "i" + n;
        document.getElementById(j).setAttribute('src', icp[n]);
        n += 1;
      }
    }


  });