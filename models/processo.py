class Processo:
    def __init__(self, id, tempoNecessario):
        self.id = id
        self.tempoNecessario = tempoNecessario

    def getId(self):
        return self.id

    def setId(self, value):
        self.id = value

    def getTempoNecessario(self):
        return self.tempoNecessario

    def setTempoNecessario(self, value):
        self.tempoNecessario = value
