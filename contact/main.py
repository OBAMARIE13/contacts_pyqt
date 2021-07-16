import sys
from PyQt5 import QtWidgets
from widgets.contact import Contact


def main():
    app = QtWidgets.QApplication([sys.argv])
    win = Contact()
    win.show()
    app.exec_()

if __name__ == '__main__':
    main()