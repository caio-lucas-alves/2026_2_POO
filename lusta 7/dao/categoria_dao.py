class CategoriaDAO:
    def __init__(self):
        self.categorias = []
        self.proximo_id = 1

    def inserir(self, categoria):
        categoria.id = self.proximo_id
        self.proximo_id += 1
        self.categorias.append(categoria)

    def listar(self):
        return self.categorias

    def listar_id(self, id):
        for categoria in self.categorias:
            if categoria.id == id:
                return categoria
        return None

    def atualizar(self, categoria_nova):
        for i in range(len(self.categorias)):
            if self.categorias[i].id == categoria_nova.id:
                self.categorias[i] = categoria_nova
                return True
        return False

    def excluir(self, id):
        categoria = self.listar_id(id)

        if categoria is not None:
            self.categorias.remove(categoria)
            return True

        return False