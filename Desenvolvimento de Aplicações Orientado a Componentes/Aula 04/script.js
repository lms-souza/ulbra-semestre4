// Função para criar um objeto com os dados do formulário
function criarObjetoContato(nome, email, telefone) {
    return {
        nome: nome,
        email: email,
        telefone: telefone
    };
}

// Função para exibir os dados do objeto na tabela
function exibirObjetoContato(objeto) {
    // Selecionar a linha da tabela
    var linha = document.getElementById("linha-contato");
    // Limpar a linha
    linha.innerHTML = "";
    // Criar as células da linha com os dados do objeto
    for (var propriedade in objeto) {
        var celula = document.createElement("td");
        celula.textContent = objeto[propriedade];
        linha.appendChild(celula);
    }
    // Exibir a tabela
    document.getElementById("tabela-contato").style.display = "block";
}

// Selecionar o formulário
var form = document.getElementById("form-contato");
// Adicionar um evento de submit ao formulário
form.addEventListener("submit", function (event) {
    // Evitar o comportamento padrão do formulário (recarregar a página)
    event.preventDefault();
    // Obter os valores dos campos do formulário
    var nome = form.elements.nome.value;
    var email = form.elements.email.value;
    var telefone = form.elements.telefone.value;
    // Criar um objeto com os dados do formulário
    var objeto = criarObjetoContato(nome, email, telefone);
    // Exibir o objeto na tabela
    exibirObjetoContato(objeto);
});

// Função para mostrar uma página e esconder as outras
function mostrarPagina(id) {
    // Selecionar todas as páginas
    var paginas = document.getElementsByClassName("page");
    // Percorrer as páginas
    for (var i = 0; i < paginas.length; i++) {
        // Verificar se o id da página é igual ao id passado como parâmetro
        if (paginas[i].id == id) {
            // Mostrar a página
            paginas[i].style.display = "block";
        } else {
            // Esconder a página
            paginas[i].style.display = "none";
        }
    }
}

// Função para obter o id da página a partir do hash da URL
function obterIdPagina() {
    // Obter o hash da URL (parte depois do #)
    var hash = window.location.hash;
    // Remover o # do hash
    var id = hash.substring(1);
    // Retornar o id
    return id;
}

// Função para atualizar a página de acordo com o hash da URL
function atualizarPagina() {
    // Obter o id da página a partir do hash da URL
    var id = obterIdPagina();
    // Verificar se o id é válido
    if (id) {
        // Mostrar a página correspondente ao id
        mostrarPagina(id);
    } else {
        // Mostrar a página inicial (home)
        mostrarPagina("home");
    }
}

// Adicionar um evento de hashchange à janela
window.addEventListener("hashchange", function () {
    // Atualizar a página quando o hash da URL mudar
    atualizarPagina();
});

// Atualizar a página quando a janela carregar
window.addEventListener("load", function () {
    atualizarPagina();
});
