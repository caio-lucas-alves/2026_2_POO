
import json
import os
from Cliente import Cliente


class ClienteDAO:
    clientes = []

    def Inserir(self, cliente):
        if self.Listar_Id(cliente.get_id()) is not None:
            print("ID já cadastrado.")
            return False

        self.clientes.append(cliente)
        self.Salvar()
        return True

    def Listar(self):
        return self.clientes

    def Listar_Id(self, id):
        for cliente in self.clientes:
            if cliente.get_id() == id:
                return cliente
        return None

    def Atualizar(self, id, nome, email, telefone):
        cliente = self.Listar_Id(id)

        if cliente is not None:
            cliente.set_nome(nome)
            cliente.set_email(email)
            cliente.set_telefone(telefone)
            self.Salvar()
            return True

        return False

    def Excluir(self, id):
        cliente = self.Listar_Id(id)

        if cliente is not None:
            self.clientes.remove(cliente)
            self.Salvar()
            return True

        return False

    def Abrir(self):
        if os.path.exists("clientes.json"):
            try:
                with open("clientes.json", "r", encoding="utf-8") as arquivo:
                    dados = json.load(arquivo)

                self.clientes.clear()

                for dado in dados:
                    cliente = Cliente(
                        dado["id"],
                        dado["nome"],
                        dado["email"],
                        dado["telefone"]
                    )
                    self.clientes.append(cliente)

            except (json.JSONDecodeError, KeyError, TypeError):
                print("Erro ao abrir o arquivo.")

    def Salvar(self):
        dados = []

        for cliente in self.clientes:
            dados.append({
                "id": cliente.get_id(),
                "nome": cliente.get_nome(),
                "email": cliente.get_email(),
                "telefone": cliente.get_telefone()
            })

        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
