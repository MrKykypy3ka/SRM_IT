from PyQt5 import QtGui, QtWidgets, uic
from forms.viewForm import Ui_viewForm
import sqlite3

FormV, WindowV = uic.loadUiType("forms/viewForm.ui")
db = sqlite3.connect('identifier.sqlite')
sql = db.cursor()


class UiV(QtWidgets.QDialog, FormV):
    def __init__(self, parent=None):
        super(UiV, self).__init__(parent)
        self.notes = None
        self.order = None
        self.uiv = Ui_viewForm()
        self.uiv.setupUi(self)
        self.setFixedSize(self.width(), self.height())

    def closeEvent(self, event):
        print("view")

        event.accept()

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        try:
            sqlite_insert_query = """SELECT * FROM orders WHERE notes == (?);"""
            self.order = list(sql.execute(sqlite_insert_query, (self.notes,)).fetchone())
            request = """SELECT name FROM type_of_work WHERE type_of_work_id == (?);"""
            self.order[2] = sql.execute(request, (self.order[2],)).fetchone()[0]
            request = """SELECT last_name FROM masters WHERE masters_id == (?);"""
            self.order[3] = sql.execute(request, (self.order[3],)).fetchone()[0]
            request = """SELECT name FROM completion_mark WHERE completion_mark_id == (?);"""
            self.order[6] = sql.execute(request, (self.order[6],)).fetchone()[0]
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
        d_s = str(self.order[4]).split()
        self.uiv.date_start.setText(f"{d_s[2]}.{d_s[1]}.{d_s[0]} ({d_s[3]}:{d_s[4]})")
        d_e = str(self.order[5]).split()
        self.uiv.date_end.setText(f"{d_e[2]}.{d_e[1]}.{d_e[0]} ({d_e[3]}:{d_e[4]})")
        self.uiv.mark.setText(str(self.order[6]))
        self.uiv.price.setText(str(self.order[7]))
        self.uiv.notes.setText(str(self.order[8]))
