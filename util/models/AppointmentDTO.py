import random
import string
from datetime import datetime
import re
import copy


class AppointmentDTO:
    time_regex = re.compile('([0-9]{1,2}):([0-9]{2})')

    def __init__(self, uid: string = None, start: datetime = None, end: datetime = None, description: string = None):
        now = str(datetime.now())
        if uid:
            self.uid = uid
        else:
            self.uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        self.start = start
        self.end = end
        self.description = description

        if start == None or end == None:
            self.start = now
            self.end = now

        if self.description == None:
            self.description = 'no description yet'

    @classmethod
    def create_from_hstr(cls, text: str, today: datetime):
        text = text.replace('\n', '')
        text = text.replace(':oo', ':00')
        text = text.replace(':o0', ':00')
        text = text.replace(':0o', ':00')
        result = cls.time_regex.findall(text)

        start = copy.copy(today)
        end = copy.copy(today)

        if len(result) == 1:
            start_time = result[0]
            start = start.replace(hour=int(start_time[0]), minute=int(start_time[1]), second=0, microsecond=0)
            end = end.replace(hour=int(start_time[0]) + 1, minute=int(start_time[1]), second=0, microsecond=0)
        elif len(result) == 2:
            start_time = result[0]
            end_time = result[1]
            start = start.replace(hour=int(start_time[0]), minute=int(start_time[1]), second=0, microsecond=0)
            end = end.replace(hour=int(end_time[0]), minute=int(end_time[1]), second=0, microsecond=0)
        else:
            return None

        subject = cls.time_regex.sub('', text.replace('-', '')).strip()

        appointment = AppointmentDTO(start=start, end=end,
                                     description=subject)
        return appointment

    def toString(self):
        print('---- printing AppointmentDTO ----')
        print('uid: ' + self.uid)
        print('start: ' + str(self.start))
        print('end: ' + str(self.end))
        print('description: ' + self.description)
        print('-------------------------------')


def main():
    from CalendarStuff import Calendar
    cal = Calendar()
    test = AppointmentDTO.create_from_hstr('Kaffee 11:00', datetime.now())
    cal.createAppointmentFromDTO('michi', test)
    calendar = cal.get_calendarEntries('michi')
    for appointment in calendar.appointments:
        print(appointment.toString())
    print(test.toString())


if __name__ == '__main__':
    main()