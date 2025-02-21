def calcAmount(percent,salary):
  return(percent / 100) * salary

def totalAmount(savings_amount, rent_amount, electricity_amount):
  return(savings_amount + rent_amount + electricity_amount)

def calcRemainder(salary, sum_amount):
  return(salary - sum_amount)

def calcYearly(rent_amount, electricity_amount):
  return(rent_amount * 12, electricity_amount * 12)


month = input("Enter the month: ")
salary = float(input("Enter your salary: "))
percent = input("Enter the % for your Savings, Rent and Elecricity separated by a comma: ")

savings, rent, electricity = [float(value) for value in percent.split(",")]

savings_amount = calcAmount(savings, salary)
rent_amount = calcAmount(rent, salary)
electricity_amount = calcAmount(electricity, salary)

sum_amount = totalAmount(savings_amount, rent_amount, electricity_amount)

print(calcYearly(rent_amount, electricity_amount))