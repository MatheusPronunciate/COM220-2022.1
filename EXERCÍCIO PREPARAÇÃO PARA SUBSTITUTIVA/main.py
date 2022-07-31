import tkinter as tk
from tkinter import messagebox
import jogos as jog

# Matheus Rodrigues Pronunciate
# 2021030800

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.jogosMenu = tk.Menu(self.menubar)
        self.salva = tk.Menu(self.menubar)
        self.sair = tk.Menu(self.menubar)

        self.jogosMenu.add_command(label="Cadastrar", command=self.controle.cadastrajogos)
        self.jogosMenu.add_command(label="Avaliar", command=self.controle.avaliajogos)
        self.jogosMenu.add_command(label="Consultar", command=self.controle.consultajogos)
        self.menubar.add_cascade(label="Jogos", menu=self.jogosMenu)

        self.menubar.add_cascade(label="Salvar", menu=self.salva)
        self.salva.add_command(label="Salvar os Dados", command=self.controle.salvaDados)

        self.menubar.add_cascade(label="Sair", menu=self.sair)
        self.sair.add_command(label="Sair do Programa", command=self.controle.sair)

        self.root.config(menu=self.menubar)

    def mostraMessagebox(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrljogos = jog.Ctrljogos(self)
        
        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("ESTUDO RECUPERAÇÃO")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastrajogos(self):
        self.ctrljogos.cadastraJogos()
    
    def avaliajogos(self):
        self.ctrljogos.avaliaJogos()

    def consultajogos(self):
        self.ctrljogos.consultaJogos()

    def salvaDados(self):
        self.ctrljogos.salvaJogos()
        self.ctrljogos.salvaAvaliacoes()
        self.limite.mostraMessagebox('SUCESSO', 'Dados salvos com sucesso')
        
    def sair(self):
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()