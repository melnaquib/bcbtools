from PyQt5.QtWidgets import QTabWidget

from bcbtools.ui2.tools.Genesis import Genisis


def load(widget):
    # widget = QTabWidget()

    w1 = Genisis(widget)
    w1.setWindowTitle("Genesis")
    widget.addTab(w1, "Genesis")
