"""Restaurant rating lister."""
import sys
from random import choice as randomchoice


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


def main():
    ratings_dictionary = process_ratings(sys.argv[1])

    while True:
        print "\n\nWhat do you want to do?"
        print "1. Add/Update restaurant information"
        print "2. View ratings"
        print "3. Update random resturant rating"
        print "4. Quit"
        choice = raw_input(">>")
        if choice == "4" or choice[0] in ("q", "Q"):
            break
        else:
            if choice == "1":
                # if sys.argv[2] == "-add":
                #     ratings_dictionary.setdefault(raw_input("Type restaurant name: ").capitalize(),
                #                                   raw_input("Type rating: "))
                # elif sys.argv[2] == "-update":
                user_restaurant = raw_input("Type restaurant name: ").capitalize()
                user_rating = raw_input("Type rating: ")
                if user_rating not in [str(item) for item in range(1,6)]:
                    print "This is not a valid rating (1-5)"
                    continue

                ratings_dictionary.update({user_restaurant: user_rating})
            elif choice == "3":
                random_restaurant = randomchoice(ratings_dictionary.keys())
                print """The randomly chosen restaurant is {} and the rating is {}
                """.format(random_restaurant, ratings_dictionary[random_restaurant])
                new_rating = raw_input("What should the new rating be? ")
                if new_rating not in [str(item) for item in range(1,6)]:
                    print "This is not a valid rating (1-5)"
                    continue
                ratings_dictionary.update({random_restaurant: new_rating})

            sorted_ratings(ratings_dictionary)

main()