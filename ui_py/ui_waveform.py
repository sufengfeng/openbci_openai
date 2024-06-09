#!/usr/bin/env python3
# -*- coding:GBK -*-

import os, sys, re, math

import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QDateTime, QMargins, QTimer, QTime
from PyQt5.QtGui import QBrush, QPen, QColor, QFont
import sys, random
# import QCustomPlot_PyQt5
# from QCustomPlot_PyQt5 import QCustomPlot, QCP, QCPAxisRect, QCPAxis, QCPGraph, QCPScatterStyle, QCPItemBracket, \
#     QCPItemText, QCPItemTracer
# from QCustomPlot_PyQt5 import *

timeStart = QTime.currentTime()


class QCustomPlotWaveform(QWidget):
    def __init__(self):
        super(QCustomPlotWaveform, self).__init__()
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.resize(600, 600)
        self.setWindowTitle("Real Time Data ")
        self.layout = QVBoxLayout(self)
        self.customPlot = QCustomPlot(self)
        self.layout.addWidget(self.customPlot)

        self.customPlot.addGraph()  # blue line
        self.customPlot.graph(0).setPen(QPen(QColor(40, 110, 255)))
        self.customPlot.addGraph()  # red line
        self.customPlot.graph(1).setPen(QPen(QColor(255, 110, 40)))

        self.customPlot.setInteractions(
            QCP.iRangeDrag | QCP.iRangeZoom | QCP.iSelectAxes | QCP.iSelectLegend | QCP.iSelectPlottables)

        timeTicker = QCPAxisTickerTime()
        timeTicker.setTimeFormat("%h:%m:%s")
        self.customPlot.xAxis.setTicker(timeTicker)
        self.customPlot.axisRect().setupFullAxesBox()
        self.customPlot.yAxis.setRange(-1.2, 1.2)
        # make left and bottom axes transfer their ranges to right and top axes:
        self.customPlot.xAxis.rangeChanged[QCPRange].connect(self.customPlot.xAxis2.setRange)
        self.customPlot.yAxis.rangeChanged[QCPRange].connect(self.customPlot.yAxis2.setRange)

        dataTimer = QTimer(self)
        dataTimer.timeout.connect(self.realtimeDataSlot)
        dataTimer.start(10)
        self._ch00Value = 0.0
        self._ch01Value = 0.0

    def realtimeDataSlot(self):
        key = timeStart.msecsTo(QTime.currentTime()) / 1000.0
        # self.customPlot.graph(0).addData(key, math.sin(key))
        # # print(key, math.sin(key)+ random.randint(0,5))
        # self.customPlot.graph(1).addData(key, math.cos(key))
        self.customPlot.graph(0).addData(key, self._ch00Value)
        self.customPlot.graph(1).addData(key, self._ch01Value)
        # self.customPlot.xAxis.setRange(key, 8, Qt.AlignRight)
        self.customPlot.replot()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    test = QCustomPlotWaveform()
    test.show()
    sys.exit(app.exec_())
