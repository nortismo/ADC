import string
from datetime import datetime

from PyQt5.QtCore import pyqtProperty


class DefaultCalendarEntryModel:

    def __init__(self, start_position: datetime = None, end_position: datetime = None, uid: string = None,
                 start: datetime = None, end: datetime = None, description: string = None):
        self.start_position = start_position
        self.end_position = end_position
        self.uid = None
        self.start = None
        self.end = None
        self.description = None
        self._fullText = None
        self.reset_data()
        self.set_data(uid, start, end, description)


    def set_data(self, uid: string = None, start: datetime = None, end: datetime = None, description: string = None):
        self.uid = uid
        self.start = start
        self.end = end
        self.description = description

        time_appendix = ""


        if uid is not None:
            if start >= self.start_position and start <= self.end_position:
                time_appendix = "(" + str(start.hour) + ":" + str(start.minute) + " - " + str(end.hour) + ":" + str(end.minute) + ")"  # TODO: Maybe we are able to simplify that

        if self.description is None:
            self.description = '-'

        self._fullText = time_appendix + self.description
        return self._fullText

    def reset_data(self):
        self.uid = None
        self.start = None
        self.end = None
        self.description = None
        self._fullText = None

    @pyqtProperty(str)  # This Annotation is IMPORTANT!
    def full_text(self):
        return self._fullText

    def to_string(self):
        print('---- printing DefaultCalendarEntryModel ----')
        print('uid: ' + self.uid)
        print('start: ' + str(self.start))
        print('end: ' + str(self.end))
        print('description: ' + self.description)
        print('Full Text is: ' + self.full_text)
        print('-------------------------------')
