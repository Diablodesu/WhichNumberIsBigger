# Input numbers 
x = input('Enter first number: ')
y = input('Enter second number: ')


# Calculation
if int(x) == int(y):
    print("Your numbers are equal!")
elif int(x) > int(y):
    print("Your first number is greater than your second number.")
else:
    print("Your second number is greater than your first number.")


# Prompt user to quit the program
input("Press any key to exit.")