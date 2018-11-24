from util.models import CalendarDTO


class Calendar:
    def __init__(self):
        self.calendarDTO = CalendarDTO('calendarNameFromConstructor', None)

    def get_calendarEntries(self, date):
        pass

    def get_calendarEntries(self):
        return self.calendarDTO

