
while True:
    try:
        n = float(input("Please enter a number: "))
        print("this is valid input",n)
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
