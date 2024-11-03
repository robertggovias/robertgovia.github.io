import java.util.ArrayList;
import java.util.List;

public class Servicio {
    // Propiedades/atributos
    private String s_nombre;
    private int valor;

    // Constructor
    public Servicio(String s_nombre, int valor) {
        this.s_nombre = s_nombre;
        this.valor = valor;
    }

    // Método para informar del precio del servicio
    public void presupuesto() {
        System.out.println("Gracias por solicitar el servicio " + s_nombre + ", el valor de ese servicio es " + valor);
    }

    // Getters para acceder a los atributos en Cliente
    public String getNombre() {
        return s_nombre;
    }

    public int getValor() {
        return valor;
    }
}

public class Cliente {
    // Propiedades/atributos
    private String nombre;
    private List<Servicio> serviciosAdquiridos;

    // Constructor
    public Cliente(String nombre) {
        this.nombre = nombre;
        this.serviciosAdquiridos = new ArrayList<>();
    }

    // Método para añadir un servicio al cliente
    public void adquirirServicio(Servicio servicio) {
        serviciosAdquiridos.add(servicio);
    }

    // Método para mostrar los servicios adquiridos y el total
    public void mostrarServicios() {
        System.out.println("Cliente: " + nombre);
        int total = 0;
        for (Servicio servicio : serviciosAdquiridos) {
            System.out.println("Servicio: " + servicio.getNombre() + " - Valor: " + servicio.getValor());
            total += servicio.getValor();
        }
        System.out.println("Total a pagar: " + total);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creación de servicios
        Servicio servicio1 = new Servicio("Video", 1500);
        Servicio servicio2 = new Servicio("Logotipo", 1000);

        // Creación del cliente
        Cliente cliente1 = new Cliente("Raul");

        // Cliente adquiere servicios
        cliente1.adquirirServicio(servicio1);
        cliente1.adquirirServicio(servicio2);

        // Mostrar los servicios adquiridos por el cliente
        cliente1.mostrarServicios();
    }
}