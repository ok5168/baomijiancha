'''
2020-2-13 OK!
'''

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from Ui_hhx1 import *
from bmjc14 import *  #导入具体处理过程

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
    def clear(self):
        self.lineEdit_out.clear()
 
    def shuchu(self):
        self.plainTextEdit.clear()   #清空输出框
        p=myWin.lineEdit_mulu.text() #取得目录文本框的内容
        d=myWin.dateEdit.date().toString("yyyy-MM-dd") #取得日期文本框的内容
        print(d)
        jieguo=chuli(d,p)  #调用外部bmjc14模块中的chuli函数
        self.plainTextEdit.setPlainText(jieguo) #在plainTextEdit输出结果
      
        # self.plainTextEdit.appendHtml(jieguo) #在plainTextEdit输出结果

def test():
    # app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    myWin = MyWindow()
    myWin.show()
    myWin.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
    myWin.ok.clicked.connect(myWin.shuchu) #点击ok按钮后执行
   
    # myWin.ok.clicked.connect(myWin.test3)
    sys.exit(app.exec_())