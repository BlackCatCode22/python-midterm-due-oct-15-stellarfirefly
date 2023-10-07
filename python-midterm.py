import animal
import species
import namepool
import habitat

#----
# This is the main program for the midterm assignment.
#
# We make use of the classes defined in the other files, imported above.
#
# The processing of the main file "arrivingAnimals.txt" is done here,
# as is all the associated tasks such as generating a name, birthdate,
# and assigning to a habitat.
#----

arriving_file = "arrivingAnimals.txt"
name_file = "animalNames.txt"
report_file = "animal_report.txt"
name_pool = namepool.NamePool(name_file)    # prep the pool of names

#---- functions ----
# We separate the tasks into a tree of functions just for readability
# and easy maintenance.
#----

#----
# Process an arrival.
#
def process_arrival(line):
    arrival = line.split(",")
        # 1st field will give us age, gender, and species
    (age, gender, specie) = process_age_gender_species(arrival[0])
    if specie == "hyena":
        new_animal = species.Hyena()
    elif specie == "lion":
        new_animal = species.Lion()
    elif specie == "tiger":
        new_animal = species.Tiger()
    elif specie == "bear":
        new_animal = species.Bear()
    else:
        raise "Invalid species: {}".format(line)
        exit()
    new_animal.set_gender(gender)
        # now that we have an animal class and a species, we can name it
    new_animal.set_name(name_pool.genAnimalName(specie))
        # 2nd field should give us a birth season
    birth_season = process_birthday(arrival[1])
    new_animal.genBirthDay(age, birth_season)
        # 3rd field should give us a color
    new_animal.set_color(process_color(arrival[2]))
        # 4th field should give us a weight
    new_animal.set_weight(process_weight(arrival[3]))
        # source location is split between fields 5 and 6
    new_animal.set_source_location(process_location(arrival[4], arrival[5]))
    return (new_animal, specie)

def process_age_gender_species(field):
    info = field.split(" ")
    if info[1].strip() != "year" or info[2].strip() != "old":
        raise Exception("Invalid format for age/gender/species: {}".format(field))
        exit()
    age = int(info[0])  # first field has the age
    gender = info[3]    # 4th field has the gender
    species = info[4]   # 5th field has the species
    return (age, gender, species)

def process_birthday(field):
    info = field.strip().split(" ")
    if info[0] == "unknown":            # either first field is "unknown"
        return info[0]
    if info[0] != "born" or info[1] != "in":    # or must begin with "born in"
        raise Exception("Invalid format for birth season: {}".format(field))
        exit()
    return info[2]

def process_color(field):
    info = field.strip().split(" ")
    if info[len(info)-1] != "color":    # last field must be "color"
        raise Exception("Invalid format for color: {}".format(field))
        exit()
    return field.strip()    # for simplicity, will include the word "color"

def process_weight(field):
    info = field.strip().split(" ")
    if info[1] != "pounds":             # must be "<int> pounds"
        raise Exception("Invalid format for weight: {}".format(field))
        exit()
    return field.strip()    # for simplicity, will be string "<int> pounds"

def process_location(field1, field2):
    return field1.strip() + "," + field2    # just re-join the two fields

    # use the specie to assign to a habitat; create if not yet made
def genZooHabitat(habitats, specie, new_animal):
    if not specie in habitats.keys():
            # make habitat name to human-readable version for outputs
        habitats[specie] = habitat.Habitat(specie.capitalize()+" Habitat")
    habitats[specie].add(new_animal)    # add animal to habitat

    # generate a line of the report from an animal object
def genReportLine(ani):
    output = []
    output.append(ani.get_ID())
    output.append(ani.get_name())
    output.append(str(ani.get_age()) + " years old")
    output.append("birth date " + ani.getBirthday())
    output.append(ani.get_color())
    output.append(ani.get_gender())
    output.append(ani.get_weight())
    output.append(ani.get_source_location())
    string_out = ""
    for idx, field in enumerate(output):
        if idx > 0:
            string_out += "; "
        string_out += field
    return string_out

#---- main ----

habitats = {}   # dictionary of the created habitats, with list of animals

    # read and process the incoming animals file
try:
    data_file = open(arriving_file, "r")
except Exception as e:
    print("ERROR Opening Arrivals file:", e)
    exit()
line = data_file.readline()
while line != "":
    (new_animal, specie) = process_arrival(line.strip())
    genZooHabitat(habitats, specie, new_animal)
    line = data_file.readline()
data_file.close()

    # write the report to the report file
try:
    output_file = open(report_file, "w")
except Exception as e:
    print("ERROR Opening Report file:", e)
    exit()
for hab in habitats.keys():     # iterate through all habitats
        # write habitat name
    output_file.write(habitats[hab].get_name() + ":\n\n")
    for ani in habitats[hab].get_residents():
            # write animal information line
        output_file.write(genReportLine(ani) + "\n")
    output_file.write("\n")     # assignment has blank lines around headers
output_file.close()
print("Done processing incoming animals.")

