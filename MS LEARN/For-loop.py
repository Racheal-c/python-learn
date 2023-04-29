# Loop over a list
## In the previous exercise, you created code to prompt users to enter a list of planet names. 
## In this exercise, you'll complete the application by writing code that displays the planet names one by one.
new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a planet name or type "done": ')

## Display the list of planets
## The planets variable stores the planet names that a user entered. You'll now use a for loop to display those entries.
## Create a for loop to iterate over the planets name list. You can use planet as the name of the variable for each planet. 
## Inside the for loop, use print to display each planet name.

for planet in planets:
    print(planet)