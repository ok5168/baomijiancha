import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_hhx1 import *
from bmjc14 import *

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
    def clear(self):
        self.lineEdit_out.clear()
 
    def shuchu(self):
        p=myWin.lineEdit_mulu.text()
        d=myWin.lineEdit_riqi.text()
        jieguo=chuli(d,p)
        self.plainTextEdit.setPlainText(jieguo)
    # def test2(self):
    #     self.lineEdit_out.insert(self.lineEdit_mulu.text())
    # def test3(self):
        self.lineEdit_out.insert(self.lineEdit_riqi.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    
    myWin.ok.clicked.connect(myWin.shuchu)
   
    # myWin.ok.clicked.connect(myWin.test3)
    sys.exit(app.exec_())