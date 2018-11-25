import sys
from PyQt5.QtGui import QGuiApplication, QWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QObject
from TextStuff.GoogleCloudVision import GoogleCloudVision
import base64
from util.models import AppointmentDTO
from CalendarStuff import Calendar
import datetime

from ViewStuff.binding_experiments.controller import MyPersonalViewController


# Start of the application itself


class TextInputController(QMainWindow):
    def __init__(self, user, parent=None):
        super(TextInputController, self).__init__(parent)
        self.user = user
        self.engine = QQmlApplicationEngine()
        ctx = self.engine.rootContext()
        ctx.setContextProperty('main', self.engine)
        self.engine.load(QUrl('ViewStuff/text_input/text-input.qml'))
        self.win = self.engine.rootObjects()[0]
        btn = self.win.findChild(QObject, 'finishButton')
        btn.clicked.connect(self.finished)  # works too
        self.vision = GoogleCloudVision()

    def finished(self):
        cal = Calendar()
        canvas = self.win.findChild(QObject, 'textCanvas')
        image = canvas.toDataURL().replace('data:image/png;base64,', '')
        imagedata = base64.b64decode(image)
        hstr = self.vision.detectTextInBase64Image(imagedata)
        appointment = AppointmentDTO.create_from_hstr(hstr, datetime.datetime.now())
        cal.createAppointmentFromDTO(self.user, appointment)


def main():
    app = QGuiApplication(sys.argv)

    txtInput = TextInputController('michi')

    txtInput.engine.quit.connect(app.quit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
