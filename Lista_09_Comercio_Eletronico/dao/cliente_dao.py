from dao.database import conectar
from model.cliente import Cliente

class ClienteDAO:
    @staticmethod
    def inserir(cliente):
        with conectar() as conexao:
            cursor = conexao.execute(
                "INSERT INTO cliente (nome, email, fone) VALUES (?, ?, ?)",
                (cliente.nome, cliente.email, cliente.fone)
            )
            cliente.id = cursor.lastrowid
            return cliente.id

    @staticmethod
    def listar():
        with conectar() as conexao:
            registros = conexao.execute(
                "SELECT id, nome, email, fone FROM cliente ORDER BY nome"
            ).fetchall()
            return [Cliente(r["nome"], r["email"], r["fone"], r["id"]) for r in registros]

    @staticmethod
    def listar_id(id):
        with conectar() as conexao:
            r = conexao.execute(
                "SELECT id, nome, email, fone FROM cliente WHERE id = ?", (id,)
            ).fetchone()
            if r is None:
                return None
            return Cliente(r["nome"], r["email"], r["fone"], r["id"])

    @staticmethod
    def atualizar(cliente):
        with conectar() as conexao:
            cursor = conexao.execute(
                "UPDATE cliente SET nome = ?, email = ?, fone = ? WHERE id = ?",
                (cliente.nome, cliente.email, cliente.fone, cliente.id)
            )
            return cursor.rowcount > 0

    @staticmethod
    def excluir(id):
        with conectar() as conexao:
            cursor = conexao.execute("DELETE FROM cliente WHERE id = ?", (id,))
            return cursor.rowcount > 0
