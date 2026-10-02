class PlayListItem:

    def __init__(self, id, id_playlist, id_musica, data_inclusao, sequencia):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__data_inclusao = data_inclusao
        self.__sequencia = sequencia

    def getId(self):
        return self.__id

    def getIdPlaylist(self):
        return self.__id_playlist

    def getIdMusica(self):
        return self.__id_musica

    def getDataInclusao(self):
        return self.__data_inclusao

    def getSequencia(self):
        return self.__sequencia


    def setId(self, id):
        self.__id = id

    def setIdPlaylist(self, id_playlist):
        self.__id_playlist = id_playlist

    def setIdMusica(self, id_musica):
        self.__id_musica = id_musica

    def setDataInclusao(self, data_inclusao):
        self.__data_inclusao = data_inclusao

    def setSequencia(self, sequencia):
        self.__sequencia = sequencia

    def __str__(self):

        return (
            f"ID: {self.__id} | "
            f"Playlist: {self.__id_playlist} | "
            f"Música: {self.__id_musica} | "
            f"Data inclusão: {self.__data_inclusao} | "
            f"Sequência: {self.__sequencia}"
        )
