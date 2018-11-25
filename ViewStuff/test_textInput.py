import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QObject
from TextStuff.GoogleCloudVision import GoogleCloudVision
import base64

from ViewStuff.binding_experiments.controller import MyPersonalViewController


# Start of the application itself


class TextInput:
    def __init__(self):
        self.engine = QQmlApplicationEngine()
        ctx = self.engine.rootContext()
        ctx.setContextProperty('main', self.engine)
        self.engine.load(QUrl('text-input.qml'))
        self.win = self.engine.rootObjects()[0]
        btn = self.win.findChild(QObject, 'finishButton')
        btn.clicked.connect(self.finished)  # works too
        self.vision = GoogleCloudVision()

    def finished(self):
        canvas = self.win.findChild(QObject, 'textCanvas')
        image = canvas.toDataURL().replace('data:image/png;base64,', '')
        imagedata = base64.b64decode(image)
        print(self.vision.detectTextInBase64Image(imagedata))


def main():
    app = QGuiApplication(sys.argv)

    txtInput = TextInput()

    txtInput.engine.quit.connect(app.quit)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
