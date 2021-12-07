from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QTextEdit
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MazePanel:
    def __init__(self, main_window, steps):
        self.main_window = main_window
        self.pos_x = 214
        self.width = 620
        self.steps = steps

        self.state_slogan = QLabel(main_window)
        self.state_slogan.resize(500, 35)
        self.state_slogan.setText(f'   状态: A*算法演示中，共{self.steps}步，点击下一步开始演示')
        self.state_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.state_slogan.move(10, 10)

        self.last_btn = QPushButton(main_window)
        self.last_btn.resize(90, 35)
        self.last_btn.move(640, 10)
        self.last_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.last_btn.setText('上一步')

        self.next_btn = QPushButton(main_window)
        self.next_btn.resize(90, 35)
        self.next_btn.setStyleSheet('background-color:white;font-size:16px;')
        self.next_btn.move(745, 10)
        self.next_btn.setText('下一步')

        self.maze_slogan = QLabel(main_window)
        self.maze_slogan.resize(500, 35)
        self.maze_slogan.setText('问题迷宫')
        self.maze_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.maze_slogan.move(230, 50)

        self.explain_slogan = QLabel(main_window)
        self.explain_slogan.resize(500, 35)
        self.explain_slogan.setText('演示说明')
        self.explain_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.explain_slogan.move(230, 435)

        self.explain_tx = QTextEdit(main_window)
        self.explain_tx.setStyleSheet('font-size:16px')
        self.explain_tx.resize(558, 160)
        self.explain_tx.setReadOnly(True)
        self.explain_tx.move(230, 470)
        self.explain_tx.setText('<body>'
                                '使用A*算法对给定迷宫进行寻路<br>'
                                '黑色块：墙壁<br>'
                                '白色块：可走道路<br>'
                                '<font color="blue">蓝色块</font>：起点<br>'
                                '<font color="red">红色块</font>：终点<br>'
                                '<font color="gold">黄色块</font>：搜索边界<br>'
                                '<font color="green">绿色块</font>：已搜索位置'
                                '<body>')

        self.maze = None

    def show(self):
        self.maze.show()
        self.state_slogan.show()
        self.last_btn.show()
        self.next_btn.show()
        self.maze_slogan.show()
        self.explain_tx.show()
        self.explain_slogan.show()

    def hide(self):
        if self.maze is not None:
            self.maze.hide()
        self.state_slogan.hide()
        self.last_btn.hide()
        self.next_btn.hide()
        self.maze_slogan.hide()
        self.explain_tx.hide()
        self.explain_slogan.hide()

    def update(self, maze_map, Astar_ans, step_index):
        if self.maze is not None:
            self.maze.hide()
        if step_index == -1:
            maze_tuple = maze_map
            self.state_slogan.setText(f'   状态: A*算法演示中，共{self.steps}步，点击下一步开始演示')
        else:
            maze_tuple = Astar_ans[step_index]
            self.state_slogan.setText(f'   状态: A*算法演示中，当前第{step_index+1}/{self.steps}步')
        self.maze = Maze(maze_tuple)
        self.maze.setParent(self.main_window)
        self.maze.move(230, 90)
        self.maze.setStyleSheet('background-color:white')


class Maze(QWidget):
    def __init__(self, maze_tuple):
        super(Maze, self).__init__()
        self.maze_tuple = maze_tuple
        self.col_len = 40
        self.col_interval = 3
        self.row_len = 40
        self.row_interval = 3

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.maze_update(painter)
        painter.end()

    def maze_update(self, painter):

        for i in range(len(self.maze_tuple)):
            for j in range(len(self.maze_tuple[0])):
                # 0：屏障 1：可走 2：起点 3：终点 4：已访问点 5：访问边界
                if self.maze_tuple[i][j] == 0:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.black)
                if self.maze_tuple[i][j] == 1:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.white)
                if self.maze_tuple[i][j] == 2:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.blue)
                if self.maze_tuple[i][j] == 3:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.red)
                if self.maze_tuple[i][j] == 4:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.green)
                if self.maze_tuple[i][j] == 5:
                    painter.setPen(Qt.black)
                    painter.setBrush(Qt.yellow)
                painter.drawRect(j * (self.row_len + self.row_interval), i * (self.col_len + self.col_interval),
                                 self.row_len, self.col_len)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication, QWidget

    app = QApplication(sys.argv)
    login_win = QWidget()
    login_win.setFixedSize(850, 650)
    recv = MazePanel(login_win)
    login_win.show()

    sys.exit(app.exec_())
