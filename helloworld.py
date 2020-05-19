# print('Hello World')
# print()
# print('Did you see that blank line?')
# print('Blank line \nin the middle of string')
# print('Adding numbers')
# x = 42 + 206
# print()
# first_name = 'John'
# last_name = 'Stratton'
# output = 'Hello, ' + first_name + ' ' + last_name
# print(output)
# print()
# output = 'Hello, {0} {1}'.format(first_name, last_name)
# print(output)
# print()
# days_in_feb = 28
# print(str(days_in_feb) + 'in February')

# first_num = '5'
# second_num = '6'
# print(int(first_num) + int(second_num))
from datetime import datetime
current_date = datetime.now()
print('Today is: ' + str(current_date))

################################### Data Conversion ##################################

# Write a program which prompts the user for a Celsius temperature
# convert the temperature to Farenheit, and 
# print out the converted temperature

tempInC = input('What is the temperature in (in C!): ') #ask the user for temp in C
tempInC = float(tempInC) # then convert the value from the string to float
tempInF = tempInC * 9/5 + 32 # convert the temperature to Farenheit
print(tempInF) # print out the converted temperature
print('{0} C = {1} F'.format(tempInC, tempInF))


