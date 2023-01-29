from PyQt5 import QtCore, QtGui, QtWidgets
import image_rc


class Ui_autoresationForm(object):
    def setupUi(self, autoresationForm):
        autoresationForm.setObjectName("autoresationForm")
        autoresationForm.resize(200, 160)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/computer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        autoresationForm.setWindowIcon(icon)
        self.singinButton = QtWidgets.QPushButton(autoresationForm)
        self.singinButton.setGeometry(QtCore.QRect(40, 120, 111, 31))
        self.singinButton.setObjectName("singinButton")
        self.inputLogin = QtWidgets.QLineEdit(autoresationForm)
        self.inputLogin.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.inputLogin.setInputMask("")
        self.inputLogin.setText("")
        self.inputLogin.setObjectName("inputLogin")
        self.inputPassword = QtWidgets.QLineEdit(autoresationForm)
        self.inputPassword.setGeometry(QtCore.QRect(10, 80, 181, 31))
        self.inputPassword.setInputMask("")
        self.inputPassword.setObjectName("inputPassword")
        self.label = QtWidgets.QLabel(autoresationForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(autoresationForm)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.inputPassword.raise_()
        self.singinButton.raise_()
        self.inputLogin.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(autoresationForm)
        QtCore.QMetaObject.connectSlotsByName(autoresationForm)

    def retranslateUi(self, autoresationForm):
        _translate = QtCore.QCoreApplication.translate
        autoresationForm.setWindowTitle(_translate("autoresationForm", "Авторизация"))
        self.singinButton.setText(_translate("autoresationForm", "Войти"))
        self.label.setText(_translate("autoresationForm", "Логин"))
        self.label_2.setText(_translate("autoresationForm", "Пароль"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autoresationForm = QtWidgets.QDialog()
    ui = Ui_autoresationForm()
    ui.setupUi(autoresationForm)
    autoresationForm.show()
    sys.exit(app.exec_())
