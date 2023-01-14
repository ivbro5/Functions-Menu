#1
def months_and_days():
  month = input("Enter your birth month: ")
  if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "August" or month == "October" or month == "December":
    print("This month has 31 days.")
  elif month == "February": 
    print("This month has 28 days.")
  elif month == "April" or month == "June" or month == "September" or month == "November": 
    print("This month has 30 days.")
  else:
    print("Invalid input.")

#months_and_days()

#2
def zodiac():
  birth_month = input("Enter your birth month: ")
  birth_date = int(input("Enter your birth date: "))
  if birth_month == "January" and birth_date < 20: 
    print("You're a Capricorn")
  elif birth_month == "January" and birth_date > 20 and birth_date <= 31:
    print("You're an Aquarius")
  elif birth_month == "February" and birth_date < 19:
    print("You're an Aquarius")
  elif birth_month == "February" and birth_date > 19 and birth_date <= 28:
    print("You're a Pisces ")
  elif birth_month == "March" and birth_date < 21:
    print("You're a Pisces")
  elif birth_month == "March" and birth_date > 21 and birth_date <= 31:
    print("You're an Aries")
  elif birth_month == "April" and birth_date < 20:
    print("You're an Aries")
  elif birth_month == "April" and birth_date > 20 and birth_date <= 30:
    print("You're a Taurus")
  elif birth_month == "May" and birth_date < 21:
    print("You're a Taurus")
  elif birth_month == "May" and birth_date > 21 and birth_date <= 31:
    print("You're a Gemini")
  elif birth_month == "June" and birth_date < 21:
    print("You're a Gemini")
  elif birth_month == "June" and birth_date > 21 and birth_date <= 30:
    print("You're a Cancer")
  elif birth_month == "July" and birth_date < 23:
    print("You're a Cancer")
  elif birth_month == "July" and birth_date > 21 and birth_date <= 31:
    print("You're a Leo")
  elif birth_month == "August" and birth_date < 23:
    print("You're a Leo")
  elif birth_month == "August" and birth_date > 23 and birth_date <= 31:
    print("You're a Virgo")
  elif birth_month == "September" and birth_date < 23:
    print("You're a Virgo")
  elif birth_month == "September" and birth_date > 23 and birth_date <= 30:
    print("You're a Libra")
  elif birth_month == "October" and birth_date < 23:
    print("You're a Libra")
  elif birth_month == "October" and birth_date > 23 and birth_date <= 31:
    print("You're a Scorpio")
  elif birth_month == "November" and birth_date < 22:
    print("You're a Scorpio")
  elif birth_month == "November" and birth_date > 22 and birth_date <= 30:
    print("You're a Sagittarius")
  elif birth_month == "December" and birth_date < 22:
    print("You're a Sagittarius")
  elif birth_month == "December" and birth_date > 22 and birth_date <= 31:
    print("You're a Capricorn")
  else:
    print("Invalid input.")
#zodiac()


#3 
def sides_of_triangle():
  l1 = int(input("Enter a number to replace a: "))
  l2 = int(input("Enter a number to replace b: "))
  l3 = int(input("Enter a number to replace c: "))

  if l1 == l2 == l3:
    print("This is a equilateral triagle.") 
  elif l1 == l2 or l1 == l3 or l3 == l2: 
    print("This is a isosceles triangle.")
  else:
    print("This is a scalene triangle.")
  
#sides_of_triangle()


def menu():
  print("Option 1: Month & Days, Option 2: Zodiac, Option 3: Triangles ")
  option = int(input("Pick an option (1-3): "))

  if option == 1:
    months_and_days()
  elif option == 2:
    zodiac()
  elif option == 3:
    sides_of_triangle()
  else:
    print("Invalid input.")

menu()