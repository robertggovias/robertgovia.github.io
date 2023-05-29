 let idade = 26
 let tenhoCNH = true
 console.clear()
 const possoDirigir = idade >= 18 && tenhoCNH === true

 console.log("Posso dirigir?", possoDirigir)

 const votoFacultativo = idade <= 18 || idade >= 70

 console.log("Tienes voto facultativo:?", votoFacultativo)
