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