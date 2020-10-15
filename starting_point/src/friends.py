def get_name(dictionary):
    return dictionary["name"]

def get_favourite_tv_show(dictionary):
    return dictionary["favourites"]["tv_show"]

def likes_to_eat(dictionary, food):
    for item in dictionary["favourites"] ["snacks"]:
        if item == food:
            return True
    else:
        return False


def add_friend(dictionary, friend_name):
    dictionary["friends"].append(friend_name)

def remove_friend(dictionary, friend_name):
    for friend in dictionary["friends"]:
        if friend == friend_name:
            dictionary["friends"].remove(friend_name)

def total_money(list):
    total_money = 0
    for person in list:
        total_money += person["monies"]
    return total_money


def l_money(person_1, person_2, loan_amount):
    person_1["monies"] -= loan_amount
    person_2["monies"] += loan_amount

def all_favourite_foods(people):
    all_food = []
    for person in people:
        for item in person["favourites"]["snacks"]:
            all_food.append(item)
    return all_food

def find_no_friendends(list):
    no_mates = []
    for person in list:
        if len(person["friends"]) == 0:
            no_mates.append(person)
    return no_mates