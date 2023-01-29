from PyQt5 import QtCore, QtWidgets, uic
from forms.addForm import Ui_addForm
import sqlite3

FormD, WindowD = uic.loadUiType("forms/addForm.ui")


class UiD(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiD, self).__init__(parent)
        self.uid = Ui_addForm()
        self.uid.setupUi(self)
        self.uid.spinBox.setEnabled(False)
        self.setFixedSize(self.width(), self.height())
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
            self.close()

    def loadForm(self):
        self.uid.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        self.uid.dateTimeEdit_2.setDateTime(QtCore.QDateTime.currentDateTime())
        self.uid.dateTimeEdit_2.setDisplayFormat("dd.MM.yyyy (hh:mm)")
        try:
            if self.sql.execute("SELECT MAX(order_id) FROM orders").fetchone()[0] is None:
                self.uid.spinBox.setValue(1)
            else:
                self.uid.spinBox.setValue(self.sql.execute("SELECT MAX(order_id) FROM orders").fetchone()[0] + 1)
            for value in self.sql.execute("SELECT name FROM type_of_work"):
                self.uid.comboBox.addItem(value[0])
            for value in self.sql.execute("SELECT last_name FROM masters"):
                self.uid.comboBox_2.addItem(value[0])
            for value in self.sql.execute("SELECT name FROM completion_mark"):
                self.uid.comboBox_3.addItem(value[0])
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        self.uid.lineEdit_3.setText("")
        self.uid.lineEdit_2.setText("")
        self.uid.textEdit.setText("")
        self.uid.textEdit.setStyleSheet("QTextEdit {background-color: White;}")

    def showEvent(self, event):
        self.uid.comboBox.clear()
        self.uid.comboBox_2.clear()
        self.uid.comboBox_3.clear()
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
        o_id = self.uid.spinBox.value()
        customer = self.uid.lineEdit_3.text()
        data_start = self.uid.dateTimeEdit.dateTime().toString('yyyy MM dd hh mm')
        print(data_start)
        data_end = self.uid.dateTimeEdit_2.dateTime().toString('yyyy MM dd hh mm')
        price = self.uid.lineEdit_2.text()
        notes = self.uid.textEdit.toPlainText()
        try:
            request = """SELECT type_of_work_id FROM type_of_work
                                             WHERE name == (?);"""
            type_work = self.sql.execute(request, (self.uid.comboBox.currentText(),)).fetchone()[0]
            request = """SELECT masters_id FROM masters
                                             WHERE last_name == (?);"""
            master = self.sql.execute(request, (self.uid.comboBox_2.currentText(),)).fetchone()[0]
            request = """SELECT completion_mark_id FROM completion_mark
                                             WHERE name == (?);"""
            mark = self.sql.execute(request, (self.uid.comboBox_3.currentText(),)).fetchone()[0]
            sqlite_insert_query = """INSERT INTO orders
            (order_id, customer, type_of_work_id, master_id, date_start, date_end, completion_mark_id, price, notes)
                                      VALUES
                                      (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
            data = (o_id, customer, type_work, master, data_start, data_end, mark, price, notes)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
