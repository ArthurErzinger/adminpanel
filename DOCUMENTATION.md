# Documentação do Projeto: Painel de Administração de Estoque

Este documento detalha a estrutura e o funcionamento de cada componente do projeto de painel de administração, uma aplicação de desktop para operações de CRUD (Criar, Ler, Atualizar, Deletar) em um banco de dados de produtos.

## Arquitetura Geral

O projeto é dividido em duas camadas principais:

1.  **Camada de Interface Gráfica (`gui/`)**: Responsável por toda a interação com o usuário. Construída com a biblioteca `tkinter`.
2.  **Camada de Lógica de Negócio (`functions/`)**: Contém as funções que se comunicam diretamente com o banco de dados MySQL para executar as operações de CRUD.

---

## Componentes Principais

### `main.py`

-   **Função**: Ponto de entrada da aplicação.
-   **Funcionamento**: Este script inicializa a janela principal do `tkinter`, instancia a classe `AppEstoque` (a tela principal da aplicação) e inicia o loop de eventos da interface gráfica, que mantém a janela aberta e responsiva às ações do usuário.

---

### Camada de Interface Gráfica (`gui/`)

Esta camada gerencia a apresentação visual e a captura de inputs do usuário.

#### `gui/ui_main.py`

-   **Função**: Define a janela principal da aplicação.
-   **Funcionamento**:
    -   A classe `AppEstoque` constrói a interface principal, que inclui uma tabela (`Treeview`) para listar os produtos e os botões principais para as ações de CRUD.
    -   `criar_tabela()`: Monta a tabela que exibe os dados dos produtos, incluindo colunas e barras de rolagem.
    -   `atualizar_lista()`: Limpa a tabela e a recarrega com os dados mais recentes do banco de dados, chamando a função `read()` de `functions/atualizar_join.py`. É chamada na inicialização e sempre que uma operação de CRUD é concluída com sucesso.
    -   `criar_botoes_principais()`: Cria os botões "Atualizar Lista", "Adicionar Produto", "Atualizar Quantidade" e "Deletar Produto".
    -   `abrir_adicionar()`, `abrir_atualizar()`, `abrir_deletar()`: Estes métodos são chamados quando os respectivos botões são clicados. Eles limpam a área de operações e instanciam os frames correspondentes (`FrameAdicionar`, `FrameAtualizar`, `FrameDeletar`), passando a função `atualizar_lista` como callback.

#### `gui/adicionar.py`

-   **Função**: Define o formulário para adicionar um novo produto.
-   **Funcionamento**:
    -   A classe `FrameAdicionar` cria um formulário com campos de entrada para o nome, valor, quantidade atual e quantidade mínima do produto.
    -   O método `adicionar_produto()` é chamado quando o botão "Salvar Produto" é clicado.
    -   Ele coleta os dados dos campos, faz a validação para garantir que todos os campos estão preenchidos e que os valores numéricos são válidos.
    -   Chama a função `add()` de `functions/adicionar_produto.py` para inserir os dados no banco.
    -   Exibe uma mensagem de sucesso ou erro e, em caso de sucesso, executa o `callback` (`atualizar_lista`) para atualizar a tabela na tela principal.

#### `gui/atualizar.py`

-   **Função**: Define o formulário para atualizar a quantidade de um produto.
-   **Funcionamento**:
    -   A classe `FrameAtualizar` cria um formulário com campos para o ID do produto e a nova quantidade.
    -   O método `atualizar_quantidade()` coleta os dados, valida se são números inteiros e chama a função `update()` de `functions/atualizar_quantidade.py`.
    -   Exibe uma mensagem de status e executa o `callback` em caso de sucesso.

#### `gui/deletar.py`

-   **Função**: Define o formulário para deletar um produto.
-   **Funcionamento**:
    -   A classe `FrameDeletar` cria um campo para inserir o ID do produto a ser deletado.
    -   O método `deletar_produto()` pega o ID, chama a função `delete()` de `functions/deletar_produto.py` e executa o `callback` para atualizar a lista.

---

### Camada de Lógica de Negócio (`functions/`)

Esta camada lida diretamente com as queries do banco de dados.

#### `functions/atualizar_join.py`

-   **Função**: `read()`
-   **Funcionamento**: Conecta-se ao banco de dados e executa uma query `SELECT` com `JOIN` entre as tabelas `produto` e `estoque` para buscar a lista completa de todos os produtos e seus respectivos dados de estoque. Retorna uma lista de dicionários, onde cada dicionário representa um produto.

#### `functions/adicionar_produto.py`

-   **Função**: `add(nome, valor, quantidade_atual, quantidade_minima)`
-   **Funcionamento**:
    1.  Insere um novo registro na tabela `produto` com o nome e o valor.
    2.  Usa `cursor.lastrowid` para obter o `Id_produto` que acabou de ser gerado.
    3.  Insere um novo registro na tabela `estoque` com as quantidades e o `Id_produto` como chave estrangeira.
    4.  Executa um `commit` para salvar as duas inserções como uma transação única. Em caso de erro, executa `rollback`.

#### `functions/atualizar_quantidade.py`

-   **Função**: `update(id_produto, nova_quantidade)`
-   **Funcionamento**: Executa uma query `UPDATE` na tabela `estoque` para atualizar a `quantidade_atual` de um produto específico, identificado pelo `fk_Produto_Id_produto`.

#### `functions/deletar_produto.py`

-   **Função**: `delete(id)`
-   **Funcionamento**: Executa uma query `DELETE` na tabela `produto` para remover o produto com o `Id_produto` fornecido. Se o banco de dados estiver configurado com `ON DELETE CASCADE`, o registro correspondente na tabela `estoque` (e em outras tabelas dependentes) será removido automaticamente.
