import random
from datetime import date   # used for creating birthdate
import calendar             # used for various date functions

#----
# Animal class that contains all things common to all animals.
# In this case, a birthday, including a way to generate one and to
# retrieve it in human-readable format. Also a species and a name.
#
# The species is intended to simply be a generic descriptor for the
# animal, e.g. lion, tiger, bear, etc.
#
class Animal:
            # dictionary for valid months of a season,
            # this data isn't provided by the calendar module
    seasonMonths = {
        "spring":   [3, 4, 5],
        "summer":   [6, 7, 8],
        "fall":     [9, 10, 11],
        "winter":   [12, 1, 2],
    }

    #----
    # Constructor, must specify at least a species. Can also specify
    # a name if it is known at construction time.
    #
    def __init__(self, species, name = "unnamed"):
        self.current_year = date.today().year   # find and stash the current year
        self.species = species
        self.name = name

    #----
    # Set a name, if it wasn't known at creation time, or if it was
    # changed at some point.
    #
    def set_name(self, name):
        self.name = name

    #----
    # Get the name. Yeah, Python has no variable hiding, but let's try to
    # be good little programmers and make a getter.
    #
    def get_name(self):
        return self.name

    #----
    # Get the animal's species, set at construction.
    #
    def get_species(self):
        return self.species

    #----
    # Generate a random birthdate for an animal, based upon a given age
    # and a season of birth. The season may be "unknown".
    #
    # We will not overly complicate this method by attempting to
    # fine-tune it based on whether or not the current date is
    # before or after the season in question, etc. We'll keep it simple.
    #
    def genBirthDay(self, age, season):
        self.birthYear = self.current_year - age
        if season == "autumn":      # account for autumn == fall
            season = "fall"
                # we'll just see if the given season is a valid key
                # and generate a random season if not;
                # this will also work fine if season == "unknown"
        if not season in self.seasonMonths.keys():
            season = list(self.seasonMonths.keys())[random.randrange(len(self.seasonMonths))]
                # generate a random birth month based on birth season
        self.birthMonth = self.seasonMonths[season][random.randrange(len(self.seasonMonths[season]))]
                # get the name of the month as a string
        self.birthMonthName = calendar.month_name[self.birthMonth]
                # get the number of days in the month given month and year
                # and pick a number at random in that range for the birth day
        day_range = calendar.monthrange(self.birthYear, self.birthMonth)[1]
        self.birthDay = random.randrange(day_range)

    #----
    # Get the animal's birthday as a human-readable format string.
    #
    def getBirthday(self):
        return self.birthMonthName + " " + str(self.birthDay) + ", " + str(self.birthYear)

    #----
    # Setter for animal color.
    #
    def set_color(self, color):
        self.color = color

if __name__ == "__main__":      # for testing the class
    random.seed()
    creature1 = Animal("bear", "Yogi")  # named bear
    creature2 = Animal("lion")          # unnamed lion
    print("current year:", creature1.current_year)
    creature1.genBirthDay(2, "unknown")
    print("random birthday of 2-yr-old", creature1.get_species(), ", unknown season:", creature1.getBirthday())
    creature2.genBirthDay(5, "winter")
    print("random birthday of 5-yr-old", creature2.get_species(), ", winter season:", creature2.getBirthday())

