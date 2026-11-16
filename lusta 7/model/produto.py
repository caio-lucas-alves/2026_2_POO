class Produto:
    def __init__(self, id, descricao, preco, estoque, idCategoria):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria

    def __str__(self):
        return f"ID: {self.id} | Produto: {self.descricao} | Preço: R$ {self.preco:.2f} | Estoque: {self.estoque} | Categoria: {self.idCategoria}"