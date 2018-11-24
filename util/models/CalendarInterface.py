from abc import ABC, abstractmethod


class CalenderInterface(ABC):

    @abstractmethod
    def get_calendarEntries(self, date):
        pass

    @abstractmethod
    def get_calendarEntries(self):
        print('return calendar entries')
