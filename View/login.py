# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Controller import banco
from View import view_estoque
from Model import usuario

class Ui_MainWindow(object):

    """
    def chamar_interface(self,objeto):
        mostrar = usuario.Usuario(objeto[0][0],objeto[0][1],objeto[0][2],objeto[0][3])
        print("-"*30)
        print(mostrar.get_id())
        print(mostrar.get_nome())
        print(mostrar.get_senha())
        print(mostrar.get_email())
        banco.listar_produtos()
"""
    def check_campos(self):

        textoUsuario = ""
        textoSenha = ""
        if not self.lineEdit_usuario.text():
                textousuario = " Usuario vazio! "
        else:
                textousuario = ""
        if not self.lineEdit_senha.text():
                textoSenha = " Senha vazia! "
        else:
                textoSenha = ""
        #if True:
        if not (textousuario + textoSenha):
                if self.checkBox.isChecked():
                        teste = banco.validar_usuario(self.lineEdit_usuario.text(), self.lineEdit_senha.text())
                        #teste = banco.validar_usuario("unisa", "unisa123")
                        if not teste:
                                self.label_erro.setText("Dados invalido!")
                                self.frame_erro_login.show()
                        else:
                                self.frame_erro_login.hide()
                                #self.chamar_interface(teste)
                                return False


                else:
                        self.label_erro.setText("Por favor, concorde com os termos!")
                        self.frame_erro_login.show()
        else:
                self.label_erro.setText(textousuario+textoSenha)
                self.frame_erro_login.show()

    def setupUi(self, MainWindow):




        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(547, 700)
        MainWindow.setMinimumSize(QtCore.QSize(500, 700))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icones/images/My-Documents-icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(219, 219, 219);\n"
