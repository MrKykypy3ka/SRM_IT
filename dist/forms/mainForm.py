# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(591, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/computer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainForm.setWindowIcon(icon)
        self.addButton = QtWidgets.QPushButton(mainForm)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.addButton.setStyleSheet("background-image: url(:/icons/add.png);")
        self.addButton.setText("")
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(mainForm)
        self.editButton.setGeometry(QtCore.QRect(70, 10, 51, 51))
        self.editButton.setStyleSheet("background-image: url(:/icons/edit.png);\n"
"")
        self.editButton.setText("")
        self.editButton.setObjectName("editButton")
        self.deleteButton = QtWidgets.QPushButton(mainForm)
        self.deleteButton.setGeometry(QtCore.QRect(130, 10, 51, 51))
        self.deleteButton.setStyleSheet("background-image: url(:/icons/del.png);")
        self.deleteButton.setText("")
        self.deleteButton.setObjectName("deleteButton")
        self.vievButton = QtWidgets.QPushButton(mainForm)
        self.vievButton.setGeometry(QtCore.QRect(190, 10, 51, 51))
        self.vievButton.setStyleSheet("background-image: url(:/icons/view.png);")
        self.vievButton.setText("")
        self.vievButton.setObjectName("vievButton")
        self.usersButton = QtWidgets.QPushButton(mainForm)
        self.usersButton.setGeometry(QtCore.QRect(250, 10, 51, 51))
        self.usersButton.setStyleSheet("background-image: url(:/icons/user.png);")
        self.usersButton.setText("")
        self.usersButton.setObjectName("usersButton")
        self.label = QtWidgets.QLabel(mainForm)
        self.label.setGeometry(QtCore.QRect(336, 30, 181, 20))
        self.label.setToolTip("")
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(mainForm)
        self.label_2.setGeometry(QtCore.QRect(10, 310, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.infoButton = QtWidgets.QPushButton(mainForm)
        self.infoButton.setGeometry(QtCore.QRect(540, 300, 41, 41))
        self.infoButton.setStyleSheet("background-image: url(:/icons/info.png);")
        self.infoButton.setText("")
        self.infoButton.setObjectName("infoButton")
        self.blindButton = QtWidgets.QPushButton(mainForm)
        self.blindButton.setGeometry(QtCore.QRect(490, 300, 41, 41))
        self.blindButton.setStyleSheet("background-image: url(:/icons/low.png);")
        self.blindButton.setText("")
        self.blindButton.setObjectName("blindButton")
        self.label_3 = QtWidgets.QLabel(mainForm)
        self.label_3.setGeometry(QtCore.QRect(530, 10, 51, 51))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(mainForm)
        self.calendarWidget.setGeometry(QtCore.QRect(310, 70, 271, 221))
        self.calendarWidget.setObjectName("calendarWidget")
        self.listWidget = QtWidgets.QListWidget(mainForm)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 291, 221))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        _translate = QtCore.QCoreApplication.translate
        mainForm.setWindowTitle(_translate("mainForm", "Техник"))
        self.label.setText(_translate("mainForm", "User"))
        self.label_2.setText(_translate("mainForm", "tips"))
        self.label_3.setText(_translate("mainForm", "Photo"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainForm = QtWidgets.QDialog()
    ui = Ui_mainForm()
    ui.setupUi(mainForm)
    mainForm.show()
    sys.exit(app.exec_())