from PyQt5 import QtWidgets
from forms.UiA import UiA
import sys
import os


def main():
    app = QtWidgets.QApplication(sys.argv)
    mwa = UiA()
    mwa.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
