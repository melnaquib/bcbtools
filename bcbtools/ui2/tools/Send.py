# -*- coding: utf-8 -*-

"""
Module implementing Send.
"""
import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget

from bcbtools.bcb import bcb
from bcbtools.ui2 import validators
from bcbtools.ui2.validators import make_addr_v
from .Ui_Send import Ui_Form


class Send(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Send, self).__init__(parent)
        self.setupUi(self)

        self.amount_v = validators.make_amount_v(self)
        self.amountText.setValidator(self.amount_v)

        self.addr_v = make_addr_v(self)
        self.dstText.setValidator(self.addr_v)


    def gen(self, account):
        res = bcb.send(account['prvk'], account['addr'], account['balance'][0],
                           self.amountText.text(), self.dstText.text(), account['frontier'])
        res = json.dumps(res, indent=2)
        return res
