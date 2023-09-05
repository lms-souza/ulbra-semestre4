const data = [
    {id:1, nome:"Daniel", idade: 25},
    {id:2, nome:"Mateus", idade: 26},
    {id:3, nome:"Leo", idade: 19},
    {id:4, nome:"Paulo", idade: 50},
    {id:5, nome:"Chicao", idade: 21},
    {id:6, nome:"Felipe", idade: 20}
]

function initialize(){
    
    const minhaLista = document.getElementById("minhaLista")
    
    minhaLista.innerHTML =  MinhaListaDePessoasComponente(data)
    
    mostrarPessoaPorId(2);
    
}


function MinhaListaDePessoasComponente(data){
    return data.map(item =>{
        console.log(item)
        return(
            `<li>ID:${item.id}      Nome:    ${item.nome}    Idade:      ${item.idade} anos </li>`
        )
        //implementação do que a função vai fazer
    }).join("")
    
}

function mostrarPessoaPorId(id) {
    const pessoa = data.find(item => item.id === id);
    const pessoaId = document.getElementById("pessoaId");

    if (pessoa) {
        pessoaId.innerHTML = `<li>ID:${pessoa.id} Nome: ${pessoa.nome} Idade: ${pessoa.idade} anos</li>`;
    } else {
        pessoaId.innerHTML = `<li>ID de pessoa não encontrado.</li>`;
    }
}
