


#  A string can be thought of as a list of characters.

favorite_fruit = "blueberry"

my_name = 'Bocy'
first_initial = my_name[0]

string_name[first_index:last_index]	

favorite_fruit = 'blueberry'
>>> favorite_fruit[3:8]
'eberr'
>>> favorite_fruit[:4]
'blue'
>>> favorite_fruit[4:]
'berry'

>>> length = len(favorite_fruit)
>>> favorite_fruit[length]      #  IndexError because, remember, the indices start at 0, so the final character in a string has the index of length(string_name) - 1.
>>> favorite_fruit[length-1]
'y'
>>> favorite_fruit[length-4:]
'erry'





first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
temp_password = last_name[2:6]
print(last_name[-2:])
>>> 'va'


first_name = "Julie"
last_name = "Blevins"

def account_generator (first_name, last_name):
  new_account_name = first_name[:3] + " " + last_name[:3]
  return new_account_name

new_account = account_generator (first_name, last_name)

print(new_account)

>>> Jul Ble




first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return temp_password

temp_password = password_generator(first_name, last_name)
>>> print(temp_password)
ikouki




first_name = "Bob"
last_name = "Daily"

first_name[0] = "R"   # you can't do thsi as string are immutable
Traceback (most recent call last):
  File "script.py", line 4, in <module>
    first_name[0] = "R"
TypeError: 'str' object does not support item assignment





first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R"

fixed_first_name = "R" + first_name[1:]




# By adding a backslash in front of the special character we want to escape, \", we can include it in a string.
\
# \ escape character
favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""



favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter)



def letter_check(word, letter):
  for l in word:
    if l == letter:
      return True
  else:
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





def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])

print_some_characters("watermelon")


w
t
r
e
o








String methods that gives you the power to perform complicated tasks on strings very quickly and efficiently.
# String methods all have the same syntax:



.upper(), .title(), and .lower() adjust the casing of your string.
.split() takes a string and creates a list of substrings.
.join() takes a list of strings and creates a string.
.strip() cleans off whitespace, or other noise from the beginning and end of a string.
.replace() replaces all instances of a character/string in a string with another character/string.
.find() searches a string for a character/string and returns the index value that character/string is found at.
.format() and f-strings allow you to interpolate a string with variables.

string_name.string_method(arguments)


>>> favorite_song = 'SmOoTH'
>>> favorite_song_lowercase = favorite_song.lower()
>>> favorite_song_lowercase
'smooth'



poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)


string_name.split(delimiter)
If you do not provide an argument for .split() it will default to splitting at spaces.







# Create another list called author_last_names that only contains the last names of the poets in the provided string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')

print(author_names)

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1])
  
print(author_last_names)



# \n Newline
# \t Horizontal Tab



smooth_chorus = \
"""And if you said, "This life ain't good enough."
I would give my world to lift you up
I could change my life to better suit your mood
Because you're so smooth"""

chorus_lines = smooth_chorus.split('\n')

print(chorus_lines)





.join() is essentially the opposite of .split(), it joins a list of strings together with a given delimiter. 
The syntax of .join() is:
'delimiter'.join(list_you_want_to_join)


reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

new_variable = ' '.join(reapers_line_one_words)






smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio', 'You feel the turning of the world so soft and slow', 'Turning you \'round and \'round']

smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)

print(smooth_fifth_verse)

# Well I'm from the barrio
You hear my rhythm on your radio
You feel the turning of the world so soft and slow
Turning you 'round and 'round





# Python provides a great method for cleaning strings: .strip().
# Stripping a string removes all whitespace characters from the beginning and end. Consider the following example
# >>> featuring = "!!!rob thomas       !!!!!"
>>> featuring.strip('!')
'rob thomas       '





love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']


love_maybe_lines_stripped = []

for line in love_maybe_lines:
  love_maybe_lines_stripped.append(line.strip())
  
love_maybe_full = '\n'.join(love_maybe_lines_stripped)

print(love_maybe_full)



string_name.replace(character_being_replaced, new_character)

toomer_bio = \
"""
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""
toomer_bio_fixed = toomer_bio.replace('Tomer', 'Toomer')




#.find() takes a string as an argument and searching the string it was run on for that string. It then returns the first index value where that string is located.
>>>"smooth".find('oo')
'2'
Notice here that 2 is the index of the first o.



def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)


def poem_title_card(poet, title):
  poem_desc = "The poem \"{}\" is written by {}".format(title, poet)
  return poem_desc




def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)





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




