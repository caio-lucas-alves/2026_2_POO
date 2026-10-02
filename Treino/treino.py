class Treino:

    def __init__(self, id, data, distancia, tempo):
        self.__id = id
        self.__data = data
        self.__distancia = distancia
        self.__tempo = tempo

    # Getters

    def getId(self):
        return self.__id

    def getData(self):
        return self.__data

    def getDistancia(self):
        return self.__distancia

    def getTempo(self):
        return self.__tempo

    # Setters

    def setId(self, id):
        self.__id = id

    def setData(self, data):
        self.__data = data

    def setDistancia(self, distancia):
        self.__distancia = distancia

    def setTempo(self, tempo):
        self.__tempo = tempo

    # Calcula o pace

    def Pace(self):

        if self.__distancia <= 0:
            return 0

        return self.__tempo / self.__distancia

    # Mostra os dados do treino

    def __str__(self):

        pace = self.Pace()

        minutos = int(pace)
        segundos = int((pace - minutos) * 60)

        return (
            f"ID: {self.__id} | "
            f"Data: {self.__data} | "
            f"Distância: {self.__distancia:.2f} km | "
            f"Tempo: {self.__tempo:.2f} min | "
            f"Pace: {minutos}:{segundos:02d} min/km"
        )
