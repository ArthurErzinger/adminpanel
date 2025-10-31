import mysql.connector

def add(nome, valor, quantidade_atual, quantidade_minima):
    """
    Adiciona um novo produto e seu estoque correspondente no banco de dados.
    """
    conexao = mysql.connector.connect(
        user='root', 
        password='PUC@1234', 
        host='localhost', 
        database='neocommercedb'
    )
    cursor = conexao.cursor()

    try:
        # Inserir na tabela produto
        query_produto = "INSERT INTO produto (Nome, Valor) VALUES (%s, %s)"
        cursor.execute(query_produto, (nome, valor))
        id_produto = cursor.lastrowid  # Pega o ID do produto recém-inserido

        # Inserir na tabela estoque
        query_estoque = "INSERT INTO estoque (fk_Produto_Id_produto, quantidade_atual, quantidade_minima) VALUES (%s, %s, %s)"
        cursor.execute(query_estoque, (id_produto, quantidade_atual, quantidade_minima))

        conexao.commit()
        print(f"Produto '{nome}' adicionado com sucesso com o ID {id_produto}.")
        return True

    except mysql.connector.Error as erro:
        print(f"Erro ao adicionar produto: {erro}")
        conexao.rollback()
        return False

    finally:
        cursor.close()
        conexao.close()
