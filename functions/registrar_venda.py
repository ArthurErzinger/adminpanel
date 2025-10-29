import mysql.connector

def list():

    conexao = mysql.connector.connect(user='root', password='PUC@1234', host='localhost', database='neocommercedb')

    cursor = conexao.cursor(dictionary=True)

    conn.autocommit = False

    query = ("""SELECT
     c.Nome AS Cliente,
     p.Id_pedido AS Codigo_Pedido,
     p.Data AS Data_Pedido,
     ROUND(f.Valor, 2) AS Valor_Fatura,
     f.Status AS Status_Fatura
    FROM cliente c
    JOIN pedido p ON p.fk_Cliente_Id_cliente = c.Id_cliente
    JOIN fatura f ON f.fk_Pedido_Id_pedido = p.Id_pedido
    ORDER BY c.Nome, p.Data;""")

    cursor.execute(query)

    resultados = cursor.fetchall()

    conexao.close()

    return resultados

    # for linha in resultados:
    #     print(linha)

    # for linha in resultados:
    #     print(linha["Id_cliente"])
