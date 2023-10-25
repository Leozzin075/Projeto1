# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(595, 424)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(595, 424))
        Form.setMaximumSize(QSize(595, 424))
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(140, 60, 311, 281))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255,0.3);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.txt_login = QLineEdit(self.frame)
        self.txt_login.setObjectName(u"txt_login")
        self.txt_login.setEnabled(True)
        font = QFont()
        font.setPointSize(13)
        self.txt_login.setFont(font)

        self.verticalLayout.addWidget(self.txt_login)

        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEnabled(True)
        self.txt_senha.setFont(font)
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.txt_senha)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout.addWidget(self.btn_login)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#0000ff;\">Login</span></p></body></html>", None))
        self.txt_login.setText("")
        self.txt_login.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"Entrar", None))
    # retranslateUi

