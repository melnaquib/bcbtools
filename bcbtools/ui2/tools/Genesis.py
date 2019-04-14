# -*- coding: utf-8 -*-

"""
Module implementing Genisis.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from bcbtools.bcb import bcb
from .Ui_Genesis import Ui_Form


class Genisis(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Genisis, self).__init__(parent)
        self.setupUi(self)

    def gen(self, account):
        return bcb.genesis(account['prvk'])