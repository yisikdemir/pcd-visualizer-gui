#------------------------------------------------------------------------------
# Author: Yunus Emre Işıkdemir
# 
# Create Date: 02/11/2021
#
# Project Name: Point Cloud Data Visualizer Graphical User Interface
#
# Description: The script creates a user interface to use application.
# 
#------------------------------------------------------------------------------

from PyQt5.QtWidgets import QDialog
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from PyQt5.QtWidgets import QPushButton, QHBoxLayout,QVBoxLayout,QLabel
from PyQt5 import QtCore, QtWidgets
from configs import Configure


class Window(QDialog):
       
    def __init__(self, parent=None) -> None:
        super(Window, self).__init__(parent)
   
        self.figure = plt.figure(figsize = (15, 10), dpi=80, facecolor = 'lightgrey')
        self.figure.set_figheight(50)
        self.figure.set_figwidth(50)
        
        self.layout_config = Configure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
   
        self.button_point_cloud = QPushButton('RUN')
        self.next_cloud = QPushButton('FETCH NEXT CLOUD')
        self.reset_button = QPushButton('RESET')

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
              
        h_box1 = QVBoxLayout()
        h_box1.addWidget(self.button_point_cloud)
        h_box1.addWidget(self.next_cloud)
        h_box1.addWidget(self.reset_button)

        h_box2 = QHBoxLayout()
        self.label= QLabel('Point Size ',self)
        self.empty_spacer = QLabel(' '*3,self)
        self.horizontalSlider = QtWidgets.QSlider()
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.alpha_param= QLabel('Alpha ',self)
        self.horizontalSlider2 = QtWidgets.QSlider()
        self.horizontalSlider2.setMinimum(1)
        self.horizontalSlider2.setMaximum(10)
        self.horizontalSlider2.setSingleStep(1)
        self.horizontalSlider2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider2.setObjectName("horizontalSlider2")
        
        h_box2.addWidget(self.label)
        h_box2.addWidget(self.horizontalSlider)
        h_box2.addWidget(self.empty_spacer)
        h_box2.addWidget(self.alpha_param)
        h_box2.addWidget(self.horizontalSlider2)
       
        v_box = QVBoxLayout() 
        v_box.addLayout(layout)    
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        self.setLayout(v_box)        
        
        self.figure.tight_layout()
