import random

class Processo:
    def __init__(self, id, tempoNecessario):
        self.id = id
        self.tempoNecessario = tempoNecessario
        self.tempoAtual = 0
        self.entradaSaidaIOBound = {}

        # só faz com 50% de chance
        if random.randint(1, 2) == 1:
            # só gera I/O Bound se o tempo for maior que 3 pois se não abre brechas
            if tempoNecessario > 3:
                entrada = random.randint(2, tempoNecessario - 1)
                saida = random.randint(2, tempoNecessario - 1)

                if entrada > saida:
                    temp = saida
                    saida = entrada
                    entrada = temp

                if entrada == saida:
                    if entrada > 2:
                        entrada = entrada - 1
                    else:
                        saida = saida + 1

                self.entradaSaidaIOBound = {'entrada': entrada, 'saida': saida}

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value

    def getTempoNecessario(self):
        return self.tempoNecessario

    def setTempoNecessario(self, value):
        self.tempoNecessario = value

    def getTempoAtual(self):
        return self.tempoAtual

    def setTempoAtual(self, value):
        self.tempoAtual = value

    def getEntradaSaidaIOBound(self):
        return self.entradaSaidaIOBound

    def setEntradaSaidaIOBound(self, value):
        self.entradaSaidaIOBound = value

    def getTempoIOBound(self):
        if 'entrada' in self.getEntradaSaidaIOBound() and 'saida' in self.getEntradaSaidaIOBound():
            return abs(self.getEntradaSaidaIOBound()['entrada'] - self.getEntradaSaidaIOBound()['saida'])

        return 0
