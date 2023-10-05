import random
from datetime import date   # used for creating birthdate
import calendar             # used for various date functions

class Animal:
            # dictionary for valid months of a season,
            # this data isn't provided by the calendar module
    seasonMonths = {
        "spring":   [3, 4, 5],
        "summer":   [6, 7, 8],
        "fall":     [9, 10, 11],
        "winter":   [12, 1, 2],
    }
    def __init__(self):
        self.current_year = date.today().year   # find and stash the current year

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

if __name__ == "__main__":      # for testing the class
    random.seed()
    creature = Animal()
    print("current year:", creature.current_year)
    creature.genBirthDay(2, "unknown")
    print("random birthday of 2-yr-old, unknown season:", creature.getBirthday())
    creature.genBirthDay(5, "winter")
    print("random birthday of 5-yr-old, winter season:", creature.getBirthday())
