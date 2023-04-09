# -*- coding: utf-8 -*-
"""----------------------------------------------------------------------------
Author:
	hejiawen@corp.netease.com.
Description:
	main
Date:
	2023/04/09
----------------------------------------------------------------------------"""
import sys
import os
parentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentPath)

from qtpy.QtWidgets import QApplication

from UI.MainWindow import MainWindow
from UI.SystemTrayIcon import SystemTrayIcon

import images  # type: ignore

if __name__ == "__main__":
	QApplication.setQuitOnLastWindowClosed(False)

	app = QApplication()
	mainWindow = MainWindow()
	mainWindow.show()

	sys.exit(app.exec_())
