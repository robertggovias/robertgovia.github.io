let calculator = {    
    a: 0,
    b: 0,       

    read() {
        this.a = parseFloat(document.getElementById('inputA').value);
        this.b = parseFloat(document.getElementById('inputB').value);
        document.getElementById('result').textContent = "Valores leídos.";
    },
    sum() {
        return this.a + this.b;
    },
    mul() {
        return this.a * this.b;
    },
    showSum() {
        const result = this.sum();
        document.getElementById('result').textContent = "Suma: " + result;
    },
    showMul() {
        const result = this.mul();
        document.getElementById('result').textContent = "Multiplicación: " + result;
    }
};

//calculator.read();
//console.log(calculator.sum());
//console.log(calculator.mul());