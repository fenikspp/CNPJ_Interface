from tkinter import *
from Backend.connection import *
import csv

connection = Conexao("pq://postgres:170163768@localhost/empresas")

janela = Tk()
janela.title("CPNJ")
janela.geometry("500x500+100+100")


def bt_insertdb():
    dado = ed1.get()
    sql = "insert into cidade values (default, '%s')" % dado
    print(ed1.get())
    if connection.manipular(sql):
        print('inserido com sucesso!')


def bt_selectdb():
    with open('mycsv.csv', 'w', newline='') as f:
        thewriter = csv.writer(f)
        dado = ed_select.get()
        dado2 = ed_select2.get()
        dado3 = ed_select3.get()
        if len(ed_select2.get()) == 0:
            rs = connection.consultar(
                "select * from empresas.empresas_cnpj where empresas_cnpj.uf = '%s'" % dado)
        elif len(ed_select3.get()) == 0:
            rs = connection.consultar(
                "select * from empresas.empresas_cnpj where empresas_cnpj.uf = '%s' and empresas_cnpj.municipio = '%s'" % (dado, dado2))
        else:
            rs = connection.consultar(
                "select * from empresas.empresas_cnpj where empresas_cnpj.uf = '%s' and empresas_cnpj.municipio = '%s' and empresas_cnpj.bairro = '%s'" % (dado, dado2, dado3))
        for linha in rs:
            thewriter.writerow(linha)
        print('Criado csv')


def bt_click2():
    rs = connection.consultar("select * from cidade")
    for linha in rs:
        print(linha)


'''lb1 = Label(janela, text="INSERT")
lb1.place(x=10, y=30)

ed1 = Entry(janela, width=20)
ed1.place(x=10, y=50)

bt1 = Button(janela, width=20, text="Inserir dado", command=bt_insertdb)
bt1.place(x=200, y=45)
'''
''' UF '''

lb_selectUF = Label(janela, text="ESTADO(UF)")
lb_selectUF.place(x=10, y=100)

ed_select = Entry(janela, width=20)
ed_select.place(x=10, y=130)

bt_select = Button(janela, width=20, text="Selecionar CNPJ's",
                   command=bt_selectdb)
bt_select.place(x=200, y=125)

''' MUNICIPIO '''

lb_selectMUNICIPIO = Label(janela, text="MUNICIPIO")
lb_selectMUNICIPIO.place(x=10, y=170)

ed_select2 = Entry(janela, width=20)
ed_select2.place(x=10, y=200)

''' BAIRRO '''

lb_selectBAIRRO = Label(janela, text="BAIRRO")
lb_selectBAIRRO.place(x=10, y=240)

ed_select3 = Entry(janela, width=20)
ed_select3.place(x=10, y=270)

''' DEV '''

'''
bt_all = Button(janela, width=20, text="Mostrar todos os dados",
                command=bt_click2)
bt_all.place(x=300, y=300)
'''

'''print(len(ed1.get()) == 0)'''


janela.mainloop()

'''print(connection.proximaPK('cidade', 'id'))
rs = connection.consultar("select * from cidade")
for linha in rs:
    print(linha)
'''
connection.fechar()
