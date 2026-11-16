class ClienteDAO:
    def __init__(self):
        self.clientes = []
        self.proximo_id = 1

    def inserir(self, cliente):
        cliente.id = self.proximo_id
        self.proximo_id += 1
        self.clientes.append(cliente)

    def listar(self):
        return self.clientes

    def listar_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def atualizar(self, cliente_novo):
        for i in range(len(self.clientes)):
            if self.clientes[i].id == cliente_novo.id:
                self.clientes[i] = cliente_novo
                return True
        return False

    def excluir(self, id):
        cliente = self.listar_id(id)

        if cliente is not None:
            self.clientes.remove(cliente)
            return True

        return False