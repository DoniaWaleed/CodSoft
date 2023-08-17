import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# -------------------------Dark Theme--------------------------------------------------
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.black)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
# -------------------------Dark Theme--------------------------------------------------


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.WindowIcon = QIcon('images/icon.png')
        self.setWindowTitle("Calculator")
        self.setWindowIcon(self.WindowIcon)
        self.setMinimumSize(680, 1120)
        self.setMaximumHeight(1120)

        self.mainLayout = QVBoxLayout()

        self.LCD_Screen = QLCDNumber()
        self.LCD_Screen.setNumDigits(10)
        self.LCD_Screen.setSmallDecimalPoint(True)
        self.LCD_Screen.setMinimumSize(637, 250)

        self.ScreenText = ''
        self.chkScreenText = False
        self.tempText = ''
        self.numbers_and_operations = []

        self.gridLayout = QGridLayout()

        calc_btn_names = ['C', '(', ')', '%', '7', '8', '9', '÷', '4', '5', '6', '×', '1', '2', '3', '-', '0', '.', '=', '+']

        calc_btns = []
        for i in range(20):
            calc_btns.append(QPushButton(str(calc_btn_names[i])))
            calc_btns[i].setMinimumSize(150, 150)
            calc_btns[i].setFont(QFont('Arial', 15))
            calc_btns[i].clicked.connect(lambda _, index=i: self.btn_click(str(calc_btn_names[index])))
            if i == 0 or i == 18:
                calc_btns[i].setStyleSheet("background-color :rgb(139, 186, 187)")

        list_counter = 0
        for i in range(5):
            for j in range(4):
                self.gridLayout.addWidget(calc_btns[list_counter], i, j, QtCore.Qt.AlignCenter)
                list_counter += 1

        self.mainLayout.addWidget(self.LCD_Screen)
        self.mainLayout.addLayout(self.gridLayout)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)
        self.adjustSize()

    # -------------------------Functions-----------------------------------------------START
    def btn_click(self, btnText):
        error = QMessageBox()
        error.setWindowTitle("Error!!")
        error.setIcon(QMessageBox.Critical)
        error.setWindowIcon(QIcon('images/icon.png'))
        error.setText("InCorrect Equation!!                               ")
        if btnText in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            self.ScreenText += btnText
            self.tempText = ''
            self.LCD_Screen.display(self.ScreenText)
        elif btnText in ('(', ')', '%', '÷', '×', '-', '+'):
            if self.ScreenText == '' and btnText != '(' and self.numbers_and_operations[len(self.numbers_and_operations)-1] not in (')', '%'):
                print('List: ', self.numbers_and_operations)
                error.setText("InCorrect Equation!!                               ")
                error.exec()
                self.LCD_Screen.display(0)
                self.ScreenText = ''
                self.tempText = ''
                self.numbers_and_operations = []
            elif btnText == '(' or btnText == ')':
                if self.ScreenText != '':
                    self.numbers_and_operations.append(self.ScreenText)
                self.ScreenText = btnText
                self.LCD_Screen.display(self.ScreenText)
                self.numbers_and_operations.append(self.ScreenText)
                self.tempText = btnText
                self.ScreenText = ''
            else:
                self.numbers_and_operations.append(self.ScreenText)
                self.ScreenText = btnText
                self.LCD_Screen.display(self.ScreenText)
                self.numbers_and_operations.append(self.ScreenText)
                self.tempText = btnText
                self.ScreenText = ''
        elif btnText == '.':
            self.ScreenText += btnText
            self.tempText = btnText
            self.LCD_Screen.display(self.ScreenText)
        elif btnText in ('C', '='):
            if btnText == 'C':
                self.numbers_and_operations = []
                self.ScreenText = ''
                self.tempText = btnText
                self.LCD_Screen.display(0)
            elif btnText == '=':
                self.chkScreenText = self.ScreenText.replace('.', '', 1).isdigit()
                if self.tempText in ('(', ')', '%'):
                    if self.ScreenText != '':
                        self.numbers_and_operations.append(self.ScreenText)
                    print('List: ', self.numbers_and_operations)
                    equation = ''
                    for parameter in self.numbers_and_operations:
                        if parameter == '×':
                            equation += '*'
                        elif parameter == '÷':
                            equation += '/'
                        elif parameter == '%':
                            equation += '*(1/100)'
                        else:
                            equation += str(parameter)
                    answer = 0
                    try:
                        answer = eval(equation.strip())
                    except:
                        error.setText("InCorrect Equation!!                               ")
                        error.exec()
                        self.LCD_Screen.display(0)
                    print('Equation: ', equation)
                    print('Answer: ', answer)
                    self.ScreenText = answer
                    self.LCD_Screen.display(str(answer))
                    self.numbers_and_operations = []
                    self.ScreenText = ''
                    self.tempText = ''

                elif self.ScreenText == '' or self.chkScreenText:
                    if self.ScreenText != '':
                        self.numbers_and_operations.append(self.ScreenText)
                    print('List: ', self.numbers_and_operations)
                    equation = ''
                    for parameter in self.numbers_and_operations:
                        if parameter == '×':
                            equation += '*'
                        elif parameter == '÷':
                            equation += '/'
                        elif parameter == '%':
                            equation += '*(1/100)'
                        else:
                            equation += str(parameter)
                    answer = 0
                    try:
                        answer = eval(equation.strip())
                    except:
                        error.setText("InCorrect Equation!!                               ")
                        error.exec()
                        self.LCD_Screen.display(0)
                    print('Equation: ', equation)
                    print('Answer: ', answer)
                    self.ScreenText = answer
                    self.LCD_Screen.display(str(answer))
                    self.numbers_and_operations = []
                    self.ScreenText = ''

    # -------------------------Functions-------------------------------------------END

# -------------------------Class MainWindow----------------------------------------END


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(palette)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
