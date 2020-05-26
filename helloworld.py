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

x = 2020
print(x)

x += 10 # Takes x and increments by 10
print(x)

x -= 10 # Takes x and decrements by 10
print(x)