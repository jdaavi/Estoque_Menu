document.getElementById('unidades').addEventListener('click', function() {
    showForm('unidades');
});
document.getElementById('departamentos').addEventListener('click', function() {
    showForm('departamentos');
});
document.getElementById('funcionarios').addEventListener('click', function() {
    showForm('funcionarios');
});

function showForm(section) {
    let formArea = document.getElementById('form-area');
    let htmlContent = '';

    switch(section) {
        case 'unidades':
            htmlContent = `
                <h3>Cadastrar Unidade</h3>
                <form id="unidade-form">
                    <label for="unidade-name">Nome da Unidade</label>
                    <input type="text" id="unidade-name" placeholder="Digite o nome da unidade" required />
                    <button type="submit">Cadastrar</button>
                </form>
            `;
            break;
        case 'departamentos':
            htmlContent = `
                <h3>Cadastrar Departamento</h3>
                <form id="departamento-form">
                    <label for="departamento-name">Nome do Departamento</label>
                    <input type="text" id="departamento-name" placeholder="Digite o nome do departamento" required />
                    <button type="submit">Cadastrar</button>
                </form>
            `;
            break;
        case 'funcionarios':
            htmlContent = `
                <h3>Cadastrar Funcionário</h3>
                <form id="funcionario-form">
                    <label for="funcionario-nome">Nome do Funcionário</label>
                    <input type="text" id="funcionario-nome" placeholder="Digite o nome do funcionário" required />
                    <label for="funcionario-cargo">Cargo</label>
                    <input type="text" id="funcionario-cargo" placeholder="Digite o cargo do funcionário" required />
                    <label for="funcionario-matricula">Matrícula</label>
                    <input type="text" id="funcionario-matricula" placeholder="Digite a matrícula" required />
                    <button type="submit">Cadastrar</button>
                </form>
            `;
            break;
    }

    formArea.innerHTML = htmlContent;
}

// Simulação de dados (contagem de unidades, departamentos e funcionários)
document.getElementById('unidades-count').innerText = '5';  // Exemplo de dados
document.getElementById('departamentos-count').innerText = '3';
document.getElementById('funcionarios-count').innerText = '20';
