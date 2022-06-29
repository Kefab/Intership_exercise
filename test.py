import unittest
from Controller.Employee_controller import Employee_controller

from Controller.Utils import clear_data
from Model.Employee_model import Employee_model

class testing(unittest.TestCase):
    def test_clear_data(self):
        line = '1231\n\n1  21313 1231'
        cleaned_line = clear_data(line)
        expected_line = '12311213131231'

        self.assertEqual(cleaned_line,expected_line)

    def test_compare_employee1(self):
        employee1 = Employee_model('Kevin','MO10:00-12:00,TU10:00-12:00')
        employee2 = Employee_model('Vanessa','MO10:00-12:00,TU10:00-12:00')

        employe_controller = Employee_controller()
        matches = employe_controller.compare(employee1,employee2)
        expected_matches = 2

        self.assertEqual(matches,expected_matches)
    
    def test_compare_employee2(self):
        employee1 = Employee_model('Kevin','WE10:00-12:00,SA10:00-12:00')
        employee2 = Employee_model('Vanessa','MO10:00-12:00,TU10:00-12:00')

        employe_controller = Employee_controller()
        matches = employe_controller.compare(employee1,employee2)
        expected_matches = 0

        self.assertEqual(matches,expected_matches)

    def test_compare_employee3(self):
        employee1 = Employee_model('Kevin','MO10:00-12:00,TU10:00-12:00')
        employee2 = Employee_model('Vanessa','MO10:00-12:00,TU10:00-12:00,WE10:00-12:00,SA10:00-12:00')

        employe_controller = Employee_controller()
        matches = employe_controller.compare(employee1,employee2)
        expected_matches = 2

        self.assertEqual(matches,expected_matches)
    
    def test_compare_employee4(self):
        employee1 = Employee_model('Kevin','MO10:00-12:00,TU10:00-12:00,WE10:00-12:00,SA10:00-12:00')
        employee2 = Employee_model('Vanessa','MO10:00-12:00,TU10:00-12:00')

        employe_controller = Employee_controller()
        matches = employe_controller.compare(employee1,employee2)
        expected_matches = 2

        self.assertEqual(matches,expected_matches)


if __name__ == '__main__':

    unittest.main()