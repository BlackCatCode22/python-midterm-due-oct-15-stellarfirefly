import random

#---
# We really don't need to put this functionality into a class, but the whole
# point of OOP is to make code modular and easily maintainable. So, why not?
#
# The namepool class will handle loading the potential animal names from the
# specified text file, under the assumption that its formatting is exactly
# as in the example file given. It provides a method for assigning a random
# name from the pool given a species, and then removing the name from the pool
# so that two animals do not end up with the same name.
#
# Exceptions will be handled in this class to make things easy, but in a
# professional setting they should probably be handled by the calling code
# so that the program doesn't just immediately exit.
#----

class NamePool:
    name_dict = {}      # dictionary of names by species
    
    #----
    # Constructor
    #
    def __init__(self, datafile):
        random.seed()       # in case the RNG isn't seeded elsewhere
        try:
            data_file = open(datafile, "r")
        except Exception as e:
            print("ERROR Opening Names File:", e)
            exit()
        current_species = "unknown"     # until we read a species name
        line = data_file.readline()
        while line != "":
            line = line.strip()             # strip out excess whitespaces
            if line.find("Names:") >= 0:    # line contains next species name
                fields = line.split(" ")
                current_species = fields[0].lower()
            if line.find(",") > 0:          # line contains csv, must be names
                    # we'll use list comprehension to generate the list
                    # and also strip away whitespaces
                self.name_dict[current_species] = [n.strip() for n in line.split(",")]
            line = data_file.readline()
        data_file.close()

    #----
    # Generate a name with a given species, then remove that name so that
    # we don't get duplicates. Return the name, or raise exceptions on either
    # out of names or invalid species.
    #
    def make_name(self, species):
        if not species in self.name_dict.keys():
            raise KeyError("Invalid species.")
        potentials = self.name_dict[species]
        if len(potentials) < 1:
            raise IndexError("Out of names.")
        idx = random.randrange(len(potentials)) # get random index
        name = potentials[idx]
        del potentials[idx]                     # delete from list by index
        self.name_dict[species] = potentials    # set dict to new list
        return name
        

if __name__ == "__main__":      # for testing the class
    pool = NamePool("animalNames.txt")
    print(pool.name_dict)
    print(pool.make_name("lion"))   # make 3 lions and a bear
    print(pool.make_name("lion"))
    print(pool.make_name("lion"))
    print(pool.make_name("bear"))
    print(pool.make_name("bear"))
    print(pool.name_dict)           # final dict should not have those names
