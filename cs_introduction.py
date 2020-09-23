# This is a Python Dictionary that contains all of the students in Kenny's class as well as their grades.
student_grades = {"Jeremy" : 87, "Kyla" : 82, "Ayesha" : 90, "Aleida" : 94, "Todd" : 79, "Maxwell" : 98, "Yolonda" : 81, "Kiyoko" : 71, "Dagmar" : 73, "Laura" : 91, "Shimeah" : 81, "Songqiao" : 92, "Frankie" : 87, "Natalia" : 95, "Gonzalo" : 82, "Pavel" : 78}

# This is a function that determines the student with the highest grade given a dictionary
def highest_grade(grades):
	top_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] > grades[student_b]) and (grades[student_a] > grades[top_of_class]):
				top_of_class = student_a
			elif (grades[student_b] > grades[student_a]) and (grades[student_b] > grades[top_of_class]):
				top_of_class = student_b
	return top_of_class

# This is a function that determines the student with the lowest grade given a dictionary
def lowest_grade(grades):
	bottom_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] < grades[student_b]) and (grades[student_a] < grades[bottom_of_class]):
				bottom_of_class = student_a
			elif (grades[student_b] < grades[student_a]) and (grades[student_b] < grades[bottom_of_class]):
				bottom_of_class = student_b
	return bottom_of_class

# This is Kenny's Algorithm! It sorts the students into pairs based on their grades.
def kennys_algorithm(grade_dict):
	student_pairs = []
	while len(grade_dict) > 0:
		student_pairs.append([highest_grade(grade_dict), lowest_grade(grade_dict)])
		grade_dict.pop(highest_grade(grade_dict))
		grade_dict.pop(lowest_grade(grade_dict))
	print(student_pairs)
  
# Paste the code below!


kennys_algorithm(student_grades)













import textwrap
import random

