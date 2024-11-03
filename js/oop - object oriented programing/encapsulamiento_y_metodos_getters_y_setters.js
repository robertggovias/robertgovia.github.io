class Producto {
    constructor(nombre, precio) {
        this._nombre = nombre;
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
            console.log("El precio debe ser positivo.");
        }
    }
}

const producto1 = new Producto("Laptop", 800);
console.log(producto1.precio);  // Obtiene el precio: 800
producto1.precio = 900;         // Cambia el precio
console.log(producto1.precio);  // Obtiene el precio: 800