# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/melnaquib/work/client/freelancer.com/bb/code/bcbtools/bcbtools/ui2/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 414)
        MainWindow.setProperty("showPasswdChecked", False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.prevBlockText = QtWidgets.QLineEdit(self.widget)
        self.prevBlockText.setObjectName("prevBlockText")
        self.gridLayout_2.addWidget(self.prevBlockText, 4, 1, 1, 1)
        self.pubkLabel = QtWidgets.QLabel(self.widget)
        self.pubkLabel.setText("")
        self.pubkLabel.setObjectName("pubkLabel")
        self.gridLayout_2.addWidget(self.pubkLabel, 2, 0, 1, 1)
        self.resultTool = QtWidgets.QLabel(self.widget)
        self.resultTool.setText("")
        self.resultTool.setObjectName("resultTool")
        self.gridLayout_2.addWidget(self.resultTool, 6, 0, 1, 1)
        self.balanceText = QtWidgets.QLineEdit(self.widget)
        self.balanceText.setObjectName("balanceText")
        self.gridLayout_2.addWidget(self.balanceText, 4, 0, 1, 1)
        self.prvkBtn = QtWidgets.QPushButton(self.widget)
        self.prvkBtn.setText("")
        self.prvkBtn.setObjectName("prvkBtn")
        self.gridLayout_2.addWidget(self.prvkBtn, 1, 0, 1, 2)
        self.genBtn = QtWidgets.QPushButton(self.widget)
        self.genBtn.setObjectName("genBtn")
        self.gridLayout_2.addWidget(self.genBtn, 5, 0, 1, 2)
        self.resultWidget = QtWidgets.QWidget(self.widget)
        self.resultWidget.setObjectName("resultWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.resultWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2.addWidget(self.resultWidget, 7, 0, 1, 2)
        self.addrLabel = QtWidgets.QLabel(self.widget)
        self.addrLabel.setText("")
        self.addrLabel.setObjectName("addrLabel")
        self.gridLayout_2.addWidget(self.addrLabel, 2, 1, 1, 1)
        self.seedEdit = QtWidgets.QLineEdit(self.widget)
        self.seedEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.seedEdit.setObjectName("seedEdit")
        self.gridLayout_2.addWidget(self.seedEdit, 0, 0, 1, 1)
        self.prvkText = QtWidgets.QLineEdit(self.widget)
        self.prvkText.setObjectName("prvkText")
        self.gridLayout_2.addWidget(self.prvkText, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        self.toolsTabs = QtWidgets.QTabWidget(self.centralWidget)
        self.toolsTabs.setObjectName("toolsTabs")
        self.gridLayout.addWidget(self.toolsTabs, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 524, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.seedEdit, self.prvkText)
        MainWindow.setTabOrder(self.prvkText, self.prvkBtn)
        MainWindow.setTabOrder(self.prvkBtn, self.balanceText)
        MainWindow.setTabOrder(self.balanceText, self.prevBlockText)
        MainWindow.setTabOrder(self.prevBlockText, self.genBtn)
        MainWindow.setTabOrder(self.genBtn, self.toolsTabs)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.genBtn.setText(_translate("MainWindow", "Generate"))
        self.seedEdit.setPlaceholderText(_translate("MainWindow", "Seed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