"background-color: rgb(43, 116, 168);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_superior = QtWidgets.QFrame(self.centralwidget)
        self.frame_superior.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_superior.setStyleSheet("")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_erro_login = QtWidgets.QFrame(self.frame_superior)
        self.frame_erro_login.setMaximumSize(QtCore.QSize(430, 16777215))
        self.frame_erro_login.setStyleSheet("background-color: rgb(204, 0, 0);\n"
"border-radius: 8px;")
        self.frame_erro_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_erro_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro_login.setObjectName("frame_erro_login")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_erro_login)
        self.horizontalLayout_3.setContentsMargins(8, 3, 8, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_erro = QtWidgets.QLabel(self.frame_erro_login)
        self.label_erro.setAlignment(QtCore.Qt.AlignCenter)
        self.label_erro.setObjectName("label_erro")
        self.horizontalLayout_3.addWidget(self.label_erro)
        self.pushButton_fechar_erro = QtWidgets.QPushButton(self.frame_erro_login)
        self.pushButton_fechar_erro.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_fechar_erro.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_fechar_erro.setStyleSheet("QPushButton {\n"
"    background-image: url(:/icones/images/fechar.png);\n"
"    background-position: center;\n"
"    border-radius 8px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(226, 129, 63);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(252, 233, 79);\n"
"}")
        self.pushButton_fechar_erro.setText("")
        self.pushButton_fechar_erro.setObjectName("pushButton_fechar_erro")
        self.horizontalLayout_3.addWidget(self.pushButton_fechar_erro)

        self.horizontalLayout_2.addWidget(self.frame_erro_login)
        self.verticalLayout.addWidget(self.frame_superior)
        self.frame_central = QtWidgets.QFrame(self.centralwidget)
        self.frame_central.setStyleSheet("")
        self.frame_central.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_central.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_central.setObjectName("frame_central")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_central)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_login_area = QtWidgets.QFrame(self.frame_central)
        self.frame_login_area.setMaximumSize(QtCore.QSize(430, 550))
        self.frame_login_area.setStyleSheet("background-color: rgb(1, 71, 123);\n"
"border-radius: 10px;")
        self.frame_login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login_area.setObjectName("frame_login_area")
        self.frame_logo_unisa = QtWidgets.QFrame(self.frame_login_area)
        self.frame_logo_unisa.setGeometry(QtCore.QRect(60, 20, 321, 141))
        self.frame_logo_unisa.setStyleSheet("background-image: url(:/Logo/images/unisa.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_logo_unisa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo_unisa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo_unisa.setObjectName("frame_logo_unisa")
        self.frame_avatar = QtWidgets.QFrame(self.frame_login_area)
        self.frame_avatar.setGeometry(QtCore.QRect(160, 180, 120, 120))
        self.frame_avatar.setMinimumSize(QtCore.QSize(120, 120))
        self.frame_avatar.setMaximumSize(QtCore.QSize(120, 120))
        self.frame_avatar.setStyleSheet("QFrame{\n"
"    background-image: url(:/avatar/images/ursinho.png);\n"
"    background-position: center;\n"
"    border-radius: 60px;\n"
"    border: 8px solid rgb(243, 243, 243);\n"
"}")
        self.frame_avatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_avatar.setObjectName("frame_avatar")
        self.lineEdit_usuario = QtWidgets.QLineEdit(self.frame_login_area)
        self.lineEdit_usuario.setGeometry(QtCore.QRect(80, 320, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_usuario.setFont(font)
        self.lineEdit_usuario.setToolTip("")
        self.lineEdit_usuario.setAutoFillBackground(False)
        self.lineEdit_usuario.setStyleSheet("QLineEdit{\n"
"    border: 3px solid rgb(243, 243, 243);\n"
"    background-color: rgb(26, 50, 133);\n"
"    border-radius: 5px;\n"
"    color: rgb(243, 243, 243);\n"
"    padding: 8px;\n"
"}\n"
"QLineEdit:hover{\n"
"        border: 3px solid rgb(114, 159, 207);\n"
"}\n"
"QLineEdit:focus{\n"
"        border: 3px solid rgb(101, 0, 255);\n"
"}")
        self.lineEdit_usuario.setMaxLength(120)
        self.lineEdit_usuario.setObjectName("lineEdit_usuario")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.frame_login_area)
        self.lineEdit_senha.setGeometry(QtCore.QRect(80, 380, 281, 50))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setToolTip("")
        self.lineEdit_senha.setAutoFillBackground(False)
        self.lineEdit_senha.setStyleSheet("QLineEdit{\n"
"    border: 3px solid rgb(243, 243, 243);\n"
"    background-color: rgb(26, 50, 133);\n"
"    border-radius: 5px;\n"
"    color: rgb(243, 243, 243);\n"
"    padding: 8px;\n"
"}\n"
"QLineEdit:hover{\n"
"        border: 3px solid rgb(114, 159, 207);\n"
"}\n"
"QLineEdit:focus{\n"
"        border: 3px solid rgb(101, 0, 255);\n"
"}")
        self.lineEdit_senha.setMaxLength(120)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.checkBox = QtWidgets.QCheckBox(self.frame_login_area)
        self.checkBox.setGeometry(QtCore.QRect(80, 440, 281, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet("QCheckBox::indicator{\n"
"    border: 3px solid rgb(211, 215, 207);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 13px;\n"
"    background-color:  rgb(1, 71, 123);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"    background-image: url(:/icones/images/ok-icon.png);\n"
"    background-position: center;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border: 3px solid rgb(26, 50, 133);\n"
"    background-color: rgb(241, 255, 46);\n"
"}")
        self.checkBox.setObjectName("checkBox")
        self.pushButton_acesso = QtWidgets.QPushButton(self.frame_login_area)
        self.pushButton_acesso.setGeometry(QtCore.QRect(80, 480, 281, 50))
        self.pushButton_acesso.setStyleSheet("QPushButton {    \n"
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
        self.pushButton_acesso.setObjectName("pushButton_acesso")
        self.horizontalLayout.addWidget(self.frame_login_area)
        self.verticalLayout.addWidget(self.frame_central)
        self.frame_inferior = QtWidgets.QFrame(self.centralwidget)
        self.frame_inferior.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_inferior.setStyleSheet("")
        self.frame_inferior.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_inferior.setObjectName("frame_inferior")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_inferior)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(114, 159, 207);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_inferior)
        MainWindow.setCentralWidget(self.centralwidget)


        #função de fechar o aba de erro
        #botão de fechar o pop
        self.pushButton_fechar_erro.clicked.connect(lambda: self.frame_erro_login.hide())       
        #frame erro começa oculto
        self.frame_erro_login.hide()
        self.pushButton_acesso.clicked.connect(lambda: self.check_campos())
        #self.lineEdit_usuario.setText("unisa")
        #self.lineEdit_senha.setText("unisa123")

        #função do botão de acesso
        ###função do botao acesso

        ###



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label_erro.setText(_translate("MainWindow", "TextLabel"))
        self.lineEdit_usuario.setPlaceholderText(_translate("MainWindow", "Usuário:"))
        self.lineEdit_senha.setPlaceholderText(_translate("MainWindow", "Senha:"))
        self.checkBox.setText(_translate("MainWindow", "Concorda com os Termos de Uso?"))
        self.pushButton_acesso.setText(_translate("MainWindow", "Acesso ao Estoque"))
        self.label.setText(_translate("MainWindow", "Desenvolvido por: Luis Fernando"))
from View import recursos_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

