# -*- coding: utf- 8 -*-
"""Train_c3d_ucf101 & predict_c3d_ucf101"""
import numpy as np
import pyqtgraph as pg
import subprocess
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class EmittingStream(QtCore.QObject):

	textWritten = QtCore.pyqtSignal(str)

	def write(self, text):
		self.textWritten.emit(str(text))

class TPWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(TPWindow, self).__init__()

		sys.stdout = EmittingStream(textWritten = self.normalOutputWritten)

		self.setWindowTitle("训练&预测")

		self.plot_btn = QtWidgets.QPushButton("PLOT")
		self.plot_btn.clicked.connect(self.run_plot)

		self.console_print = QtWidgets.QTextEdit()

		self.plotWidget = pg.PlotWidget(title = "accuracy")

		self.train_color_label = QtWidgets.QLabel("train")
		self.train_color_label.setFixedSize(40, 27)
		pe = QPalette()
		pe.setColor(QPalette.WindowText, Qt.red)
		self.train_color_label.setPalette(pe)
		self.predict_color_label = QtWidgets.QLabel("validation")
		self.predict_color_label.setFixedSize(60, 27)
		pe.setColor(QPalette.WindowText, Qt.green)
		self.predict_color_label.setPalette(pe)

		main_ground = QtWidgets.QWidget()
		self.setCentralWidget(main_ground)

		grid = QtWidgets.QGridLayout()

		grid.addWidget(self.plot_btn, 1, 4)
		grid.addWidget(self.console_print, 1, 0, 11, 3)
		grid.addWidget(self.train_color_label, 1, 7)
		grid.addWidget(self.predict_color_label, 1, 8)
		grid.addWidget(self.plotWidget, 2, 4, 10, 5)

		main_ground.setLayout(grid)

		#重定向输出
		sys.stdout = EmittingStream(textWritten = self.normalOutputWritten)
		sys.stderr = EmittingStream(textWritten = self.normalOutputWritten)

	def run_plot(self):
		self.console_print.setText("")
		
		train_x_list = []
		train_y_list = []
		print("Training:")
		train_out = open("train_out.txt", "r")
		for line in train_out:
			mylist = line.rstrip().split(", ")
			print("step: " + mylist[0] + ", accuracy: " + mylist[1])
			train_x_list.append(int(mylist[0]))
			train_y_list.append(float(mylist[1]))
		self.plotWidget.plot(train_x_list, train_y_list, pen = (0, 3))

		val_x_list = []
		val_y_list = []
		print("\nValidation:")
		val_out = open("val_out.txt", "r")
		for line in val_out:
			mylist = line.rstrip().split(', ')
			print("step: " + mylist[0] + ", accuracy: " + mylist[1])
			val_x_list.append(int(mylist[0]))
			val_y_list.append(float(mylist[1]))
		self.plotWidget.plot(val_x_list, val_y_list, pen = (1, 3))

	def __del__(self):
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__

	def normalOutputWritten(self, text):
		cursor = self.console_print.textCursor()
		cursor.movePosition(QtGui.QTextCursor.End)
		cursor.insertText(text)
		self.console_print.setTextCursor(cursor)
		self.console_print.ensureCursorVisible()