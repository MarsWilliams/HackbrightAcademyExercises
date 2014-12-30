from operator import itemgetter

def make_restaurant_rating_dictionary():
    """reads file and populates dictionary"""

    with open("scores.txt", 'r') as restaurant_ratings:  

        restaurant_rating_dict = {}
        
        for line in restaurant_ratings:
            aline = line.rstrip().split(':')

            restaurant_rating_dict[aline[0]] = aline[1]
        
        return restaurant_rating_dict



def restaurant_sorting(sort_choice):
    """sorts restaurant guide by name or by rating"""

    restaurant_rating_dict = make_restaurant_rating_dictionary()

    if sort_choice[0] == "r":
        sorted_by_rating = sorted(restaurant_rating_dict.items(), key = itemgetter(1), reverse = True)
        return sorted_by_rating

    elif sort_choice[0] == "n":
        sorted_by_name = sorted(restaurant_rating_dict.items())
        return sorted_by_name

    else:
        print "you didn't enter name or rating"


# def guide_edit():

#     modification = raw_input('\nWould you like to add or remove a rating? Type "a" for add or "r," or type "e" to exit.\n>').lower()

#     restaurant_rating_dict = make_restaurant_rating_dictionary()

#     if (modification != "a" or modification != "r"):
#         print "sadness"

#     elif modification == "A":
#         restaurant_name = raw_input("What is the name of the restaurant that you would like to add?").capitalize()
#         restaurant_rating = raw_input("What rating would you like to give this restaurant, on a scale of 1 to 5?")

#         restaurant_rating_dict[restaurant_name] = restaurant_rating

#     elif modification == "R":
#         restaurant_name = raw_input("What is the name of the restaurant that you would like to add?").capitalize()

#         del restaurant_rating_dict[restaurant_name]
    
#     return restaurant_rating_dict

def main():  
    """user defines sort preference, and guide is displayed accordingly"""

    while True:
        sort_choice = raw_input("How would you like the restaurant guide to be sorted? By rating or by name?\n>").lower()
        
        restaurant_and_ratings_sorted = restaurant_sorting(sort_choice)

        if restaurant_and_ratings_sorted != None:

            for restaurant_and_rating in restaurant_and_ratings_sorted:
                print "%s has a rating of %s stars." % (restaurant_and_rating[0], restaurant_and_rating[1])
            break
            
        else:
            continue
        
        # modification = raw_input('\nWould you like to add or remove a rating? Type "a" for add or "r," or type "e" to exit.\n>').lower()

        # guide_edit()
        







if __name__ == '__main__':
    main()
