# -*- coding: utf-8 -*-
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QTableWidget, QApplication, QTableWidgetItem, QLabel
import sys
import csv

class PredictTable(QTableWidget):
	def __init__(self, parent = None):
		super(PredictTable, self).__init__(parent)
		self.resize(520, 420)
		self.setColumnCount(6)
		myfile = open("predict_ret.txt", "r")
		mylistfile = open("test.list", "r")
		count = len(myfile.readlines())
		self.setRowCount(count)
		self.setHorizontalHeaderLabels(['true label', '1st frame of true class', 'class prob for true label', 'predicted label', '1st frame of predicted class', 'class prob for predicted label'])
		myfile.seek(0)
		i = 0
		for line in myfile:
			mylist = line.split(', ')
			self.setColumnWidth(i, 80)#320
			self.setRowHeight(i, 60)#240
			self.setItem(i, 2, QTableWidgetItem(mylist[1]))
			self.setItem(i, 5, QTableWidgetItem(mylist[3]))
			mylistfile.seek(0)
			flag0 = 0
			flag2 = 0
			for myline in mylistfile:
				if flag0 == 0 and (" " + mylist[0]) in myline:
					self.setItem(i, 0, QTableWidgetItem(myline.split('/')[-2]))
					lbp = QLabel()
					pixmap = QPixmap(myline.split(' ')[0] + "/00001.jpg")
					scaledPixmap = pixmap.scaled(80, 60)
					lbp.setPixmap(scaledPixmap)
					self.setCellWidget(i, 1, lbp)
					flag0 = 1
				if flag2 == 0 and (" " + mylist[2]) in myline:
					self.setItem(i, 3, QTableWidgetItem(myline.split('/')[-2]))
					lbp = QLabel()
					pixmap = QPixmap(myline.split(' ')[0] + "/00001.jpg")
					scaledPixmap = pixmap.scaled(80, 60)
					lbp.setPixmap(scaledPixmap)
					self.setCellWidget(i, 4, lbp)
					flag2 = 1
				if flag0 == 1 and flag2 == 1:
					break
			i += 1
		myfile.close()
		mylistfile.close()