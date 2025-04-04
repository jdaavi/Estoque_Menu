const express = require('express');
const { Client } = require('pg');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());

const client = new Client({
    user: 'datalake_menu',
    host: 'datalake_menu.postgresql.dbaas.com.br',
    database: 'datalake_menu',
    password: 'Acesso1!',
    port: 5432,
});

client.connect();

app.get('/api/funcionarios', async (req, res) => {
    try {
        const result = await client.query('SELECT * FROM funcionarios');
        res.json(result.rows);
    } catch (error) {
        console.error('Erro ao recuperar dados:' , error);
        res.status(500).send('Erro ao recuperar dados');
    }});

app.listen(port, () => {
    console.log('Servidor rodando na porta ${port}')
});

app.get('/api/stats', async (req, res) => {
    // Lógica para buscar as contagens no banco de dados
    const unidades = await db.query('SELECT COUNT(*) FROM unidades');
    const departamentos = await db.query('SELECT COUNT(*) FROM departamentos');
    const funcionarios = await db.query('SELECT COUNT(*) FROM funcionarios');
    
    res.json({
        unidades: unidades.rows[0].count,
        departamentos: departamentos.rows[0].count,
        funcionarios: funcionarios.rows[0].count
    });
});