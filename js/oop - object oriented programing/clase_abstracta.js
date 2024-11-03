//Supongamos que queremos una clase abstracta Publicacion que sirva como base para Libro, Revista, y Ebook. Queremos que todas las publicaciones tengan un método llamado detalles, pero cada clase implementará este método a su manera.
class Publicacion {
    constructor(titulo, autor, precio) {
        if (this.constructor === Publicacion) {
            throw new Error("No se puede instanciar una clase abstracta");
        }
        this.titulo = titulo;
        this.autor = autor;
        this.precio = precio;
    }

    // Método abstracto
    detalles() {
        throw new Error("Este método debe ser implementado en la subclase");
    }
}

//Aquí, Publicacion actúa como una clase abstracta. La idea es que cada subclase (Libro, Revista, Ebook) implemente su propio método detalles.
//Implementación en Subclases
//Ahora, las clases Libro, Revista, y Ebook extenderán Publicacion e implementarán detalles.

class Libro extends Publicacion {
    detalles() {
        console.log(`Título: ${this.titulo}, Autor: ${this.autor}, Precio: ${this.precio}`);
    }
}

class Revista extends Publicacion {
    constructor(titulo, autor, precio, numeroEdicion) {
        super(titulo, autor, precio);
        this.numeroEdicion = numeroEdicion;
    }

    detalles() {
        console.log(`Título: ${this.titulo}, Autor: ${this.autor}, Precio: ${this.precio}, Número de edición: ${this.numeroEdicion}`);
    }
}

class Ebook extends Publicacion {
    constructor(titulo, autor, precio, formato) {
        super(titulo, autor, precio);
        this.formato = formato;
    }

    detalles() {
        console.log(`Título: ${this.titulo}, Autor: ${this.autor}, Precio: ${this.precio}, Formato: ${this.formato}`);
    }
}

const ebook1 = new Ebook("cascada","pedrito",34,"pdf")
ebook1.detalles();