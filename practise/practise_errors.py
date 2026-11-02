try:
    number = int(input("Enter a number to divide by 100: "))
    print("The result: ",100/number)
except ValueError:
    print("That is not a number! Please enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero! Please enter a number")
