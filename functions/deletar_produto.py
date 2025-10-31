import mysql.connector

def delete(id):

    conexao = mysql.connector.connect(user='root', password='PUC@1234', host='localhost', database='neocommercedb')

    cursor = conexao.cursor(dictionary=True)

    query = "DELETE FROM produto WHERE Id_produto = %s"
    cursor.execute(query, (id,))
    conexao.commit()



    conexao.close()


    return None