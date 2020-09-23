first_name = 'Jule'
last_name = 'Blevins'

def account_generator(first_name, last_name):
	account_name = first_name[:3] + last_name[:3]
	return account_name



new_account = account_generator(first_name, last_name)

print(new_account)



first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)




company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]

final_word = company_motto[-4:]



Strings are Immutable

Escape Characters
password = "theycallme\"crazy\"91"



def print_each_letter(word):
  for letter in word:
    print(letter)




def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False



def contains(big_string, little_string):
	return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common



def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name
  
    
def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password





Strings Methods


.lower() returns the string with all lowercase characters.
.upper() returns the string with all uppercase characters.
.title() returns the string in title case, which means the first letter of each word is capitalized.
.split() takes a string and creates a list of substrings.
.join() takes a list of strings and creates a string.
.strip() cleans off whitespace, or other noise from the beginning and end of a string.
.replace() replaces all instances of a character/string in a string with another character/string.
.find() searches a string for a character/string and returns the index value that character/string is found at.
.format() and f-strings allow you to interpolate a string with variables.



highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
  
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
  
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))







Modules are also often referred to as "libraries" or "packages" — a package is really a directory that holds a collection of modules.
A module is simply a file containing Python code.

from module_name import object_name

from library import object_name



from datetime import datetime 
import random     # With random, we'll be using more than one piece of the module's functionality, so the import syntax will look



random.choice() which takes a list as an argument and returns a number from the list
random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in



# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996





Dictionary

A dictionary is an unordered set of key: value pairs.



children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"] , "Corleone":["Sonny", "Fredo", "Michael"]}

Add A Key

my_dict["new_key"] = "new_value"

animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0
print(animals_in_zoo)



sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}


Overwrite Values

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}




List Comprehensions to Dictionaries


names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]


students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}




Use a key to get a value from a dictionary

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

>>> building_heights["Burj Khalifa"]
828
>>> building_heights["Ping An"]
599

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])



Get an Invalid Key


print(building_heights["Landmark 81"])

KeyError: 'Landmark 81'




Check for existence of keys


key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")


caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")
 


building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")


You can also specify a value to return if the key doesnt exist.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)

print(tc_id)
print(stack_id)

100019
100000



Delete a Key


available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


{'strength sandwich': 25, 'health potion': 10, 'cake of the cure': 5, 'green elixir': 20}
65





Find the length of a dictionary


Iterate through keys and values in dictionaries


test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for student in test_scores.keys():
  print(student)

.keys() method that returns a dict_keys object.
 dict_keys object is a view object, which provides a look at the current state of the dicitonary, without the user being able to modify anything


>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]



.values() method that returns a dict_values object (just like a dict_keys object but for values!)



num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)



Get All Items

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")








Types

a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"

print(type(an_int))
# prints "<class 'int'>"

ou cannot .get() something from an integer, because those operations are defined at the type/class level.

A class is a template for a data type.

Instantiation

A class doesnt accomplish anything simply by being defined. 
A class must be instantiated. In other words, we must create an instance of the class, in order to breathe life into the schematic


Object-Oriented Programming

A class instance is also called an object. 
The pattern of defining classes and creating objects to represent the responsibilities of a program is known as Object Oriented Programming or OOP.




Class Variables


class Musician:
  title = "Rockstar"

drummer = Musician()
print(drummer.title)
# prints "Rockstar"


Methods 

are functions that are defined as part of a class. 


class Dog():
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."



class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"




Constructors


__init__ method (note the two underscores before and after the word "init"). 
This method is used to initialize a newly created object. 
It is called every time the class is instantiated.


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




Instance Variables

each instance of a class can hold different kinds of data.

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"     # here we are assigning the string to .fake_key attribute
fake_dict2.fake_key = "This too!"

# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"



Attribute Functions

class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")

# prints "This text gets printed!"

getattr() is a Python function that works a lot like the usual dot-syntax (i.e., object_name.attribute_name) but we can supply a third argument that will be the default if the object does not have the given attribute. 

hasattr() return True or False


how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]] # this is a lists

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))






class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)

codecademy = SearchEngineEntry("www.codecademy.com")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"


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




We can use the dir() function to investigate an object attributes at runtime.


class Employee():
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"





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



User as our base class. 
we created the subclass Admin



issubclass()


Exception is a class that inherits from Python Exception class.

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
except KitchenException:     # here is where we get advantage of the subclass.
  food = order_takeout()



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



class Admin(User):
  def has_permission_for(self, key):
    return True




class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
      
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text




Super()


class Sink:
  def __init__(self, basin, nozzle):
    self.basin = basin
    self.nozzle = nozzle

class KitchenSink(Sink):
  def __init__(self, basin, nozzle, trash_compactor=None):
    super().__init__(self, basin, nozzle)
    if trash_compactor:
      self.trash_compactor = trash_compactor




class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
    
class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40



class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * .00005



Polymorphism





class Color:
  def __init__(self, red, blue, green):
    self.red = red
    self.blue = blue
    self.green = green

  def __repr__(self):
    return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)


  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_blue = min(self.blue + other.blue, 255)
    new_green = min(self.green + other.green, 255)

    return Color(new_red, new_blue, new_green)





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


>>>
2
diana
frank


