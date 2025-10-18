'''
Autor: Alexandre Borgmann
Data: 19/04/2020
Sololearn Day of the Week

You receive a date and need to know what day of the week it is.

Task:
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format:
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format:
A string containing the day of the week from the provided date.

Sample Input:
11/19/2019

Sample Output:
Tuesday
'''
from datetime import datetime

diasSemana = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

datetime_object = datetime.strptime
s = input("")
try:
    data = datetime.strptime(s,"%m/%d/%Y")
except:
    try:
        data = datetime.strptime(s,"%B %d, %Y")
    except:
        raise
print(diasSemana[data.weekday()])

