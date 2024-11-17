const nombre = "Hiram"
console.log(`Hola, ${nombre}
    Línea 2`);

function saludo(palabras,nombre){
    return `${palabras[0]}${nombre.toUpperCase()} meu amigo querido!`;
}
console.log(saludo`Hola, e ahi, ${"Hiram"}`);

function tarjetaProducto(producto){
    return `<div>
    <h2></h2>
    `
}