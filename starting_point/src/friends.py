def get_name(dictionary):
    return dictionary["name"]

def get_favourite_tv_show(dictionary):
    return dictionary["favourites"]["tv_show"]

def likes_to_eat(dictionary, food):
    # food_type = dictionary["favourites"] ["snacks"]
    for item in dictionary["favourites"] ["snacks"]:
        if item == food:
            return True
