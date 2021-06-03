from Controller import banco
from Controller import banco
from View import login
from PyQt5 import QtWidgets

import sys
def main():
    banco.validar_usuario("luis", "unisa123")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = login.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


main()

