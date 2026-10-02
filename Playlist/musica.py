class Musica:

    def __init__(self, id, titulo, artista, album, duracao):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__duracao = duracao

    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getDuracao(self):
        return self.__duracao

    def setId(self, id):
        self.__id = id

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setArtista(self, artista):
        self.__artista = artista

    def setAlbum(self, album):
        self.__album = album

    def setDuracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):

        minutos = self.__duracao // 60
        segundos = self.__duracao % 60

        return (
            f"ID: {self.__id} | "
            f"Título: {self.__titulo} | "
            f"Artista: {self.__artista} | "
            f"Álbum: {self.__album} | "
            f"Duração: {minutos}:{segundos:02d}"
        )
