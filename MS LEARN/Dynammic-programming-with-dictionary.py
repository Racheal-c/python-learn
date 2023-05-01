# Calculating values
# In this scenario, you will calculate both the total number of moons in the solar system and the average number of moons a planet has. You will do this by using a dictionary object.

# Start by creating a variable named planet_moons as a dictionary with the following key/values:
planet_moons = {    
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Obtain a list of moons and number of planets
## Python dictionaries allow you to retrieve all the values and keys by using the values and keys methods, respectively. Each method returns a list containing the data, which can then be used like a regular Python list. You can determine the number of items by using len, and iterate through it by using for loops. In the dictionary you created, the planet names are keys and the number of moons are the values.
## Start by retrieving a list with the number of moons, and store this in a variable named moons. Then obtain the total number of planets and store that value in a variable named total_planets.
moons = planet_moons.values()
total_planets = len(planet_moons.keys())

# Determine the avergae number of moons
## You will finish this exercise by determining the average number of moons. Start by creating a variable named total_moons; this will be your counter for the total number of moons. Then add a for loop to loop through the list of moons, adding each value to total_moons. Finally, calculate the average by dividing total_moons by total_planets and displaying the value.
total_moons = 0
for moon in moons:
    total_moons = moon + total_moons
average_moons = total_moons / total_planets

print(f'The average number of moons is {average_moons} for each planet')
