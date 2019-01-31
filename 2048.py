import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import random
from PyQt5.QtCore import pyqtSignal


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pole = [['1', '1', '1', '1'],
                     ['1', '1', '1', '1'],
                     ['1', '1', '1', '1'],
                     ['1', '1', '1', '1']]

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('2048')

        self.btn_up = QPushButton('Z', self)
        self.btn_up.resize(25, 25)
        self.btn_up.move(250, 200)
        self.btn_up.clicked.connect(self.c)

        self.btn_down = QPushButton('', self)
        self.btn_down.resize(25, 25)
        self.btn_down.move(250, 150)
        self.btn_down.clicked.connect(self.c2)

        self.btn_left = QPushButton('', self)
        self.btn_left.resize(25, 25)
        self.btn_left.move(250, 100)
        self.btn_left.clicked.connect(self.c3)

        self.btn_right = QPushButton('', self)
        self.btn_right.resize(25, 25)
        self.btn_right.move(250, 50)
        self.btn_right.clicked.connect(self.c4)

        self.btn1 = QPushButton(self.pole[3][3], self)
        self.btn1.resize(50, 50)
        self.btn1.move(200, 200)
        self.btn1.clicked.connect(self.b)

        self.btn2 = QPushButton(self.pole[3][2], self)
        self.btn2.resize(50, 50)
        self.btn2.move(200, 150)
        self.btn2.clicked.connect(self.b2)

        self.btn3 = QPushButton(self.pole[3][1], self)
        self.btn3.resize(50, 50)
        self.btn3.move(200, 100)
        self.btn3.clicked.connect(self.b3)

        self.btn4 = QPushButton(self.pole[3][0], self)
        self.btn4.resize(50, 50)
        self.btn4.move(200, 50)
        self.btn4.clicked.connect(self.b4)

        self.btn5 = QPushButton(self.pole[2][3], self)
        self.btn5.resize(50, 50)
        self.btn5.move(150, 200)
        self.btn5.clicked.connect(self.b5)

        self.btn6 = QPushButton(self.pole[2][2], self)
        self.btn6.resize(50, 50)
        self.btn6.move(150, 150)
        self.btn6.clicked.connect(self.b6)

        self.btn7 = QPushButton(self.pole[2][1], self)
        self.btn7.resize(50, 50)
        self.btn7.move(150, 100)
        self.btn7.clicked.connect(self.b7)

        self.btn8 = QPushButton(self.pole[2][0], self)
        self.btn8.resize(50, 50)
        self.btn8.move(150, 50)
        self.btn8.clicked.connect(self.b8)

        self.btn9 = QPushButton(self.pole[1][3], self)
        self.btn9.resize(50, 50)
        self.btn9.move(100, 200)
        self.btn9.clicked.connect(self.b9)

        self.btn10 = QPushButton(self.pole[1][2], self)
        self.btn10.resize(50, 50)
        self.btn10.move(100, 150)
        self.btn10.clicked.connect(self.b10)

        self.btn11 = QPushButton(self.pole[1][1], self)
        self.btn11.resize(50, 50)
        self.btn11.move(100, 100)
        self.btn11.clicked.connect(self.b11)

        self.btn12 = QPushButton(self.pole[1][0], self)
        self.btn12.resize(50, 50)
        self.btn12.move(100, 50)
        self.btn12.clicked.connect(self.b12)

        self.btn13 = QPushButton(self.pole[0][3], self)
        self.btn13.resize(50, 50)
        self.btn13.move(50, 200)
        self.btn13.clicked.connect(self.b13)

        self.btn14 = QPushButton(self.pole[0][2], self)
        self.btn14.resize(50, 50)
        self.btn14.move(50, 150)
        self.btn14.clicked.connect(self.b14)

        self.btn15 = QPushButton(self.pole[0][1], self)
        self.btn15.resize(50, 50)
        self.btn15.move(50, 100)
        self.btn15.clicked.connect(self.b15)

        self.btn16 = QPushButton(self.pole[0][0], self)
        self.btn16.resize(50, 50)
        self.btn16.move(50, 50)
        self.btn16.clicked.connect(self.b16)

    def b(self):
        self.btn.setText('X')

    def b2(self):
        self.btn2.setText('X')

    def b3(self):
        self.btn3.setText('X')

    def b4(self):
        self.bt4.setText('X')

    def b5(self):
        self.btn5.setText('X')

    def b6(self):
        self.btn6.setText('X')

    def b7(self):
        self.btn7.setText('X')

    def b8(self):
        self.btn8.setText('X')

    def b9(self):
        self.btn9.setText('X')

    def b10(self):
        self.btn10.setText('X')

    def b11(self):
        self.btn11.setText('X')

    def b12(self):
        self.btn12.setText('X')

    def b13(self):
        self.btn13.setText('X')

    def b14(self):
        self.btn14.setText('X')

    def b15(self):
        self.btn15.setText('X')

    def b16(self):
        self.btn16.setText('X')

    def c(self):
        self.btn_up.setText('wee')
        self.move_u()
        self.plus()
        self.change_text()

    def c2(self):
        self.btn_down.setText('down')
        self.move_d()
        self.plus()
        self.change_text()

    def c3(self):
        self.btn_left.setText('left')
        self.move_l()
        self.plus()
        self.change_text()
        self.move_l()

    def c4(self):
        self.btn_right.setText('right')
        self.move_r()
        self.plus()
        self.change_text()

    def change_text(self):
        self.btn1.setText(str(self.pole[0][0]))
        self.btn2.setText(str(self.pole[0][1]))
        self.btn3.setText(str(self.pole[0][2]))
        self.btn4.setText(str(self.pole[0][3]))
        self.btn5.setText(str(self.pole[1][0]))
        self.btn6.setText(str(self.pole[1][1]))
        self.btn7.setText(str(self.pole[1][2]))
        self.btn8.setText(str(self.pole[1][3]))
        self.btn9.setText(str(self.pole[2][0]))
        self.btn10.setText(str(self.pole[2][1]))
        self.btn11.setText(str(self.pole[2][2]))
        self.btn12.setText(str(self.pole[2][3]))
        self.btn13.setText(str(self.pole[3][0]))
        self.btn14.setText(str(self.pole[3][1]))
        self.btn15.setText(str(self.pole[3][2]))
        self.btn16.setText(str(self.pole[3][3]))

    def move_l(self):
        for k in range(2):
            for i in range(4):
                for j in range(1, 4):
                    if self.pole[i][j] == 1:
                        self.pole[i][j] = self.pole[i][j - 1]
                        self.pole[i][j - 1] = 1
                    if self.pole[i][j] == self.pole[i][j - 1] != 1:
                        self.pole[i][j - 1] = 1
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)

    def move_r(self):
        for k in range(2):
            for i in range(4):
                for j in range(3):
                    if self.pole[i][j] == 1:
                        self.pole[i][j] = self.pole[i][j + 1]
                        self.pole[i][j + 1] = 1
                    if self.pole[i][j] == self.pole[i][j + 1] != 1:
                        self.pole[i][j + 1] = 1
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)

    def move_d(self):
        for k in range(2):
            for i in range(1, 4):
                for j in range(1, 4):
                    if self.pole[i][j] == 1:
                        self.pole[i][j] = self.pole[i - 1][j]
                        self.pole[i - 1][j] = 1
                    if self.pole[i][j] == self.pole[i - 1][j] != 1:
                        self.pole[i - 1][j] = 1
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)

    def move_u(self):
        print('hi')
        for k in range(2):
            for i in range(3):
                for j in range(3):
                    if self.pole[i][j] == 1:
                        self.pole[i][j] = self.pole[i + 1][j]
                        self.pole[i + 1][j] = 1
                    if self.pole[i][j] == self.pole[i + 1][j] != 1:
                        self.pole[i + 1][j] = 1
                        self.pole[i][j] = str(int(self.pole[i][j]) * 2)

    def plus(self):
        r = random.randint(1, 4)
        string = random.randint(0, 3)
        collum = random.randint(0, 3)
        while self.pole[string][collum] != 1:
            string = random.randint(0, 3)
            collum = random.randint(0, 3)
            print(string, collum)
        if r == 1 or r == 2 or r == 3:
            self.pole[string][collum] = 2
        else:
            self.pole[string][collum] = 4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
