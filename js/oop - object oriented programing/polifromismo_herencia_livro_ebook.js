class Libro {
    constructor(titulo, autor, precio) {
        this.titulo = titulo;
        this.autor = autor;
        this._precio = precio;
    }

    get precio() {
        return this._precio;
    }

    set precio(nuevoPrecio) {
        if (nuevoPrecio > 0) {
            this._precio = nuevoPrecio;
        } else {
            console.log("Nada de precios negativos.");
        }
    }

    descontar(descuento) {
        if (descuento > 0) {
            this._precio -= descuento;
        } else {
            console.log("El descuento debe ser un valor positivo.");
        }
    }
    mostrarInformacion() {
        console.log(`Título: ${this.titulo}, Autor: ${this.autor}, Precio: ${this.precio}`);
    }
}

// Clase Ebook que hereda de Libro
class Ebook extends Libro {
    constructor(titulo, autor, precio, formato) {
        super(titulo, autor, precio); // Llama al constructor de la clase padre
        this.formato = formato; // Propiedad específica de Ebook
    }

    // Método adicional para mostrar información del Ebook
    mostrarInformacion() {
        console.log(`Título: ${this.titulo}, Autor: ${this.autor}, Precio: ${this.precio}, Formato: ${this.formato}`);
    }
}

const libro1 = new Libro("El perdón", "Boid K, Packer", 45);
libro1.mostrarInformacion();

const ebook1 = new Ebook("El perdón", "Boid K, Packer", 30, "PDF");
ebook1.mostrarInformacion();