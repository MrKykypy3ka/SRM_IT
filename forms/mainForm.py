from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.userForm import Ui_usersForm, UiU
from forms.addForm import Ui_addForm, UiD
from forms.viewForm import Ui_viewForm, UiV
import sys

FormM, WindowM = uic.loadUiType("forms/mainForm.ui")
class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(591, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("forms\\../computer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        self.addButton = QtWidgets.QPushButton(mainForm)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(mainForm)
        self.editButton.setGeometry(QtCore.QRect(70, 10, 51, 51))
        self.editButton.setObjectName("editButton")
        self.deleteButton = QtWidgets.QPushButton(mainForm)
        self.deleteButton.setGeometry(QtCore.QRect(130, 10, 51, 51))
        self.deleteButton.setObjectName("deleteButton")
        self.vievButton = QtWidgets.QPushButton(mainForm)
        self.vievButton.setGeometry(QtCore.QRect(190, 10, 51, 51))
        self.vievButton.setObjectName("vievButton")
        self.usersButton = QtWidgets.QPushButton(mainForm)
        self.usersButton.setGeometry(QtCore.QRect(250, 10, 51, 51))
        self.usersButton.setObjectName("usersButton")
        self.label = QtWidgets.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(336, 30, 181, 20))
        self.label.setToolTip("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(mainForm)
        self.scrollArea.setGeometry(QtCore.QRect(10, 80, 291, 211))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 209))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2 = QtWidgets.QLabel(mainForm)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.infoButton = QtWidgets.QPushButton(mainForm)
        self.infoButton.setGeometry(QtCore.QRect(550, 310, 31, 31))
        self.infoButton.setObjectName("infoButton")
        self.blindButton = QtWidgets.QPushButton(mainForm)
        self.blindButton.setGeometry(QtCore.QRect(510, 310, 31, 31))
        self.blindButton.setObjectName("blindButton")
        self.label_3 = QtWidgets.QLabel(mainForm)
        self.label_3.setGeometry(QtCore.QRect(530, 10, 51, 51))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(mainForm)
        self.calendarWidget.setGeometry(QtCore.QRect(310, 80, 271, 211))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Техник"))
        self.addButton.setText(_translate("mainForm", "ADD"))
        self.editButton.setText(_translate("mainForm", "EDIT"))
        self.deleteButton.setText(_translate("mainForm", "DELETE"))
        self.vievButton.setText(_translate("mainForm", "VIEV"))
        self.usersButton.setText(_translate("mainForm", "ADD\n"
"USER"))
        self.label.setText(_translate("mainForm", "User"))
        self.label_2.setText(_translate("mainForm", "tips"))
        self.infoButton.setText(_translate("mainForm", "info"))
        self.blindButton.setText(_translate("mainForm", "blind"))
        self.label_3.setText(_translate("mainForm", "Photo"))


class UiM(QtWidgets.QDialog, FormM):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.uim.addButton.clicked.connect(self.addButtonPresed)
        self.uim.editButton.clicked.connect(self.editButtonPresed)
        self.uim.usersButton.clicked.connect(self.userButtonPresed)
        self.uim.vievButton.clicked.connect(self.viewButtonPresed)
        self.addForm = UiD(self)
        self.userForm = UiU(self)
        self.viewForm = UiV(self)

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
