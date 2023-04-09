# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	hejiawen@corp.netease.com.
Description:
	MainWindow
Date:
	2023/04/09
----------------------------------------------------------------------------"""
from system_hotkey import SystemHotkey

from qtpy.QtGui import QIcon
from qtpy.QtCore import Signal
from qtpy.QtWidgets import QWidget

from UI.SystemTrayIcon import SystemTrayIcon


class MainWindow(QWidget):
	keyHot = Signal()

	def __init__(self, parent=None):
		super().__init__(parent)

		self._initUI()
		self._initListener()

	def _initUI(self):
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle("ChatGpt")
		self.setWindowIcon(QIcon(":Resources/icon.png"))
		self.trayIcon = SystemTrayIcon(self)
		self.trayIcon.show()

	def _initListener(self):
		self.keyHot.connect(self.onHotKey)
		self.systemHotKey = SystemHotkey()
		self.systemHotKey.register(('control', 'h'), callback=lambda _: self.keyHot.emit())

	def onHotKey(self):
		if self.isHidden():
			self.show()
		else:
			self.hide()
