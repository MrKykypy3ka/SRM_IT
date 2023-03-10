# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms\viewForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewForm(object):
    def setupUi(self, viewForm):
        viewForm.setObjectName("viewForm")
        viewForm.resize(314, 418)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/computer.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        viewForm.setWindowIcon(icon)
        self.label_6 = QtWidgets.QLabel(viewForm)
        self.label_6.setGeometry(QtCore.QRect(10, 190, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(1)
        self.label_6.setObjectName("label_6")
        self.label_4 = QtWidgets.QLabel(viewForm)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(viewForm)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(viewForm)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(viewForm)
        self.label_7.setGeometry(QtCore.QRect(10, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(1)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(viewForm)
        self.label_8.setGeometry(QtCore.QRect(10, 270, 141, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(1)
        self.label_8.setObjectName("label_8")
        self.label_5 = QtWidgets.QLabel(viewForm)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.addButton = QtWidgets.QPushButton(viewForm)
        self.addButton.setGeometry(QtCore.QRect(110, 370, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.label = QtWidgets.QLabel(viewForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(viewForm)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.customer = QtWidgets.QLabel(viewForm)
        self.customer.setGeometry(QtCore.QRect(150, 40, 151, 21))
        self.customer.setObjectName("customer")
        self.name = QtWidgets.QLabel(viewForm)
        self.name.setGeometry(QtCore.QRect(150, 10, 151, 21))
        self.name.setObjectName("name")
        self.type = QtWidgets.QLabel(viewForm)
        self.type.setGeometry(QtCore.QRect(150, 70, 151, 21))
        self.type.setObjectName("type")
        self.master = QtWidgets.QLabel(viewForm)
        self.master.setGeometry(QtCore.QRect(150, 100, 151, 21))
        self.master.setObjectName("master")
        self.date_start = QtWidgets.QLabel(viewForm)
        self.date_start.setGeometry(QtCore.QRect(150, 130, 151, 21))
        self.date_start.setObjectName("date_start")
        self.price = QtWidgets.QLabel(viewForm)
        self.price.setGeometry(QtCore.QRect(150, 240, 151, 21))
        self.price.setObjectName("price")
        self.mark = QtWidgets.QLabel(viewForm)
        self.mark.setGeometry(QtCore.QRect(150, 200, 151, 21))
        self.mark.setObjectName("mark")
        self.notes = QtWidgets.QLabel(viewForm)
        self.notes.setGeometry(QtCore.QRect(150, 270, 151, 91))
        self.notes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.notes.setObjectName("notes")
        self.label_10 = QtWidgets.QLabel(viewForm)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.date_end = QtWidgets.QLabel(viewForm)
        self.date_end.setGeometry(QtCore.QRect(150, 160, 151, 21))
        self.date_end.setObjectName("date_end")

        self.retranslateUi(viewForm)
        QtCore.QMetaObject.connectSlotsByName(viewForm)

    def retranslateUi(self, viewForm):
        _translate = QtCore.QCoreApplication.translate
        viewForm.setWindowTitle(_translate("viewForm", "????????????????"))
        self.label_6.setText(_translate("viewForm", "<html><head/><body><p>?????????????? ??</p></body></html>"))
        self.label_4.setText(_translate("viewForm", "???????? ??????????????"))
        self.label_3.setText(_translate("viewForm", "????????????????????"))
        self.label_9.setText(_translate("viewForm", "????????????????"))
        self.label_7.setText(_translate("viewForm", "<html><head/><body><p>????????????????????</p></body></html>"))
        self.label_8.setText(_translate("viewForm", "<html><head/><body><p>????????????????????</p></body></html>"))
        self.label_5.setText(_translate("viewForm", "??????????????????"))
        self.addButton.setText(_translate("viewForm", "??????????????"))
        self.label.setText(_translate("viewForm", "?????????? ????????????"))
        self.label_2.setText(_translate("viewForm", "?????? ????????????"))
        self.customer.setText(_translate("viewForm", "TextLabel"))
        self.name.setText(_translate("viewForm", "TextLabel"))
        self.type.setText(_translate("viewForm", "TextLabel"))
        self.master.setText(_translate("viewForm", "TextLabel"))
        self.date_start.setText(_translate("viewForm", "TextLabel"))
        self.price.setText(_translate("viewForm", "price"))
        self.mark.setText(_translate("viewForm", "TextLabel"))
        self.notes.setText(_translate("viewForm", "TextLabel"))
        self.label_10.setText(_translate("viewForm", "???????? ??????????"))
        self.date_end.setText(_translate("viewForm", "TextLabel"))
import image_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewForm = QtWidgets.QDialog()
    ui = Ui_viewForm()
    ui.setupUi(viewForm)
    viewForm.show()
    sys.exit(app.exec_())
