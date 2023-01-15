from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.viewForm import Ui_viewForm
FormV, WindowV = uic.loadUiType("forms/viewForm.ui")

class UiV(QtWidgets.QDialog, FormV):
    def __init__(self, parent=None):
        super(UiV, self).__init__(parent)
        self.uiv = Ui_viewForm()
        self.uiv.setupUi(self)