import logging
import os

import qdarkstyle

log = logging.getLogger(__name__)

from PyQt5.QtGui import QGuiApplication
import sys


from .settings import setup as settings_setup
from bcbtools.ui2.setup import setup as ui_setup

from PyQt5.QtWidgets import QApplication
import utils

def start_rpc():
    os.system('btcb_node --daemon &')
    #return p


def main():
    # app = QApplication(sys.argv+['--style', 'material'])
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    settings = settings_setup()

    w = ui_setup()

    #node_p = start_rpc()
    start_rpc()

    res = app.exec_()
    return res

if __name__ == '__main__':
    main()
