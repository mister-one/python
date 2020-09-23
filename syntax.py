
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:

print("The total price is", total_price)


# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why should you not speak to me? And why should I not speak to you?
"""


print(to_you)





def mult_x_add_y(number, x, y):
  print(number*x + y)
  
mult_x_add_y(5, 2, 3)
mult_x_add_y(1, 3, 1)




def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+title+" with "+str(row_count)+" rows.")
  
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)




Returns
So far, we have only seen functions that print out some result to the console. 
Functions can also return a value to the user so that this value can be modified or used later. 
When there is a result from a function that can be stored in a variable, it is called a returned function value. We use the keyword return to do this.

# Here's an example of a function divide_by_four that takes an integer argument, divides it by four, and returns the result:

def divide_by_four(input_number):
    return input_number/4

#The program that calls divide_by_four can then use the result later:

result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")
This would print out:

16 divided by 4 is 4!
4 divided by 4 is 1!
In this example, we returned a number, but we could also return a String:

def create_special_string(special_item):
    return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string)
Our special is banana yogurt.





def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age


my_age = calculate_age(2018,1993)

dads_age = calculate_age(2018, 1953)

print("I am {x} years old and my dad is {y} yeas old".format(x=my_age, y=dads_age))







Sometimes we may want to return more than one value from a function. 
We can return several values by separating them with a comma:

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
This function takes in an x value and a y value, and returns them both, squared. 
	We can get those values by assigning them both to variables when we call the function:

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
This will print:

1
9










def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit

low, high = get_boundaries(100, 20)
print("Low limit: "+str(low)+", high limit: "+str(high))






#Scope
#Let's say we have our function from the last exercise that creates a string about a special item:

def create_special_string(special_item):
    return "Our special is " + special_item + "."
What if we wanted to access the variable special_item outside of the function? Could we use it?

def create_special_string(special_item):
    return "Our special is " + special_item + "."

print("I don't like " + special_item)
If we try to run this code, we will get a NameError, telling us that 'special_item' is not defined. The variable special_item has only been defined inside the space of a function, so it does not exist outside the function. We call the part of a program where special_item can be accessed its scope. The scope of special_item is only the create_special_string function.

Variables defined outside the scope of a function may be accessible inside the body of the function:

header_string = "Our special is " 

def create_special_string(special_item):
    return header_string + special_item + "."
print(create_special_string("grapes"))
There is no error here. header_string can be used inside the create_special_string function because the scope of header_string is the whole file. This file would produce:

Our special is grapes.








current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age(1970))



train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

c0_in_fahrenheit = f_to_c(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)




We can use elif statements to control the order we want our program to check each of our conditional statements. 
First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.








