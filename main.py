from Controller import banco
from Controller import banco
from View import login,view_estoque
from PyQt5 import QtWidgets
from Model.usuario import Usuario
import sys
teste = []

def main():
    def fechar():
        ui.check_campos()
        global teste
        teste = banco.validar_usuario(ui.lineEdit_usuario.text(), ui.lineEdit_senha.text())
        if teste:
            usuario = Usuario(teste[0][0],teste[0][1], teste[0][2], teste[0][3])
            MainWindow.close()

#    banco.listar_produtos()
#    banco.validar_usuario("luis", "unisa123")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton_acesso.clicked.connect(lambda: fechar())

    MainWindow.show()
    app.exec_()
    segundatela(teste)


def segundatela(var):
    f = open('test.txt', 'w')
    f.write(var[0][1])
    f.close()
    global app
    print("--"*40)
    print("--"*40)
    print("--"*40)

    print(var)
    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
        app = QtGui.QApplication(sys.argv)
    mainEstoque = QtWidgets.QMainWindow()
    ui2 = view_estoque.Ui_MainWindow()
    ui2.setupUi(mainEstoque)
    mainEstoque.show()
    app.exec_()

def aff():
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

main()

