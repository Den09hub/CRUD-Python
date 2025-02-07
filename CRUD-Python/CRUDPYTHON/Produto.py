from Database import Database

class Produto:
    def __init__(self) -> None:
        self.nome = None
        self.descricao = None
        self.marca = None
        self.modelo = None
        self.preco = None
        self.qte = None
        self.cor = None
        self.peso = None
        self.banco = Database()

    def cadastrar_prod(self):
        tupla_prod = (self.nome, self.descricao, self.marca, self.modelo, self.preco, self.qte, self.cor, self.peso)
        res = self.banco.insert_prod(tupla_prod)
        return res
    
    def listar_prod(self):
        res = self.banco.select_prod()
        return res
    
    def listar_por_idprod(self, id_prod):
        res = self.banco.select_by_idprod(id_prod)
        return res
    
    def atualizar_prod(self, indice):
        res = self.banco.update_prod(indice)
        return res
    
    def excluir_prod(self, id_prod):
        res = self.banco.delete_prod(id_prod)
        return res


    