import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import aluno as alu

# Matheus Rodrigues Pronunciate
# 2021030800

class codigoInv(Exception):
    pass

class campoVazio(Exception):
    pass

class quantidadeinv(Exception):
    pass

class nomeinv(Exception):
    pass
       

class bandas:
    def __init__(self, nome, integrantes):
        self.__nome = nome
        self.__integrantes = integrantes

    def getNome(self):
        return self.__nome

    def getIntegrantes(self):
        return self.__integrantes

    def getDados(self):
        return "\nNome: " + str(self.getNome())\
        + "\nintegrantes: " + str(self.getIntegrantes())\
        + "\n"

class LimiteInserebanda(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Cadastrar Bandas")
        self.controle = controle

        self.frameNomeBanda = tk.Frame(self)
        self.frameAluno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNomeBanda.pack()
        self.frameAluno.pack()
        self.frameButton.pack()

        self.labelNomeBanda = tk.Label(self.frameNomeBanda, text="Informe o nome da banda: ")
        self.labelNomeBanda.pack(side="left")
        self.inputNomeBanda = tk.Entry(self.frameNomeBanda, width=20)
        self.inputNomeBanda.pack(side="left")

        self.labelcodigoAl = tk.Label(self.frameAluno, text="Informe o código do aluno: ")
        self.labelcodigoAl.pack(side="left")
        self.inputcodigoAl = tk.Entry(self.frameAluno, width=20)
        self.inputcodigoAl.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Inserir Aluno")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonCriarBanda = tk.Button(self.frameButton ,text="Criar Banda")      
        self.buttonCriarBanda.pack(side="left")
        self.buttonCriarBanda.bind("<Button>", controle.criarBanda)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, Nome, msg):
        messagebox.showinfo(Nome, msg)

class LimiteConsultaBandas(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("CONSULTA")
        self.controle = controle

        self.frameNomeBanda = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNomeBanda.pack()
        self.frameButton.pack()

        self.labelNomeBanda = tk.Label(self.frameNomeBanda, text="Informe o nome da banda: ")
        self.labelNomeBanda.pack(side="left")
        self.inputNomeBanda = tk.Entry(self.frameNomeBanda, width=20)
        self.inputNomeBanda.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="BUSCAR BANDA")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.buscabanda)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, Nome, msg):
        messagebox.showinfo(Nome, msg)

class CtrlBandas():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaBandas = []
        self.__integrantes = []

        #self.ctrlalunos = alu.Ctrlalunos(self)

    def cadastraBandas(self):
        self.limiteIns = LimiteInserebanda(self)
    
    def consultaBandas(self):
        self.limitecons = LimiteConsultaBandas(self)

    def enterHandler(self, event):
        nomeBanda = self.limiteIns.inputNomeBanda.get()
        codigo = self.limiteIns.inputcodigoAl.get()

        try:
            if not nomeBanda or not codigo:
                raise campoVazio()
            if codigo not in self.controlador.ctrlalunos.getListaCodigo():
                raise codigoInv()
        except campoVazio:
            self.limiteIns.mostraJanela('ERRO', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        except codigoInv:
            self.limiteIns.mostraJanela('ERRO', 'CODIGO NÃO CORRESPONDE A UM ALUNO')
        else:
            alunoatual = self.controlador.ctrlalunos.getalunos(codigo)
            self.__integrantes.append(alunoatual)
            self.limiteIns.mostraJanela('TUDO CERTO', 'ALUNO(A) {} ADICIONADO! \n Continue adicionando ou crie uma banda'.format(alunoatual.getNome()))
            self.clearHandler(event)

    def criarBanda(self, event):
        quantidade_integrantes = len(self.__integrantes)
        
        if quantidade_integrantes < 3 or quantidade_integrantes > 6:
            self.limiteIns.mostraJanela('ERRO', 'SÃO NECESSÁRIOS AO MENOS 3 INTEGRANTES E NO MÁXIMO 6\n VOCÊ ADICIONOU: {} INTEGRANTES'.format(quantidade_integrantes))
        else:    
            nomeBanda = self.limiteIns.inputNomeBanda.get()
            banda = bandas(nomeBanda, self.__integrantes)
            self.listaBandas.append(banda)
            self.limiteIns.mostraJanela('SUCESSO!', 'Banda Criada com sucesso')
            self.fechaHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputcodigoAl.delete(0, len(self.limiteIns.inputcodigoAl.get()))

    def buscabanda(self, event):
        nomebanda = self.limitecons.inputNomeBanda.get()
        listanomebandas = []

        for nomband in self.listaBandas:
            listanomebandas.append(nomband.getNome())

        try:
            if not nomebanda:
                raise campoVazio()
            if nomebanda not in listanomebandas:
                raise nomeinv()
        except campoVazio:
            self.limitecons.mostraJanela('ERRO', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        except nomeinv:
            self.limitecons.mostraJanela('ERRO', 'NÃO EXISTE NENHUMA BANDA COM O NOME FORNECIDO')
        else:
            Bandainst = ''
            Bandainst += 'BANDA "{}" ENCONTRADA\n'.format(nomebanda)
            Bandainst += 'Os integrantes são: \n'
            for buscabanda in self.listaBandas:
                if nomebanda == buscabanda.getNome():
                    for buscainte in buscabanda.getIntegrantes():
                        Bandainst += buscainte.getDados() + '\n'
            self.limitecons.mostraJanela('RESULTADO', Bandainst)


    def fechaHandler(self, event):
        self.limiteIns.destroy()

    