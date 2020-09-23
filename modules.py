# A module is a collection of Python declarations intended broadly to be used as a tool.
# Modules are also often referred to as "libraries" or "packages" — a package is really a directory that holds a collection of modules.


from module_name import object_name
#Let's get started by importing and using the datetime module. In this case, you'll notice that datetime is both the name of the library and the name of the object that you are importing.
from datetime import datetime

random.choice() # which takes a list as an argument and returns a number from the list
random.randint() # which takes two numbers as arguments and generates a random number between the two numbers you passed in




# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)




import module_name as name_you_pick_for_the_module      # Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.


from matplotlib import pyplot as plt





import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt

import random

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)     # Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).

plt.plot(numbers_a, numbers_b)

plt.show()





cost_of_gum = 0.10
cost_of_gumdrop = 0.35

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.44999999999999996
from decimal import Decimal

cost_of_gum = Decimal('0.10')
cost_of_gumdrop = Decimal('0.35')

cost_of_transaction = cost_of_gum + cost_of_gumdrop
# Returns 0.45 instead of 0.44999999999999996




# Import Decimal below:
from decimal import Decimal

# Fix the floating point math below:
three_decimal_points = Decimal('0.2') + Decimal('0.69')
print(three_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)




# Import library below:
from library import always_three


# Call your function below:
always_three()