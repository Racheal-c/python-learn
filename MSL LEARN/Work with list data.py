## Use slices to retrieve portions of a list
#Create the list of planets
#First, create a variable named planets. Add the eight planets (without Pluto) to the list. The planets are:

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Prompt the user for the reference planet
##Next you will add the code to prompt the user for the name of a planet. You will do this by using input. Because strings are case sensitive in Python, ask the user to use a capital letter to start the name of the planet.

user_planet = input("Enter the name of a planet (Begin with a capital letter): ")

# Find the position of the reference planet
##Now you will add the code to find the position of the reference planet in the list. You will do this by using the index method. The index method returns the position of the first occurrence of an item in a list. The index method takes one argument, the item to search for. The index method returns the position of the item if it is found in the list. If the item is not found in the list, the index method raises a ValueError exception.

planet_index = planets.index(user_planet)

# Display planets closer to the sun
## With the index determined, you can now add the code to 
## display planets closer to the sun than the one selected. 
## Use the slicing abilities of a list to display all planets 
# up to the one selected.

print ("Planets closer to the sun is " + user_planet) 
print(planets[0:planet_index])

# Display planets further
## You can use the same index to display planets farther from the sun. 
## However, remember that the starting index is included when you're using a slice. 
## As a result, you'll have to add 1 to the value. 
## Add the code to display the planets farther from the sun.
print("Planets farther from the sun are " + planets[planet_index+1])
print(planets[planet_index +1:])