CLASSES

'''
A class is a template for a data type. It describes the kinds of information that class will hold and how a programmer will interact with that data. 
A variable's type determines what you can do with it and how you can use it. 
You can't .get() something from an integer, just as you can't add two dictionaries together using +. 
This is because those operations are defined at the type level.
'''

print(type(5))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

<class 'int'>
<class 'dict'>
<class 'list'>









class CoolClass:   # we created a class and named it CoolClass. 
  pass    # We used the pass keyword in Python to indicate that the body of the class was intentionally left blank so we don't cause an IndentationError



# A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic.
#Instantiating a class looks a lot like calling a function. We would be able to create an instance of our defined CoolClass as follows:

cool_instance = CoolClass() # we created an object by adding parentheses to the name of the class.  
                            # We then assigned that new instance to the variable cool_instance for safe-keeping.



class Facade:
  pass

facade_1 = Facade()   #Make a Facade instance and save it to the variable facade_1.


# A class instance is also called an object. The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.
# type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.




print(type(cool_instance))
# prints "<class '__main__.CoolClass'>"
When called with an object, it returns the class that the object is an instance of.
We then print out the type() of cool_instance and it shows us that this object is of type __main__.CoolClass.
In Python __main__ means "this current file that we're running" and so one could read the output from type() to mean "the class CoolClass that was defined here, in the script you're currently running."




class Musician:
  title = "Rockstar"        # A class variable is a variable that's the same for every instance of the class.

drummer = Musician()
print(drummer.title)
# prints "Rockstar"

'''
Above we defined the class Musician, then instantiated drummer to be an object of type Musician. We then printed out the drummer's .title attribute, which is a class variable that we defined as the string "Rockstar".
If we defined another musician, like guitarist = Musician() they would have the same .title attribute.
'''



Methods are functions that are defined as part of a class

class Dog():
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

# Above we created a Dog class with a time_explanation method that takes one argument, self, which refers to the object calling the function. 
# We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object for Pipi.
# Notice we didn't pass any arguments when we called .time_explanation(), but were able to refer to self in the function body. 
# When you call a method it automatically passes the object calling the method as the first argument.




class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."




class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

# Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. 
# Notice that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is implicitly passed (and refers to the object converter).




Methods are functions that are defined as part of a class. 

class Circle:
  pi = 3.14
  
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)







Methods that are used to prepare an object being instantiated are called constructors. 
The word "constructor" is used to describe similar features in other object-oriented programming languages
but programmers who refer to a constructor in Python are usually talking about the __init__ method.
dunder methods, so-named because they have two underscores (double-underscore abbreviated to "dunder") 



__init__ method 
This method is used to initialize a newly created object.


class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"




class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"





class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)





Instance variable = is the data held by an object 

class FakeDict:
  pass
We can instantiate two different objects from this class, fake_dict1 and fake_dict2, 
and assign instance variables to these objects using the same attribute notation that was used for accessing class variables.

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!" 



class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"       # Give them both instance attributes called store_name. 
isabelles_ices.store_name = "Isabelle's Ices"           # Set alternative_rocks's store_name to "Alternative Rocks". Set isabelles_ices's store_name to "Isabelle's Ices".






class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

Above we checked if the attributeless object has the attribute fake_attribute. Since it does not, hasattr() returned False. 
After that, we used getattr to attempt to retrieve other_fake_attribute. 
Since other_fake_attribute isn't a real attribute on attributeless, our call to getattr() returned the supplied default value 800, instead of throwing an AttributeError.



# we have a list of different data types, some strings, some lists, and some dictionaries, all saved in the variable how_many_s.
# For every element in the list, check if the element has the attribute count. 
# If so, count the number of times the string "s" appears in the element. Print this number.

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))




Self

Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.


class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    
    self.radius = diameter / 2
    
  def circumference(self):
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())






Everything is an Object

Attributes can be added to user-defined objects after instantiation,
so it's possible for an object to have some attributes that are not explicitly defined in an object's constructor. 
We can use the dir() function to investigate an object's attributes at runtime. dir() is short for directory and offers an organized presentation of object attributes.'


fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']







class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"





String Representation


class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"


This default string representation gives us some information, 
like where the class is defined and our computer's memory address where this object is stored, but is usually not useful information to have when we are trying to debug our code.'
We learned about the dunder method __init__. 
Now, we will learn another dunder method called __repr__. 
__repr__ is a method we can use to tell Python what we want the string representation of the class to be. 
__repr__ can only have one parameter, self, and must return a string.

In our Employee class above, we have an instance variable called name that should be unique enough to be useful when we're printing out an instance of the Employee class.

class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"
We implemented the __repr__ method and had it return the .name attribute of the object. When we printed the object out it simply printed the .name of the object! Cool!








class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)








class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)      

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))







Inheritance



class User:
  is_admin = False
  def __init__(self, username)
    self.username = username

class Admin(User):
  is_admin = True



'''

Above we defined User as our base class. We want to create a new class that inherits from it, so we created the subclass Admin. 
In the above example, Admin has the same constructor as User. Only the class variable is_admin is set differently between the two.
Sometimes a base class is called a parent class. In these terms, the class inheriting from it, the subclass, is also referred to as a child class.
'''

class Bin:
  pass

class RecyclingBin(Bin):
  pass




issubclass() is a Python built-in function that takes two parameters. 
issubclass() returns True if the first argument is a subclass of the second argument. 
It returns False if the first class is not a subclass of the second. issubclass() raises a TypeError if either argument passed in is not a class.


issubclass(ZeroDivisionError, Exception)
# Returns True




class KitchenException(Exception):
  """
  Exception that gets thrown when a kitchen appliance isn't working
  """

