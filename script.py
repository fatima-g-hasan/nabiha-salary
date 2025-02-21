month = input("Enter the month: ")
salary = float(input("Enter your salary: "))
percent = input("Enter the % for your Savings, Rent and Elecricity separated by a comma: ")

savings, rent, electricity = [float(value) for value in percent.split(",")]

print(savings, rent, electricity)