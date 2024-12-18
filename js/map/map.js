let listaDePessoasAprovadas = [
    'robert@gmail.com' ,
    'hiram@gmail.com' ,
    'esther@gmail.com' ,
    'pepito@gmail.com' ,
];



let listaDeEmails;

listaDeEmails = listaDePessoasAprovadas.map((obrigado) => {
    return { email : obrigado , nota: 10 };
     
} );

console.log(listaDeEmails)

//enviar email depende de utilizar el map e modifca algunos detalle

const enviarRata = (rata) => {
    console.log(`Email para ${rata.email} con a nota ${rata.nota} enviado com sucesso`)
};

//lo hacemos con for each

listaDeEmails.forEach((rataw) => enviarRata (rataw));