const requestURL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={89bc7a863b25584dbe9c64dc38e40845}';

fconst apiURL = "...";
fetch(apiURL)
  .then((response) => response.json())
  .then((jsObject) => {
    console.log(jsObject);
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