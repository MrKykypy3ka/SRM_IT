from PyQt5 import QtWidgets, QtCore, uic
from forms.autoresationForm import Ui_autoresationForm
from forms.UiM import UiM
import sqlite3

FormA, WindowA = uic.loadUiType("forms/autoresationForm.ui")


class UiA(QtWidgets.QDialog, FormA):
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_autoresationForm()
        self.uia.setupUi(self)
        self.uia.singinButton.clicked.connect(self.singinButtonPresed)
        self.uim = UiM(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.db = sqlite3.connect('identifier.sqlite')
        self.sql = self.db.cursor()

    def autoresation(self, login, password):
        for value in self.sql.execute("SELECT login, password FROM masters"):
            if value[0] == login and value[1] == password:
                return True
        return False

    def singinButtonPresed(self):
        #if autoresation(self.uia.inputLogin.text(), self.uia.inputPassword.text()):
        if True:
            self.close()
            self.uim.show()
            self.uim.setLogin(self.uia.inputLogin.text(), "1")
