

# ### Day 1: Python Basics
# Start by installing Python and a text editor. Learn the basics of Python, such as: 
#  variables, data types, Math Operators, Comments, Input() function, Print() function, The str(), int(), and float() Functions

# #### Exercise
# Simple Python Calculator Program: Write a simple program that does basic math operations including addition, subtraction, deletion, division, power, squareroot,etc,. 

import math

# i didnt understand what deletion was but here's the code for the rest

# so this shows the user what options to pick for different arithmetic operations
def calculator():
    print("Simple Python Calculator")
    print("Operations: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("0. Exit")

    while True:  #starts a loop
        choice = input("Enter operation number (0-6): ")  #then this assigns the users answer to the variable choice 

        if choice == '0':
            print("Calculator has exited.")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:  #error for invalid choice
            print("Invalid input. Please try again.")
            continue          #so what continue does is, its like break except it loops to the beginning instead of leaving the loop4

        num1 = float(input("Enter the first number: "))  #im changing this to float to cater for decimals too

        if choice != '6':
            num2 = float(input("Enter the second number: "))

        if choice == '1':                       #self explanatory from here hehehe
            result = num1 + num2
            print("Result: ", result)
        elif choice == '2':
            result = num1 - num2
            print("Result: ", result)
        elif choice == '3':
            result = num1 * num2
            print("Result: ", result)
        elif choice == '4':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print("Result: ", result)
        elif choice == '5':
            result = num1 ** num2
            print("Result: ", result)
        elif choice == '6':
            if num1 < 0:
                print("Error: Cannot calculate square root of a negative number!")
            else:
                result = math.sqrt(num1)    #oh this line is why we import math at the beginning
                print("Result: ", result)

               

calculator()
