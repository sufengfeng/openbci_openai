import logging
import os

import sys
from idlelib import query

import qdarkstyle
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

from ui.main_window import Ui_MainWindow

# def ReceiveData(name,_self):
#     while _self.m_bIsRunning:

from ctypes import *
# import xlwt
from math import log, sin, atan
from ui.setup import Ui_MainWindow
UART_CANOPEN_FILE01=0x01
UART_CANOPEN_FILE02=0x01
UART_CANOPEN_FILE03=0x01
UART_CANOPEN_FILE04=0x01
class Setup_Dialog(QtWidgets.QMainWindow, Ui_MainWindow):
    signal_TestControl = pyqtSignal(str)
    def __init__(self):
        super(Setup_Dialog, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.m_bIsConnected = False
        self.m_lDataList = []
        self.m_lDataListSend = []
        # 串口相关
        self.m_dUartCom = QSerialPort()
        self.m_dUartCom.readyRead.connect(self.on_UartRecvInterrupt)

        self.m_lUartNameList = []
        self.m_lUartDescList = []
        self.m_nUartPortcount = 0
        self.refreash_uart_port()  # 刷新uart
        self.pushButton_uartRefresh.clicked.connect(self.refreash_uart_port)
        self.pushButton_Connect_uart.clicked.connect(self.On_Connect_uart)
        self.g_BEnableTerminalLog = False

    def on_UartRecvInterrupt(self):  # 串口接收处理
        if self.m_bIsConnected:
            revData = self.m_dUartCom.readAll()
            # revData = bytes(revData)
            try:
                revData = str(revData, encoding='utf-8')
                self.signal_TestControl.emit(revData)
            except Exception as e:
                logging.error(e)
            # if (revData[0] == UART_CANOPEN_FILE01 and revData[1] == UART_CANOPEN_FILE02 and revData[
            #     2] == UART_CANOPEN_FILE03 and revData[3] == UART_CANOPEN_FILE04):
            #     recv_msg = revData[7]
            #     recv_msg.ID = revData[4] + revData[5] * 256
            #     # for i in range(len(revData) - 7):
            #     #     recv_msg.Data[i] = revData[i + 6]
            #     # self.hanleReceive(8, recv_msg)
            # else:
            #     revData_ = bytes(revData)
            #     print('%d read' % len(revData_))
            #     # string = str(revData_, 'utf-8')
            #     string = str(revData_, 'GBK')
            #     print(string)

    def refreash_uart_port(self):
        # self.plainTextEdit.setReadOnly(1)

        self.comboBox_uartPort.clear()
        self.m_lUartNameList.clear()
        self.m_lUartDescList.clear()
        self.com = QSerialPort()
        port_numb = QSerialPortInfo.availablePorts()
        for info in port_numb:
            if info.portName().count('COM', 0, len(info.portName())) != 0:
                uart_str_desc = info.description().split()
                uart_str_name = info.portName().split()
                self.m_lUartNameList.append(uart_str_name[0])
                self.m_lUartDescList.append(uart_str_desc[0])
        else:
            # print("uart_desc_list = %s" % uart_desc_list)
            # print("uart_name_list = %s" % uart_name_list)
            count = str(self.m_lUartNameList).count('COM', 0, len(str(self.m_lUartNameList)))
            # print("count= %s" % count)
            if count > 256:
                QMessageBox.critical(self, '错误', '连接串口太多')
            else:
                for i in range(0, count):
                    self.comboBox_uartPort.addItem(self.m_lUartNameList[i] + ' ' + self.m_lUartDescList[i])

    def On_Connect_uart(self):
        comindex = self.comboBox_uartPort.currentIndex()
        self.m_dUartCom.setPortName(self.m_lUartNameList[comindex])
        baudRate = int(self.comboBox_uartBaudRate.currentText())
        self.m_dUartCom.setBaudRate(baudRate)
        if self.m_bIsConnected:
            self.m_dUartCom.close()
            self.m_bIsConnected = False
            self.pushButton_Connect_uart.setText("Connect")
            self.statusbar.showMessage("disconnected...", 3000)
            self.hide()
        else:
            if self.m_dUartCom.open(QSerialPort.ReadWrite) == False:
                QMessageBox.critical(self, '错误', '连接串口失败')
                return
            self.m_bIsConnected = True

            self.pushButton_Connect_uart.setText("Disconnect")
            self.statusbar.showMessage("{0} connected...".format(self.m_lUartNameList[comindex]), 3000)
            self.hide()

    def SendDataByUart(self, send_msg):
        if self.g_BEnableTerminalLog:  # 使能terminal日志
            print(send_msg.decode())
        if self.m_bIsConnected:
            writeData = []

            # data_len=len(send_msg)
            # writeData.append(data_len & 0xff)
            # writeData.append(data_len // 0xff)
            # # writeData.append(id & 0xff)
            # # writeData.append(id // 0xff)
            # for i in range(len(send_msg)):
            #     tmpValue=int(send_msg[i]*10)
            #     writeData.append(tmpValue & 0xff)
            #     writeData.append(tmpValue // 0xff)
            # writeData_ = bytes(writeData)  # 需要发送的十六进制数据
            writeData_ = bytes(send_msg)  # 需要发送的十六进制数据
            ret = self.m_dUartCom.write(writeData_)  # 用write函数向串口发送数据
            # ret = self.m_dUartCom.write(byref(send_msg))
        else:
            # logging.error("Uart not opened")
            reply3 = QMessageBox.critical(self, "异常", "Uart not opened")
