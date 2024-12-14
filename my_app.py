from PyQt5.QtCore import qt 
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton, 
    QPushButton, QLabel, QListWidget, QLineEdit,)

from instr import * 
from second_win import *

class MainWin (QWidget): 
   def __init__(self):
    super().__init__()
    # creating and configuring graphic elements
    self.initUI()
    #establish connections between elements
    self.connects()
    #sets what the window will look like (Label, size, location)
    self.set_appear()
    #start: 

def initUI(self): 
  self.btn_next = QPushButton(txt_next, self)
  self.hello_text = QLabel(txt_hello)
  self.instruction = QLabel(txt_instruction)
  self.Layout_line = QVBoxLayout()
  self.Layout_line.addWidgets(self.hello_test, alignment = Qt.AlignLef)
  self.Layout_line.addWidgets(self.instruction, alignment = Qt.Alignlef)
  self.Lyout_line.addWidgets(self.btn_next, alignment = Qt.Aligncente)
  self.setLayout(self.Layout.line)
