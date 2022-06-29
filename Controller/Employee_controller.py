class Employee_controller:            
    
    def compare(self,employee_a,employee_b):
        
        count = 0
        for day_a in employee_a.days:
            for day_b in employee_b.days:
                if(day_b.name == day_a.name and not(day_b.end < day_a.start or day_a.end < day_b.start)):
                    count += 1
        return count
    