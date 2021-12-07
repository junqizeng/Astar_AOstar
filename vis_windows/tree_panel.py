import os
from vis_windows.images.AOstar import AO_images
from PyQt5.QtWidgets import QLabel, QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPixmap
import base64


class TreePanel:
    def __init__(self, main_window, steps):
        self.pos_x = 214
        self.width = 620
        self.steps = steps

        self.state_slogan = QLabel(main_window)
        self.state_slogan.resize(500, 35)
        self.state_slogan.setText(f'   状态: AO*算法演示中，共{self.steps}步，点击下一步开始演示')
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

        self.image_lb = QLabel(main_window)
        self.image_lb.resize(400, 400)
        self.image_lb.setScaledContents(True)
        self.image_lb.move(360, 50)
        self.image_lb.setStyleSheet('background-color:white')

        self.image_title = QLabel(main_window)
        self.image_title.setText('问题与或图：')
        self.image_title.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.image_title.move(self.image_lb.x() - self.image_title.width(), self.image_lb.y())

        self.ans_tx = QTextEdit(main_window)
        self.ans_tx.setStyleSheet('font-size:16px')
        self.ans_tx.resize(self.image_lb.width(), 170)
        self.ans_tx.setReadOnly(True)
        self.ans_tx.move(self.image_lb.x(), self.image_lb.y() + 10 + self.image_lb.height())
        self.ans_tx.setPlaceholderText("点击“下一步”开始AO*图搜索，这里显示每一轮搜索后选择标记的路径！")

        self.ans_title = QLabel(main_window)
        self.ans_title.setText('AO*搜索过程：')
        self.ans_title.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.ans_title.move(self.ans_tx.x() - self.ans_title.width() - 3, self.ans_tx.y())

        self.images = AO_images.imgs

        self.explain_slogan = QLabel(main_window)
        self.explain_slogan.resize(500, 35)
        self.explain_slogan.setText('演示说明')
        self.explain_slogan.setStyleSheet('font-size:16px;font-weight:bold;font-family:SimHei;')
        self.explain_slogan.move(15, 200)

        self.explain_tx = QTextEdit(main_window)
        self.explain_tx.setStyleSheet('font-size:16px')
        self.explain_tx.resize(180, 400)
        self.explain_tx.setReadOnly(True)
        self.explain_tx.move(15, 230)
        self.explain_tx.setText('<body>'
                                '使用AO*算法对给定与或图进行求解<br><br>'
                                'n1：结点编号<br>'
                                '圆圈数字：cost值<br>'
                                '<font color="blue">蓝色圈</font>：待解结点<br>'
                                '<font color="green">绿色圈</font>：已解结点<br>'
                                '<font color="red">红色边</font>：与边<br>'
                                '黑色边：或边<br>'
                                '<font color="blue">蓝色边</font>：标记边<br>'
                                '<body>')

    def show(self):
        self.state_slogan.show()
        self.last_btn.show()
        self.next_btn.show()
        self.image_lb.show()
        self.image_title.show()
        self.ans_tx.show()
        self.ans_title.show()
        self.explain_slogan.show()
        self.explain_tx.show()

    def hide(self):
        self.state_slogan.hide()
        self.last_btn.hide()
        self.next_btn.hide()
        self.image_lb.hide()
        self.image_title.hide()
        self.ans_tx.hide()
        self.ans_title.hide()
        self.explain_slogan.hide()
        self.explain_tx.hide()

    def update(self, AOstar_ans, index):
        update_text = ""
        if index == -1:
            self.ans_tx.setText("")
            self.state_slogan.setText(f'   状态: AO*算法演示中，共{self.steps}步，点击下一步开始演示')
        else:
            update_text = ""
            for i in range(index+1):
                start_text = "n"+str(AOstar_ans[i][0])
                ends = AOstar_ans[i][1]
                ends_text = ""
                for j in range(len(ends)):
                    if j == len(ends)-1:
                        ends_text += "n"+str(ends[j]) + "弧"
                    else:
                        ends_text += "n"+str(ends[j]) + "--"
                update_text += start_text + " -> " + ends_text + "\n"
            self.state_slogan.setText(f'   状态: AO*算法演示中，当前第{index+1}/{self.steps}步')
        tmp = open(f'./{index}.png', 'wb')
        tmp.write(base64.b64decode(self.images[index+1]))
        tmp.close()
        cur_image = QPixmap(f'./{index}.png')
        self.image_lb.setPixmap(cur_image)
        self.ans_tx.setText(update_text)
        os.remove(f'./{index}.png')


if __name__ == '__main__':

    import sys
    from PyQt5.QtWidgets import QApplication, QWidget
    app = QApplication(sys.argv)
    login_win = QWidget()
    login_win.setFixedSize(850, 650)
    recv = TreePanel(login_win)
    login_win.show()

    sys.exit(app.exec_())
