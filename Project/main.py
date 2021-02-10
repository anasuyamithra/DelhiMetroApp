''' importing header files '''

import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib import pyplot as plt


''' Gui Window '''
from toggle_window import Ui_MainWindow

''' import files '''
from main_functions import *
from back import *

counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ''' Toggle menu '''
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 150, True))
        
        
        ''' pages '''

        # PAGE 1
        self.ui.Btn_page_1.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_1))
        
        # PAGE 2
        self.ui.Btn_page_2.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_2))

        # PAGE 3
        self.ui.Btn_page_3.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_3))
  
        # PAGE PATH
        self.ui.Btn_algorithm.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_path))

        
        self.ui.comboBox_start.setEditable(True) 
        self.ui.comboBox_start.completer().setCompletionMode(QCompleter.PopupCompletion) 
        self.ui.comboBox_start.setInsertPolicy(QComboBox.NoInsert) 
        self.ui.comboBox_end.setEditable(True) 
        self.ui.comboBox_end.completer().setCompletionMode(QCompleter.PopupCompletion) 
        self.ui.comboBox_end.setInsertPolicy(QComboBox.NoInsert)
        
       
        UIFunctions.addTexttocomboBox(self)

        """ Initialising the plot 
        """
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.figure.patch.set_facecolor('#232323')
        self.ui.verticalLayout_16.addWidget(self.toolbar)
        self.ui.verticalLayout_16.addWidget(self.canvas)
        
        self.figure_main = plt.figure()
        self.canvas_main = FigureCanvas(self.figure_main)
        self.toolbar_main = NavigationToolbar(self.canvas_main, self)
        self.figure_main.patch.set_facecolor('#232323')
        self.ui.verticalLayout_6.addWidget(self.toolbar_main)
        self.ui.verticalLayout_6.addWidget(self.canvas_main)
        self.ui.Btn_page_2.clicked.connect(lambda: UIFunctions.plot_main_graph(self))

        self.figure_compare = plt.figure()
        self.canvas_compare = FigureCanvas(self.figure_compare)
        self.toolbar_compare = NavigationToolbar(self.canvas_compare, self)
        self.figure_compare.patch.set_facecolor('#232323')
        self.ui.verticalLayout_7.addWidget(self.toolbar_compare)
        self.ui.verticalLayout_7.addWidget(self.canvas_compare)
        self.ui.Btn_page_3.clicked.connect(lambda: UIFunctions.plot_compare_graph(self,int(g.key_to_name[str(self.ui.comboBox_start.currentText())]), int(g.key_to_name[str(self.ui.comboBox_end.currentText())])))


        try:
            self.ui.Btn_algorithm.clicked.connect(lambda: UIFunctions.clearLayout(self,self.ui.verticalLayout_15))
            self.ui.Btn_algorithm.clicked.connect(lambda: UIFunctions.printPathsLabels_staions(self, int(g.key_to_name[str(self.ui.comboBox_start.currentText())]), int(g.key_to_name[str(self.ui.comboBox_end.currentText())])))            
            self.ui.Btn_algorithm.clicked.connect(lambda: self.ui.label_start.setText(self.ui.comboBox_start.currentText()))
            self.ui.Btn_algorithm.clicked.connect(lambda: self.ui.label_end.setText(self.ui.comboBox_end.currentText()))
            self.ui.Btn_algorithm.clicked.connect(lambda: UIFunctions.plot(self, int(g.key_to_name[str(self.ui.comboBox_start.currentText())]), int(g.key_to_name[str(self.ui.comboBox_end.currentText())])))
            ## QTIMER ==> START
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)
            # TIMER IN MILLISECONDS
            self.ui.Btn_algorithm.clicked.connect(lambda: self.timer.start(13))
            self.ui.Btn_algorithm.clicked.connect(lambda: UIFunctions.setInfo(self))

        except:
            print("Error in main GUI function")
        
        self.show()
        

    def progress(self):
    
        global counter
        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            # STOP TIMER
            self.timer.stop()
            counter = 0

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())