class MicrowaveException(KitchenException):
  """
  Exception for when the microwave stops working
  """

class RefrigeratorException(KitchenException):
  """
  Exception for when the refrigerator stops working
  """






In the example below, we attempt to retrieve food from the fridge and heat it in the microwave. 
If either RefrigeratorException or MicrowaveException is raised, we opt to order takeout instead. 
We catch both RefrigeratorException and MicrowaveException in our try/except block because both are subclasses of KitchenException.

def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException
  else:
    return food

def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException
  else:
    microwave.cook(food)
    return food

try:
  food = get_food_from_fridge()
  food = heat_food(food)
except KitchenException:
  food = order_takeout()




# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')





Overriding Methods

class User:
  def __init__(self, username, permissions):
    self.username = username
    self.permissions = permissions

  def has_permission_for(self, key):
    if self.permissions.get(key):
      return True
    else:
      return False


Above we defined a class User which takes a permissions parameter in its constructor. 
Let's assume permissions is a dict. User has a method .has_permission_for() implemented, where it checks to see if a given key is in its permissions dictionary. 
We could then define our Admin user like this:

class Admin(User):
  def has_permission_for(self, key):
    return True

Here we define an Admin class that subclasses User. 
It has all methods, attributes, and functionality that User has. 
However, if you call has_permission_for on an instance of Admin, it won\'t check its permissions dictionary. 
Since this User is also an Admin, we just say they have permission to see everything!




Super()
Overriding methods is really useful in some cases but sometimes we want to add some extra logic to the existing method. 
In order to do that we need a way to call the method from the parent class. Python gives us a way to do that using super().

class Sink:
  def __init__(self, basin, nozzle):
    self.basin = basin
    self.nozzle = nozzle

class KitchenSink(Sink):
  def __init__(self, basin, nozzle, trash_compactor=None):
    super().__init__(self, basin, nozzle)
    if trash_compactor:
      self.trash_compactor = trash_compactor




Above we defined two classes. 
First, we defined a Sink class with a constructor that assigns a rinse basin and a sink nozzle to a Sink instance. 
Afterwards, we defined a KitchenSink class that inherits from Sink. KitchenSink's constructor takes an additional parameter, a trash_compactor. 
KitchenSink then calls the constructor for Sink with the basin and nozzle it received using the super() function, 

with this line of code:

super().__init__(self, basin, nozzle)

This line says "call the constructor (the function called __init__) of the class that is this class's parent class.\
In the example given, KitchenSink's constructor calls the constructor for Sink.' \
In this way, we can override a parent class's method to add some new functionality (like adding a trash_compactor to a sink), while still retaining the behavior of the original constructor (like setting the basin and nozzle as instance variables).




class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)   #Create a new constructor for SpecialPotatoSalad that just calls the parent constructor for PotatoSalad. Make sure that SpecialPotatoSalad's constructor takes the same arguments as PotatoSalad.
    self.raisins = 40






When two classes have the same method names and attributes, we say they implement the same interface.


Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.









Dunder Methods


class Color:
  def __init__(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

  def __repr__(self):
    return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)

  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)

red = Color(255, 0, 0)
blue = Color(0, 255, 0)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 255, 0)"
In this code we defined a Color class that implements an addition function. Unfortunately, red.add(blue) is a little verbose for something that we have an intuitive symbol for (i.e., the + symbol). Well, Python offers the dunder method __add__ for this very reason! If we rename the add() method above to something that looks like this:

class Color: 
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)
Then, if we create the colors:

red = Color(255, 0, 0)
blue = Color(0, 255, 0)
green = Color(0, 0, 255)
We can add them together using the + operator!

# Color with RGB: (255, 255, 0)
magenta = red + blue

# Color with RGB: (0, 255, 255)
cyan = blue + green

# Color with RGB: (255, 0, 255)
yellow = red + green

# Color with RGB: (255, 255, 255)
white = red + blue + green
Since we defined an __add__ method for our Color class, we were able to add these objects together using the + operator.




class Atom:
  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
      self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine







Dunder Methods II

Python offers a whole suite of magic methods a class can implement that will allow us to use the same syntax as Python's built-in data types.' 
You can write functionality that allows custom defined types to behave like lists:

class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list





In our UserGroup class above we defined three methods:

__init__, our constructor, which sets a list of users to the instance variable self.user_list and sets the group's permissions when we create a new UserGroup.
__iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. For more information on iterators, review Python's documentation of Iterator Types.
__len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
__contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.
These methods allow UserGroup to act like a list using syntax Python programmers will already be familiar with. If all you need is something to act like a list you could absolutely have used a list, but if you want to bundle some other information (like a group's permissions, for instance) having syntax that allows for list-like operations can be very powerful.

We would be able to use the following code to do this, for example:

class User:
  def __init__(self, username):
    self.username = username

diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

print(len(can_edit))
# Prints 2

for user in can_edit:
  print(user.username)
# Prints "diana" and "frank"

if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")




Above we created a set of users and then added them to UserGroups with specific permissions. 
Then we used Python built-in functions and syntax to calculate the length of a UserGroup, 
to iterate through a UserGroup and to check for a User's membership in a UserGroup.





class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  def __len__(self):
    return len(self.lawyers)
  def __contains__(self, lawyer):
    return lawyer in self.lawyers
    
    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])







class SortedList(list):           # Create a class SortedList that inherits from the built-in type list.
  def append(self, value):        # Overwrite the append method, leave it blank for now with the pass keyword.
    super().append(value)         # First, we want our new .append() to actually add the item to the list.
    self.sort()                   # After you've appended the new value, sort the list.




