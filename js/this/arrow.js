let arco = {
    colorsote: "Amarillo",
    digalo() {
        let flecha = () => console.log(this.colorsote);
        flecha();
    }
};

arco.digalo();