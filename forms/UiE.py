from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.editForm import Ui_editForm
import sys
import sqlite3

FormD, WindowD = uic.loadUiType("forms/editForm.ui")


class UiE(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiE, self).__init__(parent)
        self.uid = Ui_editForm()
        self.uid.setupUi(self)
        self.uid.spinBox.setEnabled(False)
        self.uid.addButton.clicked.connect(self.addButtonPresed)
        self.uid.textEdit.textChanged.connect(self.textTextChanged)
        self.uid.lineEdit_2.textChanged.connect(self.line2TextChanged)
        self.uid.lineEdit_3.textChanged.connect(self.line3TextChanged)
        self.db = sqlite3.connect('identifier.sqlite')
        self.sql = self.db.cursor()

    def addButtonPresed(self):
        if self.uid.textEdit.toPlainText() == "":
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        elif self.uid.lineEdit_3.text() == "":
            self.uid.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uid.lineEdit_2.text() == "" or not self.uid.lineEdit_2.text().isdigit():
            self.uid.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.addOrders()

    def loadForm(self):
        pass

    def showEvent(self, event):
        self.loadForm()

    def textTextChanged(self):
        if self.uid.textEdit.toPlainText() == "":
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        else:
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

    def line2TextChanged(self):
        if self.uid.lineEdit_2.text() == "":
            self.uid.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uid.lineEdit_2.setStyleSheet("QLineEdit {background-color: White;}")

    def line3TextChanged(self):
        if self.uid.lineEdit_3.text() == "":
            self.uid.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uid.lineEdit_3.setStyleSheet("QLineEdit {background-color: White;}")

    def editOrders(self):
        pass
