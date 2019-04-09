# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/melnaquib/work/client/freelancer.com/bb/code/bcbtools/bcbtools/ui2/tools/Send.ui'
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
        self.amountText = QtWidgets.QLineEdit(Form)
        self.amountText.setObjectName("amountText")
        self.gridLayout.addWidget(self.amountText, 1, 0, 1, 1)
        self.dstText = QtWidgets.QLineEdit(Form)
        self.dstText.setObjectName("dstText")
        self.gridLayout.addWidget(self.dstText, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.amountText.setPlaceholderText(_translate("Form", "Amount"))
        self.dstText.setPlaceholderText(_translate("Form", "Receiver Address"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

