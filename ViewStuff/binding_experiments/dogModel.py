import string
import sys
from PyQt5.QtCore import QAbstractListModel, QModelIndex, pyqtProperty, QByteArray


class Dog:
    def __init__(self, name: string = None, age: int = 0):
        self._name = name
        self._age = age

    def to_string(self):
        print('Name: ' + self.name)
        print('Age: ' + str(self.age))

    @pyqtProperty(str)  # This Annotation is IMPORTANT!
    def name(self):
        return self._name

    @pyqtProperty(int)  # This Annotation is IMPORTANT!
    def age(self):
        return self._age


class DogList(QAbstractListModel):
    def __init__(self, schema, parent=None):
        super(DogList, self).__init__(parent)

        # Each item is a dictionary of key/value pairs
        self.items = list()

        # QML requires a model to define upfront
        # exactly which roles it can supply. I refer
        # to this as the models "schema".
        self.schema = schema

    def append(self, item):
        """Append item to end of model"""
        self.beginInsertRows(QModelIndex(),
                             self.rowCount(),
                             self.rowCount())

        self.items.append(item)
        self.endInsertRows()

    def data(self, index, role):
        """Return value of item[`index`] of `role`"""
        key = self.schema[role]
        return self.items[index.row()].get(key)

    def setData(self, index, value, role):
        """Set item[`index`] of `role` to `value`"""
        key = self.schema[role]
        self.items[index.row()][key] = value
        self.dataChanged.emit(index, index)

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def roleNames(self):
        """Role names are used by QML to map key to role"""
        return dict(enumerate(self.schema))
