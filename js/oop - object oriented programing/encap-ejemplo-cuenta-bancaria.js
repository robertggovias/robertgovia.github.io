class CuentaBancaria {
    constructor(titular, saldo) {
        this.titular = titular;
        this._saldo = saldo;
    }

    // Método para consultar el saldo
    get saldo() {
        return this._saldo;
    }

    // Método para depositar
    depositar(cantidad) {
        if (cantidad > 0) {
            this._saldo += cantidad;
            console.log(`Depósito exitoso: $${cantidad}`);
        } else {
            console.log("La cantidad a depositar debe ser positiva.");
        }
    }

    // Método para retirar
    retirar(cantidad) {
        if (cantidad > 0 && cantidad <= this._saldo) {
            this._saldo -= cantidad;
            console.log(`Retiro exitoso: $${cantidad}`);
        } else {
            console.log("Fondos insuficientes o cantidad inválida.");
        }
    }
}

const cuenta1 = new CuentaBancaria("Raul", 500);
console.log(cuenta1.saldo);  // Consulta el saldo actual: 500
cuenta1.depositar(200);      // Depósito exitoso
cuenta1.retirar(100);        // Retiro exitoso
console.log(cuenta1.saldo);  // Consulta el saldo actual: 600
cuenta1.depositar(56700);      // Depósito exitoso
console.log(cuenta1.saldo);  // Consulta el saldo actual: 600