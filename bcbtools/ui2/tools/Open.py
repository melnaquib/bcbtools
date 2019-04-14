# -*- coding: utf-8 -*-

"""
Module implementing Open.
"""
import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from bcbtools.bcb import bcb
from .Ui_Open import Ui_Form


class Open(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Open, self).__init__(parent)
        self.setupUi(self)

    def gen(self, account):
        res = bcb.open(account['prvk'], account['addr'], self.reprText.text(), self.sendHashText.text())
        res = json.dumps(res, indent=2)
        return res
