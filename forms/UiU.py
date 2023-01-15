from PyQt5 import QtCore, QtGui, QtWidgets,  uic
from forms.userForm import Ui_usersForm

FormU, WindowU = uic.loadUiType("forms/userForm.ui")

class UiU(QtWidgets.QDialog, FormU):
    def __init__(self, parent=None):
        super(UiU, self).__init__(parent)
        self.uiu = Ui_usersForm()
        self.uiu.setupUi(self)