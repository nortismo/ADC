from PyQt5.QtCore import QObject, QUrl
import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


class DefaultCalendarController(QObject):
    def __init__(self):
        QObject.__init__(self)

    def start_default_calendar(self):
        app = QGuiApplication(sys.argv)
        engine = QQmlApplicationEngine()
        engine.rootContext().setContextProperty("controller", self)
        engine.load(QUrl('default_calendar.qml'))
        engine.quit.connect(app.quit)
        sys.exit(app.exec_())


# This main is just for development. The main process should be started somewhere else, out of the GUI
if __name__ == "__main__":
    DefaultCalendarController().start_default_calendar()
