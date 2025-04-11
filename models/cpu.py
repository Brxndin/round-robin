import random
from processo import Processo

# a cpu faz um foreach que diminui o quantum dela com o tempo necessário do processo
# se o quantum é o suficiente pro tempo necessário do processo, remove ele da fila e considera executado
# se não é o quantum necessário, diminui o que da e coloca o processo por último na fila para depois executar novamente com o tempo necessário menor

class Cpu:
    def __init__(self, quantum, fila):
        self.quantum = quantum
        self.fila = fila

    def getQuantum(self):
        return self.quantum

    def setQuantum(self, value):
        self.quantum = value

    def getFila(self):
        return self.fila

    def setFila(self, value):
        self.fila = value

    def executa(self):
        newFila = self.getFila()

        while len(newFila) > 0:
            for processo in newFila:
                if self.getQuantum() - processo.getTempoNecessario() >= 0:
                    print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(processo.getTempoNecessario())  + ' de ' + str(processo.getTempoNecessario()) + ' unidades de tempo.')
                    print(str(processo.getId()) + ' executado com sucesso!')
                    newFila.remove(processo)
                else:
                    print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(self.getQuantum())  + ' de ' + str(processo.getTempoNecessario()) + ' unidades de tempo.')
                    processo.setTempoNecessario(abs(self.getQuantum() - processo.getTempoNecessario()))

# os processos tem tempo necessário randômico
processo1 = Processo(1, random.randint(1, 300))
processo2 = Processo(2, random.randint(1, 300))
processo3 = Processo(3, random.randint(1, 300))

fila = [processo1, processo2, processo3]

cpu = Cpu(100, fila)

cpu.executa()
