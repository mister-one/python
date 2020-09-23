Loops
A loop is a way of repeating a set of code many times.

1. Loops that let us move through each item in a list, called for loops
2. Loops that keep going until we tell them to stop, called while loops
3. Loops that create new lists, called list comprehensions



dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)



#  general way of writing a for loop is:
for <temporary variable> in <list variable>:
<action>

In our dog breeds example, breed was the temporary variable, dog_breeds was the list variable, and print(breed) was the action performed on every item in the list.

Our temporary variable can be named whatever we want and does not need to be defined beforehand. Each of the following code snippets does the exact same thing as our example:

for i in dog_breeds:
    print(i)
for dog in dog_breeds:
    print(dog)




sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in sport_games:
	print(game)


promise = "I will not chew gum in class"

for i in range(5):
  print(promise)
>>> 
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
I will not chew gum in class
  



A program that hits an infinite loop often becomes completely unusable. 
The best course of action is to never write an infinite loop. But if you accidentally stumble into one, you can end the loop 
by using control + c to terminate the program.





students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for i in students_period_A:
  students_period_B.append(i)





dog_breeds_available_for_adoption = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmation'

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break


for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    break

print("They have the dog I want!")





# Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print the age.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print (i)




While Loops ✅

# While loops can be useful when you don't know how many iterations it will take to satisfy a condition.

dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)





Nested Loops

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
for team in project_teams:
  for student in team:
    print(student)



sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for i in location:
    scoops_sold += i
    
print(scoops_sold)






List Comprehensions


words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []

for word in words:
  if word[0] == '@':
    usernames.append(word)


usernames = [word for word in words if word[0] == '@']       #  list comprehension.
'''
Takes an element in words
Assigns that element to a variable called word
Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
Repeats steps 1-3 for all of the strings in words
'''



heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [ i for i in heights if i>161]


print(can_ride_coaster)



>>> print(usernames)
["@coolguy35", "@kewldawg54", "@matchamom"]

messages = [user + " please follow me!" for user in usernames]

Takes a string in usernames
Assigns that number to a variable called user
Adds " please follow me!" to user
Appends that concatenation to the new list called messages
Repeats steps 1-4 for all of the strings in usernames




ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if i < 21:
    continue
  print (i)


#  Let's say we want to print out all of the numbers in a list, unless they're negative. We can use continue to move to the next i in the list:



celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [temp*(9/5) + 32 for temp in celsius]

print(fahrenheit)




single_digits = range(10)
squares = []

for item in single_digits:
  print(item)
  squares.append(item**2)
  
cubes = [item**3 for item in single_digits]
print(cubes)




numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)

>>> 1 1 3




my_list = [5, 10, -2, 8, 20]

desired_list = [i for i in my_list if i>5]
desired_list = [10, 8, 20]


desired_list = [i-1 for i in range(5)]
print(desired_list)
>>> [-1, 0, 1, 2, 3]




def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))


#Write your function here
def add_greetings(names):
  lista = []
  for name in names:
    a = "Hello, " + str(name)
    lista.append(a)
  return lista


#Write your function here
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))



# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
>>>  [11, 12, 15]
>>>  []


# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst








# Create a function named exponents() that takes two lists as parameters named bases and powers. 
# Return a new list containing every number in bases raised to every number in powers.
# For example, consider the following code. 

exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]
def exponents(bases, powers):
  lst = []
  for i in bases:
    for x in range(len(powers)):
      c = i**powers[x]
      lst.append(c)
  return lst



def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))


def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))




def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))


def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))



def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))





# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

cuts_under_30 = [ # expression, #for statement, # condition]
cuts_under_30 =  [ hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]









destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]


test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]


def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(treveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index



test_destination_index = get_traveler_location(test_traveler)


































