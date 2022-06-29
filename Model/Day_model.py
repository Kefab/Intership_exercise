import datetime
import sys

class Day_model:
    
    def __init__(self,schedule):

        schedule = schedule.split('-')
        start = schedule[0][2:].split(':')
        end = schedule[1].split(':')
        
        self.name = schedule[0][:2]     
        try:

            self.start = datetime.time(int(start[0]), int(start[1]))
            self.end = datetime.time(int(end[0]), int(end[1]))  
        except:
            sys.exit('Imposible start time')