# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	hejiawen@corp.netease.com.
Description:
	SystemTrayIcon
Date:
	2023/04/09
----------------------------------------------------------------------------"""
from qtpy.QtGui import QIcon, QAction
from qtpy.QtWidgets import QSystemTrayIcon, QMenu


class SystemTrayIcon(QSystemTrayIcon):

	def __init__(self, parent=None):
		super().__init__(parent)

		self.setToolTip("ChatGpt")
		self.setIcon(QIcon(":Resources/icon.png"))

		menu = QMenu(parent)
		showAction = QAction("显示", self)
		showAction.triggered.connect(self.showWindow)

		menu.addAction(showAction)

		self.setContextMenu(menu)

	def showWindow(self):
		self.parent().show()
