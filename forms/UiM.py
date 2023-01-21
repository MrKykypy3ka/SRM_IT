from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from forms.mainForm import Ui_mainForm
from forms.UiU import UiU
from forms.UiD import UiD
from forms.UiV import UiV
from forms.UiE import UiE
import sqlite3


FormM, WindowM = uic.loadUiType("forms/mainForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()


class MouseTracker(QtCore.QObject):
    positionChanged = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.setMouseTracking(True)
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, o, e):
        if o is self.widget and e.type() == QtCore.QEvent.MouseMove:
            self.positionChanged.emit(e.pos())
        return super().eventFilter(o, e)


class UiM(QtWidgets.QDialog, FormM):
    def __init__(self, parent=None):
        super(UiM, self).__init__(parent)
        self.uim = Ui_mainForm()
        self.uim.setupUi(self)
        self.uim.addButton.clicked.connect(self.addButtonPresed)
        self.uim.deleteButton.clicked.connect(self.deleteButtonPresed)
        self.uim.editButton.clicked.connect(self.editButtonPresed)
        self.uim.usersButton.clicked.connect(self.userButtonPresed)
        self.uim.vievButton.clicked.connect(self.viewButtonPresed)
        self.uim.infoButton.clicked.connect(self.infoButtonPresed)
        self.uim.blindButton.clicked.connect(self.blitButtonPresed)
        self.addForm = UiD(self)
        self.userForm = UiU(self)
        self.viewForm = UiV(self)
        self.editForm = UiE(self)
        self.trackerAdd = MouseTracker(self.uim.addButton)
        self.trackerAdd.positionChanged.connect(self.on_positionChangedAdd)
        self.trackerEdit = MouseTracker(self.uim.editButton)
        self.trackerEdit.positionChanged.connect(self.on_positionChangedEdit)
        self.trackerView = MouseTracker(self.uim.vievButton)
        self.trackerView.positionChanged.connect(self.on_positionChangedView)
        self.trackerDel = MouseTracker(self.uim.deleteButton)
        self.trackerDel.positionChanged.connect(self.on_positionChangedDel)
        self.trackerUser = MouseTracker(self.uim.usersButton)
        self.trackerUser.positionChanged.connect(self.on_positionChangedUser)
        self.trackerInfo = MouseTracker(self.uim.infoButton)
        self.trackerInfo.positionChanged.connect(self.on_positionChangedInfo)
        self.trackerLow = MouseTracker(self.uim.blindButton)
        self.trackerLow.positionChanged.connect(self.on_positionChangedLow)
        self.loadForm()

    def addButtonPresed(self):
        self.setEnabled(False)
        self.addForm.show()
        self.addForm.setEnabled(True)
        if not self.addForm.exec_():
            self.setEnabled(True)
            self.uim.listWidget.clear()
            self.loadForm()

    def editButtonPresed(self):
        if self.uim.listWidget.selectedItems():
            self.setEnabled(False)
            self.editForm.show()
            self.editForm.setEnabled(True)
            if not self.editForm.exec_():
                self.setEnabled(True)
                self.uim.listWidget.clear()
                self.loadForm()

    def deleteButtonPresed(self):
        if self.uim.listWidget.selectedItems():
            msg = QMessageBox(self)
            msg.setWindowTitle("Подтвердите удаление")
            msg.setText("Вы точно хотите удалить запись?")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setInformativeText(self.uim.listWidget.selectedItems()[0].text())
            x = msg.exec_()
            print(x)
            if x == 16384:
                try:
                    request = """DELETE FROM orders
                                 WHERE notes == (?);"""
                    sql.execute(request, (self.uim.listWidget.selectedItems()[0].text(),))
                    db.commit()
                except sqlite3.Error as error:
                    print("Ошибка при работе с SQLite", error)
        self.loadForm()



    def userButtonPresed(self):
        self.setEnabled(False)
        self.userForm.show()
        self.userForm.setEnabled(True)
        if not self.userForm.exec_():
            self.setEnabled(True)
            self.loadForm()

    def viewButtonPresed(self):
        if self.uim.listWidget.selectedItems():
            self.setEnabled(False)
            self.viewForm.setData(self.uim.listWidget.selectedItems()[0].text())
            self.viewForm.show()
            self.viewForm.setEnabled(True)
            if not self.viewForm.exec_():
                self.setEnabled(True)
                self.uim.listWidget.clear()
                self.loadForm()

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
        self.uim.listWidget.clear()
        for value in sql.execute("SELECT notes FROM orders"):
            self.uim.listWidget.addItems(value)

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedAdd(self, pos):
        self.uim.label_2.setText("Добавить запись")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedEdit(self, pos):
        self.uim.label_2.setText("Редактирвоать запить")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedDel(self, pos):
        self.uim.label_2.setText("Удалить запить")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedView(self, pos):
        self.uim.label_2.setText("Просмотреть запись")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedUser(self, pos):
        self.uim.label_2.setText("Добавить пользователя")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedInfo(self, pos):
        self.uim.label_2.setText("Руководство пользователя")

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_positionChangedLow(self, pos):
        self.uim.label_2.setText("Режим для слаюовидящих")

    def setLogin(self, login, avatar):
        self.uim.label.setText(login)

