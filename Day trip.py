#My first project


import random
from tracemalloc import stop

destinations_list = ['Ankor Wat', 'Phi Phi Island', 'Hawaii']
restaurants_list = ["Bob's Burger", 'Cheesecake Factory', 'Danials Broiler', "BJ's"]
transportation_list = ['car', 'bike', 'uber', 'walk', 'bus']
entertainment_list = ['concert', 'hiking', 'snorkeling', 'surfing']

# comment to test Git
random_destinations = random.choice(destinations_list)
print(random_destinations)

random_resturants = random.choice(restaurants_list)
print(random_resturants)

random_transportation = random.choice(transportation_list)
print(random_transportation)

random_entertainment = random.choice( entertainment_list)
print(random_entertainment)

print('Do you like these selections?')
user_input = input()



if user_input == 'yes':
    print("Great!")

elif user_input == 'no':
    print("Let's try again")











#steps
#1 - Hello, please enter your name:
#2 - welcome, name!
#3 - Today's destination is, random (destination)
#4 - Would you like to book this today?
#5 - if yes, selec your favorite resturant
#6 - if no, click choose another


