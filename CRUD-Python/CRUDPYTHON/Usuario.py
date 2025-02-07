####CONTROLE####
from Database import Database

class Usuario:
    def __init__(self) -> None:
        self.nome = None
        self.cpf = None
        self.email = None
        self.senha = None
        self.banco = Database()

    def cadastrar(self):
        tupla = (self.nome, self.cpf, self.email, self.senha)
        res = self.banco.insert(tupla)
        return res

    def listar(self):
        res = self.banco.select()
        return res
    
    def lista_por_id(self, id):
        res = self.banco.select_by_id(id)
        return res
    
    def atualizar(self, lista):
        res = self.banco.update(lista)
        return res
    
    def excluir(self, id):
        res = self.banco.delete(id)
        return res