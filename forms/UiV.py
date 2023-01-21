from PyQt5 import QtCore, QtGui, QtWidgets, uic
from forms.viewForm import Ui_viewForm
import sqlite3

FormV, WindowV = uic.loadUiType("forms/viewForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()


class UiV(QtWidgets.QDialog, FormV):
    def __init__(self, parent=None):
        super(UiV, self).__init__(parent)
        self.uiv = Ui_viewForm()
        self.uiv.setupUi(self)

    def closeEvent(self, event):
        print("view")
        event.accept()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        try:
            sqlite_insert_query = """SELECT * FROM orders
                                                 WHERE notes == (?);"""
            self.order = list(sql.execute(sqlite_insert_query, (self.notes,)).fetchone())
            request = """SELECT name FROM type_of_work
                                                         WHERE type_of_work_id == (?);"""
            print("1")
            self.order[2] = sql.execute(request, (self.order[2],)).fetchone()[0]
            print("2")
            request = """SELECT last_name FROM masters
                                                         WHERE masters_id == (?);"""
            self.order[3] = sql.execute(request, (self.order[3],)).fetchone()[0]
            request = """SELECT name FROM completion_mark
                                                         WHERE completion_mark_id == (?);"""
            self.order[6] = sql.execute(request, (self.order[6],)).fetchone()[0]
            print(self.order)
            self.showData()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def setData(self, notes):
        self.notes = notes

    def showData(self):
        self.uiv.name.setText(str(self.order[0]))
        self.uiv.customer.setText(str(self.order[1]))
        self.uiv.type.setText(str(self.order[2]))
        self.uiv.master.setText(str(self.order[3]))
        self.uiv.date_start.setText(str(self.order[4]))
        self.uiv.date_end.setText(str(self.order[5]))
        self.uiv.mark.setText(str(self.order[6]))
        self.uiv.price.setText(str(self.order[7]))
        self.uiv.notes.setText(str(self.order[8]))
