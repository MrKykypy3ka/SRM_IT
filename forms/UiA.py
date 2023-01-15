from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.mainForm import Ui_mainForm
from forms.autoresationForm import Ui_autoresationForm
from forms.UiM import UiM

FormA, WindowA = uic.loadUiType("forms/autoresationForm.ui")

class UiA(QtWidgets.QDialog, FormA):
    def __init__(self, parent=None):
        super(UiA, self).__init__(parent)
        self.uia = Ui_autoresationForm()
        self.uia.setupUi(self)
        self.uia.singinButton.clicked.connect(self.singinButtonPresed)
        self.mainForm = UiM(self)

    def singinButtonPresed(self):
        self.close()
        self.mainForm.show()


def autoresation(login, password):
    pass

def main():
    pass