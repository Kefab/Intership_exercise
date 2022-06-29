import sys
from Controller.Employee_controller import Employee_controller
from Controller.File_manager import File_manager
from View.print_data import print_data

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        file_manager = File_manager(sys.argv[1])                    
    else:
        file_name = input('Enter the file name: ')
        file_manager = File_manager(file_name)   
    
    employees = file_manager.get_employees()

    employee_controller = Employee_controller()

    for i in range(len(employees)):
        for j in range(i+1,len(employees)):
            matches = employee_controller.compare(employees[i],employees[j])
            print_data(employees[i],employees[j],matches)

