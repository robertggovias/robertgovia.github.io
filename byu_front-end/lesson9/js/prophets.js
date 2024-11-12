const requestURL = 'https://byui-cit230.github.io/lessons/lesson-09/data/latter-day-prophets.json';

fetch('data/latter-day-prophets.json')
  .then(function (response) {
    return response.json();
  })
  .then(function (jsonObject) {
    const prophets = jsonObject['prophets'];
    // loop through every record and process them into their own 'cards' (HTML output)
  for (let i = 0; i < prophets.length; i++ ) {
    //Now we just build the HTML of the prophet card using the createElement(), textContent(), and appendChild() methods on the document. 
    let card = document.createElement('section');
    let h2 = document.createElement('h2');
    h2.textContent = prophets[i].name + ' ' + prophets[i].lastname;
    card.appendChild(h2);
    let p = document.createElement('p');
    p.innerHTML = "<h3>Date of birth:</h3>" + prophets[i].birthdate+ "<h3>Place of birth:</h3>" +prophets[i].birthplace;
    card.appendChild(p);
    let img = document.createElement('img');
    img.setAttribute('src', prophets[i].imageurl)
    img.setAttribute('alt', prophets[i].name + " "+ prophets[i].lastname)
    card.appendChild(img);
    document.querySelector('div.cards').appendChild(card);
    
}
  });