from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.mainForm import Ui_mainForm
from forms.autoresationForm import Ui_autoresationForm
from forms.UiM import UiM
import sqlite3

FormA, WindowA = uic.loadUiType("forms/autoresationForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor( )

def autoresation(login, password):
    for value in sql.execute("SELECT login, password FROM masters"):
        if value[0] == login and value[1] == password:
            return True
    return False

def main():
    pass

class UiA(QtWidgets.QDialog, FormA):
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_autoresationForm()
        self.uia.setupUi(self)
        self.uia.singinButton.clicked.connect(self.singinButtonPresed)
        self.mainForm = UiM(self)

    def singinButtonPresed(self):
        if autoresation(self.uia.inputLogin.text(), self.uia.inputPassword.text()):
            self.close()
            self.mainForm.show()