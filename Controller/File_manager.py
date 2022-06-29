import sys
from Controller.Utils import clear_data
from Model.Employee_model import Employee_model

class File_manager:    

    def __init__(self,file_name):

        self.file_name = file_name
        

    def get_employees(self):

        try:
            file = open(self.file_name,'r')        
        except:
            sys.exit(f'Impossible to open: {self.file_name}')
            
        lines = file.readlines()
        employees = []

        for i in range(len(lines)):
            lines[i] = clear_data(lines[i])

        for line in lines:
            data = line.split('=')
            name = data[0]
            schedule = data[1]
            employee = Employee_model(name,schedule)
            employees.append(employee)
        
        file.close()

        return employees
    

