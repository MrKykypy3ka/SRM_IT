from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QDateTime
from forms.editForm import Ui_editForm
import sqlite3

FormE, WindowD = uic.loadUiType("forms/editForm.ui")


class UiE(QtWidgets.QDialog, FormE):
    def __init__(self, parent=None):
        super(UiE, self).__init__(parent)
        self.notes = None
        self.order = None
        self.uie = Ui_editForm()
        self.uie.setupUi(self)
        self.uie.spinBox.setEnabled(False)
        self.setFixedSize(self.width(), self.height())
        self.uie.addButton.clicked.connect(self.addButtonPresed)
        self.uie.textEdit.textChanged.connect(self.textTextChanged)
        self.uie.lineEdit_2.textChanged.connect(self.line2TextChanged)
        self.uie.lineEdit_3.textChanged.connect(self.line3TextChanged)
        self.db = sqlite3.connect('identifier.sqlite')
        self.sql = self.db.cursor()

    def addButtonPresed(self):
        if self.uie.textEdit.toPlainText() == "":
            self.uie.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        elif self.uie.lineEdit_3.text() == "":
            self.uie.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uie.lineEdit_2.text() == "" or not self.uie.lineEdit_2.text().isdigit():
            self.uie.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.editOrders()
            self.close()

    def loadForm(self):
        for value in self.sql.execute("SELECT name FROM type_of_work"):
            self.uie.comboBox.addItem(value[0])
        for value in self.sql.execute("SELECT last_name FROM masters"):
            self.uie.comboBox_2.addItem(value[0])
        for value in self.sql.execute("SELECT name FROM completion_mark"):
            self.uie.comboBox_3.addItem(value[0])
        self.uie.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

    def setData(self, notes):
        self.notes = notes

    def showData(self):
        self.uie.spinBox.setValue(self.order[0])
        self.uie.lineEdit_3.setText(self.order[1])
        self.uie.comboBox.setCurrentText(str(self.order[2]))
        self.uie.comboBox_2.setCurrentText(str(self.order[3]))
        self.uie.dateTimeEdit.setDateTime(QDateTime(*map(int, self.order[4].split(' '))))
        self.uie.dateTimeEdit.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        self.uie.dateTimeEdit_2.setDateTime(QDateTime(*map(int, self.order[5].split(' '))))
        self.uie.dateTimeEdit_2.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        self.uie.comboBox_3.setCurrentText(str(self.order[6]))
        self.uie.lineEdit_2.setText(str(self.order[7]))
        self.uie.textEdit.setPlainText(self.order[8])

    def textTextChanged(self):
        if self.uie.textEdit.toPlainText() == "":
            self.uie.textEdit.setStyleSheet("QTextEdit {background-color: Salmon;}")
        else:
            self.uie.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

    def line2TextChanged(self):
        if self.uie.lineEdit_2.text() == "":
            self.uie.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uie.lineEdit_2.setStyleSheet("QLineEdit {background-color: White;}")

    def line3TextChanged(self):
        if self.uie.lineEdit_3.text() == "":
            self.uie.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uie.lineEdit_3.setStyleSheet("QLineEdit {background-color: White;}")

    def editOrders(self):
        o_id = self.uie.spinBox.value()
        customer = self.uie.lineEdit_3.text()
        data_start = self.uie.dateTimeEdit.dateTime().toString('yyyy MM dd hh mm')
        data_end = self.uie.dateTimeEdit_2.dateTime().toString('yyyy MM dd hh mm')
        price = self.uie.lineEdit_2.text()
        notes = self.uie.textEdit.toPlainText()

        try:
            request = """SELECT type_of_work_id FROM type_of_work WHERE name == (?);"""
            type_work = self.sql.execute(request, (self.uie.comboBox.currentText(),)).fetchone()[0]
            request = """SELECT masters_id FROM masters WHERE last_name == (?);"""
            master = self.sql.execute(request, (self.uie.comboBox_2.currentText(),)).fetchone()[0]
            request = """SELECT completion_mark_id FROM completion_mark WHERE name == (?);"""
            mark = self.sql.execute(request, (self.uie.comboBox_3.currentText(),)).fetchone()[0]
            sqlite_insert_query = """UPDATE orders 
            SET customer = ?, type_of_work_id = ?, master_id = ?, date_start = ?,
            date_end = ?, completion_mark_id = ?, price = ?, notes = ? WHERE order_id = ?;"""
            data = (customer, type_work, master, data_start, data_end, mark, price, notes, o_id)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.uie.comboBox.clear()
        self.uie.comboBox_2.clear()
        self.uie.comboBox_3.clear()
        try:
            sqlite_insert_query = """SELECT * FROM orders WHERE notes == (?);"""
            self.order = list(self.sql.execute(sqlite_insert_query, (self.notes,)).fetchone())
            request = """SELECT name FROM type_of_work WHERE type_of_work_id == (?);"""
            self.order[2] = self.sql.execute(request, (self.order[2],)).fetchone()[0]
            request = """SELECT last_name FROM masters WHERE masters_id == (?);"""
            self.order[3] = self.sql.execute(request, (self.order[3],)).fetchone()[0]
            request = """SELECT name FROM completion_mark WHERE completion_mark_id == (?);"""
            self.order[6] = self.sql.execute(request, (self.order[6],)).fetchone()[0]
            self.loadForm()
            self.showData()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
