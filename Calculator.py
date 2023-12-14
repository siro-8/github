print("-"*40)
print("Welcome to this simple calculator.")
print("-"*40)

while True:

    number1 = float(input("Please enter your first number: "))
    number2 = float(input("Please enter your second number: "))


    print(f"You have entered numbers {number1} and {number2}. \n")

    print("Operations menu: ")
    print("1 - addition")
    print("2 - substraction")
    print("3 - multiplication")
    print("4 - division \n")

    while True:

        operation = input("Please enter type of operation you would like to perform with your numbers from the menu above: ")

        if operation == "1":
            addition = round(number1 + number2, 2)
            print(f"The result of your chosen calculation (addition) is: {addition}. \n")
            break

        elif operation == "2":
            substraction = round(number1 - number2, 2)
            print(f"The result of your chosen calculation (substraction) is: {substraction}. \n")
            break

        elif operation == "3":
            multiplication = round(number1 * number2, 2)
            print(f"The result of your chosen calculation (multiplication) is: {multiplication}. \n")
            break

        elif operation == "4":

            if number2 == 0:
                print("Sorry, it's not possible to divide by 0! ")
                break

            else: 
                division = round(number1 / number2, 2)
                print(f"The result of your chosen calculation (division) is: {division}. \n")  
                break

        else: 
            print("Invalid option. Please chose option from the menu above. \n")  

    print("-"*40)

    another_calculation = input("Would you like to perform another calculation? (y/n): ").lower()

    while another_calculation not in ["y", "n"]:
        print("Invalid option. Please chose y/n. \n")
        another_calculation = input("Would you like to perform another calculation? (y/n): ").lower()

    if another_calculation == "y":
        print("Great, let's do it!")
        print("-"*40)
            
    elif another_calculation == "n":
        print("Thank you for using our simple calculator. ")
        print("-"*40)
        break

# end 