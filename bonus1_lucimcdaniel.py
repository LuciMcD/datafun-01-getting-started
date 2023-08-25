# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# Import from Python Standard Library

import math

# Use the math module's constant for pi
pi = math.pi

# get 3 numbers from the user and calculate sum, min, max, and range.
# Use \n to add a blank new line to the terminal before we ask for input
print('Enter 3 unique integers and we will find the sum, min, max, and range')

number1 = int(input('Enter your first integer: '))
number2 = int(input('Enter your second integer: '))
number3 = int(input('Enter your third integer: '))


# find the sum
sum = number1 + number2 + number3


# find the minimum
minimum = number1
if number2 < minimum:
    minimum = number2

if number3 < minimum:
    minimum = number3


#find the maximum
maximum = number1
if number2 > maximum:
    maximum = number2

if number3 > maximum:
    maximum = number3





# log the results
logger.info(f"The sum of the integers is {sum}.")
logger.info(f"The minimum of the integers is {minimum}.")
logger.info(f"The maximum of the intgers is {maximum}.")
logger.info(f"The range of integers is {minimum} - {maximum}.")
logger.info("Thanks for participating!")



