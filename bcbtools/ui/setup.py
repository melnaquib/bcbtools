import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl

from .UiProxy import UiProxy

from . import qml

def setup():
    engine = QQmlApplicationEngine()
    context = engine.rootContext()

    uip = UiProxy(engine)
    context.setContextProperty("uip", uip)

    # qml_root = 'qrc:/'
    qml_root = './bcbtools/ui/'
    qml_file = 'main.qml'
    qml_file = qml_root + qml_file
    engine.load(QUrl(qml_file))

    # engine.quit.connect(QGuiApplication.instance().quit)

    return engine

if __name__ == '__main__':
    setup()

