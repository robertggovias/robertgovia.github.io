let user = {
    nombre: "Robert",
    edad: 42,

    holaAmigo(){
        console.log("Hola " + this.nombre + " como estás amigo")
    },    

    estasViejo() {        
        console.log(this.nombre + " ya no eres joven, tienes " + this.edad)
    }};

user.holaAmigo();
user.estasViejo();
