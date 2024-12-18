console.log("solicitando datos");
console.log("recibidos");

// URL de la API de PokeAPI para el Pokémon Ditto

const urlPoke = 'https://pokeapi.co/api/v2/pokemon/';
/* //promise style
const pepito = fetch(urlPoke);


console.log('Se creo la promesa', pepito instanceof Promise);


pepito
    .then(response => {
        //console.log('Llegó perfecto', response);
        return response.json();
    })
    .then(data => {
        console.log(data);
        console.log("me llamo", data.name, ", y peso ", data.weight)
    
    }
    )
//Verificamos si la respuesta se creo correctamente
console.log('Se creo la promesa', promise instanceof Promise);

promise
    .then(response => {
        console.log('Llegó perfecto', response);
        return response.json();
    })
    .then(data => {
        console.log('Json baby', data);
    }) */

//async solo funciona con funciones
let results = null;

async function gettingPokemon(urlPoke) {
    const response = await fetch (urlPoke);
    if (response.ok) {
        const data = await response.json();
        doStuff(data);
    }
}
function doStuff(data) {
    results = data;
    console.log('first: ', results);
    results.results.forEach((pokemon) => {
      const div = document.createElement('div');
      div.textContent = pokemon.name;
      document.querySelector('main').appendChild(div);
        // assumes you have a <main> element in your HTML document
    });
  }
   




gettingPokemon(urlPoke);
console.log("second: ", results);


//const pokemons = document.getElementById("pokemons");
/* for (var i=0; i < 20; i++) {
    pokemons.innerHTML = pokemons.innerHTML + '<select value="' + results[i]['name']> + '</select>';
} */
