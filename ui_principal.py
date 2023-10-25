# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 478)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contato = QPushButton(self.frame)
        self.btn_contato.setObjectName(u"btn_contato")

        self.horizontalLayout.addWidget(self.btn_contato)

        self.btn_outro = QPushButton(self.frame)
        self.btn_outro.setObjectName(u"btn_outro")

        self.horizontalLayout.addWidget(self.btn_outro)


        self.verticalLayout.addWidget(self.frame)

        self.page = QStackedWidget(self.centralwidget)
        self.page.setObjectName(u"page")
        self.pg_table = QWidget()
        self.pg_table.setObjectName(u"pg_table")
        self.verticalLayout_7 = QVBoxLayout(self.pg_table)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(self.pg_table)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tables = QWidget()
        self.tables.setObjectName(u"tables")
        self.verticalLayout_6 = QVBoxLayout(self.tables)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_file = QLineEdit(self.tables)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_3.addWidget(self.txt_file)

        self.btn_abrir = QPushButton(self.tables)
        self.btn_abrir.setObjectName(u"btn_abrir")

        self.horizontalLayout_3.addWidget(self.btn_abrir)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.tables)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.tw_estoque = QTreeWidget(self.tables)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_2.addWidget(self.tw_estoque)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tables)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tables)
        self.tw_saida.setObjectName(u"tw_saida")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.frame_2 = QFrame(self.tables)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_importar = QPushButton(self.frame_2)
        self.btn_importar.setObjectName(u"btn_importar")

        self.verticalLayout_3.addWidget(self.btn_importar)

        self.btn_gerarSaida = QPushButton(self.frame_2)
        self.btn_gerarSaida.setObjectName(u"btn_gerarSaida")

        self.verticalLayout_3.addWidget(self.btn_gerarSaida)

        self.btn_estorno = QPushButton(self.frame_2)
        self.btn_estorno.setObjectName(u"btn_estorno")

        self.verticalLayout_3.addWidget(self.btn_estorno)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tables, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_7.addWidget(self.tabWidget)

        self.page.addWidget(self.pg_table)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.pg_cadastro)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)

        self.label_6 = QLabel(self.pg_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.pg_cadastro)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.txt_cadNome = QLineEdit(self.pg_cadastro)
        self.txt_cadNome.setObjectName(u"txt_cadNome")

        self.horizontalLayout_10.addWidget(self.txt_cadNome)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.pg_cadastro)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_9.addWidget(self.label_8)

        self.txt_cadUsuario = QLineEdit(self.pg_cadastro)
        self.txt_cadUsuario.setObjectName(u"txt_cadUsuario")

        self.horizontalLayout_9.addWidget(self.txt_cadUsuario)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.pg_cadastro)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.txt_cadSenha = QLineEdit(self.pg_cadastro)
        self.txt_cadSenha.setObjectName(u"txt_cadSenha")

        self.horizontalLayout_8.addWidget(self.txt_cadSenha)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.txt_cadSenha2 = QLineEdit(self.pg_cadastro)
        self.txt_cadSenha2.setObjectName(u"txt_cadSenha2")

        self.horizontalLayout_7.addWidget(self.txt_cadSenha2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.pg_cadastro)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.cb_perfil = QComboBox(self.pg_cadastro)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")

        self.horizontalLayout_6.addWidget(self.cb_perfil)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.pg_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.btn_cadUsuario = QPushButton(self.pg_cadastro)
        self.btn_cadUsuario.setObjectName(u"btn_cadUsuario")

        self.horizontalLayout_11.addWidget(self.btn_cadUsuario)

        self.label_14 = QLabel(self.pg_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_11.addWidget(self.label_14)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.page.addWidget(self.pg_cadastro)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout_2 = QHBoxLayout(self.pg_home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.pg_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label)

        self.page.addWidget(self.pg_home)

        self.verticalLayout.addWidget(self.page)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.btn_pg_cadastro = QPushButton(self.centralwidget)
        self.btn_pg_cadastro.setObjectName(u"btn_pg_cadastro")

        self.horizontalLayout_5.addWidget(self.btn_pg_cadastro)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.page.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_tables.setText(QCoreApplication.translate("MainWindow", u"Tables", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_outro.setText(QCoreApplication.translate("MainWindow", u"Outro", None))
        self.btn_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("MainWindow", u"Valor Nfe", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("MainWindow", u"Especie", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("MainWindow", u"UN", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("MainWindow", u"Quantidade", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("MainWindow", u"Cod Item", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Municipio", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Saida", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("MainWindow", u"Usuario", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("MainWindow", u"Data Saida", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("MainWindow", u"Data Importa\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("MainWindow", u"Serie", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Nfe", None));
        self.btn_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.btn_gerarSaida.setText(QCoreApplication.translate("MainWindow", u"Gerar Saida", None))
        self.btn_estorno.setText(QCoreApplication.translate("MainWindow", u"Estorno", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tables), QCoreApplication.translate("MainWindow", u"TreeWidget", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Tela de Cadastro</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Cadastrar Usuario</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.txt_cadUsuario.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Senha:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Perfil:", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_13.setText("")
        self.btn_cadUsuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_14.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#2124ff;\"><br/></span></p><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#2124ff;\">StackCodes</span></p><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#2124ff;\">Sistema de Gerenciamento</span></p></body></html>", None))
        self.label_4.setText("")
        self.btn_pg_cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usuario", None))
        self.label_5.setText("")
    # retranslateUi

