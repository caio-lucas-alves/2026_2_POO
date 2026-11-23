class Produto:
    def __init__(self, descricao, preco, estoque, idCategoria, id=None):
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
