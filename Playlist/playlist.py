class PlayList:

    def __init__(self, id, nome, descricao):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__tempo_total = 0

    def getId(self):
        return self.__id

    def getNome(self):
        return self.__nome

    def getDescricao(self):
        return self.__descricao

    def getTempoTotal(self):
        return self.__tempo_total

    def setId(self, id):
        self.__id = id

    def setNome(self, nome):
        self.__nome = nome

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def setTempoTotal(self, tempo_total):
        self.__tempo_total = tempo_total

    def MostrarTempoTotal(self):

        minutos = self.__tempo_total // 60
        segundos = self.__tempo_total % 60

        return f"{minutos}:{segundos:02d}"

    def __str__(self):

        return (
            f"ID: {self.__id} | "
            f"Nome: {self.__nome} | "
            f"Descrição: {self.__descricao} | "
            f"Tempo total: {self.MostrarTempoTotal()}"
        )
