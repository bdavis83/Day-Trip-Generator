# Done (5 points): As a developer, I want to make at least three commits with descriptive messages. 
# Done (5 points): As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment selections in their own separate lists. 
# Done (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# Done (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 
# Done (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# Done (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 
# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 
# (10 points): As a user, I want to display my completed trip in the console. 
# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
# '''

import random

destination_choice = ['Detroit', 'Mordor', 'Gondolin','Paris', 'Numenor', 'Boyne City', 'Bozeman', 'Auckland']

def select_rand_dest (destination_list):
    selected_destination = random.choice(destination_list)
    # selected_destination = random.range (len(destination_list))
    return selected_destination

destination = select_rand_dest (destination_choice)
# print (destination)


restaurant_choice = ['In N Out Burger', 'MAP Brewery', 'Hells Pizza', 'The Leaky Cauldron', 'Streetside Seafood', 'Bilbos Pizza', 'Dog and Pony Show', 'Als Backyard', ]
def select_rand_restaurant (restaurant_list):
    selected_restaurant = random.choice(restaurant_list)
    # selected_restaurant = random.range (len(restaurant_list))
    return selected_restaurant

restaurant = select_rand_restaurant (restaurant_choice)
# print (restaurant)


entertainment_choice = ['Skiing', 'Hunting Sauron', 'Drinking Local Grog', 'Sailing', 'Hiking', 'Live Music', 'Archery']
def select_rand_entertainment (entertainment_list):
    selected_entertainemnt = random.choice (entertainment_list)
    # selected_entertainemnt = random.range (len(entertainment_list))
    return selected_entertainemnt

entertainment = select_rand_entertainment(entertainment_choice)
# print (entertainment)



transportation_choice = ['Boat', 'Train', 'Floating Piece of Driftwood', 'Snowcat', 'Horse', 'Spitting Llama', '1970s Hearse']
def select_rand_transport (transportation_list):
    selected_transportaion = random.choice (transportation_choice)
    # selected_transportaion = random.range (len(transportation_choice))
    return selected_transportaion


transportation = select_rand_transport (transportation_choice)
# print (transportation)

def print_sequence():
    print (destination)
    print (restaurant)
    print (entertainment)
    print (transportation)


def run_sequence ():
    select_rand_dest (destination)
    select_rand_transport (transportation)
    select_rand_restaurant (restaurant)
    select_rand_entertainment (entertainment)
    print_sequence ()

run_sequence ()
print (f'''
Your trip takes you to the {restaurant} in {destination} for {entertainment} via {transportation}.
''')


# print (destination)
# print (restaurant)
# print (entertainment)
# print (transportation)



# user_input = input ('Are you happy with your upcoming trip? (y/n)')

# def new_trip (satisfaction):
#     while user_input != 'y':
#         trip_regen = random.choice ([(destination), (restaurant), (entertainment), (transportation)])
#         satisfaction = input (f'Your new trip itinerary is {trip_regen}. Does this trip work for you? (y/n)')
#     else: 
#         print ('Enjoy your trip!')

# new_trip (user_input)