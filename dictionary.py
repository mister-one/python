A dictionary is an unordered set of key: value pairs.




menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# 1. A dictionary begins and ends with curly braces ({ and }).
# 2. Each item consists of a key (i.e., "oatmeal") and a value (i.e., 3)
# 3. Each key: value pair (i.e., "oatmeal": 3 or "avocado toast": 6) is separated by a comma (,)
# 4. It's considered good practice to insert a space () after each comma, but your code will still run without the space.


Dictionaries provide us with a way to map pieces of data to each other, so that we can quickly find values that are associated with one another.



sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, 'pantry': 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


# The keys can be numbers as well.
# For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}


students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}


keys must always be unchangeable, hashable data types, like numbers or strings.



my_dict["new_key"] = "new_value"
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["cheesecake"] = 8
>>>
{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}





animals_in_zoo = {}

animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0


print(animals_in_zoo)







If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

print(sensors)
>>>    {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}






#our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

would yield:

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}





names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}

This list comprehension:

# 1. Takes a pair from the zipped list of pairs from names and heights
# 2. Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
# 3. Creates a key : value item in the students dictionary
# 4. Repeats steps 1-3 for the entire list of pairs



drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}




songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.
plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}   # plays = {key: value for key, value in zip(songs, playcounts)}


plays["Respect"] = 94
plays["Purple Haze"] = 1

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)





zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['earth'])
print(zodiac_elements['fire'])
>>>
['Taurus', 'Virgo', 'Capricorn']
['Aries', 'Leo', 'Sagittarius']




# One way to avoid this error is to first check if the key exists in the dictionary:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
key_to_check = "Landmark 81"
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])


key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")



caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")




caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level['matcha'] = 30
try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")
  

>>> 30






Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

# You can also specify a value to return if the key doesn't exist. 
# For example, we might want to return a building height of 0 if our desired building is not in the dictionary:


>>> building_heights.get('Shanghai Tower', 0)
632
>>> building_heights.get('Mt Olympus', 0)
0
>>> building_heights.get('Kilimanjaro', 'No Value')
'No Value'




user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)   # Use .get() to get the value of "teraCoder"'s user ID, with 100000 as a default value if the user doesn't exist. 
stack_id = user_ids.get("superStackSmash", 100000)     # Use .get() to get the value of "superStackSmash"'s user ID, with 100000 as a default value if the user doesn't exist.  





.pop() is like .get() but after returnung the value it also remove that pair from the dictionary
# Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:
#When we get a ticket number, we want to return the prize and also remove that pair from the dictionary,
>>> raffle.pop(320291, "No Prize")
"Gift Basket"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(100000, "No Prize")
"No Prize"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(872921, "No Prize")
"Concert Tickets"
>>> raffle
{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}



available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)




test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for student in test_scores.keys():
  print(student)


>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]




user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()         # Create a variable called users and assign it to be all of the keys of the user_ids list.
lessons = num_exercises.keys()  # Create a variable called lessons and assign it to be all of the keys of the num_exercises list.






num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)



print(users)
print(lessons)






You can get both the keys and the values with the .items()

biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")


Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.






tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread['past'] = tarot.pop(13)
spread['present'] = tarot.pop(22)
spread['future'] = tarot.pop(10)


for key, value in spread.items():
  print('Your ' + key + ' is the ' + value + ' card.')




combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals[3])
>>> KeyError



combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"])
>>> ["hamburger", "fries"]




inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print("the peacemaker" in inventory)
>>> True




oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars:
  print element
>>>
"Best Picture"
"Best Actor"
"Best Actress"
"Animated Feature"


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

print(12 in inventory)

>>> False







What is the output of the following code?

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

for element in oscars.values():
  print element



"Moonlight"
"Casey Affleck"
"Emma Stone"
"Zootopia"




raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

raffle.pop(561721, "No Value")
print(raffle)


>>> {223842: 'Teddy Bear', 872921: 'Concert Tickets', 320291: 'Gift Basket', 412123: 'Necklace', 298787: 'Pasta Maker'}


