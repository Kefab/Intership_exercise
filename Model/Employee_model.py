from Model.Day_model import Day_model


class Employee_model:

    def __init__(self,name,schedule):
                
        schedule = schedule.split(',')

        self.name = name
        self.days = []
        
        for s in schedule:
            day = Day_model(s)            
            self.days.append(day)