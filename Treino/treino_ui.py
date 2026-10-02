from treino import Treino


class TreinoUI:

    def __init__(self):
        self.__treinos = []

    def Menu(self):
        print("\n========== MENU TREINOS ==========")
        print("1 - Inserir novo treino")
        print("2 - Listar todos os treinos")
        print("3 - Listar treino por ID")
        print("4 - Atualizar treino")
        print("5 - Excluir treino")
        print("6 - Encontrar treino mais rápido")
        print("0 - Sair")
        print("==================================")

    def Inserir(self):
        print("\n--- Inserir treino ---")

        id = int(input("ID: "))
        data = input("Data: ")
        distancia = float(input("Distância (km): "))
        tempo = float(input("Tempo (minutos): "))

        treino = Treino(id, data, distancia, tempo)

        self.__treinos.append(treino)

        print("Treino inserido com sucesso!")

    def Listar(self):
        print("\n--- Lista de treinos ---")

        if len(self.__treinos) == 0:
            print("Nenhum treino cadastrado.")
            return

        for treino in self.__treinos:
            print(treino)

    def Listar_Id(self):
        print("\n--- Buscar treino ---")

        id = int(input("Digite o ID: "))

        treino = self.__buscar_por_id(id)

        if treino is None:
            print("Treino não encontrado.")
        else:
            print(treino)

    def Atualizar(self):
        print("\n--- Atualizar treino ---")

        id = int(input("Digite o ID do treino: "))

        treino = self.__buscar_por_id(id)

        if treino is None:
            print("Treino não encontrado.")
            return

        print("Digite os novos dados:")

        data = input("Data: ")
        distancia = float(input("Distância (km): "))
        tempo = float(input("Tempo (minutos): "))

        treino.setData(data)
        treino.setDistancia(distancia)
        treino.setTempo(tempo)

        print("Treino atualizado com sucesso!")

    def Excluir(self):
        print("\n--- Excluir treino ---")

        id = int(input("Digite o ID do treino: "))

        treino = self.__buscar_por_id(id)

        if treino is None:
            print("Treino não encontrado.")
            return

        self.__treinos.remove(treino)

        print("Treino excluído com sucesso!")

    def MaisRapido(self):
        print("\n--- Treino mais rápido ---")

        if len(self.__treinos) == 0:
            print("Nenhum treino cadastrado.")
            return

        treino_rapido = min(
            self.__treinos,
            key=lambda treino: treino.Pace()
        )

        print(treino_rapido)

    def __buscar_por_id(self, id):
        for treino in self.__treinos:
            if treino.getId() == id:
                return treino

        return None

    def Main(self):
        while True:
            self.Menu()

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.Inserir()

            elif opcao == "2":
                self.Listar()

            elif opcao == "3":
                self.Listar_Id()

            elif opcao == "4":
                self.Atualizar()

            elif opcao == "5":
                self.Excluir()

            elif opcao == "6":
                self.MaisRapido()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    ui = TreinoUI()
    ui.Main()
