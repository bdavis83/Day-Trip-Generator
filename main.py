# (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
# '''

import random

destination_list = ['Detroit', 'Mordor', 'Gondolin','Paris', 'Numenor', 'Boyne City', 'Bozeman', 'Auckland']
restaurants_list = ['In N Out Burger', 'MAP Brewery', 'Hells Pizza', 'The Leaky Cauldron', 'Streetside Seafood', 'Bilbos Pizza', 'Dog and Pony Show', 'Als Backyard', ]
entertainment_list = ['Skiing', 'Hunting Sauron', 'Drinking Local Grog', 'Sailing', 'Hiking', 'Live Music', 'Archery']
tranportation_list = ['Boat', 'Train', 'Floating Piece of Driftwood', 'Snowcat', 'Horse', 'Spitting Llama', '1970s Hearse']

def select_rand_dest (destination_list):
    selected_destination = random.choice(destination_list)
    return selected_destination
   
destinaiton = select_rand_dest (destination_list)
print (destinaiton)

def select_rand_restaurant (restaurant_list):
    selected_restaurant = random.choice(restaurant_list)
    return selected_restaurant

restaurant = select_rand_restaurant (restaurants_list)
print (restaurant)

def select_rand_entertainment (entertainment_list):
    selected_entertainemnt = random.choice (entertainment_list)
    return selected_entertainemnt

entertainment = select_rand_entertainment(entertainment_list)
print (entertainment)

def select_rand_transport (transportation_list):
    selected_transportaion = random.choice (tranportation_list)
    return selected_transportaion


transportation = select_rand_transport (tranportation_list)
print (transportation)
    