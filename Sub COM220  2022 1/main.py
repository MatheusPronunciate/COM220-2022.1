import tkinter as tk
from tkinter import messagebox
import aluno as alu
import banda as ban

# Matheus Rodrigues Pronunciate
# 2021030800

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.alunosMenu = tk.Menu(self.menubar)
        self.Banda = tk.Menu(self.menubar)
        self.sair = tk.Menu(self.menubar)

        self.alunosMenu.add_command(label="Cadastrar Alunos", command=self.controle.cadastraAlunos)
        self.alunosMenu.add_command(label="Consultar", command=self.controle.consultainstrumento)
        self.menubar.add_cascade(label="Alunos", menu=self.alunosMenu)

        self.menubar.add_cascade(label="Bandas", menu=self.Banda)
        self.Banda.add_command(label="Cadastrar Bandas", command=self.controle.cadastraBandas)
        self.Banda.add_command(label="Consultar Bandas", command=self.controle.consultaBandas)

        self.menubar.add_cascade(label="Sair", menu=self.sair)
        self.sair.add_command(label="Sair do Programa", command=self.controle.sair)

        self.root.config(menu=self.menubar)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlalunos = alu.Ctrlalunos(self)
        self.ctrlbandas = ban.CtrlBandas(self)
        
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("ESCOLA DE MUSICA")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraAlunos(self):
        self.ctrlalunos.cadastraAlunos()
    
    def consultainstrumento(self):
        self.ctrlalunos.consultainstrumento()

    def cadastraBandas(self):
        self.ctrlbandas.cadastraBandas()

    def consultaBandas(self):
        self.ctrlbandas.consultaBandas()

    '''def salvaDados(self):
        self.ctrljogos.salvaJogos()
        self.ctrljogos.salvaAvaliacoes()
        self.limite.mostraMessagebox('SUCESSO', 'Dados salvos com sucesso')'''
        
    def sair(self):
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()