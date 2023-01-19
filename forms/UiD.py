from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.addForm import Ui_addForm
import sys
import sqlite3

FormD, WindowD = uic.loadUiType("forms/addForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()

class UiD(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiD, self).__init__(parent)
        self.uid = Ui_addForm()
        self.uid.setupUi(self)
        self.uid.spinBox.setEnabled(False)
        self.uid.addButton.clicked.connect(self.addButtonPresed)
        self.uid.lineEdit.textChanged.connect(self.lineTextChanged)
        self.uid.textEdit.textChanged.connect(self.textTextChanged)


    def addButtonPresed(self):
        if self.uid.lineEdit.text() != "" and self.uid.textEdit.toPlainText() != "":
            pass


    def loadForm(self):
        self.uid.spinBox.setValue(sql.execute("SELECT MAX(order_id) FROM orders").fetchone()[0] + 1)
        self.uid.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        self.uid.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit_2.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        for value in  sql.execute("SELECT name FROM type_of_work"):
            self.uid.comboBox.addItem(value[0])
        for value in  sql.execute("SELECT last_name FROM masters"):
            self.uid.comboBox_2.addItem(value[0])
        for value in  sql.execute("SELECT name FROM completion_mark"):
            self.uid.comboBox_3.addItem(value[0])


    def showEvent(self, event):
        self.loadForm()

    def lineTextChanged(self):
        if self.uid.lineEdit.text() == "":
            self.uid.lineEdit.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uid.lineEdit.setStyleSheet("QLineEdit {background-color: White;}")

    def textTextChanged(self):
        if self.uid.textEdit.toPlainText() == "":
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        else:
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

    def addOrders(self):
        sql.
""" def closeEvent(self, event):
        return 1

    def showEvent(self, event):
        print("Ало")"""