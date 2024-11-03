class Persona {
    constructor(nombre, edad) {
        this.nombre = nombre;
        this.edad = edad;
    }

    // Método para presentar a la persona
    presentarse() {
        return `Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`;
    }
}

const persona1 = new Persona("Ana", 25);
console.log(persona1.presentarse());  // "Hola, mi nombre es Ana y tengo 25 años."