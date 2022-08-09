import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Matheus Rodrigues Pronunciate
# 2021030800

class mensalidadeinv(Exception):
    pass

class campoVazio(Exception):
    pass

class InstrumentoInv(Exception):
    pass
       

class alunos:
    def __init__(self, codigo, nome, instrumento, mensalidade):
        self.__codigo = codigo
        self.__nome = nome
        self.__instrumento = instrumento
        self.__mensalidade = mensalidade

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getInstrumento(self):
        return self.__instrumento

    def getMensalidade(self):
        return self.__mensalidade


    def getDados(self):
        return "Codigo: " + str(self.getCodigo())\
        + "\nNome: " + str(self.getNome())\
        + "\nInstrumento: " + str(self.getInstrumento())\
        + "\nMensalidade: R$ " + str(self.getMensalidade())\
        + "\n"

class LimiteInserealunos(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("alunos")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameInstrumento = tk.Frame(self)
        self.frameMensalidade = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameInstrumento.pack()
        self.frameMensalidade.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelInstrumento = tk.Label(self.frameInstrumento, text="Instrumento: ")
        self.labelMensalidade = tk.Label(self.frameMensalidade, text="Mensalidade: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelInstrumento.pack(side="left")
        self.labelMensalidade.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputInstrumento = tk.Entry(self.frameInstrumento, width=15)
        self.inputMensalidade = tk.Entry(self.frameMensalidade, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputInstrumento.pack(side="left")
        self.inputMensalidade.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, Nome, msg):
        messagebox.showinfo(Nome, msg)

class LimiteConsultaalunos(tk.Toplevel):
    def __init__(self, controle, listaInstrumentosPreenchidos):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("CONSULTA")
        self.controle = controle

        self.frameconsulta = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameconsulta.pack()
        self.frameButton.pack()

        self.labelconsultaInstrumento = tk.Label(self.frameconsulta, text="Consulte por instrumento:")
        self.labelconsultaInstrumento.pack(side="left")
        self.consultaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameconsulta, width = 15 , textvariable = self.consultaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaInstrumentosPreenchidos

        self.buttonSubmit = tk.Button(self.frameButton ,text="Consultar")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.consultar)

    def mostraJanela(self, Nome, msg):
        messagebox.showinfo(Nome, msg)

class Ctrlalunos():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaInstrumento = ["Violão", "Guitarra", "Bateria", "Teclado", "Baixo", "Saxofone"]

        self.listaAlunos = []
        self.listaAlunos.append(alunos('1001', 'José Souza', 'Violão', 250))
        self.listaAlunos.append(alunos('1002', 'Maria Silva', 'Teclado', 300))
        self.listaAlunos.append(alunos('1003', 'Mário Jorge', 'Bateria', 320))
        self.listaAlunos.append(alunos('1004', 'André Marques', 'Guitarra', 300))
        self.listaAlunos.append(alunos('1005', 'Sandra Siqueira', 'Saxofone', 350))
        self.listaAlunos.append(alunos('1006', 'Marcos Silveira', 'Baixo', 320))
        self.listaAlunos.append(alunos('1007', 'João Felipe', 'Bateria', 320))
        self.listaAlunos.append(alunos('1008', 'Laura Cintra', 'Baixo', 320))
        self.listaAlunos.append(alunos('1009', 'Daniel Cruz', 'Guitarra', 300))
        self.listaAlunos.append(alunos('1010', 'Ana Cardoso', 'Violão', 250))

    def getListaCodigo(self):
        self.listacod = []
        for est in self.listaAlunos:
            self.listacod.append(est.getCodigo())
        return self.listacod

    def getalunos(self, codigo):
        for cod in self.listaAlunos:
            if cod.getCodigo() == codigo:
                return cod
        return

    def cadastraAlunos(self):
        self.limiteIns = LimiteInserealunos(self)

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        instrumento = self.limiteIns.inputInstrumento.get()
        mensalidade = int(self.limiteIns.inputMensalidade.get())

        try:
            if not codigo or not nome or not instrumento or not mensalidade:
                raise campoVazio()
            if instrumento not in self.listaInstrumento or instrumento == self.listaInstrumento:
                raise InstrumentoInv()
            if mensalidade < 0 or mensalidade > 500:
                raise mensalidadeinv()
        except campoVazio:
            self.limiteIns.mostraJanela('ERRO', 'TODOS OS CAMPOS DEVEM SER PREENCHIDOS')
        except InstrumentoInv:
            self.limiteIns.mostraJanela('ERRO', 'INSTRUMENTO INVALIDO')
        except mensalidadeinv:
            self.limiteIns.mostraJanela('ERRO', 'A MENSALIDADE NÃO PODE SER MENOR QUE 0 REAIS OU MAIOR QUE 500 REAIS')
        else:
            aluno = alunos(codigo, nome, instrumento, mensalidade)
            self.listaAlunos.append(aluno)
            # self.__listaInstrumentosPreenchidos.append(instrumento)
            self.limiteIns.mostraJanela('TUDO CERTO!', 'ALUNO CADASTRADO COM SUCESSO')
            self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputInstrumento.delete(0, len(self.limiteIns.inputInstrumento.get()))
        self.limiteIns.inputMensalidade.delete(0, len(self.limiteIns.inputMensalidade.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def consultainstrumento(self):
        listaInstrumentosPreenchidos = []
        for inst in self.listaAlunos:
            listaInstrumentosPreenchidos.append(inst.getInstrumento())
        self.limiteCon = LimiteConsultaalunos(self, listaInstrumentosPreenchidos)

    def consultar(self, event):
        AlunosInst = ''
        AlunosInst += 'Alunos Encontrados: '
        StringInstrumento = self.limiteCon.consultaCombo.get()
        for busca in self.listaAlunos:
            if busca.getInstrumento() == StringInstrumento:
                AlunosInst += busca.getDados() + '\n'
        self.limiteCon.mostraJanela('RESULTADO', AlunosInst)
            