# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2


# c=1
# while(c==1):
#     # Take input from the user
#     choice = input("Select operations f 1, 2, 3, 4:")

#     if (int(choice)>0 and int(choice)<5):
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))

#         operations = {
#             '1': add,
#             '2': subtract,
#             '3': multiply,
#             '4': divide,
#         }
#         selected_op = operations.get(choice)
#         answer = selected_op(num1, num2)
#         print(answer)

#         continue_op = input("EXIT? (y/n): ")
#         if continue_op == "n":
#             break

#     else:
#         print("Please enter a valid input")
