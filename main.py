from PyQt5.QtWidgets import QApplication
from maps import SARSTM
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SARSTM()
    main.map_handler.show()
    sys.exit(app.exec_())