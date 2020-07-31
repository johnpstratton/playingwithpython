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

#################################### Printing datetime by importing and using datetime library ############
# from datetime import datetime
# current_date = datetime.now()
# print('Today is: ' + str(current_date))

################################### Data Conversion ##################################

# Write a program which prompts the user for a Celsius temperature
# convert the temperature to Farenheit, and
# print out the converted temperature

# tempInC = input('What is the temperature in (in C!): ') #ask the user for temp in C
# tempInC = float(tempInC) # then convert the value from the string to float
# tempInF = tempInC * 9/5 + 32 # convert the temperature to Farenheit
# print(tempInF) # print out the converted temperature
# print('{0} C = {1} F'.format(tempInC, tempInF))

############################## Data Conversion with Input from user #########
# num1 = int( input('Enter a number: '))
# num2 = int( input('Enter another number: '))
# print(num1 + num2)

##################################################################################

############################## String Lengths #################################
# soBored = 'Airplanes have rotars'
# i = int(len(soBored) - 1)
# print(len(soBored) -1)

# # randomly display one character from soBored
# import random
# print(soBored[ random.randint(0, len(soBored) - 1)])

# # Basic for loop to display random characters in soBored string
# for i in soBored:
#     print(soBored[ random.randint(0, len(soBored) - 1)])
##################################################################################

########################### Escape Characters #############################
# pizzaString = 'pizza'
# print(pizzaString)

# pizzaString = '\'pizza\''
# print(pizzaString)

# pizzaString = 'pi\\z\\za'
# print(pizzaString)

################### Check out the rest of the escape characters in slide deck ################

# ▪ Create a program that will ask the user to enter a sales price and tax rate.
# Your program should then compute the tax and total price. ###############

# itemPrice = float(input('How much does this item cost? '))
# taxRate = float(input('What is the tax rate? '))

# taxToAdd = itemPrice * taxRate
# totalPrice = itemPrice + taxToAdd
# print(str(itemPrice) + ' + tax = ' + str(totalPrice))

###############################################################################################

############################## USING DATETIME ##############################

# from datetime import datetime, timedelta

# print(datetime.now())
# print("Current time: " + str(datetime.now()))

# tenDaysAgo = datetime.now() - timedelta(days = 10)

# print(str(tenDaysAgo).split()[0])

##########################################################################


###################### Error Handling #####################

# num1 = int(input("num 1 = "))
# num2 = int(input("num 2 = "))
# print(num1/num2)

# try:
#     num1 = int(input("num 1 = "))
#     num2 = int(input("num 2 = "))
#     print(num1/num2)
#     print("Success!")
#     print("Line1")
#     print("Line2")
# except ZeroDivisionError as e:
#     print(e)
# except :
#     print("catch anything else ")
# finally:
#     print("MSSA")

########################################## How to specify incrementor #############

# x = 2020
# print(x)

# x += 10 # Takes x and increments by 10
# print(x)

# x -= 10 # Takes x and decrements by 10
# print(x)

######################################################################################

### Boolean Value examples

# print(10>9)
# print(10 == 9)

####################### CONDITIONAL LOGIC #####################################
# one = ["*"]
# asterisk = "*"

# for x in one:
#     one.append(asterisk)
#     for y in one:
#         print(x)
#         break

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# even = []

# for x in a:
#     if x %2 == 0:
#         even.append(x)
# print(even)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# allnums = a + b
# allnums.sort()
# count = 0
# counta = 0
# countb = 0
# dups = []

# while count < len(allnums):
#     if any in a == any in b and (any in a or any in b != any in dups):
#         dups.append()
# print(dups)

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = []

# for x in a (if x %2 == 0):

# import random

# num = random.randint(1, 31)
# count = 0
# a = []
# b = []
# common = []
# randRange = random.randrange(1, 31)
# while count < random.randrange(1, 31):
#     num = random.randint(1, 31)
#     a.append(num)
#     a = list(dict.fromkeys(a))
#     num = random.randint(1, 31)
#     b.append(num)
#     b = list(dict.fromkeys(b))
    
#     count += 1

# common = a + b
# common.sort()
# print(common)
# for x in a:
#     if x != b[x]:
#         a.remove(x)
# for y in b:
#     if y != a[y]:
#         b.remove(y)
# a.sort()
# b.sort()    
# print(a)
# print(b)
# import random 
# a = random.sample(range(1,30), 12) 
# b = random.sample(range(1,30), 16) 
# result_overlap = [i for i in set(a) if i in b] 
# result = [] 
# for element in result_overlap: 
#     if element not in result: 
#         result.append(element)
# a.sort()
# b.sort()     
# print(a) 
# print(b)
# print(result)
# print(result_overlap)

import random 
def randPassword():
    num = 0 # declare variable to store random number between 33-136
    password = "" #string to add characters to make password
    while len(password) < 10: # Initiate while loop 
        num = random.randint(33, 126) # Initiate 1 new random number
        password += chr(num) # append random character to password
    return password # return the password when while loop completes

print(randPassword())

lines = 8
for line in range(1, lines+1):
    for column in range(1, line +1):
        print(column, end = "")
    print("")

print("sfsdf")
print("sfsdf")
print("sfsdf")
print("sfsdf")
