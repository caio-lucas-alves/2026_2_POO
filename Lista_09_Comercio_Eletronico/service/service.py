from model.cliente import Cliente
from model.categoria import Categoria
from model.produto import Produto
from dao.cliente_dao import ClienteDAO
from dao.categoria_dao import CategoriaDAO
from dao.produto_dao import ProdutoDAO

class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(nome.strip(), email.strip(), fone.strip())
        return ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(nome.strip(), email.strip(), fone.strip(), id)
        return ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        return ClienteDAO.excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        categoria = Categoria(descricao.strip())
        return CategoriaDAO.inserir(categoria)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO.listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = Categoria(descricao.strip(), id)
        return CategoriaDAO.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        return CategoriaDAO.excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        produto = Produto(descricao.strip(), float(preco), int(estoque), int(idCategoria))
        return ProdutoDAO.inserir(produto)

    @staticmethod
    def produto_listar():
        return ProdutoDAO.listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        produto = Produto(descricao.strip(), float(preco), int(estoque), int(idCategoria), id)
        return ProdutoDAO.atualizar(produto)

    @staticmethod
    def produto_excluir(id):
        return ProdutoDAO.excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        ProdutoDAO.reajustar(float(percentual))
