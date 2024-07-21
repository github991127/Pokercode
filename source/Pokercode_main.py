from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

import Pokercode
from list_themes import *


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Pokercode.ui')

        self.ui.toolButton_s1.clicked.connect(self.handleCalc_s1)
        self.ui.toolButton_s2.clicked.connect(self.handleCalc_s2)
        self.ui.toolButton_s3.clicked.connect(self.handleCalc_s3)
        self.ui.toolButton_s4.clicked.connect(self.handleCalc_s4)
        self.ui.toolButton_s5.clicked.connect(self.handleCalc_s5)

        self.ui.toolButton_h1.clicked.connect(self.handleCalc_h1)
        self.ui.toolButton_h2.clicked.connect(self.handleCalc_h2)
        self.ui.toolButton_h3.clicked.connect(self.handleCalc_h3)
        self.ui.toolButton_h4.clicked.connect(self.handleCalc_h4)
        self.ui.toolButton_h5.clicked.connect(self.handleCalc_h5)

        self.ui.toolButton_c1.clicked.connect(self.handleCalc_c1)
        self.ui.toolButton_c2.clicked.connect(self.handleCalc_c2)
        self.ui.toolButton_c3.clicked.connect(self.handleCalc_c3)
        self.ui.toolButton_c4.clicked.connect(self.handleCalc_c4)

        self.ui.toolButton_d1.clicked.connect(self.handleCalc_d1)
        self.ui.toolButton_d2.clicked.connect(self.handleCalc_d2)
        self.ui.toolButton_d3.clicked.connect(self.handleCalc_d3)
        self.ui.toolButton_d4.clicked.connect(self.handleCalc_d4)
        self.ui.toolButton_d5.clicked.connect(self.handleCalc_d5)
        self.ui.toolButton_d6.clicked.connect(self.handleCalc_d6)
        self.ui.toolButton_d7.clicked.connect(self.handleCalc_d7)

        self.ui.toolButton_1.clicked.connect(self.handleCalc_1)
        self.ui.toolButton_2.clicked.connect(self.handleCalc_2)
        self.ui.toolButton_3.clicked.connect(self.handleCalc_3)
        self.ui.toolButton_4.clicked.connect(self.handleCalc_4)
        self.ui.toolButton_5.clicked.connect(self.handleCalc_5)
        self.ui.toolButton_6.clicked.connect(self.handleCalc_6)
        self.ui.toolButton_7.clicked.connect(self.handleCalc_7)
        self.ui.toolButton_8.clicked.connect(self.handleCalc_8)
        self.ui.toolButton_9.clicked.connect(self.handleCalc_9)

    def handleCalc_1(self):
        poker = self.ui.textEdit_1.toPlainText()
        letter = Pokercode.poker_to_letter(poker)
        self.ui.textEdit_2.setPlainText(letter)

    def handleCalc_2(self):
        letter = self.ui.textEdit_2.toPlainText()
        poker = Pokercode.letter_to_poker(letter)
        self.ui.textEdit_1.setPlainText(poker)

    def handleCalc_3(self):
        self.ui.textEdit_1.insertPlainText(',')
        self.ui.textEdit_2.insertPlainText(',')

    def handleCalc_4(self):
        self.ui.textEdit_1.insertPlainText('.')
        self.ui.textEdit_2.insertPlainText('.')

    def handleCalc_5(self):
        self.ui.textEdit_1.insertPlainText('?')
        self.ui.textEdit_2.insertPlainText('?')

    def handleCalc_6(self):
        self.ui.textEdit_1.insertPlainText('!')
        self.ui.textEdit_2.insertPlainText('!')

    def handleCalc_7(self):
        str = self.ui.textEdit_1.toPlainText()
        str = str[:-2]
        self.ui.textEdit_1.setPlainText(str)
        str = self.ui.textEdit_2.toPlainText()
        str = str[:-1]
        self.ui.textEdit_2.setPlainText(str)

    def handleCalc_8(self):
        self.ui.textEdit_1.insertPlainText('\n')
        self.ui.textEdit_2.insertPlainText('\n')

    def handleCalc_9(self):
        self.ui.textEdit_1.setPlainText("")
        self.ui.textEdit_2.setPlainText("")

    def handleCalc_s1(self):
        self.ui.textEdit_1.insertPlainText('♠1')
        self.ui.textEdit_2.insertPlainText('s')

    def handleCalc_s2(self):
        self.ui.textEdit_1.insertPlainText('♠2')
        self.ui.textEdit_2.insertPlainText('p')

    def handleCalc_s3(self):
        self.ui.textEdit_1.insertPlainText('♠3')
        self.ui.textEdit_2.insertPlainText('a')

    def handleCalc_s4(self):
        self.ui.textEdit_1.insertPlainText('♠4')
        self.ui.textEdit_2.insertPlainText('d')

    def handleCalc_s5(self):
        self.ui.textEdit_1.insertPlainText('♠5')
        self.ui.textEdit_2.insertPlainText('e')

    def handleCalc_h1(self):
        self.ui.textEdit_1.insertPlainText('♥1')
        self.ui.textEdit_2.insertPlainText('h')

    def handleCalc_h2(self):
        self.ui.textEdit_1.insertPlainText('♥2')
        self.ui.textEdit_2.insertPlainText('e')

    def handleCalc_h3(self):
        self.ui.textEdit_1.insertPlainText('♥3')
        self.ui.textEdit_2.insertPlainText('a')

    def handleCalc_h4(self):
        self.ui.textEdit_1.insertPlainText('♥4')
        self.ui.textEdit_2.insertPlainText('r')

    def handleCalc_h5(self):
        self.ui.textEdit_1.insertPlainText('♥5')
        self.ui.textEdit_2.insertPlainText('t')

    def handleCalc_c1(self):
        self.ui.textEdit_1.insertPlainText('♣1')
        self.ui.textEdit_2.insertPlainText('c')

    def handleCalc_c2(self):
        self.ui.textEdit_1.insertPlainText('♣2')
        self.ui.textEdit_2.insertPlainText('l')

    def handleCalc_c3(self):
        self.ui.textEdit_1.insertPlainText('♣3')
        self.ui.textEdit_2.insertPlainText('u')

    def handleCalc_c4(self):
        self.ui.textEdit_1.insertPlainText('♣4')
        self.ui.textEdit_2.insertPlainText('b')

    def handleCalc_d1(self):
        self.ui.textEdit_1.insertPlainText('♦1')
        self.ui.textEdit_2.insertPlainText('d')

    def handleCalc_d2(self):
        self.ui.textEdit_1.insertPlainText('♦2')
        self.ui.textEdit_2.insertPlainText('i')

    def handleCalc_d3(self):
        self.ui.textEdit_1.insertPlainText('♦3')
        self.ui.textEdit_2.insertPlainText('a')

    def handleCalc_d4(self):
        self.ui.textEdit_1.insertPlainText('♦4')
        self.ui.textEdit_2.insertPlainText('m')

    def handleCalc_d5(self):
        self.ui.textEdit_1.insertPlainText('♦5')
        self.ui.textEdit_2.insertPlainText('o')

    def handleCalc_d6(self):
        self.ui.textEdit_1.insertPlainText('♦6')
        self.ui.textEdit_2.insertPlainText('n')

    def handleCalc_d7(self):
        self.ui.textEdit_1.insertPlainText('♦7')
        self.ui.textEdit_2.insertPlainText('d')


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[29], extra=extra, invert_secondary=False)  # 默认dark-False
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    stats = Stats()
    stats.ui.show()
    app.exec_()
