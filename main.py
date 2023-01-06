from PyQt5 import QtWidgets
from forms.autoresationForm import Ui_autoresationForm, Ui
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    mw = Ui()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()