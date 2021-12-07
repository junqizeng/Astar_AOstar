import os
from algorithms import Astar, AOstar
from vis_windows import maze_panel, main_windows, tree_panel, wel_panel
from PyQt5.QtWidgets import QMessageBox, QPushButton
from PyQt5.QtGui import QIcon
from vis_windows.images import whu_ico
import base64


class MyWork:
    def __init__(self):
        self.maze_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                         [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                         [0, 2, 1, 0, 1, 1, 1, 0, 1, 3, 1, 1, 0],
                         [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                         [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.start = (3, 1)
        self.end = (3, 9)

        self.tree_map = {0: [[1], [4, 5]],
                         1: [[2], [3]],
                         2: [[3], [2, 5]],
                         3: [[5, 6]],
                         4: [[5], [8]],
                         5: [[6], [7, 8]],
                         6: [[7, 8]],
                         7: [[7]],
                         8: [[8]]}
        self.h_val = [3, 2, 4, 4, 1, 1, 2, 0, 0]

        self.Astar_flag, self.Astar_ans = Astar.Astar(self.maze_map, self.start, self.end)
        self.AOstar_flag, self.AOstar_ans = AOstar.AOstar(self.tree_map, self.h_val)

        self.step_index = 0

        self.main_win = main_windows.MainWindow()
        self.main_win.Astar_btn.clicked.connect(self.jump_to_maze)
        self.main_win.AOstar_btn.clicked.connect(self.jump_to_tree)
        tmp = open(f'./whu.ico', 'wb')
        tmp.write(base64.b64decode(whu_ico.imgs))
        tmp.close()
        self.main_win.setWindowIcon(QIcon('./whu.ico'))
        os.remove(f'./whu.ico')

        self.maze_panel = maze_panel.MazePanel(self.main_win, len(self.Astar_ans))
        self.maze_panel.next_btn.clicked.connect(self.maze_next)
        self.maze_panel.last_btn.clicked.connect(self.maze_last)

        self.tree_panel = tree_panel.TreePanel(self.main_win, len(self.AOstar_ans))
        self.tree_panel.next_btn.clicked.connect(self.tree_next)
        self.tree_panel.last_btn.clicked.connect(self.tree_last)

        self.wel_panel = wel_panel.WelPanel(self.main_win)

        self.wel_panel.show()
        self.maze_panel.hide()
        self.tree_panel.hide()

    def jump_to_maze(self):
        self.step_index = -1
        if not self.Astar_flag:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "对应与或图没有找到解！")
            message_box.setIcon(QMessageBox.Critical)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            return
        self.maze_update(0)
        self.wel_panel.hide()
        self.tree_panel.hide()
        self.maze_panel.show()

    def jump_to_tree(self):
        self.step_index = -1
        if not self.AOstar_flag:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "对应与或图没有找到解！")
            message_box.setIcon(QMessageBox.Critical)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            return
        self.tree_update(0)
        self.wel_panel.hide()
        self.maze_panel.hide()
        self.tree_panel.show()

    def tree_update(self, index_change=1):
        if index_change == 0:
            self.step_index = -1
        elif self.step_index == 0 and index_change == -1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "AO*运行到第一步")
            message_box.setInformativeText("点击上一步，退出运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            self.step_index = -1
        elif self.step_index == len(self.AOstar_ans) - 1 and index_change == 1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "AO*运行到最后一步")
            message_box.setInformativeText("点击下一步，重新运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            self.step_index = -1
        elif self.step_index == -1 and index_change == -1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "请点击下一步开始运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
        else:
            self.step_index = self.step_index + index_change
        self.tree_panel.update(AOstar_ans=self.AOstar_ans, index=self.step_index)

    def tree_next(self):
        self.tree_update(index_change=1)
        self.tree_panel.show()

    def tree_last(self):
        self.tree_update(index_change=-1)
        self.tree_panel.show()

    def maze_update(self, index_change):
        if index_change == 0:
            self.step_index = -1
        elif self.step_index == 0 and index_change == -1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "A*运行到第一步")
            message_box.setInformativeText("点击上一步，退出运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            self.step_index = - 1
        elif self.step_index == len(self.Astar_ans) - 1 and index_change == 1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "A*运行到最后一步")
            message_box.setInformativeText("点击下一步，重新运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
            self.step_index = -1
        elif self.step_index == -1 and index_change == -1:
            message_box = QMessageBox(self.main_win)
            message_box.setWindowTitle("运行提示")
            message_box.setText('<h3>%s</h3>' % "请点击下一步开始运行")
            message_box.setIcon(QMessageBox.Information)
            message_box.addButton(QPushButton('确定', message_box), QMessageBox.YesRole)
            message_box.show()
        else:
            self.step_index = self.step_index + index_change
        self.maze_panel.update(self.maze_map, self.Astar_ans, self.step_index)

    def maze_next(self):
        self.maze_update(index_change=1)
        self.maze_panel.show()

    def maze_last(self):
        self.maze_update(index_change=-1)
        self.maze_panel.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mywork = MyWork()
    mywork.main_win.show()

    sys.exit(app.exec_())
