import animal

#----
# Here we create separate species classes that all derive from a "virtual"
# virtual_animal class, which itself is derived from the Animal class.
#
# Each species contains its own specific ID generators, because this seemed
# like a good place to put them. Each time a new object is created, it will
# be automagically enumerated and a new uniqueID created.
#
# All species may be constructed with an optional name, if it is known at the
# time of construction, or it will be set to "unnamed" otherwise.
#----

#---- VIRTUAL CLASSES ----#

#---
# Python has no built-in functionality for a virtual class, but we can always
# create an "intermediate" class to act like one. This is so that we can add
# code here that is common to each of the species classes, but does not
# make any sense in the Animal class. This prevents us from repeating the
# same code four times, once for each species.
#
class virtual_animal(animal.Animal):
    #----
    # Constructor
    def __init__(self, species, name = "unnamed"):
        super().__init__(species, name)

    #----
    # Getter for the animal's unique ID. Since in Python there are no private
    # class variables, we can always access Class.uniqeID but let's try to
    # be good programmers and use a getter.
    #
    def get_ID(self):
        return self.uniqueID
    
#---- SPECIES CLASSES ----#

class Lion(virtual_animal):
    prefix = "Li{enumerator:02}"
    enumerator = 0

    #----
    # Constructor
    def __init__(self, name = "unnamed"):
        super().__init__("lion", name)
        self.name = name
        Lion.enumerator += 1    # automatically enumerate the next object
        self.uniqueID = self.prefix.format(enumerator = self.enumerator)

class Tiger(virtual_animal):
    prefix = "Ti{enumerator:02}"
    enumerator = 0

    #----
    # Constructor
    def __init__(self, name = "unnamed"):
        super().__init__("tiger", name)
        Tiger.enumerator += 1    # automatically enumerate the next object
        self.uniqueID = self.prefix.format(enumerator = self.enumerator)

class Bear(virtual_animal):
    prefix = "Be{enumerator:02}"
    enumerator = 0

    #----
    # Constructor
    def __init__(self, name = "unnamed"):
        super().__init__("bear", name)
        Bear.enumerator += 1    # automatically enumerate the next object
        self.uniqueID = self.prefix.format(enumerator = self.enumerator)

class Hyena(virtual_animal):
    prefix = "Hy{enumerator:02}"
    enumerator = 0

    #----
    # Constructor
    def __init__(self, name = "unnamed"):
        super().__init__("hyena", name)
        Hyena.enumerator += 1    # automatically enumerate the next object
        self.uniqueID = self.prefix.format(enumerator = self.enumerator)

if __name__ == "__main__":      # for testing the classes
    first_lion = Lion()
    second_lion = Lion("Leo")
    third_lion = Lion("Aslan")
    first_bear = Bear("Yogi")
    second_bear = Bear()
    
        # test auto-enumeration, should show "Li01", "Li02", and "Li03"
        # get_ID() is from our "virtual" virtual_animal class
        # and get_name() is from the Animal class
    print(first_lion.get_ID(), first_lion.get_name())
    print(second_lion.get_ID(), second_lion.get_name())
    print(third_lion.get_ID(), third_lion.get_name())
        # and this should show "Be01", "Be02"
        # which demonstrates that the different enumerators don't clash
    print(first_bear.get_ID(), first_bear.get_name())
    print(second_bear.get_ID(), second_bear.get_name())

