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


destination_list = ['Detroit', 'Mordor', 'Gondolin','Paris', 'Numenor', 'Boyne City', 'Bozeman', 'Auckland']


def destination_choice (selected_destination):
   selected_destination = random.choice (destination_list)
   return selected_destination

destination = destination_choice (destination_list)
print (destination)

dest_input = input ('Are you satisfied with this choice (y/n)?')

def dest_input_func (dest_input):
    confirm_bool = True
    while confirm_bool:
        if dest_input == 'n':
            destination_list.remove (destination)
        else:
            confirm_bool = False
        return destination_choice

destination = destination_choice (destination_list)
print (destination)


restaurant_list = ['In N Out Burger', 'MAP Brewery', 'Hells Pizza', 'The Leaky Cauldron', 'Streetside Seafood', 'Bilbos Pizza', 'Dog and Pony Show', 'Als Backyard', ]

def restaurant_choice (selected_restaurant):
    selected_restaurant = random.choice(restaurant_list)
    return selected_restaurant

restaurant = restaurant_choice (restaurant_list)
print (restaurant)

def rest_input_func (rest_input):
    confirm_bool = True
    while confirm_bool:
        rest_input = input ('Are you satisfired with the restaurant (y/n)?')
        if dest_input == 'n':
            restaurant_list.remove (restaurant)
        else:
            confirm_bool = False
        return restaurant_choice

restaurant = restaurant_choice (restaurant_list)
print (restaurant)



entertainment_list = ['Skiing', 'Hunting Sauron', 'Drinking Local Grog', 'Sailing', 'Hiking', 'Live Music', 'Archery', 'influencing']
def entertainment_choice (selected_entertainment):
   selected_entertainment = random.choice (entertainment_list)
   return selected_entertainment

entertainment = entertainment_choice (entertainment_list)
print (entertainment)

entertainment_input = input ('Are you satisfied with this choice (y/n)?')

def dest_input_func (entertainment_input):
    confirm_bool = True
    while confirm_bool:
        entertainment_input = input ('Are you satisfired with your entertainment (y/n)?')
        if entertainment_input == 'n':
            entertainment_list.remove (entertainment)
        else:
            confirm_bool = False
        return entertainment_choice

entertainment = entertainment_choice (entertainment_list)
print (entertainment)



transportation_list = ['Boat', 'Train', 'Floating Piece of Driftwood', 'Snowcat', 'Horse', 'Spitting Llama', '1970s Hearse', 'bus']
def transportation_choice (selected_transportation):
   selected_transportation = random.choice (transportation_list)
   return selected_transportation

transportation = transportation_choice (transportation_list)
print (transportation)

transportation_input = input ('Are you satisfied with this choice (y/n)?')

def transportation_input_func (transportation_input):
    confirm_bool = True
    while confirm_bool:
        transportation_input = input ('Are you satisfired with your transportation (y/n)?')
        if transportation_input == 'n':
            transportation_list.remove (transportation)
        else:
            confirm_bool = False
        return transportation_choice

transportation = transportation_choice (transportation_list)
print (f'You will be arriving via {transportation}!')

    



# def print_sequence():
#     print (destination_list [rand_dest_int])
#     print (restaurant_list [rand_dest_int] )
#     print (entertainment_list [rand_entertain_int])
#     print (transportation_list [rand_transp_int])



# def run_sequence ():
#     select_rand_dest (destination)
#     select_rand_transport (transportation)
#     select_rand_restaurant (restaurant)
#     select_rand_entertainment (entertainment)
#     print_sequence ()
    
# run_sequence ()


# def user_input_satisfaction ():
#     satisfaction = input ("Does your trip look good? (y/n)")
#     while satisfaction:
#         if satisfaction != 'y':
#             new_trip = [select_rand_dest (str(destination_list)), select_rand_restaurant (str(restaurant_list)), select_rand_entertainment (str(entertainment_list)), select_rand_transport (str(transportation_list))]
#             print (new_trip)
#         else:
#             satisfaction=True
            
# user_input_satisfaction ()
