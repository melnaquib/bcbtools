# -*- coding: utf-8 -*-

"""
Module implementing SendMutli.
"""
import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from bcbtools.bcb import bcb
from bcbtools.ui2.utils import parse_amount_units
from .Ui_SendMutli import Ui_Form


class SendMutli(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SendMutli, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_resetBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tableWidget.setRowCount(0)


    @pyqtSlot()
    def on_delBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        indeces = self.tableWidget.selectedIndexes()
        if len(indeces):
            self.tableWidget.removeRow(indeces[0].row())


    @pyqtSlot()
    def on_addBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        self.tableWidget.insertRow(0)

    def gen(self, account):

        def l2s(l):
            r = str(l).replace("l", "").replace("L", "")
            return r

        balance = account['balance']
        balance = int(balance[0])

        res = []
        prev = {}
        prev['hash'] = account['frontier']

        for i in range(self.tableWidget.rowCount()):
            addr = self.tableWidget.item(i, 0).text().strip()
            amount = self.tableWidget.item(i, 1).text().strip()
            amount = parse_amount_units(amount)
            r = bcb.send(account['prvk'], account['addr'], l2s(balance),
                           amount, addr, prev['hash'])
            balance -= int(amount)
            res.append(r)
            prev = r
        res = json.dumps(res, indent=2)
        return res
