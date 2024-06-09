#!/usr/bin/python3
# -*- coding: utf-8 -*-


from PyQt5.QtGui import QIcon
from ui_py.ui_main_window import Main_Form
# !/usr/bin/env python3
# -*- coding:GBK -*-

from PyQt5.QtWidgets import *
import sys


if __name__ == '__main__':

    app = QApplication(sys.argv)
    # arguments = sys.argv[1:]  # 去除第一个参数（程序本身的路径）

    app.setApplicationName("PyQt MianWindow")
    app.setWindowIcon(QIcon("./ui/images/icon.png"))

    MainWindow = Main_Form()
    # MainWindow = Setup_Dialog()
    # if len(arguments) >= 1:
    #     index = arguments[0].find("log_terminal")
    #     if index >= 0:
    #         MainWindow.EnableTerminalLog()
    MainWindow.show()
    sys.exit(app.exec_())
