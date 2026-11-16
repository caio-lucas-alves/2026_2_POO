from service import Service


class UI:

    @staticmethod
    def menu():
        print("\n===== SISTEMA DE COMÉRCIO ELETRÔNICO =====")
        print("1 - Inserir cliente")
        print("2 - Listar clientes")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Inserir categoria")
        print("6 - Listar categorias")
        print("7 - Atualizar categoria")
        print("8 - Excluir categoria")
        print("9 - Inserir produto")
        print("10 - Listar produtos")
        print("11 - Atualizar produto")
        print("12 - Excluir produto")
        print("13 - Reajustar preços")
        print("0 - Finalizar")

        return input("Escolha uma opção: ")

    @staticmethod
    def cliente_inserir():
        nome = input("Nome: ")
        email = input("E-mail: ")
        fone = input("Telefone: ")

        Service.cliente_inserir(nome, email, fone)

        print("Cliente cadastrado.")

    @staticmethod
    def cliente_listar():
        clientes = Service.cliente_listar()

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")

        for cliente in clientes:
            print(cliente)

    @staticmethod
    def cliente_atualizar():
        id = int(input("ID do cliente: "))

        if Service.cliente_listar_id(id) is None:
            print("Cliente não encontrado.")
            return

        nome = input("Novo nome: ")
        email = input("Novo e-mail: ")
        fone = input("Novo telefone: ")

        Service.cliente_atualizar(id, nome, email, fone)

        print("Cliente atualizado.")

    @staticmethod
    def cliente_excluir():
        id = int(input("ID do cliente: "))

        if Service.cliente_excluir(id):
            print("Cliente excluído.")
        else:
            print("Cliente não encontrado.")

    @staticmethod
    def categoria_inserir():
        descricao = input("Descrição: ")

        Service.categoria_inserir(descricao)

        print("Categoria cadastrada.")

    @staticmethod
    def categoria_listar():
        categorias = Service.categoria_listar()

        if len(categorias) == 0:
            print("Nenhuma categoria cadastrada.")

        for categoria in categorias:
            print(categoria)

    @staticmethod
    def categoria_atualizar():
        id = int(input("ID da categoria: "))

        if Service.categoria_listar_id(id) is None:
            print("Categoria não encontrada.")
            return

        descricao = input("Nova descrição: ")

        Service.categoria_atualizar(id, descricao)

        print("Categoria atualizada.")

    @staticmethod
    def categoria_excluir():
        id = int(input("ID da categoria: "))

        resultado = Service.categoria_excluir(id)

        if resultado:
            print("Categoria excluída.")
        else:
            print("Não foi possível excluir a categoria.")

    @staticmethod
    def produto_inserir():
        descricao = input("Descrição: ")
        preco = float(input("Preço: R$ ").replace(",", "."))
        estoque = int(input("Estoque: "))

        UI.categoria_listar()

        id_categoria = int(input("ID da categoria: "))

        if Service.produto_inserir(descricao, preco, estoque, id_categoria):
            print("Produto cadastrado.")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def produto_listar():
        produtos = Service.produto_listar()

        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")

        for produto in produtos:
            print(produto)

    @staticmethod
    def produto_atualizar():
        id = int(input("ID do produto: "))

        if Service.produto_listar_id(id) is None:
            print("Produto não encontrado.")
            return

        descricao = input("Nova descrição: ")
        preco = float(input("Novo preço: R$ ").replace(",", "."))
        estoque = int(input("Novo estoque: "))

        UI.categoria_listar()

        id_categoria = int(input("ID da categoria: "))

        if Service.produto_atualizar(id, descricao, preco, estoque, id_categoria):
            print("Produto atualizado.")
        else:
            print("Categoria não encontrada.")

    @staticmethod
    def produto_excluir():
        id = int(input("ID do produto: "))

        if Service.produto_excluir(id):
            print("Produto excluído.")
        else:
            print("Produto não encontrado.")

    @staticmethod
    def produto_reajustar():
        percentual = float(input("Percentual de reajuste: ").replace(",", "."))

        if Service.produto_reajustar(percentual):
            print("Preços atualizados.")
        else:
            print("O desconto não pode ser maior que 100%.")

    @staticmethod
    def main():
        while True:
            opcao = UI.menu()

            if opcao == "1":
                UI.cliente_inserir()

            elif opcao == "2":
                UI.cliente_listar()

            elif opcao == "3":
                UI.cliente_atualizar()

            elif opcao == "4":
                UI.cliente_excluir()

            elif opcao == "5":
                UI.categoria_inserir()

            elif opcao == "6":
                UI.categoria_listar()

            elif opcao == "7":
                UI.categoria_atualizar()

            elif opcao == "8":
                UI.categoria_excluir()

            elif opcao == "9":
                UI.produto_inserir()

            elif opcao == "10":
                UI.produto_listar()

            elif opcao == "11":
                UI.produto_atualizar()

            elif opcao == "12":
                UI.produto_excluir()

            elif opcao == "13":
                UI.produto_reajustar()

            elif opcao == "0":
                print("Aplicação finalizada.")
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    UI.main()