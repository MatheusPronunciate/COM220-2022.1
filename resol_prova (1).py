from abc import ABC, abstractclassmethod, abstractmethod

class Dependente():
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade


class Trabalhador(ABC):
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
        self.__listaDependentes = []

    def getCpf(self):
        return self.__cpf

    def getNome(self):
        return self.__nome

    def getListaDependentes(self):
        return self.__listaDependentes

    def insereDependente(self, nome, idade):
        self.__listaDependentes.append(Dependente(nome, idade))

    @abstractmethod
    def calculaPagto(self, mes, ano):
        pass

    def imprimeRecibo(self, mes, ano):
        print('Nome: {}'.format(self.__nome))
        print('Valor recebido: {}'.format(self.calculaPagto(mes, ano)))
        print()


class Diaria():
    def __init__(self, dia, mes, ano, refeicao, atraso):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__refeicao = refeicao
        self.__atraso = atraso

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def isRefeicao(self):
        return self.__refeicao

    def isAtraso(self):
        return self.__atraso


class Diarista(Trabalhador):
    def __init__(self, cpf, nome, valorDiaria):
        super().__init__(cpf, nome)
        self.__valorDiaria = valorDiaria
        self.__listaDiaria = []

    def getValorDiaria(self):
        return self.__valorDiaria

    def getListaDiaria(self):
        return self.__listaDiaria

    def adicionaDiaria(self, dia, mes, ano, refeicao, atraso):
        self.__listaDiaria.append(Diaria(dia, mes, ano, refeicao, atraso))

    def obtemValorAuxilio(self):
        nroDep = 0
        for dep in self.getListaDependentes():
            if dep.getIdade() < 6:
                nroDep += 1
        return 100 * nroDep

    def calculaPagto(self, mes, ano):
        pagto = 0
        for diaria in self.__listaDiaria:
            if diaria.getMes() == mes and diaria.getAno() == ano:
                valorDia = self.__valorDiaria
                if diaria.isAtraso():
                    valorDia -= valorDia * 0.1
                if diaria.isRefeicao():
                    valorDia -= 10
                pagto += valorDia
        if pagto > 0:
            pagto += self.obtemValorAuxilio()
        return pagto        

class Empreito():
    def __init__(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__mes = mes
        self.__ano = ano
        self.__descricao = descricao
        self.__valor = valor
        self.__atrasoEntrega = atrasoEntrega

    def getMes(self):
        return self.__mes

    def getAno(self):
        return self.__ano

    def getDescricao(self):
        return self.__descricao

    def getValor(self):
        return self.__valor

    def isAtrasoEntrega(self):
        return self.__atrasoEntrega


class Empreiteiro(Trabalhador):
    def __init__(self, cpf, nome):
        super().__init__(cpf, nome)
        self.__listaEmpreito = []

    def getListaEmpreito(self):
        return self.__listaEmpreito

    def adicionaEmpreito(self, mes, ano, descricao, valor, atrasoEntrega):
        self.__listaEmpreito.append(Empreito(mes, ano, descricao, valor, atrasoEntrega))

    def calculaPagto(self, mes, ano):
        pagto = 0
        for empreito in self.__listaEmpreito:
            if empreito.getMes() == mes and empreito.getAno() == ano:
                if empreito.isAtrasoEntrega():
                    pagto += empreito.getValor() * 0.8
                else:
                    pagto += empreito.getValor()
        return pagto


if __name__ == "__main__":
    listaTrab = []
    d1 = Diarista("111222", "Joao Silva", 100)
    d1.insereDependente("Pedro Silva", 4)
    d1.insereDependente("Ana Silva", 2)
    d1.adicionaDiaria(10, 3, 2022, False, False)
    d1.adicionaDiaria(12, 4, 2022, False, True)
    d2 = Diarista("222333", "Jose Cruz", 120)
    d2.insereDependente("Paula Cruz", 3)
    d2.insereDependente("Mario Cruz", 10)
    d2.adicionaDiaria(5, 4, 2022, False, False)
    d2.adicionaDiaria(6, 4, 2022, True, False)
    d2.adicionaDiaria(7, 4, 2022, True, True)
    e1 = Empreiteiro("333444", "Marcio Souza")
    e1.adicionaEmpreito(3, 2022, "Fundações", 6000, False)
    e1.adicionaEmpreito(4, 2022, "Construção muros", 4000, False)
    e1.adicionaEmpreito(4, 2022, "Instalação dos pisos", 7000, True)
    listaTrab.append(d1)
    listaTrab.append(d2)
    listaTrab.append(e1)
    for trab in listaTrab:
        trab.imprimeRecibo(4, 2022)

