
from Cliente import Cliente
from ClienteDAO import ClienteDAO


class UI:
    def __init__(self):
        self.dao = ClienteDAO()
        self.dao.Abrir()

    def Menu(self):
        print("\n===== SISTEMA DE COMÉRCIO ELETRÔNICO =====")
        print("1 - Listar clientes")
        print("2 - Inserir cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("0 - Finalizar")

    def Listar(self):
        clientes = self.dao.Listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)

    def Inserir(self):
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")

            cliente = Cliente(id, nome, email, telefone)

            if self.dao.Inserir(cliente):
                print("Cliente cadastrado com sucesso.")

        except ValueError:
            print("Digite um ID válido.")

    def Atualizar(self):
        try:
            id = int(input("Digite o ID do cliente: "))
            cliente = self.dao.Listar_Id(id)

            if cliente is None:
                print("Cliente não encontrado.")
            else:
                nome = input("Novo nome: ")
                email = input("Novo e-mail: ")
                telefone = input("Novo telefone: ")

                if self.dao.Atualizar(id, nome, email, telefone):
                    print("Cliente atualizado com sucesso.")

        except ValueError:
            print("Digite um ID válido.")

    def Excluir(self):
        try:
            id = int(input("Digite o ID do cliente: "))

            if self.dao.Excluir(id):
                print("Cliente excluído com sucesso.")
            else:
                print("Cliente não encontrado.")

        except ValueError:
            print("Digite um ID válido.")

    def Main(self):
        while True:
            self.Menu()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.Listar()
            elif opcao == "2":
                self.Inserir()
            elif opcao == "3":
                self.Atualizar()
            elif opcao == "4":
                self.Excluir()
            elif opcao == "0":
                print("Programa finalizado.")
                break
            else:
                print("Opção inválida.")
