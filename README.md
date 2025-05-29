# CRUD com Interface Gráfica

Este é um projeto de sistema de gerenciamento de clientes e pedidos com uma interface gráfica intuitiva e responsiva desenvolvida em Python utilizando a biblioteca Tkinter.

## Funcionalidades

* Cadastro, edição e exclusão de clientes
* Cadastro, edição e exclusão de pedidos
* Interface com abas separadas para Clientes e Pedidos
* Combobox para seleção de clientes ao criar pedidos
* Estilização personalizada com `ttk.Style`

## Estrutura do Projeto

```
crud-com-interface/
├── main.py            # Ponto de entrada da aplicação
├── gui.py             # Interface gráfica com Tkinter
├── database.py        # Simulação de um banco de dados em memória
├── README.md
```

## Requisitos

* Python 3.x

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/gustavolimaf/crud-com-interface.git
   cd crud-com-interface
   ```

2. Execute o projeto:

   ```bash
   python main.py
   ```

## Futuras Melhorias

* Integração com banco de dados real (ex: SQLite ou PostgreSQL)
* Exportação de relatórios em PDF ou Excel
* Sistema de autenticação de usuários
* Validações mais robustas e mensagens de erro detalhadas

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

## Autor

Desenvolvido por [Gustavo Lima](https://github.com/gustavolimaf)
