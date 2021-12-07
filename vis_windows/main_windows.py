from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(850, 650)
        self.setWindowTitle('A* AO*算法演示')
        self.move(int((QApplication.desktop().width()-self.width())*0.5),
                  int((QApplication.desktop().height()-self.height())*0.5))

        self.Astar_btn = QPushButton(self)
        self.Astar_btn.resize(180, 50)
        self.Astar_btn.move(15, 55)
        self.Astar_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.Astar_btn.setText('A* 算法')

        self.AOstar_btn = QPushButton(self)
        self.AOstar_btn.resize(180, 50)
        self.AOstar_btn.move(15, 115)
        self.AOstar_btn.setStyleSheet('background-color:white;font-size:16px')
        self.AOstar_btn.setText('AO* 算法')

