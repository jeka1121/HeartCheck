from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton, 
    QPushButton, QLabel, QListWidget, QLineEdit,)

from instr import * 
from second_win import *

class MainWin (QWidget): 
    def     __init__(self):
        super().__init__()
        # creating and configuring graphic elements
        self.initUI()
        #establish connections between elements
        self.connects()
        #sets what the window will look like (Label, size, location)
        self.set_appear()
        #start: 
        self.show()

    def initUI(self): 
        self.btn_next = QPushButton(txt_next, self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.Layout_line = QVBoxLayout()
        self.Layout_line.addWidget(self.hello_text, alignment = Qt.AlignLeft)
        self.Layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft)
        self.Layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.setLayout(self.Layout_line)


    def next_click(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw =MainWin()
app.exec()

