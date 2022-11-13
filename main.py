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
restaurant_list = ['In N Out Burger', 'MAP Brewery', 'Hells Pizza', 'The Leaky Cauldron', 'Streetside Seafood', 'Bilbos Pizza', 'Dog and Pony Show', 'Als Backyard', ]
entertainment_list = ['Skiing', 'Hunting Sauron', 'Drinking Local Grog', 'Sailing', 'Hiking', 'Live Music', 'Archery', 'influencing']
transportation_list = ['Boat', 'Train', 'Floating Piece of Driftwood', 'Snowcat', 'Horse', 'Spitting Llama', '1970s Hearse', 'bus']



def select_option (list, string_type):
    confirm_satisfaction = True
    while confirm_satisfaction:
        selected_option = random.choice(list)
        user_input = input (f'We have selected {selected_option} as your {string_type} option , are you happy with this choice? ')
        if user_input == 'n':
            list.remove (selected_option)
        else:
            confirm_satisfaction = False
    return selected_option


def confirm_trip(dest,tran,rest,ent):
    print(f'you will arrive in {dest} via a {tran} to enjoy dining at {rest} with {ent} for entertainment! ')
    user_choice = input("Would you like to confirm (y/n)")
    if user_choice == "y":
        print("Enjoy your trip")
    elif user_choice == "n":
        print ()
        print ()
        print("lets start over")
        print()
        print()
        return generate_trip()


def generate_trip():
    destination = select_option(destination_list, "destination")
    transportation = select_option(transportation_list, "transportation")
    entertainment = select_option (entertainment_list, "entertainment")
    restaurant = select_option (restaurant_list, "restaurant")
    # we would need to call the function 2 more times
    confirm_trip(destination,transportation, restaurant, entertainment)
    

generate_trip()