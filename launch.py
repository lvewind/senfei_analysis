from app.main import Main
from PySide6 import QtWidgets
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    kiki = Main()
    kiki.show()
    sys.exit(app.exec())
