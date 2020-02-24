import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QAction,QLineEdit,QMessageBox,QMainWindow,QProgressBar
#from PyQt5.QtGui import QIcon
#from PyQt5.QtCore import pyqtSlot
#from PyQt5 import QtGui
import sent


class App(QMainWindow):   #App is classname 
    def __init__(self):
        super().__init__()
        self.title = 'Automatic ER Development'
        self.top = 30
        self.left = 200
        self.width = 1020
        self.height = 400
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        mainmenu = self.menuBar()
        fileMenu = mainmenu.addMenu("File")
        '''editMenu = mainmenu.addMenu("Edit")
        viewMenu = mainmenu.addMenu("View")
        searchMenu = mainmenu.addMenu("Search")
        toolsMenu = mainmenu.addMenu("Tools")'''
        helpMenu = mainmenu.addMenu("Help")

        exitButton = QAction("Exit",self)
        exitButton.setShortcut('ctrl+Q')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        aboutButton = QAction("About",self)
        aboutButton.setShortcut('ctrl+A')
        #aboutButton.triggered.connect()
        helpMenu.addAction(aboutButton)
        
        helpButton = QAction("Help",self)
        helpButton.setShortcut('F1')
        #helpButton.triggered.connect()
        helpMenu.addAction(helpButton)
        

        self.textbox = QLineEdit(self)
        self.textbox.move(40,40)
        self.textbox.resize(900,100)

        self.button = QPushButton('Generate ER',self)
        self.button.move(40,160)
        self.button.clicked.connect(self.on_click)
        #self.progress = QProgressBar(self)
        #self.progress.setGeometry(40, 250, 250, 20)
        
        self.show()
        

    #@pyqtSlot()
    def on_click(self):
        #print("PyQt5 button clicked .")
        textBoxValue = self.textbox.text()
        
        QMessageBox.information(self,'Please Wait!','Please Wait while the ER Diagram is Generated in the PDF format in your default PDF Viewer',QMessageBox.Ok,QMessageBox.Ok)
        completion_value = 0
        sent.call_sent(textBoxValue)
        QMessageBox.information(self,'Information!','Your ER Diagram is Generated',QMessageBox.Ok,QMessageBox.Ok)
        #self.progress.setValue(completion_value)
        self.show()
        #self.set_status(100)
        self.textbox.setText("")
        
    '''def set_status(self,progress_value):
        self.progress.setValue(progress_value)'''
    def error_msg(self):
        QMessageBox.information(self,'Information!','The system could not process the input as it\'s invalid.',QMessageBox.Ok,QMessageBox.Ok)
        self.show()

if __name__=='__main__':
    app= QApplication(sys.argv)
    ex = App()
    #ex.set_status()
    sys.exit(app.exec_())