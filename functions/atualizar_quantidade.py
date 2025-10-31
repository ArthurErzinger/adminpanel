import mysql.connector

def update(id_produto, nova_quantidade):
    """
    Atualiza a quantidade de um produto no estoque.
    """
    conexao = mysql.connector.connect(
        user='root', 
        password='PUC@1234', 
        host='localhost', 
        database='neocommercedb'
    )
    cursor = conexao.cursor()

    try:
        query = "UPDATE estoque SET quantidade_atual = %s WHERE fk_Produto_Id_produto = %s"
        cursor.execute(query, (nova_quantidade, id_produto))
        conexao.commit()
        print(f"Estoque do produto com ID {id_produto} atualizado para {nova_quantidade}.")
        return True
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar estoque: {erro}")
        conexao.rollback()
        return False
    finally:
        cursor.close()
        conexao.close()
