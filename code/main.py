# -*- coding: utf-8 -*-
"""Main func"""

import sys, step1, step3, step5
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()

		self.setWindowTitle("视频行为识别程序")

		self.v2l_btn = QtWidgets.QPushButton("CONVERT VIDEO TO LIST", self)
		self.v2l_btn.clicked.connect(self.show_v2l_window)

		self.tp_btn = QtWidgets.QPushButton("PLOT REAL-TIME ACCURACY", self)
		self.tp_btn.clicked.connect(self.show_tp_window)

		self.result_btn = QtWidgets.QPushButton("SEE RESULT", self)
		self.result_btn.clicked.connect(self.show_result_window)

		main_ground = QtWidgets.QWidget()
		self.setCentralWidget(main_ground)

		grid = QtWidgets.QGridLayout()
		grid.addWidget(QtWidgets.QLabel("*PREREQUISTIES*\n1. You must have installed the following two python libs:\n    [tensorflow] (Version must be 0.11.0 or greater)\n    [Pillow]\n2. You must have downloaded the [UCF101] (Action Recognition Data Set)"), 1, 0)
		grid.addWidget(QtWidgets.QLabel("*FUNCTIONS*\nFunc 1 & Func 2:"), 2, 0)
		grid.addWidget(self.v2l_btn, 3, 0, 1, 1)
		grid.addWidget(QtWidgets.QLabel("Func 3:"), 4, 0)
		grid.addWidget(self.tp_btn, 5, 0, 1, 1)
		grid.addWidget(QtWidgets.QLabel("Func 4:"), 6, 0)
		grid.addWidget(self.result_btn, 7, 0, 1, 1)

		main_ground.setLayout(grid)

	def show_v2l_window(self):
		self.video2list_window = step1.Video2ListWindow()
		self.video2list_window.show()

	def show_tp_window(self):
		self.tp_window = step3.TPWindow()
		self.tp_window.show()

	def show_result_window(self):
		self.predictTable = step5.PredictTable()
		self.predictTable.show()

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
