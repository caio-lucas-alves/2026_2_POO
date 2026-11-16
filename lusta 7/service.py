from model.cliente import Cliente
from model.categoria import Categoria
from model.produto import Produto

from dao.cliente_dao import ClienteDAO
from dao.categoria_dao import CategoriaDAO
from dao.produto_dao import ProdutoDAO


class Service:
    cliente_dao = ClienteDAO()
    categoria_dao = CategoriaDAO()
    produto_dao = ProdutoDAO()

    @staticmethod
    def cliente_inserir(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        Service.cliente_dao.inserir(cliente)

    @staticmethod
    def cliente_listar():
        return Service.cliente_dao.listar()

    @staticmethod
    def cliente_listar_id(id):
        return Service.cliente_dao.listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        return Service.cliente_dao.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        return Service.cliente_dao.excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        categoria = Categoria(0, descricao)
        Service.categoria_dao.inserir(categoria)

    @staticmethod
    def categoria_listar():
        return Service.categoria_dao.listar()

    @staticmethod
    def categoria_listar_id(id):
        return Service.categoria_dao.listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        categoria = Categoria(id, descricao)
        return Service.categoria_dao.atualizar(categoria)

    @staticmethod
    def categoria_excluir(id):
        for produto in Service.produto_listar():
            if produto.idCategoria == id:
                return False

        return Service.categoria_dao.excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, idCategoria):
        if Service.categoria_listar_id(idCategoria) is None:
            return False

        produto = Produto(0, descricao, preco, estoque, idCategoria)
        Service.produto_dao.inserir(produto)
        return True

    @staticmethod
    def produto_listar():
        return Service.produto_dao.listar()

    @staticmethod
    def produto_listar_id(id):
        return Service.produto_dao.listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        if Service.categoria_listar_id(idCategoria) is None:
            return False

        produto = Produto(id, descricao, preco, estoque, idCategoria)
        return Service.produto_dao.atualizar(produto)

    @staticmethod
    def produto_excluir(id):
        return Service.produto_dao.excluir(id)

    @staticmethod
    def produto_reajustar(percentual):
        if percentual < -100:
            return False

        Service.produto_dao.reajustar(percentual)
        return True