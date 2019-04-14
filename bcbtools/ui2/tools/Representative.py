# -*- coding: utf-8 -*-

"""
Module implementing Representative.
"""
import json

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from bcbtools.bcb import bcb
from .Ui_Representative import Ui_Form


class Representative(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Representative, self).__init__(parent)
        self.setupUi(self)

    def gen(self, account):
        res = bcb.repr_set(account['prvk'], account['addr'], self.reprText.text(), account['frontier'])
        res = json.dumps(res, indent=2)
        return res
