# Sistema de Gerenciamento de Agenda

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completo-green.svg)

Um sistema CRUD completo para gerenciamento de agenda pessoais desenvolvido em Python.

## Funcionalidades

- ✅ Cadastro de novos contatos com ID automático
- 📋 Listagem completa de todos os contatos
- ✏️ Atualização de contatos (dados individuais ou todos)
- ❌ Exclusão de contatos
- 🔍 Busca por ID para edição/exclusão
- 🛡️ Validação de entradas

## Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/LuanGabrielDEV/CRUD_Gerenciamento_De_Agenda.git
```
2. Execute o programa:
```bash
python CadastroCliente.py
```
3. Use o menu interativo:

```bash
------- MENU PRINCIPAL -------
1 - Cadastrar contato
2 - Listar contatos
3 - Atualizar contato
4 - Excluir contato
5 - Sair
```

## Estrutura do Código
- **Contatos**: Lista de dicionários armazenando todos os contatos

- **id_generator**: Gerador automático de IDs usando itertools.count

- **Menu principal** com tratamento de opções inválidas

- **Submenu** para edição com opções específicas

## Pré-requisitos
Python 3.8 ou superior

Nenhuma dependência externa necessária

## Melhorias Futuras
Persistência em arquivo (JSON)

Busca por nome/telefone/email

Exportação/importação de contatos

Interface gráfica (Tkinter)

### Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
