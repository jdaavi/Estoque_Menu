// transferencia.js
document.getElementById('formTransferencia').addEventListener('submit', function(event) {
    event.preventDefault(); // Previne o envio do formulário

    const tipo = document.getElementById('tipoTransferencia').value;
    const valor = document.getElementById('valor').value;
    const conta = document.getElementById('conta').value;
    const data = document.getElementById('data').value;

    // Exibir um alerta (ou enviar para um banco de dados, etc)
    alert(`Transferência ${tipo} realizada!\nValor: R$${valor}\nConta: ${conta}\nData: ${data}`);

    // Redirecionar para a página de finanças ou outra página de sua escolha
    window.location.href = 'financeiro.html';
});

Document.getElementById('valor').addEventListener('input', function(e) {
    let value = e.target.value;

    value = value.replace(/[^d]/g,'');

    value = (value / 100).toFixed(2) + '';
    value = value.replace('.','.');
    value = value.replace(/(\d)(\d{3}),/, '$1.$2,');

    e.target.value = 'R$' + value;

});