class Servicio {
    constructor(nombre, valor) {
        this.nombre = nombre;
        this.valor = valor;
    }
}

class Cliente {
    constructor(nombre) {
        this.nombre = nombre;
        this.servicios = [];
    }

    agregarServicio(servicio) {
        this.servicios.push(servicio);
    }

    mostrarServicios() {
        return this.servicios.map(servicio => `${servicio.nombre}: $${servicio.valor}`).join(', ');
    }
}

// Ejemplo de uso
const cliente1 = new Cliente("Raul");
cliente1.agregarServicio(new Servicio("Video", 1500));
cliente1.agregarServicio(new Servicio("Logotipo", 1000));

// Exportar para que pueda usarse en el HTML
window.cliente1 = cliente1;