import sys
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from ViewStuff.binding_experiments.controller import MyPersonalViewController
from ViewStuff.binding_experiments.dogModel import Dog, DogList


# Start of the application itself


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    controller = MyPersonalViewController()

    #schema = [
    #    "index",
    #    "dog",
    #]
#
    #listOfDogs = DogList(schema)
    #items = [
    #    {
    #        "index": 1,
    #        "dog": Dog("Michael", 25),
    #    },
    #    {
    #        "index": 2,
    #        "dog": Dog("Philipp", 18),
    #    }
    #]

    #for item in items:
    #    listOfDogs.append(item)

    # engine.rootContext().setContextProperty("pyModel", listOfDogs)
    engine.rootContext().setContextProperty("controller", controller)
    engine.load(QUrl('view.qml'))
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
