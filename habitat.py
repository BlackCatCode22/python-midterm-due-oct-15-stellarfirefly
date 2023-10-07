import animal

#----
# Simple habitat that has a name and a list of animals housed within.
#
# We can add animals to the habitat and get the list of the animals
# by species and the number of each species.
#
# The assignment had no requirement to do any more than that, such as to
# remove animals, sort them, feed them, clean up after them, etc.
#
class Habitat:

    #----
    # Constructor, must specify a name for the habitat.
    #
    def __init__(self, name):
        self.name = name
        self.animals = []

    #----
    # Add an animal to the habitat.
    #
    # Note: We make no attempt to ensure that any given animal is
    # unique. (Well, not yet. The assignment does not require it, but we
    # may do it anyway once we implement a unique ID for animals.)
    #
    # Note: We make no attempt to ensure that items added to the
    # habitat are, in fact, Animals. We haven't, technically, learned
    # a good way of doing this, i.e. ensure an object is an ojbect
    # of a specific class or subclass. Things will probably break badly
    # if a not-animal is added to a habitat.
    #
    def add(self, animal):
        self.animals.append(animal)

    #----
    # Get list of animals in habitat by species, as a dictionary
    # keyed on species names and a value of that number of animals.
    #
    def get_species(self):
        population = {}
        for a in self.animals:
            species = a.species
            if species in population.keys():
                population[species] += 1
            else:
                population[species] = 1
        return population

    #----
    # Getter for habitat name.
    #
    def get_name(self):
        return self.name
    #----
    # Getter for the list of habitat residents.
    #
    def get_residents(self):
        return self.animals

if __name__ == "__main__":      # to debug the class
    lion = animal.Animal("lion")
    tiger = animal.Animal("tiger")
    bear = animal.Animal("bear")

    jungle = Habitat("jungle")
    jungle.add(lion)
    jungle.add(tiger)
    jungle.add(bear)
    jungle.add(lion)
    jungle.add(bear)

    print("habitat population by species:")
    population = jungle.get_species()
    for k in population.keys():
        print(k, "=", population[k])
