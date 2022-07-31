import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

# Matheus Rodrigues Pronunciate
# 2021030800

class ConsoleConsole(Exception):
    pass

class ConsoleGenero(Exception):
    pass

class precoinvalido(Exception):
    pass

class campoVazio(Exception):
    pass

class codigoInvalido(Exception):
    pass
       

class jogos:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__avaliacoes = []

    def getCodigo(self):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo

    def getConsole(self):
        return self.__console

    def getGenero(self):
        return self.__genero

    def getPreco(self):
        return self.__preco

    def getAvaliacoes(self):
        return self.__avaliacoes

    def addAvaliacoes(self, avaliacao):
        self.__avaliacoes.append(avaliacao)

    def MediaAvaliacoes(self):
        soma_das_notas = sum(self.__avaliacoes)
        quantidade_avaliacoes = len(self.__avaliacoes)
        if not soma_das_notas and not quantidade_avaliacoes:
            return 0
        else:
            return round(soma_das_notas/quantidade_avaliacoes)

    def getDados(self):
        return "Codigo: " + str(self.getCodigo())\
        + "\nTitulo: " + str(self.getTitulo())\
        + "\nConsole: " + str(self.getConsole())\
        + "\nGenero: " + str(self.getGenero())\
        + "\nPreco: " + str(self.getPreco())\
        + "\n"

