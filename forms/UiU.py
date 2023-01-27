from PyQt5 import QtWidgets, uic
from forms.userForm import Ui_usersForm
import sqlite3

FormU, WindowU = uic.loadUiType("forms/userForm.ui")

class UiU(QtWidgets.QDialog, FormU):
    def __init__(self, parent=None):
        super(UiU, self).__init__(parent)
        self.uiu = Ui_usersForm()
        self.uiu.setupUi(self)
        self.uiu.addButton.clicked.connect(self.addButtonPresed)
        self.uiu.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiu.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiu.lineEdit.textChanged.connect(self.lineTextChanged)
        self.uiu.lineEdit_2.textChanged.connect(self.line2TextChanged)
        self.uiu.lineEdit_3.textChanged.connect(self.line3TextChanged)
        self.uiu.lineEdit_4.textChanged.connect(self.line4TextChanged)
        self.uiu.lineEdit_5.textChanged.connect(self.line5TextChanged)
        self.setFixedSize(self.width(), self.height())
        self.db = sqlite3.connect('identifier.sqlite')
        self.sql = self.db.cursor()

    def showEvent(self, event):
        self.uiu.comboBox_2.clear()
        self.loadForm()

    def loadForm(self):
        for value in self.sql.execute("SELECT name FROM post"):
            self.uiu.comboBox_2.addItem(value[0])
    def addButtonPresed(self):
        if self.uiu.lineEdit.text() == "":
            self.uiu.lineEdit.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uiu.lineEdit_2.text() == "":
            self.uiu.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uiu.lineEdit_3.text() == "":
            self.uiu.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uiu.lineEdit_4.text() == "":
            self.uiu.lineEdit_4.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uiu.lineEdit_5.text() == "":
            self.uiu.lineEdit_5.setStyleSheet("QLineEdit {background-color: Salmon;}")
        elif self.uiu.lineEdit_5.text() != self.uiu.lineEdit_4.text():
            self.uiu.lineEdit_5.setStyleSheet("QLineEdit {background-color: Salmon;}")
            self.uiu.lineEdit_4.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.addOrders()
            self.close()

    def addOrders(self):

        first_name = self.uiu.lineEdit_2.text()
        last_name = self.uiu.lineEdit.text()
        login = self.uiu.lineEdit_4.text()
        password = self.uiu.lineEdit_5.text()
        try:
            if self.sql.execute("SELECT MAX(masters_id) FROM masters").fetchone()[0] is None:
                id = 1
            else:
                id = self.sql.execute("SELECT MAX(masters_id) FROM masters").fetchone()[0] + 1
            request = "SELECT post_id FROM post WHERE name == (?);"
            post = self.sql.execute(request, (self.uiu.comboBox_2.currentText(),)).fetchone()[0]
            sqlite_insert_query = """INSERT INTO masters
                                      (masters_id, first_name, last_name, post_id, login, password)
                                      VALUES
                                      (?, ?, ?, ?, ?, ?);"""
            data = (id, first_name, last_name, post, login, password)
            self.sql.execute(sqlite_insert_query, data)
            self.db.commit()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def lineTextChanged(self):
        if self.uiu.lineEdit.text() == "":
            self.uiu.lineEdit.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uiu.lineEdit.setStyleSheet("QLineEdit {background-color: White;}")

    def line2TextChanged(self):
        if self.uiu.lineEdit_2.text() == "":
            self.uiu.lineEdit_2.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uiu.lineEdit_2.setStyleSheet("QLineEdit {background-color: White;}")

    def line3TextChanged(self):
        if self.uiu.lineEdit_3.text() == "":
            self.uiu.lineEdit_3.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uiu.lineEdit_3.setStyleSheet("QLineEdit {background-color: White;}")

    def line4TextChanged(self):
        if self.uiu.lineEdit_4.text() == "":
            self.uiu.lineEdit_4.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uiu.lineEdit_4.setStyleSheet("QLineEdit {background-color: White;}")

    def line5TextChanged(self):
        if self.uiu.lineEdit_5.text() == "":
            self.uiu.lineEdit_5.setStyleSheet("QLineEdit {background-color: Salmon;}")
        else:
            self.uiu.lineEdit_5.setStyleSheet("QLineEdit {background-color: White;}")

    def closeEvent(self, event):
        print("user")
        event.accept()