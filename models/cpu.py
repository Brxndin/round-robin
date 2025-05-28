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

        tempoTotal = 0
        maior = {'id': None, 'tempoNecessario': 0}
        menor = {'id': None, 'tempoNecessario': 0}

        filaIOBound = []
        tempoTotalIOBound = 0

        for processo in fila:
            print('O tempo necessário do processo ' + str(processo.getId()) + ' é de ' + str(processo.getTempoNecessario()) + ' unidades de tempo, sendo ' + str(processo.getTempoIOBound()) + ' em I/O Bound.')

            tempoTotal += processo.getTempoNecessario()
            
            if maior['id'] is not None:
                if maior['tempoNecessario'] < processo.getTempoNecessario():
                    maior['id'] = processo.getId()
                    maior['tempoNecessario'] = processo.getTempoNecessario()
            else:
                maior['id'] = processo.getId()
                maior['tempoNecessario'] = processo.getTempoNecessario()
                
            if menor['id'] is not None:
                if menor['tempoNecessario'] > processo.getTempoNecessario():
                    menor['id'] = processo.getId()
                    menor['tempoNecessario'] = processo.getTempoNecessario()
            else:
                menor['id'] = processo.getId()
                menor['tempoNecessario'] = processo.getTempoNecessario()

        mediaTempoExecucao = round(tempoTotal / len(fila), 2)

        print('-----------------')

        agendamento = 1

        while len(fila) > 0 or len(filaIOBound) > 0:
            print('\n --- Agendamento ' + str(agendamento) + ' --- \n')

            processo = fila.pop(0) if len(fila) > 0 else None
            processoIOBound = filaIOBound.pop(0) if len(filaIOBound) > 0 else None

            mensagem = ''

            contadorQuantum = 1

            tempoNecessarioInicial = 0

            if processoIOBound is not None:
                tempoNecessarioInicial = processoIOBound.getTempoNecessario()

            while contadorQuantum <= self.getQuantum():
                # executa a fila de i/o bound
                if processoIOBound is not None:
                    processoIOBound.setTempoAtual(processoIOBound.getTempoAtual() + 1)
                    processoIOBound.setTempoNecessario(processoIOBound.getTempoNecessario() - 1)

                    tempoTotalIOBound = tempoTotalIOBound + 1

                    if 'saida' in processoIOBound.getEntradaSaidaIOBound():
                        if processoIOBound.getEntradaSaidaIOBound()['saida'] == processoIOBound.getTempoAtual():
                            print('No processo ' + str(processoIOBound.getId()) + ' foram executadas ' + str(contadorQuantum)  + ' de ' + str(tempoNecessarioInicial) + ' unidades de tempo em I/O Bound.')

                            fila.append(processoIOBound)

                            print('Processo ' + str(processoIOBound.getId()) + ' saiu de I/O Bound!')
                            break
                        else:
                            # se chegou no máximo do quantum
                            if contadorQuantum == self.getQuantum():
                                print('No processo ' + str(processoIOBound.getId()) + ' foram executadas ' + str(contadorQuantum)  + ' de ' + str(tempoNecessarioInicial) + ' unidades de tempo em I/O Bound.')

                                # adiciona novamente na lista para executar depois
                                filaIOBound.append(processoIOBound)
                else:
                    break

                contadorQuantum = contadorQuantum + 1

            contadorQuantum = 1

            tempoNecessarioInicial = 0

            if processo is not None:
                tempoNecessarioInicial = processo.getTempoNecessario()

            while contadorQuantum <= self.getQuantum():
                # executa a fila cpu bound
                if processo is not None:
                    processo.setTempoAtual(processo.getTempoAtual() + 1)
                    processo.setTempoNecessario(processo.getTempoNecessario() - 1)

                    # verifica se precisa entrar em i/o bound
                    if 'entrada' in processo.getEntradaSaidaIOBound():
                        if processo.getEntradaSaidaIOBound()['entrada'] == processo.getTempoAtual():
                            print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(contadorQuantum)  + ' de ' + str(tempoNecessarioInicial) + ' unidades de tempo em CPU Bound.')
                            print('Processo ' + str(processo.getId()) + ' entrou em I/O Bound!')

                            # coloca na fila de i/o bound e passa para o próximo processo
                            filaIOBound.append(processo)
                            break

                    # se não foi executado completamente
                    if processo.getTempoNecessario() == 0:
                        print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(contadorQuantum)  + ' de ' + str(tempoNecessarioInicial) + ' unidades de tempo em CPU Bound.')
                        print('Processo ' + str(processo.getId()) + ' executado com sucesso!')
                        break
                    else:
                        # se chegou no máximo do quantum
                        if contadorQuantum == self.getQuantum():
                            print('No processo ' + str(processo.getId()) + ' foram executadas ' + str(contadorQuantum)  + ' de ' + str(tempoNecessarioInicial) + ' unidades de tempo em CPU Bound.')

                            # adiciona novamente na lista para executar depois
                            fila.append(processo)
                else:
                    break

                contadorQuantum = contadorQuantum + 1

            if mensagem != '':
                print(mensagem)  

            agendamento += 1
        
        print('-----------------')

        print('Todos os processos foram executados com sucesso!')

        print('-----------------')

        print('Estatísticas:')
        print('Tempo total de execução: ' + str(tempoTotal) + ' unidades de tempo.')
        print('Tempo total em I/O Bound: ' + str(tempoTotalIOBound) + ' unidades de tempo.')
        print('Processo mais demorado: processo ' + str(maior['id']) + ' (' + str(maior['tempoNecessario']) + ' unidades de tempo).')
        print('Processo menos demorado: processo ' + str(menor['id']) + ' (' + str(menor['tempoNecessario']) + ' unidades de tempo).')
        print('Média de tempo de execução dos processos: ' + str(mediaTempoExecucao) + ' unidades de tempo.')

# define os dados básicos de cpu e processos
quantum = input('Informe o Quantum da CPU: ')
quantidadeMaximaProcessos = input('Informe a quantidade máxima de processos: ')
tempoMaximoProcesso = input('Informe o tempo máximo de cada processo: ')

print('-----------------')

quantum = int(quantum)
quantidadeMaximaProcessos = int(quantidadeMaximaProcessos)
tempoMaximoProcesso = int(tempoMaximoProcesso)

# monta a fila com os processos
fila = []

# a quantidade de processos é no mínimo 1
quantidadeProcessos = random.randint(1, quantidadeMaximaProcessos)
processoAtual = 1

while processoAtual <= quantidadeProcessos:
    # os processos tem tempo necessário randômico
    novoProcesso = Processo(processoAtual, random.randint(1, tempoMaximoProcesso))

    fila.append(novoProcesso)

    processoAtual += 1

# cria a cpu com o quantum definido e executa a fila de processos
cpu = Cpu(quantum)
cpu.executa(fila)
