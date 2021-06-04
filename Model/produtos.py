class Produtos:
    def __init__(self,id,  nome, valor, num_estoque):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.num_estoque = num_estoque
    def set_name(self,nome):
        self.nome = nome
    def get_name(self):
        return self.nome

    def set_valor(self,valor):
        self.valor = valor
    def get_valor(self):
        return self.valor

    def set_estoque(self,num_estoque):
        self.num_estoque = num_estoque
    def get_estoque(self):
        return self.num_estoque

    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id
