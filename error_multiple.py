try:
    number = int(input("enter number: "))
    result = 100 / number
    print(result)


except ZeroDivisionError:
    print("Cannot divide by zero")


except ValueError:
    print("Please enter numbers only")

