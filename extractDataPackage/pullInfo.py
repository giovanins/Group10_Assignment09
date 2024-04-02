
def extract_info (dict):
    new_dict = dict['results']
    dicton = new_dict[0]
    name_dict = dicton['name']
    location_dict = dicton['location']
    country_dict = location_dict['country']
    
    print("Our API generates a random person and gives information about them.")
    print("For this example our random person's name is: ", name_dict["title"], name_dict["first"], name_dict["last"])
    print("Their gender is: ", dicton['gender'])
    print("They are from: ", country_dict)