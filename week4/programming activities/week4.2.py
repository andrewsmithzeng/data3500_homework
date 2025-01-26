"""
Programming Activity 2:

Write a program which asks the user their age, then using a while loop displays the year they were born, using the following rules:
 - continue the loop while age is greater than 1
 - print each time "you were alive in year: " current_year
 - decrease age and current_year by one each time
 - add an else saying "you were born in year: " current_year
"""
from datetime import datetime
current_year = datetime.now().year
#print(type(current_year))

age = int(input('how old are you?'))

while age > 0:
    print(f'you were alive in year:{current_year}')
    current_year -= 1
    age -= 1
else:
    print(f'you were born in {current_year}.') 