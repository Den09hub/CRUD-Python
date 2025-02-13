import mysql.connector

class Database:
    def __init__(self, banco = 'crud_py'):
        self.banco = banco
        self.conn = None

    def connect(self):
        self.conn = mysql.connector.connect(host = 'localhost', database = 'crud_py', user = 'root', password = '')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            print('Conectado com sucesso!!!')
            print('UUUHHHHUUULLLLLL \\o/')
        else:
            print('Erro')

# Funções do usuário

    def insert(self, tupla):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO usuario (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)', tupla)
            self.conn.commit()
            return True

        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()

    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM usuario")
            dados = self.cursor.fetchall()
            return dados
                
        except Exception as erro:
            return erro

        finally:
            self.close_connection()

    def select_by_id(self, id):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM usuario WHERE id = {id}")
            dados = self.cursor.fetchone()
            return dados
                
        except Exception as erro:
            return erro

        finally:
            self.close_connection()

    def update(self, lista):
        self.connect()
        try:
            self.cursor.execute(f"""
                            UPDATE usuario
                                SET nome = '{lista[1]}',
                                cpf = '{lista[2]}',
                                email = '{lista[3]}',
                                senha = '{lista[4]}'
                                WHERE id = {lista[0]} 
                                """)
            self.conn.commit()
            return True

        except Exception as erro:
            return erro

        finally:
            self.close_connection()


    def delete(self, id):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM usuario where id = {id}")
            self.conn.commit()
            return True

        except Exception as erro:
            return erro

        finally:
            self.close_connection()

# Funções do Produto

    def insert_prod(self, tupla_prod):
        self.connect()
        try:
            self.cursor.execute('INSERT INTO produto (nome, descricao, marca, modelo, preco, qte, cor, peso) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', tupla_prod)
            self.conn.commit()
            return True

        except Exception as erro:
            return erro

        finally:
            self.close_connection()

    def select_prod(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM produto")
            dados = self.cursor.fetchall()
            return dados
                
        except Exception as erro:
            return erro

        finally:
            self.close_connection()

    def select_by_idprod(self, id_prod):
        self.connect()
        try:
            self.cursor.execute(f"SELECT * FROM produto WHERE {id_prod}")
            dados = self.cursor.fetchone()
            return dados
        
        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()

    def update_prod(self, indice):
        self.connect()
        try:
            self.cursor.execute(f"""
                                UPDATE produto
                                SET nome = '{indice[1]}',
                                descricao = '{indice[2]}',
                                marca = '{indice[3]}',
                                modelo = '{indice[4]}',
                                preco = {indice[5]},
                                qte = {indice[6]},
                                cor = '{indice[7]}',
                                peso = '{indice[8]}'
                                WHERE id_prod = {indice[0]}
                                """)
            self.conn.commit()
            return True
            
        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()

    def delete_prod(self, id_prod):
        self.connect()
        try:
            self.cursor.execute(f"DELETE FROM produto where id_prod = {id_prod}")
            self.conn.commit()
            return True
        
        except Exception as erro:
            return erro
        
        finally:
            self.close_connection()

# Fechamento da conexão

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!!!")

# Instanciação

if __name__ == '__main__':
    banco = Database()