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
        print "You didn't enter name or rating."



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



if __name__ == '__main__':
    main()

