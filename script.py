def calcAmount(percent,salary):
  return(percent / 100) * salary

def totalAmount(savings_amount, rent_amount, electricity_amount):
  return(savings_amount + rent_amount + electricity_amount)

def calcRemainder(salary, sum_amount):
  return(salary - sum_amount)

def calcYearly(rent_amount, electricity_amount):
  return(rent_amount * 12, electricity_amount * 12)

def squareSalary(salary):
  return salary ** 2

def realRamainder(remainder):
  return remainder - 50

month = input("Enter the month: ")
salary = int(input("Enter your salary: "))
percent = input("Enter the % for your Savings, Rent and Elecricity separated by a comma: ")

savings, rent, electricity = [int(value) for value in percent.split(",")]

savings_amount = calcAmount(savings, salary)
rent_amount = calcAmount(rent, salary)
electricity_amount = calcAmount(electricity, salary)

sum_amount = totalAmount(savings_amount, rent_amount, electricity_amount)

remainder = calcRemainder(salary, sum_amount)
