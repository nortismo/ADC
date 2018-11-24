import random
import string
from datetime import datetime

class AppointmentDTO:

    def __init__(self, start = None, end = None, description = None):
        now = str(datetime.now())
        self.uid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        self.start = start
        self.end = end
        self.description = description

        if start == None or end == None:
            self.start = now
            self.end = now

        if self.description == None:
            self.description = 'no description yet'

    def toString(self):
        print('---- printing AppointmentDTO ----')
        print('uid: ' + self.uid)
        print('start: ' + str(self.start))
        print('end: ' + str(self.end))
        print('description: ' + self.description)
        print('-------------------------------')