class LimiteInsereJogos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Jogos")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelTitulo = tk.Label(self.frameTitulo,text="Titulo: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Genero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=15)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputTitulo.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAvaliajogos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("AVALIAÇAO")
        self.controle = controle

        self.estrelas = ["1 ESTRELA", "2 ESTRELAS", "3 ESTRELAS", "4 ESTRELAS", "5 ESTRELAS"]

        self.frameCodigojogo = tk.Frame(self)
        self.frameAvalie = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.frameCodigojogo.pack()
        self.frameAvalie.pack()
        self.frameButton.pack()

        self.labelCodigojogo = tk.Label(self.frameCodigojogo, text="Digite o código do jogo")
        self.labelCodigojogo.pack(side="left")
        self.inputCodigojogo = tk.Entry(self.frameCodigojogo, width=20)
        self.inputCodigojogo.pack()

        self.labelAvaliejogo = tk.Label(self.frameAvalie, text="Avalie o jogo")
        self.labelAvaliejogo.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameAvalie, width = 15 , textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = self.estrelas

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enteravaliacao)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaAvaliacao)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaJogos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("CONSULTA")
        self.controle = controle

        self.estrelas = ["1 ESTRELA", "2 ESTRELAS", "3 ESTRELAS", "4 ESTRELAS", "5 ESTRELAS"]

        self.frameconsulta = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameconsulta.pack()
        self.frameButton.pack()

        self.labelconsultajogo = tk.Label(self.frameconsulta, text="Consulte o jogo")
        self.labelconsultajogo.pack(side="left")
        self.consultaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameconsulta, width = 15 , textvariable = self.consultaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = self.estrelas

        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultar)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class Ctrljogos():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaConsole = ["Xbox", "Playstation", "Switch", "PC"]
        self.listaGeneros = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        
        if not os.path.isfile("Jogos.pickle"):
            self.listajogos =  []
        else:
            with open("Jogos.pickle", "rb") as f:
                self.listajogos = pickle.load(f)

        if not os.path.isfile("avaliacoes.pickle"):
            for ava in self.listajogos:
                self.listaAvaliacoes = []
                self.listaAvaliacoes.append(ava.getAvaliacoes())
        else:
            with open("avaliacoes.pickle", "rb") as f:
                self.listaAvaliacoes = pickle.load(f)

    
    def salvaJogos(self):
        if len(self.listajogos) != 0:
            with open("Jogos.pickle","wb") as f:
                pickle.dump(self.listajogos, f)

        
    def salvaAvaliacoes(self):
        if len(self.listaAvaliacoes) != 0:
            with open("avaliacoes.pickle","wb") as f:
                pickle.dump(self.listaAvaliacoes, f)

    def cadastraJogos(self):
        self.limiteIns = LimiteInsereJogos(self)

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        titulo = self.limiteIns.inputTitulo.get()
        console = self.limiteIns.inputConsole.get()
        genero = self.limiteIns.inputGenero.get()
        preco = int(self.limiteIns.inputPreco.get())

        try:
            if not codigo or not titulo or not console or not genero or not preco:
                raise campoVazio()
            if console not in self.listaConsole:
                raise ConsoleConsole()
            if genero not in self.listaGeneros:
                raise ConsoleGenero()
            if preco < 0 or preco > 500:
                raise precoinvalido()
        except campoVazio:
            self.limiteIns.mostraJanela('ERRO', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        except ConsoleConsole:
            self.limiteIns.mostraJanela('ERRO', 'NÃO É UM CONSOLE VÁLIDO')
        except ConsoleGenero:
            self.limiteIns.mostraJanela('ERRO', 'NÃO É UM GENERO VÁLIDO')
        except precoinvalido:
            self.limiteIns.mostraJanela('ERRO', 'O PRECO NÃO PODE SER MENOR QUE 0 REAIS OU MAIOR QUE 500 REAIS')
        else:
            jogo = jogos(codigo, titulo, console, genero, preco)
            self.listajogos.append(jogo)
            self.limiteIns.mostraJanela('SUCESSO MANÉ', 'O JOGO FOI CADASTRADO COM SUCESSO')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputTitulo.delete(0, len(self.limiteIns.inputTitulo.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def avaliaJogos(self):
        self.limiteava = LimiteAvaliajogos(self)

    def fechaAvaliacao(self, event):
        self.limiteava.destroy()

    def enteravaliacao(self, event):
        codigojogo = self.limiteava.inputCodigojogo.get()
        Stringestrela = self.limiteava.escolhaCombo.get()

        for achacod in self.listajogos:
            if achacod.getCodigo() == codigojogo:
                if Stringestrela == "1 ESTRELA":
                    estrela = 1
                if Stringestrela == "2 ESTRELAS":
                    estrela = 2
                if Stringestrela == "3 ESTRELAS":
                    estrela = 3
                if Stringestrela == "4 ESTRELAS":
                    estrela = 4
                if Stringestrela == "5 ESTRELAS":
                    estrela = 5
                achacod.addAvaliacoes(estrela)
                self.limiteava.mostraJanela('SUCESSO', '1 AVALIACAO ADICIONADA NO JOGO {}'.format(achacod.getTitulo()))
                break
            if achacod.getCodigo() != codigojogo:
                self.limiteava.mostraJanela('ERRO', 'CODIGO INCOMPATIVEL')

    def consultaJogos(self):
        self.limitecon = LimiteConsultaJogos(self)

    def consultar(self, event):
        Uma_estrela = []
        Duas_estrelas = []
        Tres_estrelas = []
        Quatro_estrelas = []
        Cinco_estrelas = []

        for calculamedia in self.listajogos:
            if calculamedia.MediaAvaliacoes() == 0 or calculamedia.MediaAvaliacoes() == 1:
                Uma_estrela.append(calculamedia.getDados())
            if calculamedia.MediaAvaliacoes() == 2:
                Duas_estrelas.append(calculamedia.getDados())
            if calculamedia.MediaAvaliacoes() == 3:
                Tres_estrelas.append(calculamedia.getDados())
            if calculamedia.MediaAvaliacoes() == 4:
                Quatro_estrelas.append(calculamedia.getDados())
            if calculamedia.MediaAvaliacoes() == 5:
                Cinco_estrelas.append(calculamedia.getDados())

        Stringestrela = self.limitecon.consultaCombo.get()
        if Stringestrela == "1 ESTRELA":
            self.limitecon.mostraJanela('RESULTADO', Uma_estrela)
        if Stringestrela == "2 ESTRELAS":
            self.limitecon.mostraJanela('RESULTADO', Duas_estrelas)
        if Stringestrela == "3 ESTRELAS":
            self.limitecon.mostraJanela('RESULTADO', Tres_estrelas)
        if Stringestrela == "4 ESTRELAS":
            self.limitecon.mostraJanela('RESULTADO', Quatro_estrelas)
        if Stringestrela == "5 ESTRELAS":
            self.limitecon.mostraJanela('RESULTADO', Cinco_estrelas)

