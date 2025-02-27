// Função para alterar a situação do produto
function alterarSituacao() {
    // Aqui você pode incluir lógica para alterar a situação do produto
    alert("Alterar Situação (Função não implementada)");
    // Exemplo de alteração de situação (você pode customizar isso)
    // Produtos que estão em situação 'pendente' podem ser alterados para 'enviado', etc.
}

// Função para clonar o produto (simular)
function clonarCompra() {
    const idProduto = prompt("Informe o ID do produto que deseja clonar:");
    const produto = produtos.find(prod => prod.id == idProduto);
    
    if (produto) {
        // Clonar o produto
        const clonedProduto = { ...produto, id: produtos.length + 1 }; // Novo ID para o produto clonado
        produtos.push(clonedProduto); // Adiciona o clone à lista de produtos
        preencherTabela(produtos); // Atualiza a tabela com o produto clonado
        alert("Produto clonado com sucesso!");
    } else {
        alert("Produto não encontrado!");
    }
}

// Função para enviar o produto (simular)
function enviar() {
    const idProduto = prompt("Informe o ID do produto que deseja enviar:");
    const produto = produtos.find(prod => prod.id == idProduto);

    if (produto) {
        // Aqui você pode marcar o produto como 'enviado' ou realizar outras ações
        alert("Produto enviado (Função não implementada)");
        // Exemplo: Altera a situação do produto para 'enviado'
        produto.situacao = 'Enviado';
        preencherTabela(produtos); // Atualiza a tabela com a nova situação
    } else {
        alert("Produto não encontrado!");
    }
}
