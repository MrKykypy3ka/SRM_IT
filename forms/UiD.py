from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.addForm import Ui_addForm
import sys
import sqlite3

FormD, WindowD = uic.loadUiType("forms/addForm.ui")


class UiD(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiD, self).__init__(parent)
        self.uid = Ui_addForm()
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
        if self.uid.lineEdit_3.text() == "":
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        if self.uid.lineEdit_2.text() == "":
            self.uid.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        else:
            self.addOrders()

    def loadForm(self):
        self.uid.spinBox.setValue(self.sql.execute("SELECT MAX(order_id) FROM orders").fetchone()[0] + 1)
        self.uid.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        self.uid.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit_2.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        for value in self.sql.execute("SELECT name FROM type_of_work"):
            self.uid.comboBox.addItem(value[0])
        for value in self.sql.execute("SELECT last_name FROM masters"):
            self.uid.comboBox_2.addItem(value[0])
        for value in self.sql.execute("SELECT name FROM completion_mark"):
            self.uid.comboBox_3.addItem(value[0])
        self.uid.lineEdit_3.setText("")
        self.uid.lineEdit_2.setText("")
        self.uid.textEdit.setText("")
        self.uid.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

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

    def addOrders(self):
        id = self.uid.spinBox.value()
        customer = self.uid.lineEdit_3.text()
        type_work = self.uid.comboBox.currentText()
        master = self.uid.comboBox_2.currentText()
        data_start = self.uid.dateTimeEdit.dateTime().toString()
        data_end = self.uid.dateTimeEdit_2.dateTime().toString()
        mark = self.uid.comboBox_3.currentText()
        price = self.uid.lineEdit_2.text()
        notes = self.uid.textEdit.toPlainText()
        try:
            sqlite_insert_query = """INSERT INTO orders
                                      (order_id, customer, type_of_work_id, master_id, date_start, date_end, completion_mark_id, price, notes)
                                      VALUES
                                      (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            data = (id, customer, type_work, master, data_start, data_end, mark, price, notes)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
