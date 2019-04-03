import logging

log = logging.getLogger(__name__)
logger = logging.getLogger('bcbtools')

import sys, os
from PyQt5.QtCore import QSettings, QFile, QStandardPaths
from PyQt5.QtGui import QGuiApplication


def setupVendor():
    app = QGuiApplication.instance()
    log.info('load settings')
    vendor_filename = os.path.join(os.path.dirname(__file__), '../.vendor.ini')
    vendorSettings = QSettings(vendor_filename, QSettings.IniFormat)
    log.info("load org configs")
    vendorSettings.beginGroup('org')
    app.setOrganizationName(vendorSettings.value('name'))
    app.setOrganizationDomain(vendorSettings.value('domain'))
    vendorSettings.endGroup()
    log.info('load app configs')
    vendorSettings.beginGroup('app')
    app.setApplicationName(vendorSettings.value('name'))
    app.setApplicationVersion(vendorSettings.value('version'))
    vendorSettings.endGroup()


def setup_logging():
    logger = logging.getLogger('medleap')

    addin_path = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
    log_file = "medleap.log"
    log_path = os.path.join(addin_path, log_file)
    handler_path = os.getenv('LOG_PATH', log_path)
    if not handler_path:
        handler_path = addin_path
    if not os.path.exists(addin_path):
        print("CREATE", handler_path)

        os.makedirs(addin_path)

    handler = logging.FileHandler(handler_path)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(module)s.%(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info('Set up Logging Complete')
    return logger


def setup():
    setup_logging()

    setupVendor()
    settings_filename = os.path.join(os.path.dirname(__file__), '../settings/settings.ini')
    if len(sys.argv) > 1:
        settings_filename = sys.argv[1]
    elif not QFile.exists(settings_filename):
        settings_filename = None

    settings = QSettings(settings_filename, QSettings.IniFormat)
    log.info('load db configs')
    settings.beginGroup('db')
    drive = settings.value('drive')
    user = settings.value('user')
    password = settings.value('password')
    hostname = settings.value('hostname')
    name = settings.value('name')
    port = settings.value('port', type=int)
    settings.endGroup()

    return settings
