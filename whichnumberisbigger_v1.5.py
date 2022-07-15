# Imports
import time

# Input numbers 
x = input('Enter first number: ')
y = input('Enter second number: ')


# Calculation
if int(x) > int(y):
    print("Your first number is greater than your second number.")

if int(x) < int(y):
    print("Your second number is greater than your first number.")

# Tell user that program will exit

time.sleep(0.5)
print("The program will exit in 5 seconds.")

# Wait for 5 seconds

time.sleep(5)