from Backend.connection import *

if __name__ == '__main__':
    con = Conexao("pq://postgres:170163768@localhost/empresas")
    sql = "insert into cidade values (default,'Bahia')"
    if con.manipular(sql):
        print('inserido com sucesso!')
    print(con.proximaPK('cidade', 'id'))
    rs = con.consultar("select * from cidade")
    for linha in rs:
        print(linha)
    con.fechar()
