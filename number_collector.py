# My variables

try:
    number1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Use 0 instead")
    print("Exiting Program. ")
    exit () 

number2 = int(input("Enter number 2: "))
number3 = int(input("Enter number 3: "))
sum = number1 + number2 + number3 
average = sum / 3

# Project starts here

print("Enter 3 numbers. One at a time")

print(f"Enter number 1: {number1}")
print(f"Enter number 2: {number2}")
print(f"Enter number 3: {number3}")
print(f"Your numbers: {number1}, {number2}, {number3}")
print(f"Sum: {sum}")
print(f"Average: {average:.2f}")