
A list is an ordered set of objects in Python.
# A list begins and ends with square brackets ([ and ]).
# Each item (i.e., 67 or 70) is separated by a comma (,)
# It's considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.


names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]

If we wanted to create a list of lists that paired each name with a height, we could use the command zip.
zip takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs. 
# You won't be able to see much about this object from just printing it

names_and_heights = zip(names, heights)
print(names_and_heights)

#because it will return the location of this object in memory. Output would look something like this:

<zip object at 0x7f1631e86b48>

print(list(names_and_heights))

>>>
[('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 65)]






# We can add a single element to a list using .append()

empty_list = []
empty_list.append(1)   # append() takes exactly one argument (2 given)

When we want to add multiple items to a list, we can use + to combine two lists.
>>> items_sold_new = items_sold + ['biscuit', 'tart']
>>> print(items_sold_new)
['cake', 'cookie', 'bread', 'biscuit', 'tart']




orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac', 'iris']
print(new_orders)


broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)







heights = [61, 70, 67, 64]

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)


print(list(names_and_heights))


orders = ['daisies', 'periwinkle']

orders.append('tulips')
orders.append('roses')
print(orders)



my_list = [1, 2, 3]
my_list + 4

TypeError: can only concatenate list (not "int") to list

my_list + [4]  # this is the correct way of adding an elent to a list





Python gives us an easy way of creating these lists using a function called range. 
The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. 
So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:




my_range = range(10)

>>> print(my_range)
range(0, 10)

>>> print(list(my_range))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Just like with zip, the range function returns an object that we can convert into a list:

# Python gives us an easy way of creating these lists using a function called range. 
# The function range takes a single input, and generates numbers starting at 0 and ending at the number before the input. 
# So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:


list1 = range(9)
range1 = range(8)             # Create a range called range1 with the numbers 0 through 7.
print (list(range1))
print(list(list1))


my_list = range(2, 9)
>>> print(list(my_list))
[2, 3, 4, 5, 6, 7, 8]

>>> my_range2 = range(2, 9, 2)
>>> print(list(my_range2))
[2, 4, 6, 8]


list1 = range(5, 15, 3)
list2 = range(0,40,5)
print (list(list2))




first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = zip(first_names, all_ages)
print (name_and_age)
ids = range(4)










Operations on Lists 📌✅


'''
Now that we know how to create a list, we can start working with existing lists of data.
Get the length of a list
Select subsets of a list (called slicing)
Count the number of times that an element appears in a list
Sort a list of items
'''

list1 = range(2, 20, 3)
list1_len = len(list1)

print(list1_len)





calls = ['Ali', 'Bob', 'Cam', 'Doug', 'Ellie']

Element Index
'Ali' 0
'Bob' 1
'Cam' 2
'Doug'  3
'Ellie' 4






employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']

index4 = employees[4]
print(len(employees))

print(employees[6])


print(employees[6])
>>>
Traceback (most recent call last):
  File "script.py", line 6, in <module>
    print(employees[9])
IndexError: list index out of range



shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']

print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print( last_element, element5)



>>> fruits = ['apple', 'banana', 'cherry', 'date']
>>> print(fruits[0:3])
['apple', 'banana', 'cherry']


>>> print(fruits[:3])               # When starting at the beginning of the list, it is also valid to omit the 0:
['apple', 'banana', 'cherry']


>>> print(fruits[-3:])               # If we want to select the last 3 elements of fruits, we can also use this syntax:
['banana', 'cherry', 'date']






Counting elements in a list 

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print (jake_votes)





Sorting Lists


names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']

names.sort()
print(names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']

Notice that sort goes after our list, names. If we try sort(names), we will get a NameError.
sort does not return anything. 
So, if we try to assign names.sort() to a variable, our new variable would be None:

sorted_names = names.sort()
print(sorted_names)

This prints:  None

sort does not return anything. So, if we try to assign names.sort() to a variable, our new variable would be None:

sorted_names = names.sort()
print(sorted_names)
>>> None

Although sorted_names is None, the line sorted_names = names.sort() still edited names:
>>> print(names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']




A second way of sorting a list is to use sorted. sorted is different from .sort() in several ways:

It comes before a list, instead of after.
It generates a new list.

Using sorted, we can create a new list, called sorted_names:


names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
sorted_names = sorted(names)
print(sorted_names)

['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']


# The function should double the value of the element at index of lst and return the new list with the doubled value.
def double_index(lst, index):
  if index < len(lst):
  	lst[index] = lst[index] * 2
  return lst

print(double_index([3, 8, -10, 12], 2))


#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))



# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.

def more_frequent_item(lst, item1, item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))



#If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))


# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst


print(append_sum([1, 1, 2]))

[1, 1, 2, 3, 5, 8]





def combine_sort(lst1, lst2):
  unsorted = lst1 + lst2
  sortedList = sorted(unsorted)
  return sortedList

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))




# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
def append_size(lst):
  lst.append(len(lst))
  return lst


print(append_size([23, 42, 108]))



# The function should return a list of every third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))

