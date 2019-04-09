from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator


def make_seed_v(parent):
    v = QRegularExpressionValidator(QRegularExpression('[0-9A-Fa-f]{64}'), parent)
    return v

def make_addr_v(parent):
    v = QRegularExpressionValidator(QRegularExpression('bcb_[0-9A-Za-z]{60}'), parent)
    return v

def make_amount_v(parent):
    v = QRegularExpressionValidator(QRegularExpression('[0-9]{39}'), parent)
    return v


