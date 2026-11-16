class ProdutoDAO:
    def __init__(self):
        self.produtos = []
        self.proximo_id = 1

    def inserir(self, produto):
        produto.id = self.proximo_id
        self.proximo_id += 1
        self.produtos.append(produto)

    def listar(self):
        return self.produtos

    def listar_id(self, id):
        for produto in self.produtos:
            if produto.id == id:
                return produto
        return None

    def atualizar(self, produto_novo):
        for i in range(len(self.produtos)):
            if self.produtos[i].id == produto_novo.id:
                self.produtos[i] = produto_novo
                return True
        return False

    def excluir(self, id):
        produto = self.listar_id(id)

        if produto is not None:
            self.produtos.remove(produto)
            return True

        return False

    def reajustar(self, percentual):
        for produto in self.produtos:
            produto.preco = produto.preco + produto.preco * percentual / 100