# This function makes up the main body of the game and controls a players general flow through each of the options.
def health_inspector_kenny(visited):
	if visited == 0:
		print(textwrap.fill(lb +"Welcome Health Inspector Kenny.\nToday you have to inspect three restaraunts and give them ratings.", width=60) +"\nWhere would you like to go first?\n"+lb)
		choice = location_selector(locations)
		if locations[choice] == "Billy's Big Burgers":
			locations.remove("Billy's Big Burgers")
			visited += 1
			billys_grade = billys_burgers()
			print(textwrap.fill("You've finished inspecting \"Billy's Big Burgers\" and have given it a grade of {0}.".format(grades[billys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Lucy's Lemonade and Licorice":
			locations.remove("Lucy's Lemonade and Licorice")
			visited += 1
			lucys_grade = lucys_lemonade()
			print(textwrap.fill("You've finished inspecting \"Lucy's Lemonade and Licorice\" and have given it a grade of {0}.".format(grades[lucys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Laura's Luncheonette":
			locations.remove("Laura's Luncheonette")
			visited += 1
			lauras_grade = lauras_luncheonette()
			print(textwrap.fill("You've finished inspecting \"Laura's Luncheonette\" and have given it a grade of {0}.".format(grades[lauras_grade]), width=60))
			health_inspector_kenny(visited)
	elif visited < 3:
		print("Where do you want to go next?"+lbb)
		choice = location_selector(locations)
		if locations[choice] == "Billy's Big Burgers":
			locations.remove("Billy's Big Burgers")
			visited += 1
			billys_grade = billys_burgers()
			print(textwrap.fill("You've finished inspecting \"Billy's Big Burgers\" and have given it a grade of {0}.".format(grades[billys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Lucy's Lemonade and Licorice":
			locations.remove("Lucy's Lemonade and Licorice")
			visited += 1
			lucys_grade = lucys_lemonade()
			print(textwrap.fill("You've finished inspecting \"Lucy's Lemonade and Licorice\" and have given it a grade of {0}.".format(grades[lucys_grade]), width=60))
			health_inspector_kenny(visited)
		elif locations[choice] == "Laura's Luncheonette":
			locations.remove("Laura's Luncheonette")
			visited += 1
			lauras_grade = lauras_luncheonette()
			print(textwrap.fill("You've finished inspecting \"Laura's Luncheonette\" and have given it a grade of {0}.".format(grades[lauras_grade]), width=60))
			health_inspector_kenny(visited)
	else:
		print(textwrap.fill(lb + "Congratulations! You've finished a day of fullfilling health inspecting. Head home, pop open your favorite beverage, turn on old reruns of America's Next Top Model, and enjoy your evening." + lbb, width=60))

# Helper functions
def location_selector(locations):
  for i in range(0,len(locations)):
    print("("+str(i+1)+") " + locations[i]+"\n")
  selection = chooser(locations)
  return selection

def chooser(locations):
  try:
    selection = int(input("Enter the number of your choice: ")) - 1
    if selection >= len(locations):
      print("Sorry, invalid selection. Please try again.")
      selection = chooser(locations)
    return selection
  except (NameError, SyntaxError):
    print("Sorry, invalid selection. Please try again.")
    selection = chooser(location)
  return selection

def responder():
  response = int(input("Enter the number of your choice: "))
  if response not in [1, 2]:
    print("Please enter a valid choice.")
    responder()
  return response

def format_text(text):
  print(textwrap.fill(lb + text, width=60, replace_whitespace=False) + lbb)
  
# Locations
def billys_burgers():
  # 3 = A, 2 = B, 1 = C, 0 = F
  billys_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "You enter the rustic yet charming all-American diner \"Billy's Big Burgers\". Billy himself, a large swarthy man in a striped apron, comes up to you and gruffly shakes your hand.\n\"Welcome Mr. Health Inspector, please take a look around, let me know if you need anything.\" Billy retreats back to the kitchen, keeping an eye on you as he backs away. Seems like a pretty weird guy.", width=60, replace_whitespace=False))
  for i in range(len(areas)):
    print("What area of the restaraunt would you like to check?\n"+ lb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("You enter the dining room and are immediately hit with the smell of unwashed laundry. \"Hmm, that's not a good sign\" you think to yourself. Upon inspecting several tables, you find stains all over most of the tablecloths. You peer under the top of one of the booths only to find more dried gum than an elementary school's cafeteria.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("Walking behind the bar, you see everything appears fairly organized and clean. You notice a small picture of a little girl next to the glasses. Billy notices you looking at the picture and comes over. \"That's my girl Sasha\", he taps the picture and looks directly in your eyes, \"she'd be really crushed if the restaraunt didn't pass the health inspection. You wouldn't disappoint Sasha would you?\"")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("The first thing you see in the kitchen is a massive pile of dishes sitting in the sink. \"I haven't had a chance to clean those yet\", states Billy, standing in your way. Pushing past him you see more concerning things. Open packs of american cheese sitting on counters in the heat. A mysterious mound of grey meat sits on top of a cold grill. A strange orange fluid seems to be leaking from the bottom of the fridge. To top it off you see an empty container of plastic gloves sitting above a workstation, stuffed with what appears to be used tissues.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        billys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Billy's Big Burgers is currently {1}".format(areas[choice], grades[billys_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return billys_grade

def lauras_luncheonette():
# 3 = A, 2 = B, 1 = C, 0 = F
  lauras_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "You pull up to \"Laura's Luncheonette\", a plain white building with fading blue paint on the window trim. Laura meets you outside, bouncing from one foot to the other, appearing quite nervous. She leads you inside and gestures wildy. \"Please, please, inspect away, inspect it all it's perfect I promise!\" She nods enthusastically at you to begin.", width=60))
  for i in range(len(areas)):
    print("What area of the restaraunt would you like to check?"+ lb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("As you start to inspect the dining room you are interrupted as a family of mice dart across the room, running across your shoes. Clearly these mice are not afraid of people. Laura doesn't seem to notice the mice as she has begun frantically weaving between tables emptying ashtrays into a pocket on her apron.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("The bar is crowded with half finished drinks, some appear to have formed some sort of weird film on them. You want inspect behind the bar but your foot gets stuck in something extremely sticky that is coating the floor. Oh boy, it's that kind of day.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("The 'kitchen' is actually a series of cafeteria tables filled with rusty hot plates surrounded by cupboards. This place looks more like a high school chemistry lab than it does an eating establishment. Upon opening one of the cuboard you several waterbugs quickly scamper out of the light. You've seen enough here, this is bad.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lauras_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Laura's Luncheonette is currently {1}".format(areas[choice], grades[lauras_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return lauras_grade

def lucys_lemonade():
# 3 = A, 2 = B, 1 = C, 0 = F
  lucys_grade = 3
  areas = ["Dining Room", "Bar", "Kitchen"]
  print(textwrap.fill(lb + "Lucy's Lemonade in Licorice, a small hole in the wall restaraunt, is teeming with people waiting outside when you arrive. You push your way to front of the line and ask to speak to Lucy. A woman comes out, pauses to wash her hands, and then turns to you. \n\n \"Oh, I didn't expect an inspection today. Sorry for the crowd, we launched a brand new flavor of licorice today, Matcha! But everything should be in order, come in and look.\"", width=60, replace_whitespace=False))
  for i in range(len(areas)):
    print("What area of the restaraunt would you like to check?"+ lbb)
    choice = location_selector(areas)
    if areas[choice] == "Dining Room":
      format_text("You squeeze into the small dining room. All six of the tables are filled with customers, munching on pale green strands of licorice and drinking glasses of lemonade. 'Interesting color of licorice' you think to yourself 'must be the new flavor.' \n\n Despite being crowded, the waiters are moving through smoothly and the floors and tables seem quite clean. A group of patrons gets up to leave and the table is promptly wiped down and cleaned.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Dining Room")
    elif areas[choice] == "Bar":
      format_text("Dominating the wall behind the bar are rows and rows of jars of different flavors of licorice. Upon inspection, each jar is sparklingly clean and closed with an airtight seal. \n\nOn the bar itself lies three large glass barrels of lemonade. Next to the barrels are lines of cleaned glasses. You see the various lemonade garnishes properly refrigerated underneath the bartop.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Bar")
    elif areas[choice] == "Kitchen":
      format_text("In the kitchen you a large strange machine. As you go to investigate it Lucy comes over to explain it's function. \"See here,\" she points at a row of nozzels, \"this is where the strands of licorice come out and this here twirls them.\" Cool, you think to yourself as you note that this machine is also very clean. In fact, everything in the kitchen seems spotless. You've never seen such a well run lemonade and licorice establishment.")
      print("How clean is the {0}?\n\n(1) {1} (pass this area).\n\n(2) {2} (fail this area).\n".format(areas[choice], clean_responses[random.randint(0,6)], dirty_responses[random.randint(0,6)]))
      response = responder()
      if response == 2:
        lucys_grade -= 1
      print(textwrap.fill(lb + "You mark your grade for the {0} on your clipboard. The grade for Lucy's Lemonade and Licorice is currently {1}".format(areas[choice], grades[lucys_grade]) + lbb, width=60))
      areas.remove("Kitchen")
  return lucys_grade

# Global Objects
lbb = "\n------------------------------------------------------------\n"
lb = "------------------------------------------------------------\n"
grades = ["F", "C", "B", "A"]
locations = ["Billy's Big Burgers", "Lucy's Lemonade and Licorice", "Laura's Luncheonette"]
# use clean_responses[randint(0,6)] to generate a random response 
clean_responses = ["It looks pretty clean", "Clean enough", "Very clean", "I'd eat food prepared here", "Cleaner than my house", "Squeaky clean", "The cleanest I've ever seen"]
dirty_responses = ["Oh god, it's so gross", "I can't breathe in here", "Quite dirty", "Very dirty", "Really disgusting", "Dirtier than a dumpster", "I wouldn't eat here"]
visited = 0

health_inspector_kenny(visited)














on_the_griddle = [["eggs"], ["eggs"], ["eggs"], ["eggs"]]

def add_spinach(being_cooked):
	for item in being_cooked:
		item.append("spinach")
	print(being_cooked)
    
def add_mushrooms(being_cooked):
	for item in being_cooked:
		item.append("mushrooms")
	print(being_cooked)

def add_cheese(being_cooked):
	for item in being_cooked:
		item.append("cheese")
	print(being_cooked)
  
  
# Paste your code on the lines below:
add_spinach(on_the_griddle)
add_mushrooms(on_the_griddle)
add_cheese(on_the_griddle)







# This binary search function will look for a book on a bookshelf by iteratively narrowing down the area where it might find the book, until it finds the book.
def binary_search(lst, search_val):
  if len(lst) == 0:
    print("Book is not on the shelf!")
    return
  print("Checking the bookshelf and finding: {0}".format(lst[0]))
  mid = len(lst) // 2
  if lst[mid] == search_val:
    print("\nFound the book: {0}\n\n\n\n\n\n".format(search_val))
    return
  elif lst[mid] > search_val:
    binary_search(lst[:mid], search_val)
  else:
    binary_search(lst[(mid + 1):], search_val)

# This linear search looks through a bookshelf book by book until it finds the book it is looking for.    
def linear_search(lst, search_val):
  count = 0
  while len(lst) != 0:
    print("Checking the bookshelf and finding: {0}".format(lst[0]))
    if lst[0] == search_val:
    	print("\nFound the book: {0}\n\n\n\n\n\n".format(search_val))
    	return
    lst = lst[1:]
    count += 1
with open("books.csv") as f:
  books = f.read()
  bookshelf = sorted(books.split(","))
  
# Copy-paste the search code below:
binary_search(bookshelf, "Do Androids Dream of Electric Sheep?")










import random


num_people_in_room = 28 			#Change This Number

#Simulate a room with a certain number of people
def simulate(num_people):
  birthdays = []
  print("Here's what our room looks like:\n")
  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	#Assign a random birthday to each person
  for i in range(0, num_people):
    #Choose a random month
    month_choice = random.choice(months)
    #Choose a random day based on month
    if month_choice == "February":
      day = random.randint(1, 29)
    elif month_choice == "April" or month_choice == "June" or month_choice == "September" or month_choice or month_choice == "November":
      day = random.randint(1, 31)
    else:
      day = random.randint(1, 32)
    birthday = month_choice + " " + str(day)
    #Store the birthday
    birthdays.append(birthday)
    print("Person {0}'s birthday: {1}".format(i + 1, birthday))
  calculate_probability(num_people)
  match = False
  #Check for matching birthdays
  for i in range(len(birthdays)):
    if find_duplicates(birthdays, birthdays[i], i):
      match = True
      break
  if not match:
    print("\n\nIn our simulation, no two people have the same birthday")

#Calculate the probability of there being 2 people with the same birthday
def calculate_probability(num_people):
  #Check there is at least 2 people in the room
  if num_people < 2:
    print("\n\nNot enough people in the room!")
    return
  else:
    #Calculate the probability
    numerator = 365
    countdown = 364
    for i in range(2, num_people + 1):
      numerator = numerator * countdown
      countdown -= 1
    denominator = 365 ** num_people
    probability = 1 - numerator/float(denominator)
    #Change probability to percentage
    rounded = round(probability*100, 2)
    print("\n\nThe probability that two people in a room of {0} people have the same birthday is nearly {1}%".format(num_people, rounded))

    
#Find the same birthday within our list of birthdays
def find_duplicates(birthdays_list, birthday, index):
  people = []
  for i in range(len(birthdays_list)):
    if birthdays_list[i] == birthday and i != index:
      people.append(i + 1)
  if people:
    people.append(index + 1)
    print("\n\nIn our simulation, the following people have the same birthdays: ")
    for person in people:
      print("Person {0}".format(person))
    return True
  else:
    return False

simulate(num_people_in_room)





Here's what our room looks like:

Person 1's birthday: March 18
Person 2's birthday: February 7
Person 3's birthday: August 30
Person 4's birthday: July 2
Person 5's birthday: February 7
Person 6's birthday: March 7
Person 7's birthday: August 21
Person 8's birthday: May 26
Person 9's birthday: February 18
Person 10's birthday: November 4
Person 11's birthday: February 25
Person 12's birthday: August 10
Person 13's birthday: February 22
Person 14's birthday: November 5
Person 15's birthday: June 10
Person 16's birthday: April 13
Person 17's birthday: November 24
Person 18's birthday: February 13
Person 19's birthday: February 15
Person 20's birthday: July 12
Person 21's birthday: January 30
Person 22's birthday: September 30
Person 23's birthday: November 14
Person 24's birthday: October 13
Person 25's birthday: December 19
Person 26's birthday: July 1
Person 27's birthday: December 24
Person 28's birthday: June 29


The probability that two people in a room of 28 people have the same birthday is nearly 65.45%


In our simulation, the following people have the same birthdays: 
Person 5
Person 2
















"""
==================
K-means Clustering
==================

The plot displays what a K-means algorithm would yield.
"""

import codecademylib3_seaborn
import matplotlib.pyplot as plt
import numpy as np 

from os.path import join, dirname, abspath
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
from sklearn import datasets

iris = datasets.load_iris()

x = iris.data
y = iris.target

fignum = 1

# Plot the ground truthd

fig = plt.figure(fignum, figsize=(4, 3))

ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

for name, label in [('Zombies', 0),
                    ('Programmers', 1),
                    ('Vampires', 2)]:
    ax.text3D(x[y == label, 3].mean(),
              x[y == label, 0].mean(),
              x[y == label, 2].mean() + 2, name,
              horizontalalignment='center',
              bbox=dict(alpha=.2, edgecolor='w', facecolor='w'))

# Reorder the labels to have colors matching the cluster results

y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(x[:, 3], x[:, 0], x[:, 2], c=y, edgecolor='k')

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])

ax.set_xlabel('hates sunlight')
ax.set_ylabel('likes garlic')
ax.set_zlabel('canine teeth (in)')

ax.set_title('')
ax.dist = 12

#ADD CODE HERE

plt.show()








import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste histogram code:
age = new_df["age"]
sns.distplot(age)
plt.show()

# Paste mean age location code:
location_mean_age = new_df.groupby("location").age.mean()
print(location_mean_age)

# Paste barplot code:
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
   	y= "age"
)
plt.show()

# Paste violinplot code:
plt.close()
sns.violinplot(data=new_df, x="location", y="age") 
plt.show()










import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Paste code for scatter plot:
x = new_df["population_proper"]
y = new_df["age"]

plt.scatter(x, y, alpha=0.5)

plt.show()

# Paste code for linear regression:
plt.close()

sns.regplot(data=new_df, x="population_proper", y="age")

plt.show()







import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import CSVs:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Merged tables with location data:
new_df = pd.merge(user_data, pop_data)
new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"

# Code for linear regression:
sns.regplot(x="population_proper", y="age", data=new_df)

# Paste code to change the axes:
ax = plt.subplot(1, 1, 1)
ax.set_xticks([100000, 1000000, 2000000, 4000000, 8000000])
ax.set_xticklabels(["100k", "1m", "2m","4m", "8m"])
plt.show()

# Paste code to change the figure style and palette:
plt.close()

sns.set_style("darkgrid")
sns.set_palette("bright")
sns.despine()

sns.regplot(x="population_proper", y="age", data=new_df)
plt.show()

# Paste code to title the axes and the plot:
plt.close()

ax.set_xlabel("City Population") 
ax.set_ylabel("User Age") 
plt.title("Age vs Population")

sns.regplot(x="population_proper", y="age", data=new_df)
plt.show()



