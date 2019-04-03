# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, QRegularExpression, Qt
from PyQt5.QtGui import QRegularExpressionValidator, QClipboard, QColor
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication

from bcbtools import loader
from bcbtools.bcb import bcb
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

        self.seed, self.prvk, self.pubk, self.addr = '', '', '', ''

        self.seed_validator = QRegularExpressionValidator(QRegularExpression('[0-9A-Fa-f]{32}'), self)
        self.seedEdit.setValidator(self.seed_validator)

        self.showSeed()

        loader.load(self.toolsTabs)

    
    @pyqtSlot()
    def on_genBtn_clicked(self):
        """
        Slot documentation goes here.
        """
        currentTool = self.toolsTabs.currentWidget()
        res = currentTool.gen(self.seed, self.prvk, self.pubk, self.addr)
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

        self.seed, (self.prvk, self.pubk, self.addr) = (seed, bcb.expand_seed(seed)) if 32 == len(seed) else ('', ('', '', ''))


        self.pubkLabel.setText(self.pubk)
        self.addrLabel.setText(self.addr)


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
            self.prvkBtn.setText(self.prvk)
        else:
            self.seedEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
            self.prvkBtn.setText(self.tr("Show Seed and Private Key"))

