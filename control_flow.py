# control flows

Equals: ==
Not equals: !=
Greater than: >
Less than: <
Greater than or equal to: >=
Less than or equal to: <=





bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))


if is_raining:
  bring_umbrella()
  # You'll notice that instead of "then" we have a colon, :.
  # That tells the computer that what's coming next is what should be executed if the condition is met.
  # Let's take a look at another conditional statement:


def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"
  if user_name == "angela_catlady_87":
  	return "I know it is you Dave! Go away!"


user_name = "Dave"  # Enter a user name here, make sure to make it a string

print(dave_check(user_name))



def greater_than(x, y):
  if x > y:
    return x
  if y > x:
    return y
  if x == y:
    return "These numbers are the same"


def graduation_reqs(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"


>>> True or (3 + 4 == 7)
True
>>> (1 - 1 == 0) or False
True
>>> (2 < 0) or True
True
>>> (3 == 8) or (3 > 4)
False




# not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value.
# So if we have a True statement and apply a not operator we get a False statement.
>>> not 1 + 1 == 2
False
>>> not 7 < 0
True




def graduation_reqs(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"



if weekday:
  wake_up("6:30")
else:
  sleep_in()


elif
'''
We can use elif statements to control the order we want our program to check each of our conditional statements.
First, the if statement is checked, then each elif statement is checked from top to bottom,
then finally the else code is executed if none of the previous conditions have been met.
'''


def thank_you(donation):
  if donation >= 1000:
    print("Thank you for your donation! You have achieved platinum donation status!")
  elif donation >= 500:
    print("Thank you for your donation! You have achieved gold donation status!")
  elif donation >= 100:
    print("Thank you for your donation! You have achieved silver donation status!")
  else:
    print("Thank you for your donation! You have achieved bronze donation status!")



def grade_converter(gpa):
  grade = "F"

  if gpa >= 4.0:
    grade = "A"
  elif gpa >= 3.0:
    grade = "B"
  elif gpa >= 2.0:
    grade = "C"
  elif gpa >= 1.0:
    grade = "D"

  return grade



try:
    # some statement
except ErrorName:
    # some statement

First, the statement under try will be executed.
If at some point an exception is raised during this execution, such as a NameError or a ValueError and that exception matches the keyword in the except statement,
then the try statement will terminate and the except statement will execute.


def divides(a,b):
  try:
    result = a / b
    print (result)
  except ZeroDivisionError:
    print ("Can't divide by zero!")


def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")

  >>> You raised a ValueError!



def divide_two_numbers(x, y):
  result = x / y
  return result

try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")

>>>  A ZeroDivisionError occurred



Boolean expressions are statements that can be either True or False
A boolean variable is a variable that is set to either True or False.
You can create boolean expressions using relational operators:
Equals: ==
Not equals: !=
Greater than: >
Greater than or equal to: >=
Less than: <
Less than or equal to: <=
if statements can be used to create control flow in your code.
else statements can be used to execute code when the conditions of an if statement are not met.
elif statements can be used to build additional checks into your if statements
try and except statements can be used to build error control into your code.



def simple_conditional(x):
  if x = 0:
    print("x is equal to zero.")
  elif x >= 0:
    print("x is greater than zero.")
  else:
    print("x is less than zero.")


def print_something(x):
  if x <= 2:
    print("This is printed")
  if x <= 4:
    print("This is also printed")
  if x <= 6:
    print("Is this printed?")
  if x <= 8:
    print("This might be printed.")

print_something(5)  

>>> Is this prnted?
>>> This might be printed





def divide_two_numbers(x, y):
  result = x / y
  return result

try:
  result = divide_two_numbers(2,0)
  print(result)
except NameError:
  print("A NameError occurred.")
except ValueError:
  print("A ValueError occurred.") 
except ZeroDivisionError:
  print("A ZeroDivisionError occurred.")




 # Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True



# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie"



# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True




def shipping_cost_ground(weight):
  if weight <= 2:
    price = 1.50
  elif weight <= 6:
    price = 3.00
  elif weight <= 10:
    price = 4.00
  else:
    price = 4.75

  return 20 + (price * weight)

shipping_cost_premium = 125.00


def shipping_cost_drone(weight):
  if weight <= 2:
    price = 4.50
  elif weight <= 6:
    price = 9.00
  elif weight <= 10:
    price = 12.00
  else:
    price = 14.25

  return (price * weight)

def print_cheapest_shipping_ method(weight):

  ground = shipping_cost_ground(weight)
  premium = 125
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    cost = ground
    method = "ground"
  elif	drone < ground and drone < premium:
    cost = drone
    method = "drone"
  else:
  	cost = premium
  	method = "premium"

   print("the cheap is %s and the cost is $%.2f"%(method, cost))









