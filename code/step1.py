# -*- coding: utf- 8 -*-
"""Convert video to list"""
import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class Video2ListWindow(QtWidgets.QMainWindow):

	saveDir = ""

	def __init__(self):
		super(Video2ListWindow, self).__init__()

		self.setWindowTitle("视频转列表")

		self.dir_btn = QtWidgets.QPushButton("SET UCF101 DIR ", self)
		self.dir_btn.clicked.connect(self.get_dir)

		self.dir_label = QtWidgets.QLabel("./UCF101", self)

		self.fps_edit = QtWidgets.QTextEdit("5")
		self.fps_edit.setFixedSize(27, 27)

		self.run_v2i_btn = QtWidgets.QPushButton("CONVERT VIDEO TO IMAGES!")
		self.run_v2i_btn.clicked.connect(self.run_v2i)

		self.factor_edit = QtWidgets.QTextEdit("4")
		self.factor_edit.setFixedSize(27, 27)

		self.run_i2l_btn = QtWidgets.QPushButton("CONVERT IMAGES TO LIST!")
		self.run_i2l_btn.clicked.connect(self.run_i2l)

		main_ground = QtWidgets.QWidget()
		self.setCentralWidget(main_ground)

		grid = QtWidgets.QGridLayout()
		grid.addWidget(self.dir_btn, 1, 0, 1, 3)
		grid.addWidget(self.dir_label, 2, 0, 1, 3)
		grid.addWidget(QtWidgets.QLabel("FPS:"), 3, 0)
		grid.addWidget(self.fps_edit, 4, 0)
		grid.addWidget(self.run_v2i_btn, 4, 1, 1, 2)
		grid.addWidget(QtWidgets.QLabel("---------------------------------------------------------------"), 5, 0, 1, 3)
		grid.addWidget(QtWidgets.QLabel("Factor:"), 6, 0)
		grid.addWidget(self.factor_edit, 7, 0)
		grid.addWidget(self.run_i2l_btn, 7, 1, 1, 2)

		main_ground.setLayout(grid)

	def get_dir(self):
		tmpDir = QtWidgets.QFileDialog.getExistingDirectory()
		if(len(tmpDir) > 0):
			self.saveDir = tmpDir
			self.dir_label.setText(self.saveDir)
		if not os.path.exists(self.saveDir):
			os.mkdir(self.saveDir)

	def run_v2i(self):
		os.popen("./list/convert_video_to_images.sh " + self.saveDir + " "+ self.fps_edit.toPlainText())

	def run_i2l(self):
		os.popen("./list/convert_images_to_list.sh " + self.saveDir + " " + self.factor_edit.toPlainText())