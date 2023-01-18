from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.addForm import Ui_addForm
import sys
import sqlite3

FormD, WindowD = uic.loadUiType("forms/addForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()

class UiD(QtWidgets.QDialog, FormD):
    def __init__(self, parent=None):
        super(UiD, self).__init__(parent)
        self.uid = Ui_addForm()
        self.uid.setupUi(self)
        self.uid.addButton.clicked.connect(self.addButtonPresed)
        self.loadForm()

    def addButtonPresed(self):
        pass


    def loadForm(self):
        for value in  sql.execute("SELECT name FROM type_of_work"):
            self.uid.comboBox.addItem(value[0])
        for value in  sql.execute("SELECT last_name FROM masters"):
            self.uid.comboBox_2.addItem(value[0])
        for value in  sql.execute("SELECT name FROM completion_mark"):
            self.uid.comboBox_3.addItem(value[0])
"""def closeEvent(self, event):
        return 1

   def showEvent(self, event):
        print("Ало")"""