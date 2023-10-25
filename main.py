import sys
from PySide2.QtWidgets import *
from ui_tela_login import Ui_Form
from ui_principal import Ui_MainWindow
from database import DataBase



class Login(QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Sistema")

        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):
        if self.txt_senha.text() == '123':
            self.w = MainWindown()
            self.w.show()
            self.close()

        else:
            print('Senha Invalida')

class MainWindown(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindown, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Tela Principal")

        self.btn_home.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_table))
        self.btn_pg_cadastro.clicked.connect(lambda: self.page.setCurrentWidget(self.pg_cadastro))

        self.btn_cadUsuario.clicked.connect(self.cadastrar_usuario)

    def cadastrar_usuario(self):
        if self.txt_cadSenha.text() != self.txt_cadSenha2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Senhas Diferentes")
            msg.exec_()
            return None

        nome = self.txt_cadNome.text()
        user = self.txt_cadUsuario.text()
        password = self.txt_cadSenha.text()
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Cadastro Realizado com Sucesso!!")
        msg.exec_()

        self.txt_cadNome.setText("")
        self.txt_cadUsuario.setText("")
        self.txt_cadSenha.setText("")
        self.txt_cadSenha2.setText("")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()

    app.exec_()