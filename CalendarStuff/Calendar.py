from util.models import CalendarDTO


class Calendar:
    def __init__(self):
        self.calendarDTO = CalendarDTO

    def get_calendarEntries(self, date):
        pass

    def get_calendarEntries(self):
        self.calendarDTO.uid = 'eiszwoidrüvier'
        self.calendarDTO.calendarName = 'fancy first calendar'

        return self.calendarDTO

