"""Restaurant rating lister."""
import sys

def process_ratings(filename):
    f = open(filename)

    restaurant_ratings = {}

    for line in f:
        words = line.strip().split(":")
        restaurant_ratings[words[0]] = words[1]

    f.close()
    return restaurant_ratings

def sorted_ratings(dictionary):

    for restaurant, rate in sorted(dictionary.items()):
        print "{} is rated at {}".format(restaurant, rate)


ratings_dictionary = process_ratings(sys.argv[1])

if sys.argv[2] == "-add":
    ratings_dictionary.setdefault(raw_input("Type restaurant name: ").capitalize(),
                                  raw_input("Type rating: "))
elif sys.argv[2] == "-update":
    user_restaurant = raw_input("Type restaurant name: ").capitalize()
    ratings_dictionary.update({user_restaurant:
                               raw_input("Type rating: ")})

sorted_ratings(ratings_dictionary)
