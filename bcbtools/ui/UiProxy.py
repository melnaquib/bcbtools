from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtSql import QSqlDatabase


class UiProxy(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)


    @pyqtSlot(result=list)
    def db_driver(self):
        return QSqlDatabase.drivers()

