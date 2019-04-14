from PyQt5.QtWidgets import QTabWidget

from bcbtools.ui2.tools.Genesis import Genisis
from bcbtools.ui2.tools.Representative import Representative
from bcbtools.ui2.tools.Send import Send
from bcbtools.ui2.tools.SendMutli import SendMutli


def load(widget):
    # widget = QTabWidget()

    w1 = Genisis(widget)
    w1.setWindowTitle("Genesis")
    widget.addTab(w1, "Genesis")

    w2 = Send(widget)
    w2.setWindowTitle("Send")
    widget.addTab(w2, "Send")

    w3 = SendMutli(widget)
    w3.setWindowTitle("Send To Multiple Accounts")
    widget.addTab(w3, "Send To Multiple Accounts")

    w4 = Representative(widget)
    w4.setWindowTitle("Representative")
    widget.addTab(w4, "Representative")

    w4 = Representative(widget)
    w4.setWindowTitle("Representative")
    widget.addTab(w4, "Open")



