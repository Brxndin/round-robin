from processo import Processo

# a cpu faz um foreach que diminui o quantum dela com o tempo necessário do processo
# se o quantum é o suficiente pro tempo necessário do processo, remove ele da fila e considera executado
# se não é o quantum necessário, diminui o que da e coloca o processo com o tempo necessário diminuido para depois executar novamente

class Cpu:
    quantum = 100

    def __init__(self, fila):
        self.fila = fila

    def getFila(self):
        return self.fila

    def setFila(self, value):
        self.fila = value

    def executa(self):
        executados = []

        for processo in fila:

            if self.quantum - processo.getTempoNecessario() >= 0:
                print('No processo ' + str(processo.getId()) + ' foram executados ' + str(processo.getQuantum())  + ' de ' + str(tempoNecessario))

                print(str(processo.getId()) + ' executado com sucesso!')
                executados.append(processo.getId())

            tempoNecessario -= processo.getQuantum()

        print(executados)

fila = [Processo(1, 10), Processo(2, 6), Processo(3, 11)]

cpu = Cpu(fila)

cpu.executa()

