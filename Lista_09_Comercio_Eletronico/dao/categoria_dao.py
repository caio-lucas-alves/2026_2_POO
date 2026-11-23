from dao.database import conectar
from model.categoria import Categoria

class CategoriaDAO:
    @staticmethod
    def inserir(categoria):
        with conectar() as conexao:
            cursor = conexao.execute(
                "INSERT INTO categoria (descricao) VALUES (?)",
                (categoria.descricao,)
            )
            categoria.id = cursor.lastrowid
            return categoria.id

    @staticmethod
    def listar():
        with conectar() as conexao:
            registros = conexao.execute(
                "SELECT id, descricao FROM categoria ORDER BY descricao"
            ).fetchall()
            return [Categoria(r["descricao"], r["id"]) for r in registros]

    @staticmethod
    def listar_id(id):
        with conectar() as conexao:
            r = conexao.execute(
                "SELECT id, descricao FROM categoria WHERE id = ?", (id,)
            ).fetchone()
            if r is None:
                return None
            return Categoria(r["descricao"], r["id"])

    @staticmethod
    def atualizar(categoria):
        with conectar() as conexao:
            cursor = conexao.execute(
                "UPDATE categoria SET descricao = ? WHERE id = ?",
                (categoria.descricao, categoria.id)
            )
            return cursor.rowcount > 0

    @staticmethod
    def excluir(id):
        with conectar() as conexao:
            cursor = conexao.execute("DELETE FROM categoria WHERE id = ?", (id,))
            return cursor.rowcount > 0
