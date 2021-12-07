from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt


class WelPanel:
    def __init__(self, main_window):
        self.wel_slogan = QLabel(main_window)
        self.wel_slogan.resize(500, 35)
        self.wel_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.wel_slogan.move(20, 10)

        self.account_slogan = QLabel(main_window)
        self.account_slogan.resize(620, 300)
        self.account_slogan.setAlignment(Qt.AlignCenter)
        self.account_slogan.setStyleSheet('font-size:18px;font-weight:bold;font-family:SimHei;')
        self.account_slogan.move(200, 55)

        self.wel_slogan.setText('欢迎使用！')
        self.account_slogan.setText('作者：曾俊淇\n'
                                    '学号：2019300003058\n\n'
                                    'A*、AO*算法可视化演示\n\n'
                                    'A*：迷宫寻路，点击“A*”进入演示\n'
                                    'AO*：与或图搜索，点击AO*进入演示')

    def hide(self):
        self.wel_slogan.hide()
        self.account_slogan.hide()

    def show(self):
        self.wel_slogan.show()
        self.account_slogan.show()
