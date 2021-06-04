# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_estoque2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(623, 762)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(self.centralwidget)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_superior.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_superior.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_superior_esquerdo = QtWidgets.QFrame(self.frame_superior)
        self.frame_superior_esquerdo.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.frame_superior_esquerdo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_superior_esquerdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior_esquerdo.setObjectName("frame_superior_esquerdo")
        self.frame = QtWidgets.QFrame(self.frame_superior_esquerdo)
        self.frame.setGeometry(QtCore.QRect(0, 10, 141, 101))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.horizontalLayout.addWidget(self.frame_superior_esquerdo)
        self.frame_dados = QtWidgets.QFrame(self.frame_superior)
        self.frame_dados.setMaximumSize(QtCore.QSize(250, 60))
        self.frame_dados.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_dados.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"border-radius: 5px;\n"
"")
        self.frame_dados.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_dados.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dados.setObjectName("frame_dados")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_dados)
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_usuario = QtWidgets.QLabel(self.frame_dados)
        self.label_usuario.setObjectName("label_usuario")
        self.verticalLayout_2.addWidget(self.label_usuario)
        self.label_email = QtWidgets.QLabel(self.frame_dados)
        self.label_email.setObjectName("label_email")
        self.verticalLayout_2.addWidget(self.label_email)
        self.horizontalLayout.addWidget(self.frame_dados)
        self.frame_avatar = QtWidgets.QFrame(self.frame_superior)
        self.frame_avatar.setMinimumSize(QtCore.QSize(120, 120))
        self.frame_avatar.setMaximumSize(QtCore.QSize(120, 120))
        self.frame_avatar.setStyleSheet("QFrame{\n"
"    background-image: url(:/avatar/images/ursinho.png);\n"
"    background-position: center;\n"
"    border-radius: 60px;\n"
"    border: 8px solid rgb(243, 243, 243);\n"
"}")
        self.frame_avatar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avatar.setObjectName("frame_avatar")
        self.horizontalLayout.addWidget(self.frame_avatar)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_central = QtWidgets.QFrame(self.centralwidget)
        self.frame_central.setStyleSheet("background-color: rgb(60, 60, 100);")
        self.frame_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_central.setObjectName("frame_central")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_central)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_central)
        self.tableWidget.setStyleSheet("background-color: rgb(117, 80, 123);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame_central)
        self.frame_inferior = QtWidgets.QFrame(self.centralwidget)
        self.frame_inferior.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_inferior.setStyleSheet("background-color: rgb(52, 101, 164);")
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_inserir_novo = QtWidgets.QPushButton(self.frame_inferior)
        self.pushButton_inserir_novo.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_inserir_novo.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(43, 116, 168);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(26, 50, 133);\n"
"    border: 2px solid rgb(114, 159, 207);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(255, 255, 191);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_inserir_novo.setObjectName("pushButton_inserir_novo")
        self.horizontalLayout_2.addWidget(self.pushButton_inserir_novo)
        self.pushButton_atualizat = QtWidgets.QPushButton(self.frame_inferior)
        self.pushButton_atualizat.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_atualizat.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_atualizat.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(43, 116, 168);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(26, 50, 133);\n"
"    border: 2px solid rgb(114, 159, 207);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(255, 255, 191);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_atualizat.setObjectName("pushButton_atualizat")
        self.horizontalLayout_2.addWidget(self.pushButton_atualizat)
        self.pushButton_excluir = QtWidgets.QPushButton(self.frame_inferior)
        self.pushButton_excluir.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_excluir.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(43, 116, 168);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(26, 50, 133);\n"
"    border: 2px solid rgb(114, 159, 207);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(255, 255, 191);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.horizontalLayout_2.addWidget(self.pushButton_excluir)
        self.pushButton_aumentar_estoque = QtWidgets.QPushButton(self.frame_inferior)
        self.pushButton_aumentar_estoque.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_aumentar_estoque.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(43, 116, 168);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(26, 50, 133);\n"
"    border: 2px solid rgb(114, 159, 207);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(255, 255, 191);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_aumentar_estoque.setObjectName("pushButton_aumentar_estoque")
        self.horizontalLayout_2.addWidget(self.pushButton_aumentar_estoque)
        self.verticalLayout.addWidget(self.frame_inferior)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 623, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Itens:"))
        self.label_3.setText(_translate("MainWindow", "Estoque:"))
        self.label_5.setText(_translate("MainWindow", "100"))
        self.label_4.setText(_translate("MainWindow", "99"))
        self.label.setText(_translate("MainWindow", "Estatistica:"))
        self.label_usuario.setText(_translate("MainWindow", "Usuario: luis"))
        self.label_email.setText(_translate("MainWindow", "Email: luisfernando@gmail.com"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Valor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Estoque"))
        self.pushButton_inserir_novo.setText(_translate("MainWindow", "Inserir Novo"))
        self.pushButton_atualizat.setText(_translate("MainWindow", "Atualizar"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))
        self.pushButton_aumentar_estoque.setText(_translate("MainWindow", "Incrementar"))
import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
