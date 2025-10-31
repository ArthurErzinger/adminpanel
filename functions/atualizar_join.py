import mysql.connector

def read():

    conexao = mysql.connector.connect(user='root', password='PUC@1234', host='localhost', database='neocommercedb')

    cursor = conexao.cursor(dictionary=True)

    query = ("""
            SELECT p.Id_produto, \
                   p.Nome, \
                   p.Valor, \
                   e.quantidade_atual, \
                   e.quantidade_minima
            FROM produto p
                     JOIN estoque e ON p.Id_produto = e.fk_Produto_Id_produto; \
            """)

    cursor.execute(query)

    resultados = cursor.fetchall()

    conexao.close()

    # for linha in resultados:
    #     print(linha)


    return resultados

    # for linha in resultados:
    #     print(linha["Id_cliente"])