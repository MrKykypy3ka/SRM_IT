# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\userForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_usersForm(object):
    def setupUi(self, usersForm):
        usersForm.setObjectName("usersForm")
        usersForm.resize(322, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/computer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        usersForm.setWindowIcon(icon)
        self.comboBox_2 = QtWidgets.QComboBox(usersForm)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 70, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.addButton = QtWidgets.QPushButton(usersForm)
        self.addButton.setGeometry(QtCore.QRect(110, 200, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.label_6 = QtWidgets.QLabel(usersForm)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(1)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(usersForm)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(usersForm)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(usersForm)
        self.lineEdit.setGeometry(QtCore.QRect(150, 10, 161, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(usersForm)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(1)
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(usersForm)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(usersForm)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(usersForm)
        self.label.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(usersForm)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 40, 161, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(usersForm)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 100, 161, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(usersForm)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 130, 161, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(usersForm)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 160, 161, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.retranslateUi(usersForm)
        QtCore.QMetaObject.connectSlotsByName(usersForm)

    def retranslateUi(self, usersForm):
        _translate = QtCore.QCoreApplication.translate
        usersForm.setWindowTitle(_translate("usersForm", "Добавить пользователя"))
        self.addButton.setText(_translate("usersForm", "Добавить"))
        self.label_6.setText(_translate("usersForm", "<html><head/><body><p>Подтверждение</p></body></html>"))
        self.label_4.setText(_translate("usersForm", "Логин"))
        self.label_3.setText(_translate("usersForm", "Должность"))
        self.label_7.setText(_translate("usersForm", "<html><head/><body><p>пароля</p></body></html>"))
        self.label_5.setText(_translate("usersForm", "Пароль"))
        self.label_9.setText(_translate("usersForm", "Фамилия"))
        self.label.setText(_translate("usersForm", "Имя"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usersForm = QtWidgets.QDialog()
    ui = Ui_usersForm()
    ui.setupUi(usersForm)
    usersForm.show()
    sys.exit(app.exec_())
