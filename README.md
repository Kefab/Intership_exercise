# Intership_exercise

# Exercise
The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

Example 1:<br><br>
INPUT: <br>
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00 <br>
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 <br>
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 <br><br>
OUTPUT: <br>
ASTRID-RENE: 2 <br>
ASTRID-ANDRES: 3 <br>
RENE-ANDRES: 2 <br>
<br>
Example 2: <br><br>
INPUT: <br>
RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00 <br>
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 <br><br>
OUTPUT: <br>
RENE-ASTRID: 3 <br>
________________________________________
# Solution
As per given in the exercise instructions, every single line has the information about one employee and his schedule, we can make an algorithm to convert this line to objects for solve the problem.
The next step is comparing each employee and their schedule, we can do this iterating the list two time. After this the result is show the number of coincidences on the screen.
________________________________________
# Architecture

![imagen](https://user-images.githubusercontent.com/45211516/176502702-08263ced-ddab-451b-944c-1f3dfe288131.png)
________________________________________
# Approach

To solve the exercise first look for a pattern to handle the input data, after finding the pattern transform the data into objects for easy handling.
The objects are 2, employee and day, the day consists of the name, time of entry and time of exit. The employee consists of the name and a list of days corresponding to their schedule.
After obtaining the objects compare each user with the rest to know the number of times they coincided in the office and the data was presented.
________________________________________
# How to run the project
First you need have installed Python 3
After you just have to follow these steps:
  1. Download the github repository. 
  2. Enter to the project folder.
  3. run the main.py file with next code: <br>
`python main.py 'file_name.txt'` <br>
file_name.txt is the file with the employees data and its absolute or relative path can be specified, this attribute is optional and can be omitted.
________________________________________
# How to run the unit tests
First you need have installed Python 3
After you just have to follow these steps:
  1. Download the github repository. 
  2. Enter to the project folder.
  3. run the test.py file with next code: <br>
`python test.py`
