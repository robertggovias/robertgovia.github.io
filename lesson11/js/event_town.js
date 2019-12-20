var twnname, nn, t;
nn = 0;
twnname = document.getElementById('twn_name').textContent;
x = "event"
const requestURL = 'https://byui-cit230.github.io/weather/data/towndata.json';

fetch(requestURL)
  .then(function (response) {
    return response.json();
  })
  .then(function (jsonObject) {
    const towns = jsonObject['towns'];    
    for (let i = 0; i < towns.length; i++) {
      if (towns[i].name == twnname) {
        document.getElementById("myname").textContent = towns[i].name;
        for (let z = 0; z < towns[i].events.length; z++) {
          d = x + z;
          console.log(d);
          document.getElementById(d).innerHTML = towns[i].events[z];

          nn += 1;
        }


      }
    }
  });