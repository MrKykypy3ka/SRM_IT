from PyQt5 import QtWidgets
from forms.autoresationForm import Ui_autoresationForm

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    autoresationForm = QtWidgets.QDialog()
    ui = Ui_autoresationForm()
    ui.setupUi(autoresationForm)
    autoresationForm.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()