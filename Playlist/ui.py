from playlist import PlayList
from musica import Musica
from playlist_item import PlayListItem


class UI:

    def __init__(self):
        self.__playlists = []
        self.__musicas = []
        self.__itens = []

    def Menu(self):

        print("\n================ PLAYLIST ================")

        print("\n--- PLAYLISTS ---")
        print("1  - Inserir playlist")
        print("2  - Listar playlists")
        print("3  - Buscar playlist por ID")
        print("4  - Atualizar playlist")
        print("5  - Excluir playlist")

        print("\n--- MÚSICAS ---")
        print("6  - Inserir música")
        print("7  - Listar músicas")
        print("8  - Buscar música por ID")
        print("9  - Atualizar música")
        print("10 - Excluir música")

        print("\n--- ITENS DA PLAYLIST ---")
        print("11 - Inserir música em playlist")
        print("12 - Listar músicas de uma playlist")
        print("13 - Atualizar item da playlist")
        print("14 - Excluir música da playlist")
        print("15 - Mostrar tempo total da playlist")

        print("\n0  - Sair")

        print("==========================================")

    def InserirPlaylist(self):

        print("\n--- Inserir Playlist ---")

        id = int(input("ID: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")

        playlist = PlayList(
            id,
            nome,
            descricao
        )

        self.__playlists.append(playlist)

        print("Playlist inserida com sucesso!")

    def ListarPlaylists(self):

        print("\n--- Lista de Playlists ---")

        if len(self.__playlists) == 0:
            print("Nenhuma playlist cadastrada.")
            return

        for playlist in self.__playlists:
            print(playlist)

    def BuscarPlaylist(self, id):

        for playlist in self.__playlists:

            if playlist.getId() == id:
                return playlist

        return None

    def ListarPlaylistId(self):

        print("\n--- Buscar Playlist ---")

        id = int(input("Digite o ID da playlist: "))

        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
        else:
            print(playlist)

    def AtualizarPlaylist(self):

        print("\n--- Atualizar Playlist ---")

        id = int(input("Digite o ID da playlist: "))

        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        nome = input("Novo nome: ")
        descricao = input("Nova descrição: ")

        playlist.setNome(nome)
        playlist.setDescricao(descricao)

        print("Playlist atualizada com sucesso!")

    def ExcluirPlaylist(self):

        print("\n--- Excluir Playlist ---")

        id = int(input("Digite o ID da playlist: "))

        playlist = self.BuscarPlaylist(id)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        self.__itens = [
            item
            for item in self.__itens
            if item.getIdPlaylist() != id
        ]

        self.__playlists.remove(playlist)

        print("Playlist excluída com sucesso!")

    def InserirMusica(self):

        print("\n--- Inserir Música ---")

        id = int(input("ID: "))
        titulo = input("Título: ")
        artista = input("Artista: ")
        album = input("Álbum: ")

        minutos = int(input("Minutos da duração: "))
        segundos = int(input("Segundos da duração: "))

        duracao = minutos * 60 + segundos

        musica = Musica(
            id,
            titulo,
            artista,
            album,
            duracao
        )

        self.__musicas.append(musica)

        print("Música inserida com sucesso!")

    def ListarMusicas(self):

        print("\n--- Lista de Músicas ---")

        if len(self.__musicas) == 0:
            print("Nenhuma música cadastrada.")
            return

        for musica in self.__musicas:
            print(musica)

    def BuscarMusica(self, id):

        for musica in self.__musicas:

            if musica.getId() == id:
                return musica

        return None

    def ListarMusicaId(self):

        print("\n--- Buscar Música ---")

        id = int(input("Digite o ID da música: "))

        musica = self.BuscarMusica(id)

        if musica is None:
            print("Música não encontrada.")
        else:
            print(musica)

    def AtualizarMusica(self):

        print("\n--- Atualizar Música ---")

        id = int(input("Digite o ID da música: "))

        musica = self.BuscarMusica(id)

        if musica is None:
            print("Música não encontrada.")
            return

        titulo = input("Novo título: ")
        artista = input("Novo artista: ")
        album = input("Novo álbum: ")

        minutos = int(input("Novos minutos: "))
        segundos = int(input("Novos segundos: "))

        duracao = minutos * 60 + segundos

        musica.setTitulo(titulo)
        musica.setArtista(artista)
        musica.setAlbum(album)
        musica.setDuracao(duracao)

        print("Música atualizada com sucesso!")

    def ExcluirMusica(self):

        print("\n--- Excluir Música ---")

        id = int(input("Digite o ID da música: "))

        musica = self.BuscarMusica(id)

        if musica is None:
            print("Música não encontrada.")
            return

        self.__itens = [
            item
            for item in self.__itens
            if item.getIdMusica() != id
        ]

        self.__musicas.remove(musica)

        print("Música excluída com sucesso!")

    def InserirItem(self):

        print("\n--- Adicionar Música à Playlist ---")

        id = int(input("ID do item: "))

        id_playlist = int(
            input("ID da playlist: ")
        )

        id_musica = int(
            input("ID da música: ")
        )

        data = input("Data de inclusão: ")

        sequencia = int(
            input("Sequência da música: ")
        )

        playlist = self.BuscarPlaylist(id_playlist)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        musica = self.BuscarMusica(id_musica)

        if musica is None:
            print("Música não encontrada.")
            return

        item = PlayListItem(
            id,
            id_playlist,
            id_musica,
            data,
            sequencia
        )

        self.__itens.append(item)

        print("Música adicionada à playlist!")

    def ListarItensPlaylist(self):

        print("\n--- Músicas da Playlist ---")

        id_playlist = int(
            input("ID da playlist: ")
        )

        playlist = self.BuscarPlaylist(id_playlist)

        if playlist is None:
            print("Playlist não encontrada.")
            return

        encontrou = False

        for item in self.__itens:

            if item.getIdPlaylist() == id_playlist:

                musica = self.BuscarMusica(
                    item.getIdMusica()
                )

                if musica is not None:

                    print(
                        f"{item.getSequencia()} - "
                        f"{musica.getTitulo()} - "
                        f"{musica.getArtista()}"
                    )

                    encontrou = True

        if not encontrou:
            print(
                "Essa playlist não possui músicas."
            )

    def BuscarItem(self, id):

        for item in self.__itens:

            if item.getId() == id:
                return item

        return None

    def AtualizarItem(self):

        print("\n--- Atualizar Item ---")

        id = int(
            input("ID do item: ")
        )

        item = self.BuscarItem(id)

        if item is None:
            print("Item não encontrado.")
            return

        id_playlist = int(
            input("Novo ID da playlist: ")
        )

        id_musica = int(
            input("Novo ID da música: ")
        )

        data = input(
            "Nova data de inclusão: "
        )

        sequencia = int(
            input("Nova sequência: ")
        )

        playlist = self.BuscarPlaylist(
            id_playlist
        )

        if playlist is None:
            print("Playlist não encontrada.")
            return

        musica = self.BuscarMusica(
            id_musica
        )

        if musica is None:
            print("Música não encontrada.")
            return

        item.setIdPlaylist(id_playlist)
        item.setIdMusica(id_musica)
        item.setDataInclusao(data)
        item.setSequencia(sequencia)

        print("Item atualizado com sucesso!")

    def ExcluirItem(self):

        print("\n--- Excluir Música da Playlist ---")

        id = int(
            input("ID do item: ")
        )

        item = self.BuscarItem(id)

        if item is None:
            print("Item não encontrado.")
            return

        self.__itens.remove(item)

        print("Música removida da playlist!")

    def AtualizarTempoPlaylist(self, id_playlist):

        playlist = self.BuscarPlaylist(
            id_playlist
        )

        if playlist is None:
            return

        tempo_total = 0

        for item in self.__itens:

            if item.getIdPlaylist() == id_playlist:

                musica = self.BuscarMusica(
                    item.getIdMusica()
                )

                if musica is not None:

                    tempo_total += musica.getDuracao()

        playlist.setTempoTotal(
            tempo_total
        )

    def MostrarTempoPlaylist(self):

        print("\n--- Tempo Total da Playlist ---")

        id_playlist = int(
            input("ID da playlist: ")
        )

        self.AtualizarTempoPlaylist(
            id_playlist
        )

        playlist = self.BuscarPlaylist(
            id_playlist
        )

        if playlist is None:
            print("Playlist não encontrada.")
            return

        print(
            "Tempo total: "
            + playlist.MostrarTempoTotal()
        )


    def Main(self):

        while True:

            self.Menu()

            opcao = input(
                "Escolha uma opção: "
            )

            if opcao == "1":
                self.InserirPlaylist()

            elif opcao == "2":
                self.ListarPlaylists()

            elif opcao == "3":
                self.ListarPlaylistId()

            elif opcao == "4":
                self.AtualizarPlaylist()

            elif opcao == "5":
                self.ExcluirPlaylist()

            elif opcao == "6":
                self.InserirMusica()

            elif opcao == "7":
                self.ListarMusicas()

            elif opcao == "8":
                self.ListarMusicaId()

            elif opcao == "9":
                self.AtualizarMusica()

            elif opcao == "10":
                self.ExcluirMusica()

            elif opcao == "11":
                self.InserirItem()

            elif opcao == "12":
                self.ListarItensPlaylist()

            elif opcao == "13":
                self.AtualizarItem()

            elif opcao == "14":
                self.ExcluirItem()

            elif opcao == "15":
                self.MostrarTempoPlaylist()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":

    ui = UI()

    ui.Main()
