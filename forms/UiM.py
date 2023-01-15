from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from forms.mainForm import Ui_mainForm
from forms.UiU import UiU
from forms.UiD import UiD
from forms.UiV import UiV
import sqlite3


FormM, WindowM = uic.loadUiType("forms/mainForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()

class UiM(QtWidgets.QDialog, FormM):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.uim.addButton.clicked.connect(self.addButtonPresed)
        self.uim.editButton.clicked.connect(self.editButtonPresed)
        self.uim.usersButton.clicked.connect(self.userButtonPresed)
        self.uim.vievButton.clicked.connect(self.viewButtonPresed)
        self.uim.infoButton.clicked.connect(self.infoButtonPresed)
        self.uim.blindButton.clicked.connect(self.blitButtonPresed)
        self.addForm = UiD(self)
        self.userForm = UiU(self)
        self.viewForm = UiV(self)
        self.loadForm()

    def addButtonPresed(self):
        self.setEnabled(False)
        self.addForm.show()
        self.addForm.setEnabled(True)

    def editButtonPresed(self):
        self.setEnabled(False)
        self.addForm.show()
        self.addForm.setEnabled(True)

    def userButtonPresed(self):
        self.setEnabled(False)
        self.userForm.show()
        self.userForm.setEnabled(True)

    def viewButtonPresed(self):
        self.setEnabled(False)
        self.viewForm.show()
        self.viewForm.setEnabled(True)

    def infoButtonPresed(self):
        file = open("info.txt", "r", encoding="utf-8")
        s = file.read()
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, "Руководство пользователя", s, QMessageBox.Close, defaultBtn)
        file.close()

    def blitButtonPresed(self):
        defaultBtn = QMessageBox.NoButton
        result = QMessageBox.question(self, "TODO", "Режим для слабовидящих", QMessageBox.Close, defaultBtn)

    def loadForm(self):
        for value in sql.execute("SELECT notes FROM orders"):
            self.uim.listWidget.addItems(value)