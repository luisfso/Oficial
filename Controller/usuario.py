from ..View import login
from PyQt5 import QtWidgets
class usuario:
    def __init__(self, id,usuario,senha,email):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.email = email

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())