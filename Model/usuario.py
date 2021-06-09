from View import login
from PyQt5 import QtWidgets

class Usuario:
    def __init__(self, id,nome,senha,email):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.email = email

    def get_nome(self):
        return self.nome
    def get_id(self):
        return self.id
    def get_senha(self):
        return self.senha
    def get_email(self):
        return self.email
