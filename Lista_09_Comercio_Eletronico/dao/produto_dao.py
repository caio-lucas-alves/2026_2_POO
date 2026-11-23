from dao.database import conectar
from model.produto import Produto

class ProdutoDAO:
    @staticmethod
    def inserir(produto):
        with conectar() as conexao:
            cursor = conexao.execute(
                """INSERT INTO produto
                   (descricao, preco, estoque, idCategoria)
                   VALUES (?, ?, ?, ?)""",
                (produto.descricao, produto.preco, produto.estoque, produto.idCategoria)
            )
            produto.id = cursor.lastrowid
            return produto.id

    @staticmethod
    def listar():
        with conectar() as conexao:
            registros = conexao.execute(
                """SELECT id, descricao, preco, estoque, idCategoria
                   FROM produto ORDER BY descricao"""
            ).fetchall()
            return [
                Produto(r["descricao"], r["preco"], r["estoque"], r["idCategoria"], r["id"])
                for r in registros
            ]

    @staticmethod
    def listar_id(id):
        with conectar() as conexao:
            r = conexao.execute(
                """SELECT id, descricao, preco, estoque, idCategoria
                   FROM produto WHERE id = ?""", (id,)
            ).fetchone()
            if r is None:
                return None
            return Produto(r["descricao"], r["preco"], r["estoque"], r["idCategoria"], r["id"])

    @staticmethod
    def atualizar(produto):
        with conectar() as conexao:
            cursor = conexao.execute(
                """UPDATE produto
                   SET descricao = ?, preco = ?, estoque = ?, idCategoria = ?
                   WHERE id = ?""",
                (produto.descricao, produto.preco, produto.estoque,
                 produto.idCategoria, produto.id)
            )
            return cursor.rowcount > 0

    @staticmethod
    def excluir(id):
        with conectar() as conexao:
            cursor = conexao.execute("DELETE FROM produto WHERE id = ?", (id,))
            return cursor.rowcount > 0

    @staticmethod
    def reajustar(percentual):
        with conectar() as conexao:
            conexao.execute(
                "UPDATE produto SET preco = ROUND(preco * (1 + ? / 100.0), 2)",
                (percentual,)
            )
