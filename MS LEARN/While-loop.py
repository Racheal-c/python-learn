# Start by adding two variables, one for the input from the user, named new_planet, and another variable for the list of planets, named planets.
new_planet = ''
planets = []

# Create a while loop
# Starting with the variables you've just created, create a while loop. The while loop will run while new_planet is not set to done.
while new_planet.lower() != 'done':
# Inside the loop, check to see whether the new_planet variable contains a value, which should be the name of a planet. This is a quick way to see whether the user has entered a value. If they have, your code will append that value to the planets variable.
if new_planet:
    planets.append(new_planet)
# Complete the while loop by using input to prompt the user to enter a new planet name or done if they're done entering planet names. You'll store the value from input in the new_planet variable.
    new_planet = input("Enter a planet name or 'done' to finish: ")
# Finally, outside of the while loop, print the list of planets by using print.
print(planets)

# As you complete this part of the exercise, pay attention to tab levels to ensure code is run at the correct time.