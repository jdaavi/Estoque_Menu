// Exemplo de movimentações, normalmente você puxaria isso do back-end
let movimentacoes = [
    { data: '2025-02-01', tipo: 'Entrada', valor: 500.00 },
    { data: '2025-02-02', tipo: 'Saída', valor: 200.00 },
    { data: '2025-02-03', tipo: 'Entrada', valor: 300.00 }
];

// Função para atualizar as movimentações e o total
function atualizarMovimentacoes() {
    const tableBody = document.querySelector('#movimentacoes tbody');
    let totalEntrada = 0;
    let totalSaida = 0;

    // Limpar a tabela de movimentações
    tableBody.innerHTML = '';

    // Adicionar cada movimentação
    movimentacoes.forEach(movimentacao => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${movimentacao.data}</td>
            <td>${movimentacao.tipo}</td>
            <td>R$ ${movimentacao.valor.toFixed(2)}</td>
            <td><button onclick="deletarMovimentacao('${movimentacao.data}')">Deletar</button></td>
        `;
        tableBody.appendChild(row);

        // Atualizar os totais
        if (movimentacao.tipo === 'Entrada') {
            totalEntrada += movimentacao.valor;
        } else if (movimentacao.tipo === 'Saída') {
            totalSaida += movimentacao.valor;
        }
    });

    // Atualizar os valores de Entrada, Saída e Total
    document.getElementById('entradas').innerText = `R$ ${totalEntrada.toFixed(2)}`;
    document.getElementById('saidas').innerText = `R$ ${totalSaida.toFixed(2)}`;
    document.getElementById('total').innerText = `R$ ${(totalEntrada - totalSaida).toFixed(2)}`;
}

// Função para deletar movimentações
function deletarMovimentacao(data) {
    movimentacoes = movimentacoes.filter(m => m.data !== data);
    atualizarMovimentacoes();
}

// Inicializar a página com os dados
atualizarMovimentacoes();
