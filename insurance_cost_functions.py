def calculating_cost():
    name = input("Whats your name? ")
    print("Welcome", name)
    print("This program will show you estimated insurance cost, prices might vary.\nWe first need to collect some information about you")
    smoker_status = 0
    age = int(input("How old are you? "))
    smoker = input("Are you a smoker? yes/no: ")
    if smoker == 'yes':
        smoker_status += 1
        pass
    elif smoker == 'no':
        pass
    else:
        print("invalid input, please try again by typing 'yes' or 'no'")
        exit()
    bmi = (input("What is your bmi?\
    note that bmi can be calculated: kg/m2 where kg is a persons weight\n and\
    m2 is their height in metres squared: "))
    children = int(
        (input("How many children do you have? enter 0 if non: ")))
    estimated_cost = 100 * age + 140 * \
        smoker_status + 50 * float(bmi) + 180 * children
    print("Your estimated insurance cost is:", estimated_cost, "dollars.")
    last_messege = input("Would you like to check again? yes/no: ")
    while last_messege == 'yes':
        calculating_cost()
    else:
        exit()


calculating_cost()
