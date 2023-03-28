#------------------------------------------------------------------------------
# Author: Yunus Emre Işıkdemir
# 
# Create Date: 02/11/2021
#
# Project Name: Point Cloud Data Visualizer Graphical User Interface
#
# Description: Driver program
# 
#------------------------------------------------------------------------------

from PyQt5.QtWidgets import QApplication
from maps import SARSTM
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = SARSTM()
    main.map_handler.show()
    sys.exit(app.exec_())
