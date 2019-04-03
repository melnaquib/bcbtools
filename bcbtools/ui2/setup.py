import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl


from bcbtools.ui2.mainwindow import MainWindow
from .UiProxy import UiProxy


def setup():

    w = MainWindow()
    w.showMaximized()
    return w


if __name__ == '__main__':
    setup()

