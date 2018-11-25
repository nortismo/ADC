import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl, QByteArray
from ViewStuff.binding_experiments.controller import MyPersonalViewController
from ViewStuff.binding_experiments.dogModel import Dog, DogList


# Start of the application itself


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    controller = MyPersonalViewController()

    schema = [
        QByteArray(str.encode("index")),
        QByteArray(str.encode("dog")),
        QByteArray(str.encode("thirdValue")),
    ]
    michael = Dog("Michael", 23)
    philipp = Dog("Philipp", 18)

    listOfDogs = DogList(schema)
    items = [
        {
            QByteArray(str.encode("index")): "test1",
            QByteArray(str.encode("dog")): michael.name,
            QByteArray(str.encode("thirdValue")): michael.age
        },
        {
            QByteArray(str.encode("index")): "test2",
            QByteArray(str.encode("dog")): philipp.name,
            QByteArray(str.encode("thirdValue")): philipp.age,
        }
    ]
    for item in items:
        listOfDogs.append(item)

    engine.rootContext().setContextProperty("pyModel", listOfDogs)
    engine.rootContext().setContextProperty("controller", controller)
    engine.load(QUrl('view.qml'))
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
