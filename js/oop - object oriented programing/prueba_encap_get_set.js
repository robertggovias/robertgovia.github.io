class Libro {
    constructor(titulo, autor, precio){
        this.titulo = titulo;
        this.autor = autor;
        this._precio = precio;
    }
    // Getter
    get precio() {
        return this._precio;
    }
    // Setter
    set precio(nuevoPrecio) {
        if (nuevoPrecio > 0) {
            this._precio = nuevoPrecio;
        } else {
            console.log("nada de precios negativos. Cambia el precio a un valor positivo");
        }
    }
    //metodo descuento
    descontar(descuento) {
        if (this._precio - descuento > 0) {
            this._precio -= descuento            
            //nuevoPrecio = nuevoPrecio-descuento;
        } else {
            console.log("nada de valors negativos. Cambia a un valor positivo");
        }
    }
    
    
}
const livro1 = new Libro("El perdon",  "Boid K, Packer", 45);
console.log("Precio inicial", livro1.precio);
livro1.descontar(12)
console.log("Precio con descuento", livro1.precio);