from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot


class MyPersonalViewController(QObject):
    def __init__(self):
        QObject.__init__(self)

    # signal sending string
    # necessarily give the name of the argument through arguments=['textLabel']
    # otherwise it will not be possible to pick it up in QML
    textResult = pyqtSignal(str, arguments=['textLabel'])

    @pyqtSlot(str)
    def textLabel(self, arg1):
        # do something with the text and emit a signal
        arg1 = arg1.upper()
        self.textResult.emit(arg1)