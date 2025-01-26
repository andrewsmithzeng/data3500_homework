"""
Programming Activity 1

Write a program that asks the user the year they were born. Display a message telling the user 
what generation they belong to based on the following rules/years:
 - Zoomer 1997
 - Millennial 1981
 - Gen X 1965
 - Baby Boomer 1946
"""
def generation(year):
    if year >1997:
        return 'Zoomer'
    elif year >1981:
        return 'Millennial'
    elif year >1965:
        return 'Gen X'
    elif year >1946:
        return 'Baby Boomer'
 
year = eval(input('which year were you born?'))
#generation = generation(year)
print(f'you belongs to {generation(year)} generation.')

