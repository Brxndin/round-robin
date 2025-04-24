import random
from processo import Processo

# a cpu faz um for in que subtrai o quantum com o tempo necessário do processo atual
# se o quantum é o suficiente pro tempo necessário do processo, remove ele da fila e considera executado
# se o quantum não é o suficiente, diminui o que é possível e coloca o processo por último na fila para depois executar novamente com o tempo que falta

class Cpu:
    def __init__(self, quantum):
        self.quantum = quantum

    def getQuantum(self):
        return self.quantum

    def setQuantum(self, value):
        self.quantum = value

    def executa(self, fila):
        print('O Quantum da CPU é de ' + str(self.getQuantum()) + ' unidades de tempo.')
        for processo in fila:
            print('O tempo necessário do processo ' + str(processo.getId()) + ' é de ' + str(processo.getTempoNecessario()))

        print('-----------------')

        while len(fila) > 0:
            processo = fila.pop(0)

            if processo.getTempoNecessario() > 0:
                if self.getQuantum() - processo.getTempoNecessario() >= 0:
                    print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(processo.getTempoNecessario())  + ' de ' + str(processo.getTempoNecessario()) + ' unidades de tempo.')
                    print('Processo ' + str(processo.getId()) + ' executado com sucesso!')
                else:
                    print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(self.getQuantum())  + ' de ' + str(processo.getTempoNecessario()) + ' unidades de tempo.')
                    
                    processo.setTempoNecessario(abs(self.getQuantum() - processo.getTempoNecessario()))

                    # se não foi executado completamente, adiciona novamente na lista para executar depois
                    fila.append(processo)
        
        print('-----------------')

        print('Todos os processos foram executados com sucesso!')

# dados básicos
quantum = 100
quantidadeMaximaProcessos = 6
quantidadeTempoProcesso = 300

# execução
# aqui cria a fila com quantidade de processos aleatória e com tempo necessário também aleatório
processoAtual = 1
fila = []

while processoAtual <= random.randint(1, quantidadeMaximaProcessos):
    # os processos tem tempo necessário randômico
    novoProcesso = Processo(processoAtual, random.randint(1, quantidadeTempoProcesso))

    fila.append(novoProcesso)

    processoAtual += 1

cpu = Cpu(quantum)

cpu.executa(fila)
