# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import json

from PyQt5.QtCore import pyqtSlot, QRegularExpression, Qt
from PyQt5.QtGui import QRegularExpressionValidator, QClipboard, QColor
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication

from bcbtools import loader
from bcbtools.bcb import bcb
from bcbtools.ui2.validators import make_seed_v
from .Ui_mainwindow import Ui_MainWindow

from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerJSON


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.resultText = QsciScintilla(self)
        # self.resultText.SendScintilla(QsciScintilla.SCI_STYLESETBACK, QsciScintilla.STYLE_DEFAULT, QColor("gray"));

        self.resultWidget.layout().addWidget(self.resultText)
        lexer = QsciLexerJSON()
        self.resultText.setLexer(lexer)

        self.account_invalid = dict.fromkeys(['seed', 'prvk', 'pubk', 'addr', 'frontier', 'balance'], '')
        self.account = self.account_invalid

        self.seed_validator = make_seed_v(self)
        self.seedEdit.setValidator(self.seed_validator)

        self.showSeed()

        loader.load(self.toolsTabs)

    
    @pyqtSlot()
    def on_genBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        currentTool = self.toolsTabs.currentWidget()

        self.account['frontier'] = self.prevBlockText.text()
        self.account['balance'] = list(map(int, self.balanceText.text().split(', ')))

        res = currentTool.gen(self.account)
        self.resultTool.setText(currentTool.windowTitle())
        self.resultText.setText(res)
        clipboard = QApplication.clipboard()
        clipboard.setText(res)


    @pyqtSlot(str)
    def on_seedEdit_textChanged(self, seed):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """

        valid_seed = 64 == len(seed)
        if valid_seed:
            self.account['seed'] = seed
            self.account['prvk'], self.account['pubk'], self.account['addr'] = bcb.expand_seed(seed)
            self.account['frontier'], self.account['balance'] = bcb.frontier(self.account['addr']), bcb.balance(self.account['addr'])
        else:
            self.account = self.account_invalid

        self.prvkText.setText(self.account['prvk'])
        self.pubkLabel.setText(self.account['pubk'])
        self.addrLabel.setText(self.account['addr'])
        self.balanceText.setText(', '.join(self.account['balance']))
        self.prevBlockText.setText(self.account['frontier'])


    @pyqtSlot()
    def on_prvkBtn_pressed(self):
        """
        Slot documentation goes here.
        """
        showPasswdChecked = self.prvkBtn.isDown()
        self.setProperty("showPasswdChecked", showPasswdChecked)
        self.showSeed()

    @pyqtSlot()
    def on_prvkBtn_released(self):
        """
        Slot documentation goes here.
        """
        showPasswdChecked = self.prvkBtn.isDown()
        self.setProperty("showPasswdChecked", showPasswdChecked)
        self.showSeed()


    def showSeed(self):
        showPasswdChecked = self.property("showPasswdChecked")
        if showPasswdChecked:
            self.seedEdit.setEchoMode(QLineEdit.Normal)
            self.prvkText.setEchoMode(QLineEdit.Normal)
        else:
            self.seedEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
            self.prvkText.setEchoMode(QLineEdit.PasswordEchoOnEdit)
            self.prvkBtn.setText(self.tr("Show Seed and Private Key"))


