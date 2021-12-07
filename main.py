import mywork

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    mywork = mywork.MyWork()
    mywork.main_win.show()

    sys.exit(app.exec_())
