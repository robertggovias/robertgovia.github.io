let user = {
    name: "Robert",
    age: 42    
};

//Aqui ves como le this es lo mismo que decir user
// = function
user.diHola = function(){
    console.log("Hola " + this.name)
};

console.log(user.name);
user.diHola();
//function
function aDios(){
    console.log("Adios " + user.name)
};


user.aDios = aDios;

user.aDios();

