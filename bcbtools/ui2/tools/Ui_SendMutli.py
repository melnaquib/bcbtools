# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/melnaquib/work/client/freelancer.com/bb/code/bcbtools/bcbtools/ui2/tools/SendMutli.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 174, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.resetBtn = QtWidgets.QPushButton(Form)
        self.resetBtn.setObjectName("resetBtn")
        self.gridLayout.addWidget(self.resetBtn, 3, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 4, 1)
        self.addBtn = QtWidgets.QPushButton(Form)
        self.addBtn.setObjectName("addBtn")
        self.gridLayout.addWidget(self.addBtn, 0, 1, 1, 1)
        self.delBtn = QtWidgets.QPushButton(Form)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.resetBtn.setText(_translate("Form", "Clear"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ADDRESS"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "AMOUNT"))
        self.addBtn.setText(_translate("Form", "Add"))
        self.delBtn.setText(_translate("Form", "Remove"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

