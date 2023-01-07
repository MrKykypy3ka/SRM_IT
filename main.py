from PyQt5 import QtWidgets
from forms.autoresationForm import Ui_autoresationForm, UiA
import sys

def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiA()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()