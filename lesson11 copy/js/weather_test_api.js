const apiURL = 'https://api.openweathermap.org/data/2.5/weather?id=5604473&units=imperial&APPID=89bc7a863b25584dbe9c64dc38e40845';

fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.jsObject
    document.getElementById('current-temp').textContent = jsObject.main.temp;

    //icons

    const imagesrc = 'https://openweathermap.org/img/w/' + jsObject.weather[0].icon + '.png';  // note the concatenation
const desc = jsObject.weather[0].description;  // note how we reference the weather array
document.getElementById('imagesrc').textContent = imagesrc;  // informational specification only
document.getElementById('icon').setAttribute('src', imagesrc);  // focus on the setAttribute() method
document.getElementById('icon').setAttribute('alt', desc);
  });
    // loop through every record and process them into their own 'cards' (HTML output)
  /*for (let i = 0; i < towns.length; i++ ) {      
    if(towns[i].name=="Preston" || towns[i].name=="Soda Springs" || towns[i].name=="Fish Haven"){    
    let card = document.createElement('section');
    let h2 = document.createElement('h2');
    h2.textContent = towns[i].name;
    card.appendChild(h2);
    let img = document.createElement('img');
    img.setAttribute('src', towns[i].photo)
    img.setAttribute('alt', towns[i].name)
    card.appendChild(img);
    let p = document.createElement('p');
    p.innerHTML = towns[i].motto+ "<br><b>Year Founded:</b>" +towns[i].yearFounded+"<br><b>Population: </b>" + towns[i].currentPopulation + "<br><b>Annual Rain Fall: </b>" + towns[i].averageRainfall;
    card.appendChild(p);
    
    document.querySelector('div.cards').appendChild(card);
    
}}
  });*/