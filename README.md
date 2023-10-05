# tPythonMidtermFa23
tPythonMidtermFa23: Template repo for Pyton Midterm Fall 2023


Python Midterm Assignment

Welcome to your midterm assignment for the Python programming course at Fresno City College! In this assignment, you will be working on a collaborative project with your lab partner(s) to create a program that manages animals arriving at your zoo. You will present your program to your classmates and participate in a code review session to refine your code.

Assignment Description

Program Overview
Animals are arriving from zoos around the world, and your task is to give them names, calculate their birthdates, and organize them into habitats in your zoo. To accomplish this, you will write a Python program that performs the following tasks:

Reads information about arriving animals from an input text file (arrivingAnimals.txt).
Calculates a birthday based on the input data.
Generates a name for each animal using names collected from a recent community fundraiser (animalNames.txt).
Creates a unique ID for each animal to be used in your zoo information system (uniquesID must be inthe format: Hy01, Hy02, Li01, Li02, etc.)
Assigns each animal to an appropriate habitat.
Outputs a report (zooPopulation.txt) containing all zoo animals and their information.
Constraints
To limit the scope of the assignment and align it with the current class instruction, please work with the following constraints:

Limit the input to four animals from each of the four species (16 animals in total).
Programming Concepts to Demonstrate
You are required to demonstrate the following programming concepts in your Python program:

Clear, Concise, and Correct Code: Your program must adhere to the class programming style guide.
File I/O: Utilize various file operations such as creating, writing to, opening, reading from, closing, deleting, and appending to files.
Exception Handling: Handle standard file I/O exceptions and create custom exceptions to handle adding an animal to a habitat that does not have enough room for the new animal.
Functions and Lists: Organize the data read from the input zoo document using functions and lists.
Input - File and String Handling: Parse string data from input files.
Output - Formatted Output: Generate a report listing zoo animals with their attributes and their habitats (zooPopulation.txt).

Data Structures:
You will use the following data structures in your program.

Python lists and strings.
An Animal class with derived Hyena, Lion, Tiger, and Bear classes to represent different species of animals.
Functions:
Your program must include at least four functions with the following names:

genBirthDay(): Calculate a birthday from the information received from the originating zoo. Handle cases where the birth season is unknown.
genUniqueAnimalID(): Calculate a unique ID to uniquely identify each animal in your zoo.
genAnimalName(): Create an animal name based on input from a community fundraiser (animalNames.txt).
genZooHabitat(): Assign each new animal to a habitat. Each species must have its own habitat.
Input Data Format
The information about arriving animals will arrive in the following format with an unknown number of lines (arrivingAnimals.txt):

4 year old female hyena, born in spring, tan color, 70 pounds, from Friguia Park, Tunisia
12 year old male hyena, born in fall, brown color, 150 pounds, from Friguia Park, Tunisia
4 year old male hyena, born in spring, black color, 120 pounds, from Friguia Park, Tunisia
8 year old female hyena, unknown birth season, black and tan striped color, 105 pounds, from Friguia Park, Tunisia
6 year old female lion, born in spring, tan color, 300 pounds, from Zanzibar, Tanzania

Example Habitat Output (see the text file named: zooPopulation.txt):

Your program will organize animals into their respective habitats and generate a report similar to the following (see zooPopulation.txt for exact specs):

Hyena Habitat:

Hy01; Kamari; 4 years old; birth date Mar 21, 2018; tan color; female; 70 pounds; from Friguia Park, Tunisia; arrived Sept 27, 2022

Lion Habitat:

Li01; Kiara; 6 years old; birth date Sept 21, 2016; tan color; female; 305 pounds; from Zanzibar, Tanzania; arrived Sept 23, 2022

etc. 

Starter Names (These are in the file: animalNames.txt): 

Here are some starter names for each species. 

Hyena Names:

Shenzi, Banzai, Ed, Zig, Bud, Lou, Kamari, Wema, Nne, Madoa, Prince Nevarah

Lion Names:

Scar, Mufasa, Simba, Kiara, King, Drooper, Kimba, Nala, Leo, Samson, Elsa, Cecil

Bear Names:

Yogi, Smokey, Paddington, Lippy, Bungle, Baloo, Rupert, Winnie the Pooh, Snuggles, Bert

Tiger Names:

Tony, Tigger, Amber, Cosimia, Cuddles, Dave, Jiba, Rajah, Rayas, Ryker

Instructions:

Your Python program should follow the provided guidelines and adhere to the programming concepts outlined in the assignment description. Feel free to use the knowledge and skills you've acquired in this course to complete the assignment.

Remember to collaborate effectively with your lab partners, present your program to your classmates on the designated presentation date, and be open to accepting all critiques during the code review session.

Good luck with your Python midterm assignment, and thank you for your dedication to learning Python programming!
