from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.addForm import Ui_addForm

FormD, WindowD = uic.loadUiType("forms/addForm.ui")
class UiD(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiD, self).__init__(parent)
        self.uid = Ui_addForm()
        self.uid.setupUi(self)